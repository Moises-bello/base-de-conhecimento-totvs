---
content_hash: 6c157c4d6282a124a5aa049241c3825e1633f9da30ac71a5e6e7b60b667e1fe8
fetched_at: '2026-06-29T00:08:08.481979+00:00'
page_id: '238037947'
product: rm
source: tdn-rm
title: Modelo de Integração - ERP TOTVS com Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=238037947
version: 2
---

# 1.0 Integração

A integração com o Fluig Identity será feita pelo protocolo SAML 2.0 - Security Assertion Markup Language (<http://en.wikipedia.org/wiki/Security_Assertion_Markup_Language>). O Protocolo SAML é ideal para realizar um SSO – Single Sign On através de uma aplicação Web-Based.

A figura abaixo detalha o fluxo de atividades no cenário onde o usuário acessa via Identity Provider (Fluig Identity) uma serviço/aplicativo do Service Provider (Software TOTVS).

A próxima figura, detalha o fluxo de atividades no cenário onde o usuário acessa um serviço/aplicativo diretamente no Service Provider (Software TOTVS). Esse cenário não estará disponível para aplicações desktop (.exe).

# 2.0 Nomenclatura

* SAML: Security Assertion Markup Language

Padrão aberto de autenticação e autorização para single sign-on (SSO) para web  
 <http://en.wikipedia.org/wiki/Security_Assertion_Markup_Language>  
 <http://en.wikipedia.org/wiki/SAML_2.0>

* IDP: Identy Provider (Fluig Identity)  
   Autentica o usuário e gera o assertion  
   <http://en.wikipedia.org/wiki/Identity_provider>
* SP: Service Provicer (Software TOTVS)  
   Verifica o assertion e disponibiliza o serviço  
   <http://en.wikipedia.org/wiki/Service_provider>
* Assertion  
   XML com tokens de segurança da autenticação  
   <http://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Assertions>
* Resource  
   Serviço ou aplicativo do Service Provider
* Metadata  
   XML com informações sobre o Identity Provider ou Service Provider para assegurar a comunicação entre eles  
   <http://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Metadata>

# 3.0 Requisitos

* Fluig Identity  
  + Endereço (URL) do XML metadata (exemplo: [https://www.fluigidentity.com/cloudpass/saml2/metadata](https://openidp.feide.no/simplesaml/saml2/idp/metadata.php))
* Software TOTVS  
  + UI na politica de segurança do sistema para configuração do gerenciador de identidade onde o usuário informará:  
     - endereço do IDP;  
     - o endereço que o Software TOTVS responderá como SP (exemplo: <http://myhostname:8080/spEntityID>), esse será entityID do SP;  
     - lista de endereços que podem utilizar o SSO através do SP (exemplo:  [http://myhostname:8080/](http://myhostname:8080/spEntityID/saml2/get?url=www.gmail.com))  
    - certificado digital
  + HTTP configurado que responda aos endereços:  
     - XML do metadata do SP (exemplo <http://myhostname:8080/spEntityID/saml2/metadata>);  
     - serviço do SAML do SP (exemplo <http://myhostname:8080/spEntityID/saml2/get>)  
     - reposta ao assertion do IDP (exemplo <http://myhostname:8080/spEntityID/saml2/post>)
