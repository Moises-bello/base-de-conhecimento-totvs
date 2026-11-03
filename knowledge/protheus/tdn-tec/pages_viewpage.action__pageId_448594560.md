---
content_hash: 00fe981bb7b2f5c9edf15a4c22d2372130244322036d4e30c799e1ad56c7cf91
fetched_at: '2026-07-02T19:24:23.350424+00:00'
page_id: '448594560'
product: protheus
source: tdn-tec
title: TPaintPanel - Quebra de linha no método addShape
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448594560
version: 1
---

Quebra de linha no metodo addShape para o caracter pipe |

|  |  |
| --- | --- |
| Situação | Mesmo havendo o caracter pipe | , o componente não estava inserindo a quebra de linha. |
| Correção | Incluído tratamento para inserir quebra de linha sempre que houver caracter pipe no método addShape. |
| Informações adicionais | * Referente ao ticket: não há ticket associado * Referente à ocorrência: SCHTML-792 * Disponível a partir da build 7.00.131227A - 4.2.2 |
