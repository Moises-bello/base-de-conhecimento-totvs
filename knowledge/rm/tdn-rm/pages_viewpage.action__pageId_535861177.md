---
content_hash: 66cfb0985a7ecb4c5994dc1805034debcc113a6b10c1aa3513ac90388248d0d7
fetched_at: '2026-06-29T00:10:37.141066+00:00'
page_id: '535861177'
product: rm
source: tdn-rm
title: DT - Status Concluído e Parcialmente Concluído
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535861177
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, compras e faturamento |
| Função: |  |
| Ticket: | 1293382 |
| Requisito/Story/Issue (informe o requisito relacionado) : | MATFATCMPCRM01-1114 |

## **02. SITUAÇÃO/REQUISITO**

O sistema não exibe de forma clara, quais movimentos passaram pelo processo de "Conclusão de movimento"

## **03. SOLUÇÃO**

Foi criado um novo campo na tabela de movimentos (**TMOV.STSCONCLUIDO**). O qual tem como objetivo sinalizar quais movimentos foram submetidos ao processo de conclusão.

Este campo pode conter os seguintes valores:

* Parcialmente concluído (**P**): Nem todos os itens foram completamente concluídos.
* Concluído (**C**): O movimento foi completamente concluído.
* Vazio: O processo responsável pela conclusão de pedidos não foi executado para este movimento.
