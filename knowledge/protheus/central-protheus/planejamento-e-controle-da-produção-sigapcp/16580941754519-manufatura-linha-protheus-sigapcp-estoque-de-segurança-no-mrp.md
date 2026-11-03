---
article_id: 16580941754519
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e177b485503e0f2c3f19ffcc386a01178f1446f31f86ee6fbe48586684ddc37e
fetched_at: '2026-06-28T22:42:42.314109+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Estoque de segurança no MRP
type: support-article
updated_at: '2023-08-07T17:11:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16580941754519-Manufatura-Linha-Protheus-SIGAPCP-Estoque-de-seguran%C3%A7a-no-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16580916273687) Tempo aproximado para leitura: **00:00:48 min** **Dúvida**Como o **MRP -** **Material Requiriment Planning** considera o estoque de segurança no cálculo?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Quando o **MRP** está parametrizado para considerar o estoque de segurança o valor registrado como estoque de segurança, seja no campo **B1\_ESTSEG - Segurança** ou **BZ\_ESTSEG - Segurança** é descontado do saldo inicial do primeiro período.  
  
**Exemplo**Se o estoque de segurança é de 10 e a quantidade total em estoque de todos os armazéns considerados pelo MRP for de 100, o saldo inicial do primeiro período é 90 (100-10).
