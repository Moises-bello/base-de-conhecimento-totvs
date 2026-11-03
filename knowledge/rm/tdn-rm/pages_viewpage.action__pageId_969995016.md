---
content_hash: 2d73c6d184151e067208fd9dbadff8ad3cac170a93b7ae02c58748adedef72a6
fetched_at: '2026-06-29T00:12:15.109528+00:00'
page_id: '969995016'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Melhoria no filtro "Data de Afastamento"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969995016
version: 5
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Integração RM x Ahgora - Melhoria no filtro "Data de Afastamento" |
| País: | Brasil |
| Épico | [DRHROTRM-11995](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11995) |

## **02. VERSÃO**

* 12.1.2410.274
* 12.1.2502.178
* 12.1.2506.121 e superiores.

## **03. S****ITUAÇÃO/REQUISITO**

Melhoria no filtro "Data Afastamento De" e "Data Afastamento Até" para que o sistema considere os funcionários que tiveram afastamentos dentro do período informado, ou seja, com datas de afastamento compreendidas entre os dois parâmetros.

## **04. SOLUÇÃO**

Adequação no filtro "**Data Afastamento De**" e "**Data Afastamento Até**", o filtro deverá ser ajustado para identificar os funcionários que tiveram afastamentos dentro do período informado, considerando os seguintes cenários:

1. Afastamentos **iniciados dentro do período**, sem data de término (término em aberto);
2. Afastamentos **iniciados e finalizados dentro do período informado**;
3. Afastamentos **iniciados antes ou durante o período**, com término após o período informado;
4. Afastamentos com **data de término dentro do período**, mesmo que iniciados anteriormente.

**Exemplo:**  
Para o período de filtro **01/01/2025 a 31/01/2025**, devem ser exibidos os afastamentos que atendam à seguinte condição: Afastamentos iniciados <= 31/01/2025 e (terminam >= 01/01/2025 ou NULL) são mostrados em tela

Esses critérios garantem que funcionários atualmente ativos, mas que tiveram afastamentos em qualquer momento dentro do período informado, sejam devidamente considerados no resultado.

## **05. DEMAIS INFORMAÇÕES**

[Integração RM X Ponto Web (Ahgora)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=877866931)
