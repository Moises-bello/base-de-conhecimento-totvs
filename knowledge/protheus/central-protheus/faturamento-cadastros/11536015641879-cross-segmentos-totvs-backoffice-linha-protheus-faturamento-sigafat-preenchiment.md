---
article_id: 11536015641879
category: Faturamento - Cadastros
content_hash: 33231a2a255bd0af657f68b64d674948aa855d0ed40258e9dcfb139a4f21a8fc
fetched_at: '2026-06-28T22:38:36.902141+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT)
  – Preenchimento do campo "% Rateio" (EC_RATEIO)
type: support-article
updated_at: '2023-01-12T17:54:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11536015641879-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Preenchimento-do-campo-Rateio-EC-RATEIO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como realizar o preenchimento do campo "% Rateio" (EC\_RATEIO)?

**Ambiente**Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Ao realizar o cadastro de uma condição de pagamento do tipo B, ou seja, preenchendo o campo "Tipo" (E4\_TIPO) como B, é possível utilizar duas ou mais condições de pagamento de forma conjunta.

O campo "% Rateio" (EC\_RATEIO) indica o percentual, do valor da venda, que será atribuído à condição de pagamento indicada no campo "Cond. Pagto" (EC\_COND):

![Cond_PGTO_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11625296405911)

No exemplo da imagem acima, 20% do valor da venda será cobrado "à vista", 30% do valor da venda será cobrado em 30 dias e 50% será cobrado em 60 Dias, utilizando três condições de pagamento diferentes, aglutinadas na condição de tipo B.

Caso o percentual de rateio, somatória dos campos "% Rateio" (EC\_RATEIO), ultrapasse 100%, o sistema apresentará o **HELP M360RATEIO:**

**![M360RATEIO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11625409872663)**

**Saiba mais:** [Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)
