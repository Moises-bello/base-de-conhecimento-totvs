---
article_id: 29738451910679
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5e97fbb529999a288a496f8f7a24311ace97646794337e1f2924b8dfef3f5174
fetched_at: '2026-06-28T22:42:42.157245+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Data de encerramento da OP
type: support-article
updated_at: '2025-02-06T17:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29738451910679-Manufatura-Linha-Protheus-SIGAPCP-Data-de-encerramento-da-OP
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29738419572119) Tempo aproximado para leitura: **00:00:57 min  
  
Dúvida**Qual data será informada no campo **C2\_DATRF - DT Real Fim**, ao encerrar a **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O Sistema verifica o conteúdo do parâmetro **MV\_DATENC - Data encerramento da OP**, onde indicará a forma que irá gravar a data de encerramento da **OP**.  
Caso o valor do parâmetro esteja igual a **"1"** será gravada a *database* como data de encerramento da **OP** no campo **C2\_DATRF**.  
Caso o valor do parâmetro esteja igual a **"2"** será gravada a data do último movimento como data de encerramento da **OP** no campo **C2\_DATRF**.  
  
**Saiba mais**  
Para mais informações sobre o parâmetro **MV\_DATENC,** acesse: [Parâmetro MV\_DATENC](https://tdn.totvs.com/pages/releaseview.action?pageId=908333632)
