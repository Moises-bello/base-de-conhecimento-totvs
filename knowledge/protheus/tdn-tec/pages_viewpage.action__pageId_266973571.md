---
content_hash: 76eec5a7e5fd6b01c50112f067ab106e4b7ab8af69237734beba5e86854872d8
fetched_at: '2026-07-02T19:24:21.324111+00:00'
page_id: '266973571'
product: protheus
source: tdn-tec
title: 4GL - Access Violation ao usar a função CHANNEL:READ()
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266973571
version: 2
---

4GL - Access Violation ao usar a função CHANNEL:READ()

|  |  |
| --- | --- |
| Situação | 4GL - Access Violation ao usar a função CHANNEL:READ() |
| Ocorrência | Ao ler o caractere ASC 00 utilizando a função CHANNEL:READ() ocorria Access Violation no AppServer |
| Correção | Proteção na função CHANNEL:READ() para leitura de ASC 00 |
| Informações adicionais | * Referente ao chamado: TSQTDE * Referente à ocorrência: TTEC-618 * Disponível em builds superiores a 7.00.131227A - 1.0.3 |
