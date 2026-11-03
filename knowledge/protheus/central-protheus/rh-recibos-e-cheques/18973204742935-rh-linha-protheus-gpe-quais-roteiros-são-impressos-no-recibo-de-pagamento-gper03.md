---
article_id: 18973204742935
category: RH - Recibos e Cheques
content_hash: 792cef829e90775183b7dd619d243305573e4405a483894a099f3e6442df7e98
fetched_at: '2026-06-28T22:43:29.575966+00:00'
product: protheus
section_id: 360011909573
source: central-protheus
title: RH - Linha Protheus - GPE - Quais roteiros são impressos no recibo de pagamento
  GPER030
type: support-article
updated_at: '2024-07-22T19:17:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18973204742935-RH-Linha-Protheus-GPE-Quais-roteiros-s%C3%A3o-impressos-no-recibo-de-pagamento-GPER030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18973237423895) Tempo aproximado para leitura: **01:00:00 min** **Dúvida**Quais roteiros são impressos no recibo de pagamento GPER030.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A impressão do recibo de pagamento é realizada à partir das informações gravadas no movimento aberto da folha de pagamento, tabela SRC e movimento fechado tabela SRD.

Os roteiros que gravam informações nessas tabelas são: **FOL, ADI, AUT, 131, 132, PLR e VEX** quando não há integração com a folha de pagamento.

Os outros roteiros apresentados ao dar um Tab na pergunta Roteiros disponíveis nos parâmetros não serão impressos pela rotina GPER030, é apenas uma tela padrão que apresenta todos os roteiros que possuem relação com a rotina de cálculo da folha de pagamento.

**Esses roteiros que são integrados a folha de pagamento, devem ser impressos pelas suas rotinas respectivas BEN, VTR, VRF, VAL e PLA.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18973249235607)

**Saiba Mais:**

[RH - Recibos e Cheques](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909573-RH-Recibos-e-Cheques)
