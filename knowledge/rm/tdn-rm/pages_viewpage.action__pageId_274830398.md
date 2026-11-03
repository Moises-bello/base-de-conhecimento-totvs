---
content_hash: f9b87f4ac9df56c33d22d919df1c7a410e12a01b16766df256cd51fa892ea85b
fetched_at: '2026-06-29T00:08:34.659097+00:00'
page_id: '274830398'
product: rm
source: tdn-rm
title: 823322 EDUCACIONAL01-751 DT Geração de histórico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274830398
version: 93
---

# GERAÇÃO DE HISTÓRICO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de histórico |
| **Situação/Requisito:** | Ao tentar realizar a geração de histórico do aluno ocorre o erro Falha ao ativar restrições. Uma ou mais linhas contém valores que violam as restrições non-null, unique ou foreign-key. |
| **Solução/Implementação:** | Ajustar consulta que busca as notas ou faltas de etapas para que não sejam retornados valores duplicados violando restrição de valores únicos.  Tratamento de preenchimento de carga horária de disciplina quando não existem registros de nota ou falta de etapa. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
