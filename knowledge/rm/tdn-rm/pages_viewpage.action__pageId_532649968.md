---
content_hash: 91219108987c8b880aa8c00ee41fbcdfb76c366532ac0adf45d5bc9885d284c6
fetched_at: '2026-06-29T00:10:36.481346+00:00'
page_id: '532649968'
product: rm
source: tdn-rm
title: 6175701 FISCAL01-10370 DT Geração do Arquivo DCTF - Ficha 10
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532649968
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração do Arquivo DCTF |
| Ticket: | 6175701 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10370 |

## **02. SITUAÇÃO/REQUISITO**

Ao validar a DCTF foi apresentado a seguinte mensagem:  
Registro 00006 - Tipo R10 \ Erro - Registro em duplicidade.

Ao gerar DCTF com informações de débitos na ficha 10 de filiais SCP ocorre erro de duplicidade no validador oficial DCTF.

## **03. SOLUÇÃO**

Na geração do arquivo DCTF foi implementado o agrupamento do registro Tipo 10 da filial matriz com dados de guia da filial SCP.
