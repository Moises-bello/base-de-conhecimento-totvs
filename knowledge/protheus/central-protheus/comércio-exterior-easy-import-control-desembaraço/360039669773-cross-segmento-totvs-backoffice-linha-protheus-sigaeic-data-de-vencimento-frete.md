---
article_id: 360039669773
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: a57a12e8df05e768122a47f7f3c0a7c7b68073cd8a50c9a8e198d658f7945a40
fetched_at: '2026-06-28T22:39:50.042754+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Data de vencimento
  Frete e Seguro (MV_CAMBFRE e MV_CAMBSEG)
type: support-article
updated_at: '2022-09-06T10:48:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039669773-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Data-de-vencimento-Frete-e-Seguro-MV-CAMBFRE-e-MV-CAMBSEG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Na aba "transporte" não apresenta o campo referente data de vencimento do FRETE e SEGURO como configurar o mesmo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– Todas versões  
  
**Solução**Houve uma alteração no tratamento desta rotina. Para que as datas de vencimento do frete e seguro apareçam na aba ''transporte'', é necessário desabilitar os parâmetros MV\_CAMBFRE e MV\_CAMBSEG**.**

Segue documentação com orientação: [DTRADE-2982\_DT\_Titulos de Frete e Seguro do Desembaraço com Data de Emissão errada](http://tdn.totvs.com/pages/viewpage.action?pageId=507009321)  
  
Pacote de atualização disponibilizado para este tratamento de acordo com a versão do produto:

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pacote-Acumulado-Comex)

Caso os parâmetros MV\_CAMBFRE e MV\_CAMBSEG, estejam habilitados os títulos serão gerados na rotina de controle de cambio: [Geração de Títulos de Frete e Seguro](http://tdn.totvs.com/download/attachments/200910569/EIC_BT_Alteracao%20Rotina%20Geracao%20Titulos%20Frete%20Seguro_TRWQKH.pdf?version=1&modificationDate=1441051248000&api=v2)
