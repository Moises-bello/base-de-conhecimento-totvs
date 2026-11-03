---
article_id: 360035250533
category: ADVPL - Web Service
content_hash: da0d82e40374180390396e3874750764349f0b866d458814fe865730058f9fa2
fetched_at: '2026-06-28T22:40:10.232587+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Criptografia PKCS#7
  para enviar à API de cobrança online do Bradesco
type: support-article
updated_at: '2025-10-17T20:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035250533-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Criptografia-PKCS-7-para-enviar-%C3%A0-API-de-cobran%C3%A7a-online-do-Bradesco
---

**Dúvida**Como criptografar um conteúdo para enviar à **API** de cobrança online do Bradesco usando a criptografia no formato PKCS#7 com os algoritmos RSA 2048 E SHA256 (sha256WithRSAEncryption)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Utilize a função SMIMESign( ).  
  
**Exemplo**

```
// BIBLIOTECAS NECESSÁRIAS  
#Include "TOTVS.ch"  
  
// BARRA DE SEPARAÇÃO DE DIRETÓRIOS  
#Define BAR IIf(IsSrvUnix(), "/", "\")  
  
//------------------------------------------------------  
// ENVIA JSON CRIPTOGRAFADO PARA O BANCO BRADESCO  
//------------------------------------------------------  
User Function T288APCK7()  
    Local cCert    := BAR + "certificate" + BAR + "myCorp_cert.pem"  
    Local cKey     := BAR + "certificate" + BAR + "myCorp_key.pem"  
    Local cJson    := '{"status": "ok"}'  
    Local cOption  := "-nodetach"  
    Local cError   := Space(0)  
    Local cPasswd  := "MyPasswordHere"  
    Local cRet     := SMIMESign(cCert, cKey, cJson, cOption, @cError, cPasswd)  
    Local cURL     := "https://cobranca.bradesconetempresa.b.br/ibpjregistrotitulows/registrotitulo"  
    Local nTimeOut := 180  
    Local aHeadOut := {}  
    Local cHeadRet := Space(0)  
    Local cResp    := HTTPSPost(cURL, cCert, cKey, cPasswd, Space(0), cRet, nTimeOut, aHeadOut, @cHeadRet)  
Return (NIL)
```

**Observação**  
Esta disponível em anexo um exemplo completo demonstrando cada etapa para geração e envio das informações (T228PCK7.prw).  
  
**Saiba mais**  
[SMIMESign](https://tdn.totvs.com/display/tec/SMIMESign)
