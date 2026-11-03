---
content_hash: 21c786060944e6531004ac481c3542dbcb1fe6e9d3acf1c1b37aa278b765c03f
fetched_at: '2026-07-02T19:24:23.201894+00:00'
page_id: '271177994'
product: protheus
source: tdn-tec
title: 4GL - Servidor Linux abortando ao utilizar CHAR na função OutputConsoleLog
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271177994
version: 3
---

|  |  |
| --- | --- |
| Situação | 4GL - Servidor Linux abortando ao utilizar CHAR na função OutputConsoleLog |
| Ocorrência | Ao utilizar a função 4GL OutputConsoleLog enviando o segundo parâmetro como variavel CHAR, ocorre queda do AppServer. |
| Correção | Correção no tratamento do segundo parâmetro que quando passado como char(n), não estava sendo tratado corretamente gerando estouro de variável. |
| Informações adicionais | * Referente à ocorrência: TTEC-994 |
