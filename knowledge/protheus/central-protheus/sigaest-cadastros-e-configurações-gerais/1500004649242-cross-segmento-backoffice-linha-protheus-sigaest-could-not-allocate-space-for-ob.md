---
article_id: 1500004649242
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: ce986c0896279678b7506e60046ff5ecf599a448782aa7c533994b530b3621f5
fetched_at: '2026-06-28T22:39:08.000223+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - "Could not allocate
  space for object 'dbo.Tabela' in database 'NomeBancodeDados'" em Rotinas do Estoque
type: support-article
updated_at: '2021-09-30T12:58:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004649242-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Could-not-allocate-space-for-object-dbo-Tabela-in-database-NomeBancodeDados-em-Rotinas-do-Estoque
---

**Ocorrência**Em determinadas rotinas do Protheus, no módulo de Estoque/Custos, ao entrar com uma informação que será alimentada em uma (ou mais) tabelas do Banco de Dados, é apresentado o error.log *"Could not allocate space for object 'dbo.Tabela' in database 'NomeBancodeDados'"*

**Ambiente**Microsiga Protheus - Estoque/Custos - A partir da versão 12.1.17

**Causa**Este incidente ocorre quando, na tabela que será alimentada, não há mais espaço em disco para criação de novos registros.

**Solução**Como essa inconsistência é apresentada quando não existe espaço em disco para crescimento do Banco de Dados em relação à uma tabela em específico do Banco de Dados, a recomendação do Suporte Técnico da TOTVS é de que, sempre que ocorrer este problema, seja solicitado o apoio interno do DBA da Empresa (Administrador do Banco de Dados). Problemas de infraestrutura como espaço no Banco de Dados não dispõe de rotinas ou processos padronizados do Protheus para correção.

Após o espaçamento do Banco de Dados ser corrigido pelo responsável do Banco de Dados da Empresa, não ocasionará mais erro na criação implícita de registros nestas tabelas.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
