---
content_hash: abf7b4547c84aa64af6f21cf10867a676bdf1f30e620e5aa14ff6b56e88f1b41
fetched_at: '2026-06-29T00:08:13.865378+00:00'
page_id: '244428846'
product: rm
source: tdn-rm
title: TUEVIA_DT_Valores_Dependentes_Autônomos_Repetidos_DIRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244428846
version: 117
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Quando o funcionário tem múltiplos vínculos, ao gerar a DIRF quando uma das chapas de múltiplos vínculos do funcionário não possui histórico de dependente, mas a chapa tem movimentação o sistema não leva para a DIRF o valor a deduzir por dependente. |
| **Solução/Implementação:** | Adicionado na DIRF a possibilidade de utilizar o recurso de múltiplos vínculos para considerar a dedução de IRRF do dependente.  Sistema irá verificar o parâmetro 'Calcula Múltiplo vínculo sem chapa central' para identificar se deve ou não considerar. |
| **Chamados relacionados:** | *TUEVIA, TVJALM* |

divs
