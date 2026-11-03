---
content_hash: 2fc348e5ce6c417f90d4d6df1d00cb35396c11219cfbcb58e10fef16bc7b5650
fetched_at: '2026-06-29T00:08:23.849467+00:00'
page_id: '270095451'
product: rm
source: tdn-rm
title: 264576_DT_Erro_Inclusao_Movimento_Divisao_Por_Zero
type: documentation
url: https://tdn.totvs.com/display/LRM/264576_DT_Erro_Inclusao_Movimento_Divisao_Por_Zero
version: 111
---

# Erro na geração de movimentos por Competência - Divisão por zero

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de movimento por competência |
| **Situação/Requisito:** | Erro de divisão por zero na geração de movimento da última parcela. Isso ocorre porque o valor de bolsa a ser calculado leva em consideração o número de meses já gerado e, como o resultado desse cálculo é zero devido a existirem mais de um movimento para uma outra competência, o sistema emite essa mensagem de erro. |
| **Solução/Implementação:** | Sistema passou a considerar o número de meses total de competências a serem geradas para o cálculo do valor da bolsa.  Feito também um tratamento para que, quando o sistema encontrar dois movimentos gerados para a mesma competência, ele considere essa competência somente uma vez ao calcular o número de competências a gerar (Número total de competências - Número de competências geradas) |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | MEDU-1535 |
| **Requisito (ISSUE):** | *N/A* |

divs
