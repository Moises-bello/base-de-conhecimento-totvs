---
content_hash: 051449703a095afcdd44df39f3cc906159a91d0444f5b4672ecd9ea888b9072d
fetched_at: '2026-06-29T00:08:33.936758+00:00'
page_id: '274630209'
product: rm
source: tdn-rm
title: 841659 DT Webservice - Dataserver EduConsultaNotaEtapaData
type: documentation
url: https://tdn.totvs.com/display/LRM/841659+DT+Webservice+-+Dataserver+EduConsultaNotaEtapaData
version: 95
---

# WEBSERVICE - DATASERVER: EDUCONSULTANOTAETAPADATA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | EDUCACIONAL |
| **Módulo:** | TOTVS EDUCACIONAL |
| **Função:** | WEBSERVICE - Acessao ao dataServer EduConsultaNotaEtapaData |
| **Situação/Requisito:** | Ao executar o método readRecord do dataServer 'EduConsultaNotaEtapaData' é emitida uma mensagem informando que não existe tabela na posição 0. |
| **Solução/Implementação:** | O dataServer 'EduConsultaNotaEtapaData' não deve ser utilizado via webservice. Ele é um dataServer de uso interno. Foi realizado uma alteração para emitir uma mensagem tratada informando isso quando executado o dataServer via webservice. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
