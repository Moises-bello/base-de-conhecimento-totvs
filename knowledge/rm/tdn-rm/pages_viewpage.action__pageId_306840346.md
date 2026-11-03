---
content_hash: fc398cc25e2f07d17f09057820469e62be2fa9c2b6bab1ce4cefd7afa52725d1
fetched_at: '2026-06-29T00:08:43.771642+00:00'
page_id: '306840346'
product: rm
source: tdn-rm
title: DT Apresentar Lançamentos sem Conta Caixa no Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=306840346
version: 99
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
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-2959> |
| **País(es):** | *Informe o(s) Pais(es).* |
| **Banco(s) de Dados:** | *Oracle e MS-SqlServer* |
| **Tabelas Utilizadas:** | *FXCX, FLAN, FLANBAIXA, FLANRATCCU, FLANBAIXARATCCU* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Foi disponibilizado no fluxo de caixa a opção "Considerar Lançamento com Conta Caixa Vazia", no qual a coluna previsto irá apresentar dados dos lançamentos que não possui conta caixa.

## Procedimento para Utilização

       1.            Definir um lançamento sem conta caixa

       2.            No fluxo de caixa, marcar o parâmetro "Considerar Lançamento com Conta Caixa Vazia".

       3.            Dados do lançamento sem conta caixa será apresentado na coluna Previsto.

divs
