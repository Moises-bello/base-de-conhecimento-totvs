/**
 * TDN Export v3 — IndexedDB + memória de erros (sem localStorage)
 *
 * COMANDOS (após colar no console):
 *   tdnExport.run()           → continua pendentes (pula OK)
 *   tdnExport.retryFailed()   → só reprocessa páginas com erro
 *   tdnExport.status()        → resumo
 *   tdnExport.downloadMemory()→ baixa tdn-memory.json (leve, para controle)
 *   tdnExport.sendToLocal()   → envia para servidor local (RECOMENDADO)
 *   tdnExport.downloadChunk(10) → baixa UM chunk por vez (fallback)
 *   tdnExport.reset()         → apaga tudo e recomeça
 *
 * Importar no Mac:
 *   Terminal 1: .venv/bin/python tools/sync.py receive-tdn
 *   Console:    tdnExport.sendToLocal()
 *   Terminal 2: .venv/bin/python tools/sync.py import-tdn-dir .cache/chunks/tdn-fluig
 */
(() => {
  const BASE = "https://tdn.totvs.com";
  const CQL = "type=page AND space=fluig";
  const DELAY_MS = 800;
  const CHUNK_SIZE = 100;
  const LOCAL_SERVER = "http://127.0.0.1:8765";
  const DB_NAME = "tdn-fluig-export";
  const DB_VER = 1;

  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  // Confluence sobrescreve window.URL — captura API nativa via iframe
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

    // Fallback: data URI (arquivos pequenos)
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

  async function dbDelete(db, store, key) {
    return new Promise((res, rej) => {
      const tx = db.transaction(store, "readwrite");
      tx.objectStore(store).delete(key);
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
    return (
      s || {
        pageList: [],
        ok: {},
        failed: {},
        listed: false,
      }
    );
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
      if (isCloudflare(text)) throw new Error("Cloudflare ativo — passe o desafio e rode tdnExport.run() de novo.");
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
    const limit = 50;
    while (true) {
      const data = await api("/rest/api/content/search", { cql: CQL, limit, start, expand: "version" });
      if (data._err) break;
      const batch = data.results || [];
      if (!batch.length) break;
      all.push(...batch.map((p) => ({ id: String(p.id), title: p.title })));
      console.log(`  ${all.length} páginas listadas...`);
      if (batch.length < limit) break;
      start += limit;
      await sleep(DELAY_MS);
    }
    return all;
  }

  async function processQueue(mode) {
    const db = await openDb();
    const state = await getState(db);

    if (!state.listed || !state.pageList.length) {
      console.log("Listando páginas...");
      state.pageList = await listAllPages();
      state.listed = true;
      await saveState(db, state);
      console.log(`Total: ${state.pageList.length}`);
    }

    let queue;
    if (mode === "retryFailed") {
      queue = state.pageList.filter((p) => state.failed[p.id] && !state.ok[p.id]);
      console.log(`Reprocessando ${queue.length} páginas com erro...`);
    } else {
      queue = state.pageList.filter((p) => !state.ok[p.id] && !state.failed[p.id]);
      console.log(`Pendentes: ${queue.length} (OK: ${Object.keys(state.ok).length}, erros: ${Object.keys(state.failed).length})`);
    }

    for (let i = 0; i < queue.length; i++) {
      const p = queue[i];
      const full = await api(`/rest/api/content/${p.id}`, { expand: "body.storage,version" });

      if (full._err) {
        const prev = state.failed[p.id] || { attempts: 0 };
        state.failed[p.id] = {
          id: p.id,
          title: p.title,
          status: full._err,
          attempts: prev.attempts + 1,
          last_at: new Date().toISOString(),
        };
        console.warn(`  ERRO ${p.id} — ${p.title} (${full._err}) → memória de erros`);
      } else {
        await dbPut(db, "pages", p.id, full);
        state.ok[p.id] = { title: p.title, at: new Date().toISOString() };
        delete state.failed[p.id];
        if (Object.keys(state.ok).length % 10 === 0) {
          console.log(`  OK ${Object.keys(state.ok).length}/${state.pageList.length} — ${full.title}`);
        }
      }

      if ((i + 1) % 25 === 0) await saveState(db, state);
      await sleep(DELAY_MS);
    }

    await saveState(db, state);
    db.close();
    tdnExport.status();
    console.log("Fila concluída. Use tdnExport.downloadChunks() para baixar os JSONs.");
  }

  window.tdnExport = {
    async run() {
      return processQueue("continue");
    },

    async retryFailed() {
      return processQueue("retryFailed");
    },

    async status() {
      const db = await openDb();
      const state = await getState(db);
      const pages = await dbAllPages(db);
      db.close();
      const ok = Object.keys(state.ok).length;
      const failed = Object.keys(state.failed).length;
      const total = state.pageList.length;
      const pending = total - ok - failed;
      console.log(
        `TDN: ${ok} OK | ${failed} com erro | ${pending} pendentes | ${total} total | ${pages.length} no IndexedDB`
      );
      if (failed) console.table(Object.values(state.failed).slice(0, 20));
      return { ok, failed, pending, total, inDb: pages.length };
    },

    async downloadMemory() {
      const db = await openDb();
      const state = await getState(db);
      db.close();
      const mem = {
        version: 3,
        exported_at: new Date().toISOString(),
        total: state.pageList.length,
        ok_count: Object.keys(state.ok).length,
        failed_count: Object.keys(state.failed).length,
        ok_ids: Object.keys(state.ok),
        failed: Object.values(state.failed),
        page_list: state.pageList,
      };
      downloadJson(mem, "tdn-memory.json");
      console.log("Baixado tdn-memory.json (controle — não use para importar conteúdo)");
    },

    async downloadChunks() {
      console.warn("downloadChunks() falha no Chrome/Confluence. Use tdnExport.sendToLocal()");
      return this.sendToLocal();
    },

    /** Envia chunks via HTTP para sync.py receive-tdn (sem download pelo browser) */
    async sendToLocal(server = LOCAL_SERVER) {
      const db = await openDb();
      const pages = await dbAllPages(db);
      const state = await getState(db);
      db.close();

      if (!pages.length) {
        console.warn("IndexedDB vazio. Rode tdnExport.run() primeiro.");
        return;
      }

      try {
        const ping = await fetch(`${server}/status`);
        if (!ping.ok) throw new Error("servidor não responde");
      } catch (_) {
        console.error(
          `Servidor local não encontrado em ${server}\n` +
            "No Mac, rode: .venv/bin/python tools/sync.py receive-tdn"
        );
        return;
      }

      const total = Math.ceil(pages.length / CHUNK_SIZE);
      console.log(`Enviando ${pages.length} páginas em ${total} chunks para ${server}...`);

      for (let i = 0; i < pages.length; i += CHUNK_SIZE) {
        const chunk = pages.slice(i, i + CHUNK_SIZE);
        const num = String(Math.floor(i / CHUNK_SIZE) + 1).padStart(3, "0");
        const payload = {
          exported_at: new Date().toISOString(),
          chunk: num,
          pages: chunk,
          skipped: Object.values(state.failed),
        };

        const r = await fetch(`${server}/chunk`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });

        if (!r.ok) {
          console.error(`Falha no chunk ${num}: HTTP ${r.status}`);
          break;
        }
        console.log(`  ✓ chunk ${num}/${String(total).padStart(3, "0")} (${chunk.length} páginas)`);
        await sleep(300);
      }

      console.log("✓ Envio concluído. No Mac: .venv/bin/python tools/sync.py import-tdn-dir .cache/chunks/tdn-fluig");
    },

    /** Baixa UM chunk (número 1–18). Use se sendToLocal não funcionar. */
    async downloadChunk(n) {
      const db = await openDb();
      const pages = await dbAllPages(db);
      const state = await getState(db);
      db.close();

      const i = (n - 1) * CHUNK_SIZE;
      const chunk = pages.slice(i, i + CHUNK_SIZE);
      if (!chunk.length) {
        console.warn(`Chunk ${n} vazio. Total páginas: ${pages.length}`);
        return;
      }
      const num = String(n).padStart(3, "0");
      const payload = {
        exported_at: new Date().toISOString(),
        chunk: num,
        pages: chunk,
        skipped: Object.values(state.failed),
      };

      if (window.showSaveFilePicker) {
        const handle = await window.showSaveFilePicker({
          suggestedName: `tdn-chunk-${num}.json`,
          types: [{ description: "JSON", accept: { "application/json": [".json"] } }],
        });
        const w = await handle.createWritable();
        await w.write(JSON.stringify(payload, null, 2));
        await w.close();
        console.log(`✓ Salvo tdn-chunk-${num}.json (${chunk.length} páginas)`);
        return;
      }

      downloadJson(payload, `tdn-chunk-${num}.json`);
      console.log(`✓ Download iniciado: tdn-chunk-${num}.json — aguarde antes do próximo`);
    },

    async downloadAllChunksSlow() {
      const db = await openDb();
      const total = Math.ceil((await dbAllPages(db)).length / CHUNK_SIZE);
      db.close();
      console.log(`Baixando ${total} chunks, um por vez. Aguarde 3s entre cada.`);
      for (let n = 1; n <= total; n++) {
        await this.downloadChunk(n);
        await sleep(3000);
      }
    },

    async reset() {
      if (!confirm("Apagar TODO o progresso do IndexedDB?")) return;
      indexedDB.deleteDatabase(DB_NAME);
      console.log("Resetado. Rode tdnExport.run() para começar do zero.");
    },
  };

  console.log(
    "%c TDN Export v3 pronto ",
    "background:#0a0;color:#fff;padding:4px",
    "\n  tdnExport.sendToLocal()  — enviar para Mac (recomendado)\n  tdnExport.downloadChunk(1) — baixar chunk 1 só\n  tdnExport.status()       — resumo"
  );

  tdnExport.status();
})();
