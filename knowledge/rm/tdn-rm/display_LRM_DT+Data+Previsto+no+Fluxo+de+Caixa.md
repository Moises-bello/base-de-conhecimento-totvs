---
content_hash: 13a1830090c079f301a31acc22f446926107c5548d530a7b90a43563606d2ad6
fetched_at: '2026-06-29T00:08:46.327686+00:00'
page_id: '316998977'
product: rm
source: tdn-rm
title: DT Data Previsto no Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Data+Previsto+no+Fluxo+de+Caixa
version: 101
---

# Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | **Fluxo de Caixa** | **Fluxo de Caixa** | |
| **Cadastros Iniciais:** | **Conta Caixa, Rateios, Natureza, Lançamentos, Baixa, Extratos*.* |
| **Parâmetro(s):** | *Usa Rateio Para: Ambos*  *Obrigatoriedade do Rateio: Obrigatório Sempre* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *<http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-2967>* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | **Oracle e MS-SqlServer** |
| **Tabelas Utilizadas:** | **FXCX, FLAN, FLANBAIXA, FLANRATCCU, FLANBAIXARATCCU** |
| **Sistema(s) Operacional(is):** | **Windows** |

## Descrição

Permitir que usuário possa definir a data a ser considerada para a coluna previsto através da data prevista que pode ser a data de vencimento ou a data previsão de baixa para o cálculo do valor do lançamento como valor original, valor líquido ou valor líquido na data de vencimento / previsão de baixa.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Nos Parâmetros do Financeiro | Contas a Pagar / a Receber | Recursos Adicionais parametrizar conforme abaixo:

## Procedimento para Utilização

       1.       No fluxo de caixa, definindo a data previsto como "Data de vencimento" ou "Data de Previsão de Baixa" e valor previsto como "Valor Original", conforme abaixo.

                 A opção no qual leva em consideração o valor original será na data de vencimento ou de previsão de baixa do lançamento conforme a parametrização da data previsto.

       2.       Definindo a data previsto como "Data de vencimento" ou "Data de Previsão de Baixa" e valor previsto como "Líquido na Data Atual", conforme abaixo.

                 O cálculo do valor líquido será feito levando em consideração a data do sistema. Atenção: O valor será adiciona a coluna da data conforme a parametrização da data previsto.

      3.       Definindo a data previsto como "Data de vencimento" ou "Data de Previsão de Baixa" e valor previsto como "Líquido no Vencimento / Previsão de Baixa", conforme abaixo

                 O calculo do valor líquido será feito levando em consideração a data de vencimento / previsão de baixa do lançamento conforme a parametrização da data previsto.

divs
