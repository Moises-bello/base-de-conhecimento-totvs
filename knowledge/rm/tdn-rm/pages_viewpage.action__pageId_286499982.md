---
content_hash: 16984c693423c0cf9b5750775d1c4c48a1ec65616b4b07f7af9840b3a8f99ede
fetched_at: '2026-06-29T00:08:40.738786+00:00'
page_id: '286499982'
product: rm
source: tdn-rm
title: DT Visualização de XML/JSON do Registro Online no Boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286499982
version: 106
---

# Visualização de XML/JSON enviados no Registro Online de Boletos

## Registro Online

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Registro Online de Boletos* | *Registro Online de Boletos* | |
| **Cadastros Iniciais:** | *Lançamentos, Convênio, Conta/Caixa, Certificado Digital* |
| **Parâmetro(s):** | *Não se aplica* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [FINANCEIRO01-1886](http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-1886) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL, Oracle* |
| **Tabelas Utilizadas:** | *FBOLETO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Foram definidos novos campos na tabela de boletos para registrar os dados enviados aos bancos, no processo de Registro Online de Boletos, em formato XML ou JSON.

## Procedimento para Utilização

Execute o Registro Online de Boletos, através da visão de boletos:

Se houver erro no processo de envio de dados para o banco, o sistema irá abortar o processo de envio de boletos com uma mensagem de erro:

Mas os dados enviados ao banco em formato JSON ou XML ficarão registrados no cadastro de boletos, estes dados poderão ser visualizados utilizando o Notepad do Windows ao clicar no botão ao lado direito:

**Observação:**

Alguns bancos transformam os dados do JSON ou XML de envio por intermédio de uma assinatura digital, nestes casos os dados devidamente assinados são registrados em campo específico.

divs
