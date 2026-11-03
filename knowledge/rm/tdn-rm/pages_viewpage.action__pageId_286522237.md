---
content_hash: 897850463f85a8bf7dea53cbf8b2c6b6e97be4e33fb331cb5bc4b9a518dc5449
fetched_at: '2026-06-29T00:08:41.272302+00:00'
page_id: '286522237'
product: rm
source: tdn-rm
title: DT Defaults natureza orçamentaria financeira créditos de adiantamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286522237
version: 108
---

# Defaults natureza orçamentária financeira créditos de adiantamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Parametrizador* | *Parametrização de defaults para natureza orçamentária financeira de lançamentos de crédito de adiantamento.* | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | NaturezaOrcamentariaDefaultCreditoAdiantamentoPagar  NaturezaOrcamentariaDefautlCreditoAdiantamentoReceber |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-701 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | FPARAM |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Parametrização de defaults de natureza orçamentária financeira para lançamentos de crédito de adiantamentos.

O objetivo destes parâmetros e possibilitar que sejam informados as natureza orçamentárias financeiras a pagar e a receber, estas informações serão utilizadas na inclusão dos lançamentos de crédito de adiantamento, onde, os rateios que existem no lançamento de adiantamento que estão dando origem ao lançamento de crédito de adiantamento, terá a sua natureza orçamentaria financeira substituída pelo default informado no parametrizador.

Desta forma, não é mais obrigatório a utilização da natureza orçamentaria ambos nos rateios relacionados ao lançamentos de adiantamento.

## Procedimento para Utilização

       1.            Nos parâmetros do sistema configurar o parâmetro "Rateio Centro Custo/Natureza Orçamentaria" com as opções  "Natureza" ou "Ambos".

       2.            Configurar as naturezas orçamentárias nos parâmetros "Natureza Orçamentaria Default de Crédito de Adiantamento a Receber" e "Natureza Orçamentaria Default de Crédito de Adiantamento a Pagar".

       3.            Após a parametrização, o processo de baixa do lançamento de adiantamento, irá utilizar as informações destes parâmetros para as naturezas dos rateios do lançamento de crédito de adiantamento.

Obs: A utilização dos valores dos parâmetros "Natureza orçamentaria default de crédito de adiantamento a pagar" e "Natureza orçamentaria default de crédito de adiantamento a receber", está condicionado, ao parâmetro "Rateio centro custo/natureza orçamentaria" estar configurado com as opções  "Natureza" ou "Ambos". 

* Adiantamentos com natureza orçamentaria financeira ambos e natureza orçamentaria default de crédito de adiantamento não informado no parametrizador:  
  Será mantido o comportamento já existente no sistema e os lançamentos de crédito de adiantamento terão as mesmas naturezas orçamentárias que existem no lançamento de adiantamento.

* Adiantamentos com rateios sem natureza orçamentária.  
  Nos casos em que houver rateios por centro de custo sem a natureza orçamentária no lançamento de adiantamento, o lançamento de crédito de adiantamento será incluído obedecendo a parametrização do sistema e o rateio terá a informação de natureza orçamentária cadastrada nos parâmetros "Natureza orçamentaria default de crédito de adiantamento a pagar" se o lançamento de crédito de adiantamento for a pagar e "Natureza orçamentaria default de crédito de adiantamento a receber" se o lançamento de crédito de adiantamento for a receber.

divs
