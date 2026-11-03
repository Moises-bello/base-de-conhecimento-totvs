---
content_hash: 75f76033adcd57481786e784f8a2cdb47537f3187339b2a3e50a3793d002bbd5
fetched_at: '2026-06-29T00:09:51.812512+00:00'
page_id: '437264815'
product: rm
source: tdn-rm
title: 4377710 EDUCACIONAL01-7242 DT Copiar Turmas Entre Períodos Letivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=437264815
version: 2
---

# COPIAR TURMAS ENTRE PERÍODOS LETIVOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Função:** | Copiar turmas entre períodos letivos |
| **Situação/Requisito:** | Ao realizar a cópia de turmas entre períodos letivos o sistema está apresentando o erro:  Erro em ParamsProc.ReadData: Incorrect syntax near '2018'.  Unclosed quotation mark after the character string ' ) ) /AND/ SET FMTONLY OFF; SET NO\_BROWSETABLE OFF;'.  Foi identificado que o erro ocorre devido a uma turma que possui uma aspa simples no meio do código da turma. |
| **Solução/Implementação:** | O processo de copiar turmas entre períodos letivos foi alterado para considerar turmas que tenham apóstrofo (') no código. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
