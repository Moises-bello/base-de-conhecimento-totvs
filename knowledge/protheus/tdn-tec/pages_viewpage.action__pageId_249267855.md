---
content_hash: e599f2f65e3b57982bc3f242c61e4ae1bc0b7e96eb760503bd87221c067e9af9
fetched_at: '2026-07-02T19:24:20.461481+00:00'
page_id: '249267855'
product: protheus
source: tdn-tec
title: Execução de uma linha de comando muito extensa não era executada por limitação
  de caracteres do Appserver
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=249267855
version: 3
---

Execução de uma linha de comando muito extensa não era executada por limitação de caracteres do Appserver

|  |  |
| --- | --- |
| Situação | Ao executar uma linha de comando muito extensa ocorria o erro: Insufficient Buffer on tString::sprintf() |
| Ocorrência | Execução de uma linha de comando muito extensa através do comando RUN <comando> ou comando REPORT TO PIPE <comando> por limitação de caracteres do Appserver gerava erro. |
| Correção | Aumentado o limite de caracteres. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: TTEC-611 * Disponível em builds superiores a 7.00.131227A - 1.0.3 |
