---
content_hash: 340caaf833a15db90a93d37108063df63b19bb5fff43a0f27d8ac160e8c5c395
fetched_at: '2026-06-29T00:08:40.805771+00:00'
page_id: '286506978'
product: rm
source: tdn-rm
title: DT Conta Transitória
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286506978
version: 104
---

# Conta Transitória

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Inclusão de Boleto* | Lançamento - Boleto | |  |  | |
| **Cadastros Iniciais:** | *Cadastro da Conta Transitória no cadastro de Convênio* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1749 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | *SQL-Server, Oracle* |
| **Tabelas Utilizadas:** | *FBOLETO, FCONVENIO.* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

A funcionalidade da Conta Transitória, tem como objetivo de gerar e emitir um boleto buscando os dados para composição do nosso número e código de barras da conta transitória (Conta de Cobrança) cadastrada no Convênio, sendo que a baixa/retorno ocorrerá na conta normal (conta movimento).

## Procedimento para Configuração

No cadastro de Convênio, aba Conta Transitória, preencha os campos da Agência Transitória e Conta Transitória. (Utilizamos do banco Itau como exemplo)

## Procedimento para Utilização

Inclua um lançamento e gere um boleto para o mesmo. Note que o nosso número e o código de barras foi gerado com base a conta transitória.

divs
