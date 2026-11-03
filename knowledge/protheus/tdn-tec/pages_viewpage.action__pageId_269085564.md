---
content_hash: 535fca17a0adb6b5445211a9e6eafbc4828e7971935e1abe9091b3d0ee427ca6
fetched_at: '2026-07-02T19:24:22.239433+00:00'
page_id: '269085564'
product: protheus
source: tdn-tec
title: Chave SERVERTYPE com valor 4GL não altera CASESENSITIVE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269085564
version: 2
---

Com a chave SERVERTYPE=4GL, o valor da chave CASESENSITIVE deveria ser definido automaticamente para 1

|  |  |
| --- | --- |
| Situação | Com a chave SERVERTYPE=4GL a chave CASESENSITIVE não é definida. |
| Ocorrência | Com a chave SERVERTYPE=4GL a chave CASESENSITIVE não é definida. |
| Correção | * Ajuste na leitura das chaves de caseSensitive considerando a prioridade da chave "CASESENSITIVE" em relacao a chave SERVERTYPE |
| Informações adicionais | * Referente à ocorrência: TTEC-938 * Disponível em builds superiores a 7.00.131227a - 1.3.1 |
