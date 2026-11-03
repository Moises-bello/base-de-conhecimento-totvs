---
content_hash: 110378e5ecd2cfe4015b3222b34d59a76b31b19db37488c6910457e30b94c51c
fetched_at: '2026-06-29T00:08:24.732707+00:00'
page_id: '270902076'
product: rm
source: tdn-rm
title: 95981_DT_Relatório_Listagem_de_Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270902076
version: 113
---

# Relatório Listagem de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatório Listagem de Lançamento |
| **Situação/Requisito:** | Cliente informa que ao realizar a geração do relatório Listagem de lançamentos é apresentado a mensagem 'Não foram encontradas informações mínimas para a geração do relatório. Reveja os parâmetros'. Porém esta mensagem somente ocorre quando é definido número de documentos no campo 'DOCUMENTO (Inicial e Final)', mesmo havendo o número de documento preenchido corretamente no lançamento.  Neste caso o que ocorreu é que o campo no relatório não obedece as parametrizações que foram informadas. Caso seja informado para não preencher com zeros a esquerda o campo sempre é preenchido com zeros a esquerda o que atrapalha o filtro do relatório. |
| **Solução/Implementação:** | Ajuste nos campos de pesquisa de documento inicial e final do relatório Listagem de Lançamento para que respeite os parâmetros do sistema relacionado ao preenchimento de zeros a esquerda. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
