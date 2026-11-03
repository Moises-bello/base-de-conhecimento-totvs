---
article_id: 25591487491351
category: Financeiro
content_hash: 90a8de22c091164de92aeea3a536d984f5cd51b6b83334bf678cefdc74b05d3f
fetched_at: '2026-06-28T22:38:03.116602+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Código de
  Aceite = S
type: support-article
updated_at: '2024-08-15T12:00:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25591487491351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-C%C3%B3digo-de-Aceite-S
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25591443540887) Tempo aproximado para leitura: **02:00 min** **Dúvida**Qual é a tratativa do campo Aceite está = S (Sim) ao imprimir o boleto?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25591487466903)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**  
O campo **Aceite = S**, retrata o preenchimento do campo **EE\_DIASREC.**Ou seja, quando o campo **EE\_DIASREC** estiver preenchido > **0** o campo **Aceite** estará preenchido com **S** (demonstrando que o banco pode receber o pagamento até X dias).

Caso o campo **EE\_DIASREC** esteja preenchido = **0**, o campo Aceite estará preenchido com **N** (demonstrando que o banco não pode receber o pagamento após a data de vencimento).

**Saiba Mais**

[FINA713 - Envio Boletos - Banco do Brasil](https://tdn.totvs.com/pages/releaseview.action?pageId=673798283)
