---
content_hash: 28c864b235c1e6d416a424860ee0d95f17ecdde7acce7cabde3cfe92e985284b
fetched_at: '2026-06-29T00:08:25.623152+00:00'
page_id: '270919433'
product: rm
source: tdn-rm
title: 348239 MEDU-1937 DT Solicitação de atendimento gerando boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270919433
version: 111
---

# Solicitação de atendimento via portal

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Solicitação de atendimento via portal |
| **Situação/Requisito:** | Ao gerar nova solicitação que possua algum valor cadastrado no portal do aluno, é exibida a seguinte mensagem de não conformidade:  “Column "FBOLETO.CODCOLIGADA" is invalid in the ORDER BY clause because it is not contained in either an aggregate function or the GROUP BY clause.   ORDER BY items must appear in the select list if SELECT DISTINCT is specified.” |
| **Solução/Implementação:** | Ajuste na realizado nas solicitações via portal que geram boletos para que não seja apresentada nenhuma não conformidade impedindo a conclusão do processo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 348239 / MEDU-1937 |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
