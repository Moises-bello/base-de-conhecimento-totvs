---
article_id: 360055344893
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 48a546c74241f61947041965ea9ecd6e16716994e39c02d746866d87fa8cc6f9
fetched_at: '2026-06-28T22:39:57.543179+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Mensagem
  wscerrint  argument  error, expected  c->u, function strtran
type: support-article
updated_at: '2021-10-06T17:49:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055344893-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Mensagem-wscerrint-argument-error-expected-c-u-function-strtran
---

**Ocorrência**No console apresenta a mensagem:   
[ERROR][SSL] [tSSLSocketAPI][RegisterCertificateToUse] Error: error:0B080074:x509 certificate routines:X509\_check\_private\_key:key values mismatch  
  
[ERROR][SSL] Failed to initialize Context SSL.  
-------------------------------------------------------------------------------  
WSCERRINT / argument #0 error, expected C->U,  function strtran  
ADVPL WSDL Client 1.120703 / TOTVS  ORACLE Sped on 20200915 15:47:18  
-------------- CallStack --------------  
Called from DECLARACAOSERVICOSTO ( 114)  
Called from { || oWS2:Declaracao (  45)  
Called from TSSEXECWSRET        (  78)  
Called from ENVNFTS              (\*\*\*\*)  
Called from TSSNFSETRANSMISSAO  ( 689)  
Called from {|aRecProc|tssNfseTr ( 187)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Aguardando Transmissão e campo STATUS=2 na tabela SPED051.  
  
**Solução**Disponível no Binário appserver-19.3.0.6
