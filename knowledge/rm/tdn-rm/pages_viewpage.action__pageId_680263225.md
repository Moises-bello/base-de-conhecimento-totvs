---
content_hash: 4feaaadf8f8c738820ad73c6f367a4340affcb4db892558b873b04c8e01d00a3
fetched_at: '2026-06-29T00:11:17.454539+00:00'
page_id: '680263225'
product: rm
source: tdn-rm
title: DT - Folha Analítica por Dissídio - Criação do campo "Base INSS Liquida" e
  "Base INSS Dissidio Liquida"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680263225
version: 6
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Tratativa para abater o valor do campo "Estorno INSS" da "Base INSS". |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-3065 |

## **02. SITUAÇÃO/REQUISITO**

Tratativa na Folha Analítica por Dissídio.

* Criado os campos "Base INSS Liquida" e "Base INSS dissidio Liquida" nos totais por funcionário, categoria, seção e geral, dos relatórios txt (FOPREL0174) e PDF(FOL0175).
  + O valor do campo "Base INSS Liquida" será o valor da "Base de INSS" menos o valor do "Estorno Base INSS".
  + O valor do campo "Base INSS Dissidio Liquida" será o valor da "Base INSS Dissidio" menos o valor do campo "Estorno Base INSS Dissidio".

**03. SOLUÇÃO**

   Criado os campos abaixo na folha analitica por dissídio.
