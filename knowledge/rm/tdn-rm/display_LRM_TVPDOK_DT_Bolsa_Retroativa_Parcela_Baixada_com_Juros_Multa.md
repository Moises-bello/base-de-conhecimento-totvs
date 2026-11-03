---
content_hash: 4c53fca9a97792866ebc1d67fd342406ad0b87edfbacbd9b4b7f2cf51c499d71
fetched_at: '2026-06-29T00:08:16.338525+00:00'
page_id: '244938693'
product: rm
source: tdn-rm
title: TVPDOK_DT_Bolsa_Retroativa_Parcela_Baixada_com_Juros_Multa
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPDOK_DT_Bolsa_Retroativa_Parcela_Baixada_com_Juros_Multa
version: 101
---

# Inclusão Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Bolsa Retroativa |
| **Situação/Requisito:** | Ao incluir bolsa retroativa em contratos que possuem baixas com juros, ao refazer as baixas o sistema deixa os  lançamentos com status de baixado parcialmente e não refaz os cálculos corretamente.  As baixas que estão com este comportamento possuem valores de juros e multa. |
| **Solução/Implementação:** | Ajuste no processo de inclusão de bolsa retroativa para uma parcela que já foi baixada financeiramente com multa e juros, pois em algumas situações estes valores não estavam refletindo no cálculo do pagamento a maior ou menor. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVPDOK |
| **Requisito (ISSUE):** | N/A |

divs
