---
article_id: 1500011958922
category: Financeiro - Contas a Receber - PIX
content_hash: 9b0758c204d7e396e2fcaf7131a4fbbe41b9184742d4fc1bd3f87b9d4f6061c5
fetched_at: '2026-06-28T22:38:16.478651+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA890 - Funções do
  layout do CNAB para envio de remessa de PIX no Contas a Receber '
type: support-article
updated_at: '2021-05-24T20:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011958922-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA890-Fun%C3%A7%C3%B5es-do-layout-do-CNAB-para-envio-de-remessa-de-PIX-no-Contas-a-Receber
---

**Dúvida**Quais funções devo inserir no meu layout do CNAB para enviar uma remessa de PIX no Contas a Receber? **Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - A partir da versão 12.1.23

**Solução**Estão disponíveis as seguintes novas funções para uso no Layout de Remessa **CNAB Modelo 1**

* **CNABDJUR()**
  + Caso o título tenha juros, retornará a data de vencimento real do título que será considerada para o acréscimo de juros no valor original (ex: 20210120). Caso não tenha, será retornado o conteúdo "00000000"
* **CNABDMULT()**  
  + Caso o título tenha multa, retornará a data de vencimento real do título que será considerada para o acréscimo da multa no valor original. Caso não tenha, será retornado o conteúdo "00000000"
* **CNABDDESC()**
  + Caso o título tenha desconto, retornará a data de vencimento real do título que será considerada para o abatimento do desconto no valor original. Caso não tenha, será retornado o conteúdo "00000000"

**Saiba Mais**<https://tdn.totvs.com/pages/releaseview.action?pageId=569478747#Pagamentosinstant%C3%A2neos-PIX-03.CONTASARECEBER>
