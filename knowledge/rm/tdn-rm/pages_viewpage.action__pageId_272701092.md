---
content_hash: f914b19fb7d4eb9a0e00b3869e6ce447f15c58b98f72df05de60d899aaa14f7d
fetched_at: '2026-06-29T00:08:30.896655+00:00'
page_id: '272701092'
product: rm
source: tdn-rm
title: 601892 MEDU-3044 DT Reabertura de Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272701092
version: 107
---

# Exclusão de ocorrências

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Totvs Gestão Patrimonial. |
| **Função:** | Exclusão de ocorrências. |
| **Situação/Requisito:** | Ao selecionar uma transferência monetária > processo > excluir Ocorrência >  sistema apresenta erro: validação: ID da ocorrência: 20881 - ORA-01795: maximum number of expressions in a list is 1000. |
| **Solução/Implementação:** | Implementação de verificação da chamada do método de exclusão de ocorrência para que, sendo do processo de reabertura de competência, não seja necessário verificar se é a última ocorrência, pois todas do período deverão ser excluídas. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
