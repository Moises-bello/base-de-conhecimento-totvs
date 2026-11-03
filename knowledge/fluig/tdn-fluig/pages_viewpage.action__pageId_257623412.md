---
content_hash: fce86fc8cbbf361662725568e9e50e8de70e60beab38aac3a6b033653d620782
fetched_at: '2026-06-28T21:35:23.633865+00:00'
page_id: '257623412'
product: fluig
source: tdn-fluig
title: Configurações para autenticação em múltiplos servidores AD com protocolo LDAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257623412
version: 12
---

Fique atento!

Esta página foi revisada para considerar as configurações de server do TOTVS Fluig **a partir** da atualização **1.6**.

.\*ndice

# Objetivo

---

O objetivo deste guia é apresentar as configurações válidas para a autenticação em múltiplos servidores AD utilizando o protocolo LDAP (*Lightweight Directory Access Protocol*).

# Autenticação em múltiplos servidores AD com protocolo LDAP

---

Para definir as configurações, é necessário efetuar os passos a seguir de acordo com a atualização do Fluig que você utiliza:

0.5falsesamplesfadetrue1Passo 1

* **A partir da atualização 2.0:**Edite o arquivo **standalone.xml** ([diretório\_instalação]/appserver/standalone/configuration/standalone.xml).

* **Para atualizações 1.6 até 1.8.2**:  
  Edite o arquivo **domain.xml** ([diretório\_instalação]/appserver/domain/configuration/domain.xml).

true2Passo 2

* No arquivo correspondente à atualização do Fluig que você utiliza (standalone.xml ou domain.xml), procure o trecho de código abaixo:

  html/xml







  ]]>
3Passo 3

* Substitua a estrutura de *tags* **login-module** pela seguinte estrutura:

  html/xml





























  ]]>

4Passo 4

* Caso seja necessário utilizar também a autenticação pelos dados do banco de dados, deve ser adicionada também a seguinte estrutura de *tag* **login-module**:

  html/xml



  ]]>
