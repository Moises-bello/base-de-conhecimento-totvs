---
content_hash: bc94c7dd91f067527de7f7b09d12a9e7bf476ed1122ef3bb8bd41adff39ef3b7
fetched_at: '2026-06-29T00:08:03.845156+00:00'
page_id: '235326416'
product: rm
source: tdn-rm
title: TUOYG7_DT_Alteracao_Global_Salarios
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOYG7_DT_Alteracao_Global_Salarios
version: 121
---

# ALTERAÇÃO GLOBAL SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Alteração global de salários* |
| **Situação/Requisito:** | Ao realizar alteração salarial marcando o parâmetro “Reajustar os aumentos posteriores considerando o valor do aumento salarial” para bases que utilizam tabela salarial, o sistema realiza a alteração incorretamente, considerando o valor do salário na tabela salarial mais o salário da época |
| **Solução/Implementação:** | Ajuste na rotina de alteração global de salários, preenchendo o salário da época para cálculo da diferença de valor do aumento salarial, aplicando a diferença para os registros retroativos do histórico salarial |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUOYG7 TUPFGN |
| **Requisito (ISSUE):** |  |

divs
