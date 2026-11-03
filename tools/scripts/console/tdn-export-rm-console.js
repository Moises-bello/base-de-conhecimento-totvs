/**
 * TDN Export RM (espaço LRM) — mesmo fluxo do Fluig
 *
 * 1. Abra https://tdn.totvs.com/display/public/LRM/TOTVS+Linha+RM no Chrome
 * 2. Passe o Cloudflare se aparecer
 * 3. F12 → Console → cole este script
 * 4. tdnRmExport.run()
 * 5. Terminal Mac: .venv/bin/python tools/sync.py receive-tdn --source tdn-rm
 * 6. Console: tdnRmExport.sendToLocal()
 * 7. Terminal: .venv/bin/python tools/sync.py import-tdn-dir .cache/chunks/tdn-rm --source tdn-rm
 */
(() => {
  const BASE = "https://tdn.totvs.com";
  const CQL = "type=page AND space=LRM";
  const SPEED = { concurrency: 6, listDelayMs: 100, listPageSize: 100, workerStaggerMs: 80 };
  const CHUNK_SIZE = 100;
  const LOCAL_SERVER = "http://127.0.0.1:8765";
  const DB_NAME = "tdn-rm-export";
  const DB_VER = 1;

  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  const NativeURL = (() => {
    try {
      const f = document.createElement("iframe");
      f.style.display = "none";
      document.body.appendChild(f);
      const U = f.contentWindow.URL;
      document.body.removeChild(f);
      if (U && typeof U.createObjectURL === "function") return U;
    } catch (_) {}
    return window.webkitURL || window.URL;
  })();

  function downloadJson(data, filename) {
    const json = JSON.stringify(data, null, 2);
    const blob = new Blob([json], { type: "application/json" });
    if (NativeURL && typeof NativeURL.createObjectURL === "function") {
      const a = document.createElement("a");
      const href = NativeURL.createObjectURL(blob);
      a.href = href;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(() => NativeURL.revokeObjectURL(href), 2000);
      return;
    }
    const a = document.createElement("a");
    a.href = "data:application/json;charset=utf-8," + encodeURIComponent(json);
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  }

  function openDb() {
    return new Promise((resolve, reject) => {
      const req = indexedDB.open(DB_NAME, DB_VER);
      req.onerror = () => reject(req.error);
      req.onupgradeneeded = (e) => {
        const db = e.target.result;
        if (!db.objectStoreNames.contains("pages")) db.createObjectStore("pages");
        if (!db.objectStoreNames.contains("meta")) db.createObjectStore("meta");
      };
      req.onsuccess = () => resolve(req.result);
    });
  }

  async function dbGet(db, store, key) {
    return new Promise((res, rej) => {
      const r = db.transaction(store, "readonly").objectStore(store).get(key);
      r.onsuccess = () => res(r.result);
      r.onerror = () => rej(r.error);
    });
  }

  async function dbPut(db, store, key, val) {
    return new Promise((res, rej) => {
      const tx = db.transaction(store, "readwrite");
      tx.objectStore(store).put(val, key);
      tx.oncomplete = () => res();
      tx.onerror = () => rej(tx.error);
    });
  }

  async function dbAllPages(db) {
    return new Promise((res, rej) => {
      const r = db.transaction("pages", "readonly").objectStore("pages").getAll();
      r.onsuccess = () => res(r.result || []);
      r.onerror = () => rej(r.error);
    });
  }

  async function getState(db) {
    const s = await dbGet(db, "meta", "state");
    return s || { pageList: [], ok: {}, failed: {}, listed: false };
  }

  async function saveState(db, state) {
    state.updated_at = new Date().toISOString();
    await dbPut(db, "meta", "state", state);
  }

  function isCloudflare(text) {
    return text.includes("Just a moment") || text.includes("challenge-platform");
  }

  async function api(path, params = {}, retries = 3) {
    const url = new URL(BASE + path);
    Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, v));
    for (let attempt = 1; attempt <= retries; attempt++) {
      const r = await fetch(url, { credentials: "include", headers: { Accept: "application/json" } });
      const text = await r.text();
      if (r.status === 403 || r.status === 404) return { _err: r.status };
      if (isCloudflare(text)) throw new Error("Cloudflare ativo — passe o desafio e rode tdnRmExport.run() de novo.");
      if (r.status === 429 || r.status >= 500) {
        await sleep(attempt * 3000);
        continue;
      }
      if (!r.ok) return { _err: r.status };
      return JSON.parse(text);
    }
    return { _err: "timeout" };
  }

  async function listAllPages() {
    const all = [];
    let start = 0;
    const limit = SPEED.listPageSize;
    while (true) {
      const data = await api("/rest/api/content/search", { cql: CQL, limit, start, expand: "version" });
      if (data._err) break;
      const batch = data.results || [];
      if (!batch.length) break;
      all.push(...batch.map((p) => ({ id: String(p.id), title: p.title })));
      console.log(`  ${all.length} páginas LRM listadas...`);
      if (batch.length < limit) break;
      start += limit;
      await sleep(SPEED.listDelayMs);
    }
    return all;
  }

  async function fetchPage(p) {
    try {
      return await api(`/rest/api/content/${p.id}`, { expand: "body.storage,version" });
    } catch (err) {
      return { _err: "cloudflare", _message: err.message };
    }
  }

  async function processOne(db, state, p) {
    const full = await fetchPage(p);
    if (full._err === "cloudflare") {
      throw new Error(full._message);
    }
    if (full._err) {
      const prev = state.failed[p.id] || { attempts: 0 };
      state.failed[p.id] = { id: p.id, title: p.title, status: full._err, attempts: prev.attempts + 1 };
      return "failed";
    }
    await dbPut(db, "pages", p.id, full);
    state.ok[p.id] = { title: p.title, at: new Date().toISOString() };
    delete state.failed[p.id];
    return "ok";
  }

  async function processQueue(mode) {
    const db = await openDb();
    const state = await getState(db);

    if (!state.listed || !state.pageList.length) {
      console.log("Listando páginas do espaço LRM...");
      state.pageList = await listAllPages();
      state.listed = true;
      await saveState(db, state);
      console.log(`Total LRM: ${state.pageList.length}`);
    }

    let queue;
    if (mode === "retryFailed") {
      queue = state.pageList.filter((p) => state.failed[p.id] && !state.ok[p.id]);
    } else {
      queue = state.pageList.filter((p) => !state.ok[p.id] && !state.failed[p.id]);
    }

    console.log(`Baixando ${queue.length} páginas (${SPEED.concurrency} em paralelo)...`);

    let next = 0;
    let done = 0;
    const okCount = () => Object.keys(state.ok).length;

    async function worker(workerId) {
      await sleep(workerId * SPEED.workerStaggerMs);
      while (true) {
        const i = next++;
        if (i >= queue.length) break;
        const p = queue[i];
        try {
          await processOne(db, state, p);
        } catch (err) {
          console.warn(`  PAROU: ${err.message}`);
          next = queue.length;
          throw err;
        }
        done += 1;
        if (done % 50 === 0) {
          console.log(`  OK ${okCount()}/${state.pageList.length} (${done}/${queue.length} nesta fila)`);
          await saveState(db, state);
        }
      }
    }

    try {
      await Promise.all(Array.from({ length: SPEED.concurrency }, (_, i) => worker(i)));
    } catch (err) {
      await saveState(db, state);
      db.close();
      console.warn("Progresso salvo. Resolva Cloudflare e rode tdnRmExport.run() de novo.");
      return;
    }

    await saveState(db, state);
    db.close();
    tdnRmExport.status();
  }

  window.tdnRmExport = {
    run: () => processQueue("continue"),
    retryFailed: () => processQueue("retryFailed"),
    async status() {
      const db = await openDb();
      const state = await getState(db);
      const pages = await dbAllPages(db);
      db.close();
      const ok = Object.keys(state.ok).length;
      const failed = Object.keys(state.failed).length;
      const total = state.pageList.length;
      console.log(`TDN RM: ${ok} OK | ${failed} erros | ${total - ok - failed} pendentes | ${total} total`);
      return { ok, failed, total, inDb: pages.length };
    },
    async sendToLocal(server = LOCAL_SERVER) {
      const db = await openDb();
      const pages = await dbAllPages(db);
      const state = await getState(db);
      db.close();
      if (!pages.length) {
        console.warn("IndexedDB vazio. Rode tdnRmExport.run() primeiro.");
        return;
      }
      const total = Math.ceil(pages.length / CHUNK_SIZE);
      for (let i = 0; i < pages.length; i += CHUNK_SIZE) {
        const chunk = pages.slice(i, i + CHUNK_SIZE);
        const num = String(Math.floor(i / CHUNK_SIZE) + 1).padStart(3, "0");
        const r = await fetch(`${server}/chunk`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ chunk: num, pages: chunk, skipped: Object.values(state.failed) }),
        });
        if (!r.ok) break;
        console.log(`  ✓ chunk ${num}/${String(total).padStart(3, "0")}`);
        await sleep(300);
      }
      console.log("✓ Envio concluído. import-tdn-dir .cache/chunks/tdn-rm --source tdn-rm");
    },
    reset() {
      if (confirm("Apagar progresso RM?")) indexedDB.deleteDatabase(DB_NAME);
    },
    /** Antes de run(): tdnRmExport.setSpeed(8) — se der 429, use setSpeed(3) */
    setSpeed(concurrency = 6) {
      SPEED.concurrency = Math.max(1, Math.min(12, concurrency));
      console.log(`Concorrência: ${SPEED.concurrency}`);
    },
  };

  console.log(
    "%c TDN RM Export v4 (paralelo) ",
    "background:#06c;color:#fff;padding:4px",
    `\n  ${SPEED.concurrency} downloads simultâneos\n  tdnRmExport.run() — continua de onde parou`
  );
  tdnRmExport.status();
})();
