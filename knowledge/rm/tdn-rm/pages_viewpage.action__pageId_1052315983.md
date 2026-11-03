---
content_hash: 454f0129f8bf7aadd35de5093e494da3a2ed5273a85d5c3285e9d905bdb5d6cd
fetched_at: '2026-06-29T00:05:51.576052+00:00'
page_id: '1052315983'
product: rm
source: tdn-rm
title: Execução em Segundo Plano
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1052315983
version: 1
---

# Índice:

---

* [Objetivo:](https://tdn.totvs.com/display/LRM/Utilizando+o+DBMonitor#UtilizandooDBMonitor-Objetivo:)
* [Introdução:](https://tdn.totvs.com/display/LRM/Utilizando+o+DBMonitor#UtilizandooDBMonitor-Introdu%C3%A7%C3%A3o:)
* [Configuração:](https://tdn.totvs.com/display/LRM/Utilizando+o+DBMonitor#UtilizandooDBMonitor-Configura%C3%A7%C3%A3o:)

# Objetivo:

---

Este documento objetiva esclarecer como Ativar ou Desativar a integração OIDC (OpenID Connect).

# Introdução:

---

O OpenID Connect (OIDC) é um protocolo de segurança que permite que você acesse o sistema usando uma conta que você já possui (como seu e-mail corporativo).

Configuração:

---

Para que o OIDC funcione, é necessário seguir os passos abaixo:

* Habilitar nos parâmetros globais do sistema a opção "Execução em segundo plano".

     Menu Ambiente | Parâmetros | Parâmetros Globais  
  
  
  
Acesse a guia Execução em segundo plano e marque a opção Cadastrar URLs de redirecionamento OIDC automaticamente

falseNOTAS

* Tabela responsável pelo cadastro das URL's SELECT \* FROM GOIDCREDIRECTURLS
