/**
 * TDN Export TEC (espaço TEC / TOTVSTEC) — mesmo fluxo do RM (LRM)
 *
 * 1. Abra https://tdn.totvs.com/display/tec/TOTVSTEC no Chrome
 * 2. Passe o Cloudflare se aparecer
 * 3. F12 → Console → cole este script
 * 4. tdnTecExport.run()
 * 5. Terminal Mac: .venv/bin/python tools/sync.py receive-tdn --source tdn-tec
 * 6. Console: tdnTecExport.sendToLocal()
 * 7. Terminal: .venv/bin/python tools/sync.py import-tdn-dir .cache/chunks/tdn-tec --source tdn-tec
 */
(() => {
  const BASE = "https://tdn.totvs.com";
  const CQL = "type=page AND space=TEC";
  const SPEED = { concurrency: 6, listDelayMs: 100, listPageSize: 100, workerStaggerMs: 80 };
  const CHUNK_SIZE = 100;
  const LOCAL_SERVER = "http://127.0.0.1:8765";
  const DB_NAME = "tdn-tec-export";
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
    const state = s || { pageList: [], ok: {}, failed: {}, listed: false };
    // compatível com export v3 (listagem parcial já salva)
    if (state.pageList?.length && !state.listed) {
      state.listed = true;
    }
    return state;
  }

  async function saveState(db, state) {
    state.updated_at = new Date().toISOString();
    await dbPut(db, "meta", "state", state);
  }

  function isCloudflare(text) {
    return text.includes("Just a moment") || text.includes("challenge-platform");
  }

  function isSystemError(text) {
    return text.includes("System Error") || text.includes("system error has occurred");
  }

  async function api(path, params = {}, retries = 3) {
    const url = new URL(BASE + path);
    Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, v));
    for (let attempt = 1; attempt <= retries; attempt++) {
      const r = await fetch(url, { credentials: "include", headers: { Accept: "application/json" } });
      const text = await r.text();
      if (isSystemError(text)) {
        throw new Error("TDN retornou System Error — aguarde 30–60 min e tente de novo.");
      }
      if (r.status === 403 || r.status === 404) return { _err: r.status };
      if (isCloudflare(text)) {
        throw new Error("Cloudflare ativo — passe o desafio e rode tdnTecExport.run() de novo.");
      }
      if (r.status === 429 || r.status >= 500) {
        await sleep(attempt * 3000);
        continue;
      }
      if (!r.ok) return { _err: r.status };
      try {
        return JSON.parse(text);
      } catch (_) {
        return { _err: "parse" };
      }
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
      console.log(`  ${all.length} páginas TEC listadas...`);
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
      console.log("Listando páginas do espaço TEC...");
      state.pageList = await listAllPages();
      state.listed = true;
      await saveState(db, state);
      console.log(`Total TEC: ${state.pageList.length}`);
    }

    let queue;
    if (mode === "retryFailed") {
      queue = state.pageList.filter((p) => state.failed[p.id] && !state.ok[p.id]);
    } else {
      queue = state.pageList.filter((p) => !state.ok[p.id] && !state.failed[p.id]);
    }

    if (!queue.length) {
      console.log("Nada pendente. tdnTecExport.sendToLocal() ou status().");
      db.close();
      return tdnTecExport.status();
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
      console.warn("Progresso salvo. Resolva Cloudflare/System Error e rode tdnTecExport.run() de novo.");
      return;
    }

    await saveState(db, state);
    db.close();
    tdnTecExport.status();
  }

  window.tdnTecExport = {
    run: () => processQueue("continue"),
    retryFailed: () => processQueue("retryFailed"),
    downloadOnly: () => processQueue("continue"),
    async clearFailed() {
      const db = await openDb();
      const state = await getState(db);
      const n = Object.keys(state.failed).length;
      state.failed = {};
      await saveState(db, state);
      db.close();
      console.log(`Limpos ${n} erros. Rode run() ou retryFailed().`);
      return tdnTecExport.status();
    },
    async status() {
      const db = await openDb();
      const state = await getState(db);
      const pages = await dbAllPages(db);
      db.close();
      const ok = Object.keys(state.ok).length;
      const failed = Object.keys(state.failed).length;
      const total = state.pageList.length;
      console.log(`TDN TEC: ${ok} OK | ${failed} erros | ${total - ok - failed} pendentes | ${total} total`);
      return { ok, failed, total, inDb: pages.length };
    },
    async sendToLocal(server = LOCAL_SERVER) {
      const db = await openDb();
      const pages = await dbAllPages(db);
      const state = await getState(db);
      db.close();
      if (!pages.length) {
        console.warn("IndexedDB vazio. Rode tdnTecExport.run() primeiro.");
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
      console.log("✓ Envio concluído. import-tdn-dir .cache/chunks/tdn-tec --source tdn-tec");
    },
    async downloadChunks() {
      const db = await openDb();
      const pages = await dbAllPages(db);
      const state = await getState(db);
      db.close();
      if (!pages.length) return;
      const total = Math.ceil(pages.length / CHUNK_SIZE);
      for (let i = 0; i < pages.length; i += CHUNK_SIZE) {
        const chunk = pages.slice(i, i + CHUNK_SIZE);
        const num = String(Math.floor(i / CHUNK_SIZE) + 1).padStart(3, "0");
        downloadJson(
          { chunk: num, pages: chunk, skipped: Object.values(state.failed) },
          `tdn-tec-chunk-${num}.json`
        );
        console.log(`  ✓ tdn-tec-chunk-${num}.json`);
        await sleep(2500);
      }
    },
    reset() {
      if (confirm("Apagar progresso TEC?")) indexedDB.deleteDatabase(DB_NAME);
    },
    /** Antes de run(): tdnTecExport.setSpeed(3) — se der 403/429, use setSpeed(2) */
    setSpeed(concurrency = 6) {
      SPEED.concurrency = Math.max(1, Math.min(12, concurrency));
      console.log(`Concorrência: ${SPEED.concurrency}`);
    },
  };

  console.log(
    "%c TDN TEC Export (fluxo RM) ",
    "background:#060;color:#fff;padding:4px",
    `\n  ${SPEED.concurrency} downloads simultâneos (1 request/página, sem lote)`,
    "\n  tdnTecExport.clearFailed() → limpa erros 403 da tentativa anterior",
    "\n  tdnTecExport.run() — continua de onde parou (listagem já no IndexedDB)"
  );
  tdnTecExport.status();
})();
