---
article_id: 19878331947031
category: Financeiro
content_hash: 57710a9e49437aaa183a72698b589fb684619fc20fc47755c91e0025e8b93271
fetched_at: '2026-06-28T22:38:03.018887+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA430/FINA200 - Como
  realizar a retenção dos impostos na baixa/recepção CNAB?
type: support-article
updated_at: '2023-12-15T21:12:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19878331947031-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA430-FINA200-Como-realizar-a-reten%C3%A7%C3%A3o-dos-impostos-na-baixa-recep%C3%A7%C3%A3o-CNAB
---

**Dúvida**Como realizar a retenção dos impostos de PCC e IR onde o fato gerador é o pagamento, apenas na baixa do CNAB?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - **FINA430/FINA200** - Todas as versões  
  
**Solução**Para que seja possivel realizar a retenção dos impostos na recepção do arquivo **CNAB**, será necessário a ativação do parametro referente a carteira e processo:

**No contas a pagar** foi disponibilizado o parametro **MV\_CNBIMPG**

***Obs: A partir da ativação, não será mais possivel a geração do borderô via FINA241 - Borderô impostos a pagar***

Utilizar a rotina de geração de borderô **FINA240** Borderô a pagar

**No contas a receber** foi disponibilizado o parametro **MV\_CNABIMP**

***Obs: A partir da ativação, não será mais possivel a geração do borderô via FINA061 - Borderô impostos Receber***

Utilizar a rotina de geração de borderô **FINA060** borderô a receber.

**Mais informações sobre o processo de implementação nas documentações abaixo:**

<https://tdn.totvs.com/display/public/PROT/FIN0042_CNAB_MV_CNBIMPG_FINA430>

<https://tdn.totvs.com/pages/releaseview.action?pageId=152802224>
