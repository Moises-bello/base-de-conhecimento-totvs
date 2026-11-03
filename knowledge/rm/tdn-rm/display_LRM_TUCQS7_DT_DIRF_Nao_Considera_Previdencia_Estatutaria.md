---
content_hash: b65948b2438c4c8303180abf77c8069272edfb956feecdbd4bde4534c5773485
fetched_at: '2026-06-29T00:06:25.898561+00:00'
page_id: '224450529'
product: rm
source: tdn-rm
title: TUCQS7_DT_DIRF_Nao_Considera_Previdencia_Estatutaria
type: documentation
url: https://tdn.totvs.com/display/LRM/TUCQS7_DT_DIRF_Nao_Considera_Previdencia_Estatutaria
version: 118
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | *Ao gerar DIRF ou Informe de rendimentos para funcionários que contribuíram para a previdência de estatutário, o sistema não está levando os valores corretamente. Atualmente o sistema apenas abate o valor de previdência estatutário no valor de INSS (cc 3 ou cc89) e caso não tenha valor a ser abatido ele não leva nada no campo.* |
| **Solução/Implementação:** | Ajustado cálculo da previdência privada de estatutário na DIRF/Informe de Rendimentos.  1  -Quando o valor do INSS for zero deve somar a previdência privada de estatutário; 2 - Caso tenha valor de INSS deve subtrair a previdência privada de estatutário. |
| **Chamados relacionados:** | *TUCQS7,TUGIAB* |

divs
