---
content_hash: 1ecbeab550c72e3b37dbb42506c532a31786311f758a017da2ac6577649128d6
fetched_at: '2026-06-29T00:06:27.467896+00:00'
page_id: '232822390'
product: rm
source: tdn-rm
title: TUFZ06_DT_Informe_Rendimentos_Valor_Negativo_Operadora_Assistencia_Saude
type: documentation
url: https://tdn.totvs.com/display/LRM/TUFZ06_DT_Informe_Rendimentos_Valor_Negativo_Operadora_Assistencia_Saude
version: 121
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar o Informe de rendimentos de um funcionário que tenha recebido um estorno de assistência medica com valor superior ao que foi descontado, o informe de rendimentos é gerado com valor negativo. |
| **Solução/Implementação:** | *Alterado para zerar o valor e informar no log os dependentes que tiveram o valor zerado.* |
| **Chamados relacionados:** | *TUFZ06,TUJLDJ* |

divs
