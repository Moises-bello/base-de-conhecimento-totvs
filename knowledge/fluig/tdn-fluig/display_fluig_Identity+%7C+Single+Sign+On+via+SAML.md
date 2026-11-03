---
content_hash: 14989d85373a7c2ce8210099d3b4cb9a04eac119ed19c67c09a10d2522902222
fetched_at: '2026-06-28T21:35:24.032239+00:00'
page_id: '268796727'
product: fluig
source: tdn-fluig
title: Identity | Single Sign On via SAML
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Single+Sign+On+via+SAML
version: 12
---

# Índice

trueÍndicenone

# *Security Assertion Markup Language* (SAML)

---

O SAML (*Security Assertion Markup Language*) é um padrão baseado em XML para a autenticação e autorização de informações entre dois parceiros confiáveis. Ele é baseado em outros padrões:

* *Extensible Markup Language* (XML)
* XML Schema
* XML Signature
* XML Encryption (apenas SAML 2.0)
* *Hypertext Transfer Protocol* (HTTP)
* SOAP

## Atores em SAML

***Identity Provider* (IDP) / *Asserting Party***

* Autentica o usuário
* Gera o *assertion* (Isto é gerenciado pelo serviço *Single Sign On* – URL SSO)

#### *Service Provider* (SP) / *Relying Party*

* Consome o *assertion* (Isto é gerenciado pelo serviço *Assertion Consumer* – URL ACS)
* Fornece o recurso

#### *User*

* Requisita acesso ao aplicativo

# SAML no Identity

---

O Identity suporta o *Single Sign On* baseado no SAML 2.0. Eles suportam os SSO SP-initiated e IDP-initiated.

### SAML - DOIS CENÁRIOS - Responsabilidades do *Service Provider*

#### Funcionalidades de alto nível do SP para SSO IDP - initiated

1. Recebe a resposta SAML.
2. Verifica a assinatura.
3. Valida a resposta SAML.
4. Verifica o status da resposta, se foi uma autenticação válida ou não. Se o status for uma falha, ignora a assertion.
5. Valida o emissor. Isto exige que o IDP seja registrado com o SP.
6. Se criptografado, descriptografa a assertion.
7. Valida que a resposta possui uma assertion, declarações de autenticação e declarações de atributos.
8. Certifica-se que a assertion é valida na instância dada e é intencionada para o SP.
9. Determina a autorização dos usuários baseado nas declarações de autenticação e atributos na assertion.
10. Se autorizado, redireciona o usuário para o recurso requisitado/protegido.

#### Funcionalidades de alto nível do SP para SSO SP-initiated

1. Gera a requisição de autenticação e envia para o IDP.
2. Recebe a resposta SAML.
3. Verifica a assinatura.
4. Valida a resposta SAML.
5. Verifica o status da resposta, se foi uma autenticação válida ou não. Se o status for uma falha, ignora a assertion.
6. Valida o emissor. Isto exige que o IDP seja registrado com o SP.
7. Descriptografa a assertion.
8. Valida que a resposta possui uma assertion, declarações de autenticação e declarações de atributos.
9. Certifica-se que a assertion é valida na instância dada e é intencionada para o SP.
10. Determina a autorização dos usuários baseado nas declarações de autenticação e atributos na assertion.
11. Se autorizado, redireciona o usuário para o recurso requisitado/protegido.

## SAML de Exemplo

#### Requisição SAML do Google Apps

google.com

]]>

#### Resposta SAML do Identity

* Nesse exemplo pode ser observado que os campos *Nome, Sobrenome, e-mail, ID do Usuário no Identity, ID da Empresa no Identity,* estão inseridos dentro da *tag* **<saml2:AttributeStatement>.**

TotvsLabs












9+6FhzqbZL7vkh8OdkT1OrVhKD0=
HgV4uqJcqsgbWsHPou6K9x43LxHUU7Fh3Ey0DTEAnc5ZiEPfFVtRMwLXAp6AcZwf+VJCS+kLLy2qaj/inBUn0+sOYUvL7Kz7yCDnwmGlxr2nR47LghVUi0pf9Y+ntd9CF5A38DfJ0bT9TnlnR2imsDnhfS+fPd5581MMD3kzxB4=


