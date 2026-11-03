---
content_hash: 36fc7e4cfee52ce58f18e0d681c3b07fee66b1462c88e3885551ceaafed80e9a
fetched_at: '2026-06-29T00:09:08.415748+00:00'
page_id: '388235961'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-3043 DT Informações de Item/Combustível no Cadastro de Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=388235961
version: 3
---

# CAMPOS DE ITEM/COMBUSTÍVEL NO CADASTRO DE PRODUTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Cadastro de Produto. |
| **Situação/Requisito:** | Em atendimento a NF-e 4.0 se torna necessário informar os percentuais de mistura do GLP em um grupo específico para informações sobre combustíveis. |
| **Solução/Implementação:** | Criação dos campos que irá compor o grupo LA. Item / Combustível no XML da NF-e 4.0. |
| **Conversores e Parâmetros:** | Cadastros | Produtos | Edição do Produto | Aba Detalhes | Outros Dados. |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | MATESTCNTFTOF01-3043. |
| **Documento de Referência:** | [Cadastro de Produto](http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Produto.aspx). |

## Descrição

Após a execução do script necessário para a criação dos campos. Siga os passos abaixo para informar os percentuais de mistura do GLP no cadastro de produto:

1. Acesse o Cadastro de Produto | Edição do Produto | Aba Detalhes | Sub-aba Outros Dados | Preencha os percentuais nos novos campos criados, conforme figura abaixo:

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.18.341 e posteriores deste chamado.

## Dicionário de Dados

**Arquivo ou Código do Script:**/\*$Versao=NU.2018.08\_01\*/

|  |  |
| --- | --- |
| **Tabela** | TPRODUTODEF |
| **Campo** | PERGLPPROD  PERGLGNNACPROD  PERGLGNIMPPROD  VALORPARTIDA |
| **Tipo** | decimal. |
| **Tamanho** | 15,4  VALORPARTIDA: 13,2 |
| **Valor Inicial** | Não se aplica. |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Percentual Derivado do Petróleo no Produto GLP.  Percentual de Gás Natural Nacional para o Produto GLP.  Percentual de Gás Natural Importado para o Produto GLP.  Valor de Partida por Quilograma sem ICMS. |
| **Título** | GLP. |
