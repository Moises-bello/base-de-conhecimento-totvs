---
article_id: 360022030252
category: Financeiro - Recálculos
content_hash: d8c606192c925314a220d3e31f8e430068df45b81111568f85f947cc84cd709f
fetched_at: '2026-06-28T22:38:20.155786+00:00'
product: protheus
section_id: 1500001550362
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN  - FINA378 - É possível
  aglutinar títulos dos impostos PIS/COFINS/CSLL pela data de vencimento '
type: support-article
updated_at: '2023-04-17T22:51:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022030252-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA378-%C3%89-poss%C3%ADvel-aglutinar-t%C3%ADtulos-dos-impostos-PIS-COFINS-CSLL-pela-data-de-vencimento
---

**Dúvida**É possível aglutinar títulos dos impostos PIS/COFINS/CSLL pela data de vencimento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – FINA378 - A partir da versão 11.80  
  
**Solução**A rotina Aglutinação de **Pis**, **Cofins** e **Csll** (FINA378) considera a **data de emissão** e não a **data de vencimento** dos títulos de impostos.  
No exemplo abaixo, possuímos títulos com data de vencimento: 20/02/2019 e data de emissão: 21/01/2019:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019217612/mceclip0.png)

É definido nos parâmetros **F12** abaixo o período que será gerado a **Aglutinação**. Deverá ser preenchido qual período deve ser **Aglutinado** pela data de emissão:

![f12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360019080231/f12.png)

Devido não ter **título a pagar** vencido neste dia será apresentado mensagem a abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019081231/mceclip0.png)

Podendo então ajustar o **F12** da rotina informando os **títulos** com **data de emissão** neste período:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019080591/mceclip1.png)

Os **títulos a pagar** é necessário **aglutinar** com está **data de emissão** informada nos parâmetros **F12** que é feito **Aglutinação**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019081031/mceclip0.png)

**Saiba mais:**[Aglutinação de PIS, COFINS e CSLL - FINA378](https://tdn.totvs.com/pages/releaseview.action?pageId=527005577)Para realizar a Aglutinação dos impostos considerando data de vencimento, deve realizar pela rotina FINA381:

<http://tdn.totvs.com/display/public/PROT/FIN0053_CPAG_FINA381_Aglutinacao_de_Impostos_Pis_Cofins_Csll_Irrf>
