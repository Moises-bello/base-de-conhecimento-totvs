---
content_hash: dc889cc192f772f63598b2d1e332547d3e33c90697f5eae6f1fb8ee4fc3138d2
fetched_at: '2026-06-29T00:10:30.408627+00:00'
page_id: '520094308'
product: rm
source: tdn-rm
title: FISCAL01-11259 DT Layout TAF - Alteração T154
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520094308
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | TAF |
| Ticket: | FISCAL01-11259 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11259 |

## **02. SITUAÇÃO/REQUISITO**

1. Alterar a descrição e remover a ligação dos campos 13 ao 37, 41 e 42. Nova descrição: OBSOLETO.

2. Atualizar o layout incluindo o campo 46:

|  |  |  |  |
| --- | --- | --- | --- |
| Nº | Campo | Descrição | Origem da Informação |
| 46 | UNQ\_INT | ID de integração única. | ID utilizado para controlar se um registro deverá ser alterado na integração. |

## **03. SOLUÇÃO**

Campos 13 ao 37, 41 e 42 alterados para OBSOLETO.

Layout atualizado como o novo campo de nº 46 (UNQ\_INT) adicionado

## **04. DEMAIS INFORMAÇÕES**

Os campos não possuem ligação com o contexto(será implementado em outra issue).
