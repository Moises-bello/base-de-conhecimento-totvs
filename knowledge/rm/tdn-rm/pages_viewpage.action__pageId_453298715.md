---
content_hash: 8f9795a42d05f3ae330e3e1de096edb8eebd9cc3bba054048cc43b63b148ed8b
fetched_at: '2026-06-29T00:10:11.896698+00:00'
page_id: '453298715'
product: rm
source: tdn-rm
title: 4723254 DEDUINTEGRACOES-4351 DT  Inconsistência nos valores ao gerar movimento
  por competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453298715
version: 77
---

# GERAÇÃO DE MOVIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de Movimentos em regime de competência |
| **Situação/Requisito:** | Ao gerar movimento em regime de competência, caso o contrato que já possuía movimento gerado fosse alterado de forma que a data de contrato fosse preenchida com uma data superior a data da competência já gerada, o sistema se perdia e gerava um movimento com preço unitário diferente de zero, mesmo não tendo competências disponíveis. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de movimento em regime de competência, de forma que o sistema não gere movimentos para um contrato que tenha movimentação gerada para uma competência anterior a data do contrato, assim como não permitir o processamento, caso não existam competências disponíveis. A edição do contrato também foi evoluída, de forma a não permitir a edição do campo data do contrato, caso já exista movimentos gerados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
