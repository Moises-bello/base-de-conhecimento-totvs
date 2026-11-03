---
article_id: 360021429431
category: TAF - REINF
content_hash: 5ac31111118d832df0c73c04a9b90543255a39472a7cccd98a57beb39210a371
fetched_at: '2026-06-28T22:41:34.875191+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - TAF_ACCEPT- Alto consumo
  de licenças
type: support-article
updated_at: '2023-03-31T17:10:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021429431-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-TAF-ACCEPT-Alto-consumo-de-licen%C3%A7as
---

**Ocorrência**Está havendo um grande consumo de licenças no sistema e estão sendo apresentadas inúmeras conexões no monitor com os usuários **TAF\_ACCEPT**, **HTTP\_ACCEPT** e **HTTPJOB**.   
  
**Ambiente**Microsiga Protheus - Livros Fiscais – A partir da versão 11.80  
  
**Causa**Esta situação esta sendo apresentada, pois na Wizard de Configuração do TAF foi selecionada a opção **Layout TOTVS ou Web Service (Importação de arquivos ou integração via WS)** que deverá ser utilizada somente para clientes que utilizam o TAF segregado. Desta forma, ocasiona a chamada dos ***Web Services*** de integração com os demais *ERP's TOTVS.*  
  
**Solução**Para solução desta ocorrência será necessário comentar/remover a chave abaixo criada no arquivo de configuração **AppServer.ini**:

[OnStart]  
JOBS=HTTPJOB,TAF\_CFGJOB  
RefreshRate=120
