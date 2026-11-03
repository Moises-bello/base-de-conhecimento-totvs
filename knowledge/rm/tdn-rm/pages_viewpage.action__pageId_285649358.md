---
content_hash: a82b28ec20677f9fd25332cda147381f6e1f8a67000b13bfc3c8cc61c96095a7
fetched_at: '2026-06-29T00:08:38.369341+00:00'
page_id: '285649358'
product: rm
source: tdn-rm
title: DT Permissão de Informar Vencimento na Inclusão de Boletos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285649358
version: 104
---

# Permissão de Informar Vencimento na Inclusão de Boletos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Inclusão de Boletos* | *Inclusão de Boletos.* | |
| **Cadastros Iniciais:** | **Lançamentos, Convênio, Conta/Caixa.*.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1129 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Sql-Server, Oracle* |
| **Tabelas Utilizadas:** | *FLAN, FBOLETO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Foi disponibilizado no Perfil do usuário a permissão "[02.01.01.103] - Permitir Informar Data de Vencimento na Inclusão de Boleto". Esse perfil tem como objetivo, liberar para o usuário, o preenchimento manual do parâmetro Vencimento no processo de inclusão de boletos.

## Procedimento para Utilização

       1.            Definir no perfil de usuário a permissão "[02.01.01.103] - Permitir Informar Data de Vencimento na Inclusão de Boleto"

       2.            No processo de Inclusão de Boletos o parâmetro "Vencimento" ficará desabilitado caso usuário não tenha permissão.

## Vídeo

600400

divs
