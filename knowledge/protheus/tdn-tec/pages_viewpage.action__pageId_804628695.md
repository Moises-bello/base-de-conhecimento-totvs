---
content_hash: b0b42f4ad2513ecc0e53aad07fe0deff1d6654a27c8be6f9583db9a5d021fe60
fetched_at: '2026-07-02T19:24:28.665494+00:00'
page_id: '804628695'
product: protheus
source: tdn-tec
title: Correção - Problema na impressão de relatórios através da TOTVSPrinter
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804628695
version: 1
---

A chamada do SmartClient Desktop para a TOTVSPrinter estava sendo feita de forma errada.

|  |  |
| --- | --- |
| Situação | No SmartClient Linux e/ou quando o nome da impressora selecionada tem espaço, a chamada era feita errada e aimpressão não era realizada. |
| Ocorrência | A chamada na linha de comando para a TOTVSPrinter estava sendo feita com a sintaxe errada em casos específicos. |
| Correção | Sintaxe da chamada para a TOTVSPrinter corrigida e funcionando. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-4396 * Disponível em builds superiores a 20.3.2.1 |
