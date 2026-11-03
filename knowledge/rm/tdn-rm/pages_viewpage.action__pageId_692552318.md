---
content_hash: 89740af4eefc5c16619855fab49857c39ce21247b64f062c9ce9fcc789e038dd
fetched_at: '2026-06-29T00:11:21.314312+00:00'
page_id: '692552318'
product: rm
source: tdn-rm
title: FISCAL01-18098 DT - Adicionar os campos no Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=692552318
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18098 |

## **02. SITUAÇÃO/REQUISITO**

Os campos dinâmicos devem ser adicionados no Lançamento Fiscal de forma semelhante ao comportamento do Movimento.

**Caminho dos campos:**  
BO Fiscal | Obrigações Principais | Lançamentos | Informações Adicionais | NF-e Estadual

BO Fiscal | Obrigações Principais | Lançamentos | Situação tributária | Item | Informações Adicionais | NF-e Estadual

## **03. SOLUÇÃO**

Foi Adicionado no lançamento fiscal a tela NFe Estadual, onde irá ter a listagem dos campos livres escriturados ou que foram incluídos no lançamento. Além disso, os campos podem ser importados, caso algum campo default já esteja cadastrado.

As alterações dos campos livres de um lançamento escriturado serão refletido no seu respectivo movimento.

Informações

Disponível partir da versão 12.1.33:

12.1.33.277 | 12.1.34.177 | 12.1.2205.116
