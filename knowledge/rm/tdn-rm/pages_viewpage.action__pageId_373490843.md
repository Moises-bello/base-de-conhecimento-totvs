---
content_hash: 09853eeb8010e8f678f126350ac58cab3d89809eb4630256841128d94b6683e0
fetched_at: '2026-06-29T00:09:01.532359+00:00'
page_id: '373490843'
product: rm
source: tdn-rm
title: 2772040 EDUCACIONAL01-5284 DT Emssão de Recibo de Devolução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=373490843
version: 1
---

# EMISSÃO DE RECIBO DE DEVOLUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Bibliotecária |
| **Função:** | Movimentações |
| **Situação/Requisito:** | Foi verificado que antes de imprimir o recibo de devolução, o sistema verifica se o parâmetro "Emitir recibo de devolução" ou "Emitir recibo de multa" está marcado, mesmo que não exista multa. |
| **Solução/Implementação:** | O sistema foi alterado para verificar se o parâmetro "Emitir recibo de multa" está marcado somente quando houver multa. O mesmo foi feito para o recibo de renovação. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
