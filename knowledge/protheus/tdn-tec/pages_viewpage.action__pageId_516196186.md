---
content_hash: 9262f43dfbb56df42e265b6b4a9f1e2040d5687cf43c1f8f183001ea87379ca4
fetched_at: '2026-07-02T19:24:25.970532+00:00'
page_id: '516196186'
product: protheus
source: tdn-tec
title: Correção - DLL SAT não é carregada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516196186
version: 1
---

O SmartClient Lobo-Guará não consegue carregar a DLL do equipamento SAT.

|  |  |
| --- | --- |
| Situação | A DLL dllsat.dll não consegue ser carregada. |
| Ocorrência | Ocorre conflito entre as dependência da dllsat.dll com as DLLs do SmartClient. |
| Correção | As DLLs do SmartClient foram adequadas para evitar o conflito. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-65 * Disponível em builds superiores a 17.3.0.11 |
