---
content_hash: 9dbf90acacceabd3678cf6f2a70c89ceccf0a455a56eab230df329e03977dd5d
fetched_at: '2026-06-28T21:35:19.773706+00:00'
page_id: '223180790'
product: fluig
source: tdn-fluig
title: WCM - Por que não consigo visualizar páginas HTTPS pelo widget Endereço WEB?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223180790
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.6.2

**Ambiente:** Windows e Linux

# Ocorrência

Não consigo exibir o conteúdo de páginas HTTPS através do *widget* [Endereço WEB](http://tdn.totvs.com/pages/viewpage.action?pageId=234455977#Widgets.-Endere%C3%A7oWEB) em meu Fluig Plataforma.

# Causa

O problema ocorre porque o Fluig utilizado não possui contexto seguro (ou seja, é HTTP) e está tentando acessar um site com contexto seguro (HTTPS). O depurador do navegador (tecla F12) exibe mensagens semelhantes às relacionadas abaixo:

jsErro

# Solução

Existem duas possíveis soluções para este problema: implantar segurança de contexto ([HTTPS](http://tdn.totvs.com/x/D4CgBw)) no Fluig Plataforma conforme a documentação  ou, se possível, trocar a página configurada no *widget* Endereço WEB por uma opção sem contexto seguro (HTTP).
