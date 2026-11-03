---
content_hash: e9f138fa238e89b068da5d7733485dd5be7fadb56ed2c489e908e9129ac92fb2
fetched_at: '2026-06-29T00:08:39.094467+00:00'
page_id: '286009686'
product: rm
source: tdn-rm
title: 1162487 EDUCACIONAL01-1931 DT Exportação de Alunos Integração - TOTVS x Pergamum
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286009686
version: 106
---

# EXPORTAÇÃO DE ALUNOS - INTEGRAÇÃO TOTVS X PERGAMUM

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Exportação de Alunos Integração - TOTVS x Pergamum* |
| **Situação/Requisito:** | *O filtro de alunos no processo de exportação de usuários requer que os alunos estejam matriculados no período letivo que está definido no parâmetro geral secretaria / Período letivo. Surgiu a necessidade de exportar alunos que não estejam matriculados no período letivo parametrizado nos parâmetros da secretaria.* |
| **Solução/Implementação:** | *Foi criado um lookup para seleção de período letivo no momento de exportação de usuário na integração Pergamum, sendo que este lookup vem com o valor default de período letivo igual ao período letivo salvo nos parâmetros da secretaria, caso seja necessário exportar alunos que não estão no período letivo da secretaria basta selecionar outro período letivo e executar novamente o filtro da tela.*  *Para mais informações consulte o manual de integração: <http://tdn.totvs.com/x/v836E>* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
