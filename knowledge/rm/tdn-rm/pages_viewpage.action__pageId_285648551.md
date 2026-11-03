---
content_hash: 9b32e0ed1890553b00aa7c306cc3d9622ae5127e68e4e52b6523b1ccdf3bcd85
fetched_at: '2026-06-29T00:08:38.331280+00:00'
page_id: '285648551'
product: rm
source: tdn-rm
title: DT INCLUSÃO DE BOLETO PARCIAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285648551
version: 104
---

# Inclusão de Boleto com valor parcial

## Inclusão de Boleto

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Inclusão de Boleto.* | *Inclusão de Boleto* | |
| **Cadastros Iniciais:** | *Lançamentos, Convênio, Conta/Caixa.* |
| **Parâmetro(s):** | *Inclusão a Receber, Permitir inclusão de boleto parcial* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produçãokey,summary,type,created,updated,due,assignee,reporter,priority,status,resolution0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1111 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL, Oracle* |
| **Tabelas Utilizadas:** | *FLAN, FBOLETO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição:

Criação de um parâmetro para permitir a inclusão de boleto com valor parcial.

Parâmetro por coligada.

## Procedimento para Utilização

Definir os parâmetros de inclusão de lançamento conforme imagem abaixo.

**Importante**: Somente será permitido marcar o parâmetro, caso o parâmetro *Financeiro > Contas a Receber > Baixas > Baixa a Receber > Não gerar outro boleto para lançamento após baixa parcial* estiver desmarcado.

No processo de inclusão de boleto de cobrança, será apresentado ao usuário a opção de gerar um boleto com o valor parcial, conforme a tela abaixo:

Para gerar o boleto com valor parcial o usuário deverá marcar a opção "Gerar Boleto Parcial", e informar o valor que deseja gerar o boleto. O valor deverá ser menor que o valor liquido do lançamento.

## Vídeo

600400

divs
