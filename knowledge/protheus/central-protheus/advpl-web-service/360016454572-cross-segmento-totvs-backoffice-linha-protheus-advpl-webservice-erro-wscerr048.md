---
article_id: 360016454572
category: ADVPL - Web Service
content_hash: 704e8e089eaf051c7a4005d2970abf283a297d2aec737cf8ec8c3f799e88af2b
fetched_at: '2026-06-28T22:40:10.332534+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - WebService erro
  WSCERR048
type: support-article
updated_at: '2021-05-06T19:15:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016454572-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-WebService-erro-WSCERR048
---

**Dúvida**Requisição a um *Webservice* **Protheus SOAP** retorna o erro WSCERR048.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**Esta ocorrência é reproduzida, quando da utilização de um código-fonte ***Client***de **WebServices**, ao processar o pacote **SOAP**recebido como retorno da ação/método solicitado.  
Ao analisar o pacote ***SOAP***retornado pelo serviço, para a alimentação dos parâmetros **ADVPL**, caso o pacote de retorno contenha uma exceção do tipo ***SOAP FAULT***, isto indica que houve uma falha de processamento do serviço no servidor.  
O processamento é abortado com esta ocorrência, informando em **[FAULT\_CODE]** o código da excessão **SOAP**, em **<URL>** o servidor de **WebServices** que retornou o pacote, e em **FAULT\_STRING**mais detalhes sobre a ocorrência.

Esta ocorrência é capturada pelo próprio código-fonte do método, sendo que o método **'*Client'*** chamado retornará **.F.** (falso), e a descrição da ocorrência deve ser recuperada através da função [**GetWSCError().**](http://tdn.totvs.com/pages/releaseview.action?pageId=6814736)

Em grande parte dos casos esta ocorrência de erro ocorre pois, ao ser requisitado, o serviço provavelmente executou uma rotina do **Protheus**onde um erro interno foi gerado. Portando é recomendado avaliar o [**console.log**](http://tdn.totvs.com/display/tec/ConsoleLog) do processo e buscar por um possível **error.log** por exemplo.
