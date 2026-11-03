---
content_hash: 5a3a731452edcfbd9de00f9d2e64457c0cf4fd6eb574e81385d9b820eac0facc
fetched_at: '2026-06-29T00:08:43.887775+00:00'
page_id: '307832095'
product: rm
source: tdn-rm
title: DT Valor Líquido no Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307832095
version: 95
---

# Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Fluxo de Caixa.* | *Fluxo de Caixa.* | |
| **Cadastros Iniciais:** | *Conta Caixa, Rateios, Natureza, Lançamentos, Baixa, Extratos* |
| **Parâmetro(s):** | *Usa Rateio Para: Ambos*  *Obrigatoriedade do Rateio: Obrigatório Sempre* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-2958> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Oracle e MS-SqlServer* |
| **Tabelas Utilizadas:** | *FXCX, FLAN, FLANBAIXA, FLANRATCCU, FLANBAIXARATCCU* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Permitir que usuário possa definir o valor previsto do lançamento como valor original, valor líquido ou valor líquido na data de vencimento

## Procedimento para Utilização

       1.            Definindo valor previsto como "Valor Original": Opção Default no qual leva em consideração o valor original do lançamento

       2.            Definindo Valor previsto como "Valor Líquido na Data Atual": É feito o calculo do valor líquido levando em consideração a data do sistema

       3.            Definindo Valor previsto como "Valor Líquido no Vencimento": É feito o calculo do valor líquido levando em consideração a data de vencimento do lançamento

divs
