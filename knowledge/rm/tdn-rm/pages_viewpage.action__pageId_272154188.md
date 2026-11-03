---
content_hash: 04f459383b780efbf699c00e75540c6431b495f5ec1aefa542c21d1cfa45f2c2
fetched_at: '2026-06-29T00:08:29.641668+00:00'
page_id: '272154188'
product: rm
source: tdn-rm
title: 599214 MEDU-3038 DT Arquivo de Alunos do Censo da Educação Superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272154188
version: 110
---

# ARQUIVO DE ALUNOS DO CENSO DA EDUCAÇÃO SUPERIOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | *****Totvs Educacional***** |
| **Função:** | Censo da Educação Superior |
| **Situação/Requisito:** | Ao gerar o arquivo do censo, o campo 14 da linha 41, referente a deficiência, está preenchido com 2, que indica que a instituição não possui informação sobre o aluno e os campos 19, tipo de deficiência – física e 22 19, tipo de deficiência - intelectual, estão preenchidos com zero, indicando que não possui, porém os campos de tipos de deficiência, não deveriam vir preenchidos, para esses casos |
| **Solução/Implementação:** | Censo alterado para não enviar deficiências do aluno quando estiver marcado que a instituição não dispõe da informação. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
