---
content_hash: d5fdd91d65c8f286bbcbb048b8dd9c57e84c8214790ceb3c947140b1a9c8f954
fetched_at: '2026-07-02T19:24:28.636180+00:00'
page_id: '804029009'
product: protheus
source: tdn-tec
title: Correção - Arquivo bloqueado para download
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804029009
version: 1
---

|  |  |
| --- | --- |
| Situação | Smartclient está bloqueando arquivos para download mesmo sendo do tipo permitido (por exemplo pdf) |
| Ocorrência | Começaram a ocorrer dentro do SmartView |
| Correção | Por vezes o nome sugerido do arquivo estava vindo vazio do CEF, corrigimos essa situação para sempre vir com o nome do arquivo sugerido corretamente e consequentemente liberar o download |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-4375 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.2.1 |
