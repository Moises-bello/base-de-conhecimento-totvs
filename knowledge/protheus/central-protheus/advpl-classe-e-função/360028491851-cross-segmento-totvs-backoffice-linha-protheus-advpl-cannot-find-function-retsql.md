---
article_id: 360028491851
category: ADVPL - Classe e Função
content_hash: 720876f9d3985191773380d54f23f690aa5a863dac4b588025e85a1b77c7aae7
fetched_at: '2026-06-28T22:40:14.527014+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Cannot find function
  RETSQLNAME
type: support-article
updated_at: '2022-01-03T21:25:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028491851-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cannot-find-function-RETSQLNAME
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao customizar o ponto de entrada STFinishSale esta apresentando error.log: "Cannot find function RETSQLNAME"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**

A mensagem "**Cannot find function RETSQLNAME**" ocorre porque não existe a função no RPO. do PDV.  
  
**Solução**O Totvs PDV por padrão utiliza um RPO  reduzido com as funcionalidades necessárias para funcionamento do PDV.  
A rotina de cadastro de Banco não pertence ao menu padrão do PDV , sendo uma rotina a ser utilizada somente na Retaguarda.
