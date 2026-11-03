---
article_id: 360022658731
category: ADVPL - Web Service
content_hash: 7fa5889f2124999cf42603268e05a7637510cb87d7573ccea6aa66e14ec220c8
fetched_at: '2026-06-28T22:40:10.300000+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Peer certificate
  cannot be authenticated with given CA certificates
type: support-article
updated_at: '2021-05-06T18:42:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022658731-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Peer-certificate-cannot-be-authenticated-with-given-CA-certificates
---

**Ocorrência**

Ao consumir um serviço ocorre o seguinte erro:

Mensagem de erro: ***Erro SendSoapMsg: A WSDL exception occurred at0:0***  
***WsdlParser Exception : Error sending SOAP message: Peer certificate cannot be authenticated with given CA certificates.***  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– Todas versões  
  
**Causa**Existem *Web Services* exigem conexão segura para se acessar (**SSL**), exigindo certificados de uma autoridade certificadora (**CA**). Normalmente o PFX contém no certificado de CA apenas a cadeia de certificados mais necessária, pois conta com o comportamento do Windows, que procurará no repositório os certificados que faltarem. Nesse caso, após feito a extração dos arquivos de certificado e chave do PFX, a conexão feita pela TWsdlManager não é realizada, devido a falta de certificados na cadeia de certificados de CA  
  
**Solução**

Segue link com passo a passo desta ocorrência  
[Acesso a Web Services que exigem certificados de CA](http://tdn.totvs.com/display/tec/Acesso+a+Web+Services+que+exigem+certificados+de+CA)

Para web services que não exige certificado é necessário utilizar a propriedade **[lSSLInsecure](http://tdn.totvs.com/display/tec/TWsdlManager%3AlSSLInsecure)**
