---
content_hash: a05174894b37562d2933a145b04284ef9c494930de44ed526ada4b3b71668bac
fetched_at: '2026-06-29T00:08:04.151826+00:00'
page_id: '235337916'
product: rm
source: tdn-rm
title: TULUHL_DT_Exclusao_Dependente
type: documentation
url: https://tdn.totvs.com/display/LRM/TULUHL_DT_Exclusao_Dependente
version: 114
---

# DEPENDENTES

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Exclusão de Dependentes |
| **Situação/Requisito:** | Ao realizar a exclusão de dependentes, o sistema não realiza verificação se o dependente possuí registro no histórico de assistência saúde e realiza a exclusão, deixando os dados na base de dados inconsistente. |
| **Solução/Implementação:** | Implementado validação, onde é verificado se o dependente possui registro no histórico de assistência saúde, caso possua, não será permitido a exclusão. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TULUHL |

divs
