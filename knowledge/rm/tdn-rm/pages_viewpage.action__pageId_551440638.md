---
content_hash: 9070bc9d4d0a4bb428573b4ecd06743c4d24602c0b47ee02936a555608e1c742
fetched_at: '2026-06-29T00:10:43.988183+00:00'
page_id: '551440638'
product: rm
source: tdn-rm
title: Integração do RM com protocolo SAML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551440638
version: 9
---

## **ÍNDICE**

1. **Visão Geral**
2. **Requisitos**
3. **Integração SAML no RM**

**01. VISÃO GERAL**

SAML (*Security Assertion Markup Language*) é um mecanismo de autenticação segura de padrão aberto, baseado em XML para a troca de dados de autenticação e autorização de acesso entre um provedor de identidade (*Identity Provider* ou *IDP*), que atesta e certifica a identidade dos usuários, e um provedor de serviços (*Service Provider* ou *SP*).

     Para acessar o configurador da integração no sistema basta acessar "Menu Serviços Globais | Ambientes | Parâmetros | Globais | Guia Integração SAML"

* **Tipos de Integração:**
  + **Nenhuma:**Não está integrado, nada é alterado no sistema.
  + **Opcional:**O Sistema estará integrado com o Identity, todas as experiências estarão ativas. O Usuário poderá logar através do RM ou pelo Identity.
  + **Obrigatória:**O Sistema estará integrado com o Identity, todas as experiências estarão ativas. O Usuário poderá logar somente através Identity.
  + **Somente SSO Opcional:**O Sistema estará integrado com o Identity, somente o login unificado através do Identity estará ativo. O Usuário poderá logar através do RM ou pelo Identity.
  + **Somente SSO Obrigatória:**O Sistema estará integrado com o Identity, somente o login unificado através do Identity estará ativo. O Usuário poderá logar somente através do Identity.

* **Identity Provider:**
  + **Metadada Identity Provider - RM.exe:**XML com informações sobre o Identity Provider ou Service Provider (RM.exe)
  + **Metadada Identity Provider - Portal:**XML com informações sobre o Identity Provider ou Service Provider (Portal RM)

* **Validação de dispositivos:**
  + **Habilitar validação de dispositivos:** Caso a integração utilize o recurso de validar o dispositivo local, obrigando que o dispositivo esteja inscrito em um ambiente específico, será necessário ativar essa opção para que o login seja realizado seguindo os critérios de segurança estabelecidos na integração.  
    A Tag ENABLESECUREENROLLEDDEVICES, pode ser utilizada no RM.Config para habilitar a validação de dispositivos.

**02. REQUISITOS**

* **IDP: Identity Provider (Fluig Identity):**  
  Autentica o usuário e gera o assertion  
  <http://en.wikipedia.org/wiki/Identity_provider>
* **SP: Service Provicer (Software TOTVS):**  
  Verifica o assertion e disponibiliza o serviço  
  <http://en.wikipedia.org/wiki/Service_provider>
* **Assertion:**  
  XML com tokens de segurança da autenticação  
  <http://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Assertions>
* **Resource:**  
  Serviço ou aplicativo do Service Provider
* **Metadata:**  
  XML com informações sobre o Identity Provider ou Service Provider para assegurar a comunicação entre eles  
  <http://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Metadata>
* **Fluig Identity:**  
  + Endereço (URL) do XML metadata (exemplo: [https://www.fluigidentity.com/cloudpass/saml2/metadata](https://openidp.feide.no/simplesaml/saml2/idp/metadata.php))
* **Software TOTVS:**  
  + UI na politica de segurança do sistema para configuração do gerenciador de identidade onde o usuário informará:
    - Endereço do IDP;
    - O endereço que o Software TOTVS responderá como SP (exemplo: <http://myhostname:8080/spEntityID>), esse será entityID do SP;
    - Lista de endereços que podem utilizar o SSO através do SP (exemplo:  [http://myhostname:8080/](http://myhostname:8080/spEntityID/saml2/get?url=www.gmail.com))
    - Certificado digital

* + HTTP configurado que responda aos endereços:
    - XML do metadata do SP (exemplo: <http://myhostname:8080/spEntityID/saml2/metadata>);
    - Serviço do SAML do SP (exemplo: <http://myhostname:8080/spEntityID/saml2/get>)
    - Reposta ao assertion do IDP (exemplo: <http://myhostname:8080/spEntityID/saml2/post>)

**03. INTEGRAÇÃO SAML NO RM**

Abaixo temos um exemplo do metadados SAML que deve ser importado no RM:

xml1Metadatatrue














]]>

      Após obter o metadados personalizado, ele deve ser importado no RM em: Ambiente → Parâmetros → Parâmetros Globais → Integração SAML.

      Caso queira integrar com a MDI, via SAML, adicionar o metadado no campo "Metadata Identity Provider - RM.exe", Imagem demonstrativa abaixo:

      Caso queira integrar com o Portal, via SAML, adicionar o metadado no campo "Metadata Identity Provider - Portal", imagem demonstrativa abaixo:
