---
content_hash: 07842db4f16876c8712ee3bf644d0f5213afddecc4e713488139f73adbbc5393
fetched_at: '2026-06-28T21:35:19.030109+00:00'
page_id: '189305418'
product: fluig
source: tdn-fluig
title: ARQ - O que devo saber sobre a primeira inicialização da atualização 1.5 com
  LMS?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189305418
version: 12
---

Atenção

Página destinada a atualizações anteriores a release 1.5.

# Índice

true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar as características da primeira inicialização do TOTVS Fluig Plataforma com o *card* LMS.

# Inicialização LMS

Com a entrada do novo *card* de LMS, a primeira inicialização do servidor da plataforma pode ser afetada.

Existem dois fatores que afetam diretamente a primeira inicialização do *card* de LMS dentro da plataforma:

* criação da estrutura de banco de dados do LMS;
* integração dos dados de empresa, grupos, usuários e volume.

# Sobre a criação do banco de dados LMS

O LMS se une à plataforma com mais de **210** novas tabelas, representando aproximadamente **40%** do tamanho total do banco de dados do produto na versão 1.5.

A criação dessa estrutura pode demorar de acordo com o banco de dados utilizado. Cada banco de dados tem características diferentes para a criação da estrutura.

# Sobre a integração do LMS

Durante a primeira inicialização, o LMS busca todas as informações de empresa, grupos, usuários e volume das tabelas da plataforma.

Todas as informações encontradas são reestruturadas nas tabelas no LMS, com o objetivo de disponibilizar os ambientes de Aprendizado e de Avaliações para todos os usuários e empresas já existentes.
