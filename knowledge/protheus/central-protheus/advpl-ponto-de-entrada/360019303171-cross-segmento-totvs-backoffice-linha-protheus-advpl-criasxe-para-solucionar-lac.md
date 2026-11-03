---
article_id: 360019303171
category: ADVPL - Ponto de Entrada
content_hash: b88bc7baab32c7402c0162ffa9acb45bc69739d1040589ac3765691a86656f45
fetched_at: '2026-06-28T22:40:11.681491+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Criasxe para solucionar
  lacunas no controle de numeração
type: support-article
updated_at: '2023-08-20T20:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019303171-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Criasxe-para-solucionar-lacunas-no-controle-de-numera%C3%A7%C3%A3o
---

**Dúvida**Como utilizar o ponto de entrada CRIASXE para solucionar lacunas no controle de numeração?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

1. ENABLENUMBER = 1  
   Controle de numeração pelo License Server:
2. ENABLENUMBER = 0  
   Controle de numeração por SXE/SXF:

**Observação**Ao alterar o controle numeração para o modo License Server (ENABLENUMBER=0 para ENABLENUMBER=1) as tabelas SXE e SXF serão deletadas no momento em que acessar a primeira rotina que utilize numeração automática, e nesse momento, o License Server irá buscar a última numeração de cada tabela com numeração automática, e carregar em memória. Desta forma, recomendamos que faça um backup das tabelas SXE e SXF antes de alterar o modo de numeração, e após a alteração, caso a numeração esteja na ordem incorreta, utilizar a rotina APCFG110 para acertar.

Para que o Ponto de entrada seja chamado, é necessário utilizar no inicializador do campo o **GetSxeNum()** no inicializador do campo   
  
**Saiba mais**  
[CRIASXE - CONTROLE DE NUMERAÇÃO](http://tdn.totvs.com/pages/viewpage.action?pageId=6815179)[NUMERAÇÃO AUTOMÁTICA PELO LICENSE SERVER](http://tdn.totvs.com/pages/viewpage.action?pageId=309411140)  
[GetSXENum()](http://tdn.totvs.com/pages/viewpage.action?pageId=309411140)
