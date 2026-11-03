---
article_id: 1500012938642
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fcbcf6b5ff378f04c4a980e4323600d79abf9c6fbe79b9bdb361b248d34fe89d
fetched_at: '2026-06-28T22:42:40.975842+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Cálculo de necessidade no MRP
type: support-article
updated_at: '2024-05-17T20:09:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012938642-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-de-necessidade-no-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Por que o **MRP - Material Requiriment Planning** calcula a necessidade para um período sendo que em período posterior existe uma previsão de entrada do produto em estoque?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**As necessidades são sempre calculadas por período, quando existe uma entrada em estoque prevista através de **OP - Ordem de Produção**, **SC - Solicitação de Compra**, **PC - Pedido de Compra** ou **AE - Autorização de Entrega** para um período posterior ao período da necessidade, essa informação é desconsiderada, pois a entrada será posterior ao período no qual há a necessidade e um novo documento pode ser gerado de forma a atender a demanda do período.
