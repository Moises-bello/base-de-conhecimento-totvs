---
article_id: 360053154793
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: bb20ae23e4c116edac78d9e8ccfc7ff89fe31704119f2d6ed21605a18a758b02
fetched_at: '2026-06-28T22:42:43.595199+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A380QUANT
type: support-article
updated_at: '2022-01-19T18:01:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053154793-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A380QUANT
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:51 min**  
**Ocorrência**No módulo **Planejamento e Controle da Produção**, ao tentar alterar a quantidade do campo **D4\_QUANT - Sal. Empenho** no **MATA380 - Ajuste de Empenho Simples** ou no **MATA381 - Ajuste de Empenho Múltiplo** é apresentada a mensagem **A380QUANT**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086080293/mceclip0.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
Essa mensagem é apresentada pois a quantidade empenhada no campo **D4\_QTDEORI - Qtd. Empenho** está com quantidade menor que a quantidade que está sendo informada no **Sal. Empenho**.  
  
**Solução**Para poder alterar o **Saldo empenhado** é necessário primeiro ajustar a quantidade empenhada no campo **Qtd. Empenho** para uma quantidade maior ou igual ao que quer informar no campo **Sal. Empenho**.
