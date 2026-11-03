---
content_hash: c4bb1ff1affe67e8a80db547949a686048084ceacd6f774d037790ce054ab06a
fetched_at: '2026-07-02T19:24:27.680724+00:00'
page_id: '667920030'
product: protheus
source: tdn-tec
title: Correção - SmartClient aborta em rotinas 4GL chamando FGL_WINQUESTION
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=667920030
version: 1
---

Foi adicionada uma proteção para que o SmartClient não aborte.

|  |  |
| --- | --- |
| Situação | Ao chamar a função FGL\_WINQUESTION o SmartClient Harpia é abortado. |
| Ocorrência | O problema só ocorre ao executar a rotina 4GL diretamente como programa inicial. |
| Correção | Adicionada uma proteção para que o erro que fazia o SmartClient ser abortado não aconteça. |
| Informações adicionais | * Referente ao chamado: #LOGIX-32 * Referente à ocorrência: DTCLIENT01-3256 * Disponível em builds superiores a 20.3.0.3 |
