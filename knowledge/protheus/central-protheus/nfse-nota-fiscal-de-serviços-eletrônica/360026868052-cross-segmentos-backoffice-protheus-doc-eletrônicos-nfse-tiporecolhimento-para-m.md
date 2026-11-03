---
article_id: 360026868052
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: fe57977f4d71f980ac22578b90660c3f0c38785fd8271a80f7dbc1fd09565733
fetched_at: '2026-06-28T22:39:58.536226+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TipoRecolhimento
  para Municipios DSFNET
type: support-article
updated_at: '2021-10-06T18:53:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026868052-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TipoRecolhimento-para-Municipios-DSFNET
---

**Dúvida**De onde o sistema carrega a informação que é preenchida na tag <TipoRecolhimento> no XML do RPS, para municípios com modelo DSFNET?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**O Tipo de recolhimento pode ser informado nos campos A1\_RECISS  ou C5\_RECISS, esse conteúdo é gravado no F3\_RECISS e usado pelo rdmake a partir desse campo.  
  
Se F3\_RECISS=1 / Responsável pelo ISS = Tomador dos serviços (“R” - Retido na Fonte)  
Se F3\_RECISS=2 / Responsável pelo ISS = Prestador dos serviços (“A” – A Receber)

Municípios homologados no TSS com [provedor DSFNET](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340):

São Luís-MA, Campo Grande-MS, Uberlândia-MG, Belém-PA, Teresina-PI, Nova Iguaçu-RJ, Campinas-SP e Sorocaba-SP
