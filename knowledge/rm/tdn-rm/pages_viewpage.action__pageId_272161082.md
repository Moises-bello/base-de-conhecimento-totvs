---
content_hash: d09ae7891b396cd0310c702d77418ba5ebea7e35665f2e99cd14ff0c6cf78740
fetched_at: '2026-06-29T00:08:29.718672+00:00'
page_id: '272161082'
product: rm
source: tdn-rm
title: 583658 MEDU-3031 DT Importação de dados do Censo do Ensino Superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272161082
version: 112
---

# IMPORTAÇÃO DE DADOS DO CENSO DO ENSINO SUPERIOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | *****Totvs Educacional***** |
| **Função:** | Censo da Educação Superior |
| **Situação/Requisito:** | Ao tentar realizar a importação dos dados exportados do INEP surge o erro: “Aluno com matrícula no formato INEP [] não encontrado”, não sendo possível identificar qual aluno está com problema |
| **Solução/Implementação:** | Foi alterada a mensagem gerada na importação de dados do censo, pois não está sendo possível identificar os alunos que não estão sendo encontrados no sistema. O INEP não está enviando mais o RA no arquivo. Será utilizado o CPF para a verificação. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
