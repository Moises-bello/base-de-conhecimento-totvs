---
content_hash: 3b08645ce8dc114ada1e31ec16142f1e2ae74c8a6530d30733d1b379a1a6faec
fetched_at: '2026-06-29T00:08:36.158778+00:00'
page_id: '284464821'
product: rm
source: tdn-rm
title: DT_599078_MATFATCMPCRM01-137_Produtos_Inativos_Cotacao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_599078_MATFATCMPCRM01-137_Produtos_Inativos_Cotacao
version: 100
---

# Assistente de Cotação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, compras e faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Assistente de Cotação* | CmpAssistenteCotacaoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Inserir Itens na cotação* | CmpCotacaoInserirItemForm | |  |  | |
| **Cadastros Iniciais:** | *Não se Aplica* |
| **Parâmetro(s):** | *Não se Aplica* |
| **Ponto de Entrada:** | *Não se Aplica* |
| **Tickets relacionados** | 599078 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-137 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SqlServer e Oracle* |
| **Tabelas Utilizadas:** | *TPRODUTO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Foram criadas consistências para evitar que sejam incluídos produtos inativos na cotação.

A mensagem acima será exibida em dois momentos, são eles:

* Assistente de cotação: Ao selecionar os produtos e clicar em "Avançar".
* Processo "Inserir Itens Na Cotação": Ao selecionar os produtos e clicar em "Avançar".

divs
