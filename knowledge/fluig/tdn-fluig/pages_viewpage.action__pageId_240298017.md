---
content_hash: 84f9c3829c38a5d6f11669179ef3f7c44ae6e1bc90e5957529919827c4bd0654
fetched_at: '2026-06-28T21:35:22.806230+00:00'
page_id: '240298017'
product: fluig
source: tdn-fluig
title: IDE - Mensagem "SAML message intended destination endpoint did not match recipient
  endpoint" ao acessar a plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240298017
version: 15
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

**Versão:** 1.5 ou superior

# Ocorrência

Ao tentar realizar o acesso na plataforma a partir do Identity, é apresentada a mensagem abaixo na tela de login:

# Causa

Foi configurado o *proxy* reverso (sem SSL), porém não foi realizada a configuração do conector no arquivo **standalone.xml** (a partir da atualização 2.0), **domain.xml** (da atualização 1.6 até a 1.8.2) ou  **standalone.xml** (até a atualização 1.5.13).

# Solução

Revisar a configuração do *proxy* reverso, de acordo com o tópico "Configuração do Apache (sem SSL)" conforme a documentação de .

Verificar se o protocolo é HTTP ou HTTPS. Esses protocolos devem ser iguais na plataforma (wcmadmin) e no Identity (nas configurações do aplicativo).
