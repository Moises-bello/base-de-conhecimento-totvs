---
content_hash: 3205803b33951bd0099b8023e28ef7d4d3a2b1d430edb0baf192171c87cc4e69
fetched_at: '2026-06-29T00:08:35.484535+00:00'
page_id: '280928228'
product: rm
source: tdn-rm
title: 867845 CONTROLADORIA01-221 RM_Conector
type: documentation
url: https://tdn.totvs.com/display/LRM/867845+CONTROLADORIA01-221+RM_Conector
version: 102
---

# Importação Plano Contas Paralelo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Totvs Gestão Contábil. |
| **Função:** | Importação Plano Contas Paralelo. |
| **Situação/Requisito:** | Ao realizar a importação do plano de contas via conceito é apresentado uma mensagem, informando que a coluna CODCONTAPLANOPARALELO não permite valores null, mesmo com as contas do plano paralelo informadas conforme é orientado no layout: <http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.LayoutImpPlanodeContasParalelo.aspx>. |
| **Solução/Implementação:** | Atualização do conceito CONCTB0005 - Importação Contas do Plano Paralelo.icp. Foram realizadas as seguintes modificações:  1 - Inclusão dos campos CODPLANOPARALELO e CODCONTAPLANOPARALELO na coleção de campos da tabela de origem PlanoContabilParareloRelacionado.  2 - Inclusão os campos CODPLANOPARALELO, CODCONTAPLANOPARALELO e CODCONTASPLANOCONTAS na coleção da tabela de origem AssociarCentroCusto.  3 - Inclusão dos campos CODPLANOPARALELO, CODCONTAPLANOPARALELO, CODCONTAPLANOCONTAS na tabela de origem AssociarContaGerencial. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |

divs
