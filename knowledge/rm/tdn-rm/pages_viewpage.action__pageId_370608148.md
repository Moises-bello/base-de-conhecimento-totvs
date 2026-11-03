---
content_hash: a2c252c6e5e33eca2c688409344e682828de48635cb0c48136d5598bab414b00
fetched_at: '2026-06-29T00:09:00.919718+00:00'
page_id: '370608148'
product: rm
source: tdn-rm
title: 3023872 EDUCACIONAL01-5234 DT Processo Seletivo – Importar arquivo com número
  de inscrição contendo aspas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370608148
version: 1
---

# PROCESSO SELETIVO TERCEIRIZADO - IMPORTAR ARQUIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Importar arquivo no processo seletivo terceirizado |
| **Situação/Requisito:** | Ao importar arquivo no processo seletivo terceirizado, o sistema estava gravando inconsistência no campo Número de Inscrição, caso o arquivo texto estivesse com este campo contendo aspas. Desta maneira, apresentava erro ao realizar a matrícula do candidato. |
| **Solução/Implementação:** | No Processo Seletivo Terceirizado, ao executar “Importação de arquivo”, o sistema fará as seguintes validações:  - Não será possível importar linha que contenha caracteres Unicode, por exemplo “\u001f”.  - O campo Número de inscrição somente pode conter dígitos, portanto será removido automaticamente caracteres especiais como pontuação, acentos e letras. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
