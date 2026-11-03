---
content_hash: 1425d81a00bb0757b58d64eb3616773c1a1ccee7f53515667dda7bdf4fcb130e
fetched_at: '2026-06-29T00:08:30.166668+00:00'
page_id: '272406127'
product: rm
source: tdn-rm
title: 431042 MRH-8652 DT Log Geração Encargos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272406127
version: 110
---

# ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Encargos |
| **Situação/Requisito:** | No cadastro do encargo a flag ‘Aplicar arredondamento sobre o valor total’ está marcada, ao gerar o encargo do tipo 3 -Base: incidência de INSS o log está apresentado o valor 568,0912 porém ao gerar a contabilização do encargo o valor utilizado é 568,0900. |
| **Solução/Implementação:** | Ao gerar o encargo do tipo 3 -Base: incidência de INSS o log deve apresentar o mesmo valor do log de contabilização quando a flag ‘Aplicar arredondamento sobre o valor total’ estiver marcada. |
| **Tickets relacionados:** | * [431042](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22431042%22 "431042") |

divs
