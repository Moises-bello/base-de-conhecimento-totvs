---
article_id: 360035140974
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 522712e13c4250679120066c58da169afc66385dc062dd29547d123993877049
fetched_at: '2026-06-28T22:38:28.739242+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Percentual de acréscimo
  no Pedido de Venda
type: support-article
updated_at: '2026-05-22T19:38:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035140974-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Percentual-de-acr%C3%A9scimo-no-Pedido-de-Venda
---

**Dúvida**

Como informar um percentual de acréscimo no Pedido de Venda?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

O acréscimo financeiro é informado na condição de pagamento (**MATA360**) por meio do campo **E4\_ACRSFIN.**

Este percentual é apresentado no Pedido de Venda no campo **Acresc. Financ**. **- C5\_ACRSFIN,** após informar a Condição de Pagamento com o campo **E4\_ACRSFIN** preenchido com o percentual desejado.

"O campo **Acresc. Financ** (C5\_ACRSFIN) é apenas informativo, ou seja, só apresenta o percentual do acréscimo financeiro informado na Condição de Pagamento."

Este percentual é acrescentado no Preço de Venda para visualização na planilha financeira e na NF, após a preparação do Documento de Saída, pois não há alteração dos itens nas tabelas SC6 e SC9, somente nas tabelas SD2 e SFT, ou seja, o acréscimo não aparece no Pedido de Venda somente na NF e no título.
