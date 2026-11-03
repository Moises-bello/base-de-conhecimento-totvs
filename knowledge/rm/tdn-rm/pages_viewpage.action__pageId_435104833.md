---
content_hash: 2a3e9741b7d50f8570fbbcbab307d6de859ed6d92b5e2bd4314af5a24082ddc7
fetched_at: '2026-06-29T00:09:46.553361+00:00'
page_id: '435104833'
product: rm
source: tdn-rm
title: Exemplos de fórmulas que podem ser usadas para reajuste de CM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104833
version: 2
---

**Exemplos de fórmulas que podem ser usadas para reajuste de CM**

---

* **Fórmula de cálculo de juros simples sobre o componente 2 (Mensal):**

REXPARCELACOMPONENTE(2, 'VR\_COMPN') \* 0.01 \* PERIODOMENSAL

* **Fórmula de cálculo de correção sobre o componente 2 (Mensal):**

REXPARCELACOMPONENTE (2, 'VR\_COMPN') \* RECALCULACORRECAOMONETARI ('IGPM', DATBASE, DATREAJUSTE, DATVCTO, 1, 0)

---

Todas as funções de fórmulas utilizadas podem ser encontradas no menu:\* **Funções de Fórmulas usadas no TOTVS Incorporação**
