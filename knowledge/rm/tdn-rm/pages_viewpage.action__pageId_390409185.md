---
content_hash: fc66f23e60c505624e5c47a4e74ce1559a375a0eb8c9d2eac4606963da97f093
fetched_at: '2026-06-29T00:09:08.993799+00:00'
page_id: '390409185'
product: rm
source: tdn-rm
title: FINANCEIRO01-8561 DT Cobrança padrão CNAB240 para Banco CECRED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=390409185
version: 2
---

# Remessas de cobrança para o banco CECRED

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Retorno de Cobrança CNAB240 | Retorno de Cobrança CNAB240 |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Inclusão de Lançamentos | Inclusão de Lançamentos | | Inclusão de Boletos | Inclusão de Boletos | | Remessa de Cobrança CNAB240 | Remessa de Cobrança CNAB240 | |
| **Cadastros Iniciais:** | Inclusão de Lançamentos  Inclusão de Boletos  Remessa de Cobrança |
| **Parâmetro(s):** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FINANCEIRO01-8561 |
| **País(es):** | Brasil |
| **Tabelas Utilizadas:** | FLAN  FLANBOLETO  FBOLETO |

## Descrição

Constatamos que o retorno de cobrança para o banco CECRED é 100% compatível com o padrão CNAB 240

## Procedimento para Implantação

1. Proceder o cadastramento do banco / agência / conta.
2. Proceder o cadastramento da conta caixa, associar ao banco / agência / conta informado no passo 1.
3. Proceder o cadastramento do convênio associado à conta caixa informada no passo 2.
4. Importar o layout de remessa de cobrança compatível com CNAB240,
