---
article_id: 4413533797271
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: aa605cf932dd6dd23dae7d5bf75819096bdb10f8699f796f7ce07f2d09e80782
fetched_at: '2026-06-28T22:38:42.647093+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - array out of
  bounds ( 0 of 112 ) on A410NFORIG (MATV410A.PRW)
type: support-article
updated_at: '2021-11-18T14:28:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413533797271-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-array-out-of-bounds-0-of-112-on-A410NFORIG-MATV410A-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**O erro array out of bounds ( 0 of 112 ) on A410NFORIG(MATV410A.PRW) ocorre ao tentar realizar uma devolução de compra.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Causa**

O erro de array ocorre sempre que os campos **C6\_NFORI** e/ou **C6\_SERIORIG**:

* Não existem no SX3;
* Não estão marcados como usados;
* Estão com o nível alterado;
* Não estão disponíveis para o módulo acessado.

**Solução**Realize a verificação e ajustes dos campos no Configurador (SIGACFG).
