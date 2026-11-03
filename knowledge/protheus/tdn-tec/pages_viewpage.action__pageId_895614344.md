---
content_hash: a29effa025e19b22eb70ba4f83a0572191ff5d06ee4f58fd92393801857b02dd
fetched_at: '2026-07-02T19:24:29.463916+00:00'
page_id: '895614344'
product: protheus
source: tdn-tec
title: Correção - Errorlog quando um TCBrowse é limpo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=895614344
version: 1
---

Foi evitado um errorlog quando um TCBrowse é limpo em tempo de execução.

|  |  |
| --- | --- |
| Situação | Ao limpar os registros de um TCBrowse é gerado errorlog na execução do bLine. |
| Ocorrência | Mesmo sem registros é disparado o codeblock do bLine porém um nAt zerado, que ocasiona o problema. |
| Correção | O disparo do bLine não é feito caso não hajam registros no TCBrowse. |
| Informações adicionais | * Referente ao chamado: #21602059 * Referente à ocorrência: DTCLIENT01-5178 * Disponível em builds superiores a 20.3.2.9 |
