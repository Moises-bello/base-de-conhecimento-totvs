---
article_id: 4406434720663
category: Financeiro - Contas a Pagar
content_hash: 32f4dca54e3821c684b104b93b3ba19e15db0db93b4887d0ba54ad2e27285477
fetched_at: '2026-06-28T22:38:08.409800+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento BackOffice Linha Protheus - SIGAFIN - FINA080 - Taxa contratada
  na baixa por lote dos titulos em moeda estrangeira
type: support-article
updated_at: '2021-09-16T19:08:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406434720663-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-FINA080-Taxa-contratada-na-baixa-por-lote-dos-titulos-em-moeda-estrangeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Executar uma baixa por lote com moeda estrangeira e informar a taxa contratada na baixa do primeiro título no campo **ntxmoeda**, a mesma taxa informada deve ir para os demais títulos do lote, qual o processo correto?  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**

O processo de baixas em moeda estrangeira seguirá a taxa da moeda no dia de inclusão do título pelo cadastro de moedas (SM2) ou pela taxa contratada informado no campo **E2\_TXMOEDA** do título, caso o campo esteja em branco, irá trazer a taxa do dia em que o título foi incluído.  
Quando informa o valor da taxa, a mesma não sofre variação cambial ao realizar a baixa independente da moeda cadastrada no dia.

**Saiba mais:**  
<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=554658964>
