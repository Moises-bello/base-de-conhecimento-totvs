---
content_hash: 2f4fe6e14a60f982371641b433807a13ddb0a6a16bd712fdb5fb99d1e694e733
fetched_at: '2026-06-29T00:08:11.560348+00:00'
page_id: '243012879'
product: rm
source: tdn-rm
title: TVDUZD_DT_DIAS_DE_FERIAS_SUGESTAO_FLUIG
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDUZD_DT_DIAS_DE_FERIAS_SUGESTAO_FLUIG
version: 110
---

# WORKFLOW SUGESTÃO DE FÉRIAS FLUIG

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Workflow Sugestão de Férias Fluig* |
| **Situação/Requisito:** | Ao fazer o cálculo da quantidade de dias na sugestão de férias no formulário do workflow no fluig, foi utilizado a função getTime do javascript, que estava causando erro de cálculo no mês de outubro, quando tem início o horário de verão. |
| **Solução/Implementação:** | *Foi alterada a função de cálculo da quantidade de dias para que o valor seja calculado corretamente mesmo com o horário de verão* |
| **Chamados relacionados:** | *TVDUZD* |

divs
