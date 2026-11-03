---
content_hash: 0a080d291c8efdcde6bc234dfe3325f875d84e2dd0a5f560b3e7c951a37a1a26
fetched_at: '2026-06-29T00:10:12.326613+00:00'
page_id: '454434284'
product: rm
source: tdn-rm
title: 4424210 EDUCACIONAL01-7595 DT Atualização de Irmãos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454434284
version: 1
---

# ATUALIZAÇÃO DE IRMÃOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Função:** | Atualizar relação de irmãos |
| **Situação/Requisito:** | Ao realizar o processo de atualizar irmão, é mostrada mensagem que nenhum é atualizado. |
| **Solução/Implementação:** | A rotina de atualização da relação de irmãos foi alterada para verificar se existem registros duplicados de pessoas com a mesma filiação. Caso seja encontrado, apenas uma das pessoas será incluído como irmão e aparecerá no log os irmãos que não puderam ser incluídos por estarem com o nome já existente para outro irmão. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