MIICBjCCAW8CBgFkKLewqzANBgkqhkiG9w0AAQsFADBJMSYwJAYDVQQLEx1Ub3R2c0xhYnMgUHJp bWFyeSBDZXJ0aWZpY2F0ZTESMBAGA1UEChMJVG90dnNMYWJzMQswCQYDVQQGEwJVUzAeFw0xODA2 MjIxODE4MDRaFw0yODA2MjIxODE4MDRaMEkxJjAkBgNVBAsTHVRvdHZzTGFicyBQcmltYXJ5IENl cnRpZmljYXRlMRIwEAYDVQQKEwlUb3R2c0xhYnMxCzAJBgNVBAYTAlVTMIGfMA0GCSqGSIb3DQEB
AQUAA4GNADCBiQKBgQCSTmcVLlj7K58TlSqCG6m51mSQlH0hPN5z0T2iMs/d30f8udnm75nla2OJ ktdDu8Jm8/XcCFoMfyKnkZojZgRPaFOqWjhh9/nYCcm8wGGFko3WYqrzmKzVtiJZ1+PfQdd5yXCe ao8Gevt46Ssfh7mLWSU4c+DcB5wWr9jM4ejVeQIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAGxtZ6kP p+KRw0kpoqmRfY5B8ze7EmRMKvPtuJgtc4S912UWcXpTDPA+lLfOBB8E59U4KOV/1BLb2I3dH9D4
HybsurH96bJo44NJrApyQA+XNcLy/ax+PXB5405q2+bwemtuCvYkfdhAZrK334vNcVirJ5N5rPBb P4cm2mfCu/UK




TotvsLabs












ZcXfbLyk/2FGOXZdABQt8QfBGdU=
QO5XUdUJGbsGlAJ17oxFFv4NrtVT4G9Nay4jVEbi3x47oySLA+52plIe51rOBVCuUVR6IvDWBXrPgDb9szEveCcy8X8oX1EXpXTBpqdP6KQ4Oqz1bBY873+3XX51iYttXxtP3fapCzK/8uzI/JXJ+DqSUc76JrkT+SpeR+aogt4=


MIICBjCCAW8CBgFkKLewqzANBgkqhkiG9w0BAQsFADBJMSYwJAYDVQQLEx1Ub3R2c0xhYnMgUHJp bWFyeSBDZXJ0aWZpY2F0ZTESMBAGA1UEChMJVG90dnNMYWJzMQswCQYDVQQGEwJVUzAeFw0xODA2 MjIxODE4MDRaFw0yODA2MjIxODE4MDRaMEkxJjAkBgNVBAsTHVRvdHZzTGFicyBQcmltYXJ5IENl cnRpZmljYXRlMRIwEAYDVQQKEwlUb3R2c0xhYnMxCzAJBgNVBAYTAlVTMIGfMA0GCSqGSIb3DQEB
AQUAA4GNADCBiQKBgQCSTmcVLlj7K58TlSqCG6m51mSQlH0hPN5z0T2iMs/d30f8udnm75nla2AJ ktdDu8Jm8/XcCFoMfyKnkZojZgRPaFOqWjhh9/nYCcm8wGGFko3WYqrzmKzVtiJZ1+PfQdd5yXCe ao8Gevt46Ssfh7mLWSU4c+DcB5wWr9jM4ejVeQIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAGxtZ6kP p+KRw0kpoqmRfY5B8ze7EmRMKvPtuJgtc4S912UWcXpTDPA+lLfOBB8E59U4KOV/1BLb2I3dH9D4
HybsurH96bJo44NJrApyQA+XNcLy/ax+PXB5405q2+bwemtuCvYkfdhAZrK334vNcVirJ5N5rPBb P4cm2mfCu/UK

abc@totvs.com



https://www.google.com/a/totvs.com.br/acs


urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport


ft0y84vo717g8hjx

Name

false

false

ywam6h95jgk32fiq1407765456714

abc@totvs.com

Silva
 ]]>
 ]]>
