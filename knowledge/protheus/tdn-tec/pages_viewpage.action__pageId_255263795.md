---
content_hash: 59ef717a0f4be68e7520126a0535f385c08b9d6c6dd9b3c8d8e8e00463b4ed8b
fetched_at: '2026-07-02T19:24:20.516774+00:00'
page_id: '255263795'
product: protheus
source: tdn-tec
title: Correção - O agente TOTVS Printer finaliza inesperadamente ao incluir imagem
  inválida no documento PDF.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=255263795
version: 1
---

Correção - O agente TOTVS Printer finaliza inesperadamente ao incluir imagem inválida no documento PDF.

|  |  |
| --- | --- |
| Situação | O agente TOTVS Printer finaliza inesperadamente se encontrar uma imagem com sua informação binária zerada no arquivo de impressão. |
| Ocorrência | Se por algum motivo houver uma imagem com sua informação binária zerada e incluída no arquivo de impressão (por exemplo, pela função FWMsPrinter():SayBitmap) a ser enviado para o agente TOTVS Printer, este pode finalizar inesperadamente e nenhum documento será impresso. |
| Correção | A correção trata-se de um contorno para que o agente de impressão TOTVS Printer detecte uma imagem desse tipo antes de incluí-la na impressão, evitando assim a finalização inesperada. Entretanto nenhuma informação posterior a imagem será incluída no documento de impressão, ficando portanto incompleto. Cabe salientar que esse é o comportamento padrão do agente TOTVS Printer para qualquer comando inválido encontrado no arquivo de impressão. |
| Informações adicionais | * Referente ao chamado: SSIM-1210 * Referente à ocorrência: TVUHS7 * Disponível a partir da versão 1.6.4 da TOTVS Printer. |
