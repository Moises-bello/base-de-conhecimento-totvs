---
content_hash: db30ae9a9ebadd7afb020782638038c97bc456c057274235e1d2f823d19be98a
fetched_at: '2026-06-29T00:08:18.814261+00:00'
page_id: '266970174'
product: rm
source: tdn-rm
title: TVAWEQ_DT_Salario_Composto_Sempre_Proporcionalizando_Recalculo
type: documentation
url: https://tdn.totvs.com/display/LRM/TVAWEQ_DT_Salario_Composto_Sempre_Proporcionalizando_Recalculo
version: 114
---

# CÁLCULO DA FOLHA DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo da Folha de Pagamento* |
| **Situação/Requisito:** | Funcionário teve uma rescisão no mês atual e ao lançar um evento sem código de cálculo, sem fórmula de valor e com fórmula de referência e que tem proporcionalidade (todos os flags marcados na aba identificação), o sistema entra no loop toda vez que executa recálculo do envelope sempre diminuindo o valor deste evento pelo fato da proporcionalização. |
| **Solução/Implementação:** | *Ajustado para sempre realizar o cálculo do salário composto. Sistema estava fazendo o cálculo apenas quando o valor era igual a zero, com isso ao proporcionalizar ele sempre pegava o último valor e encontrava um valor diferente.* |
| **Chamados relacionados:** | *TVAWEQ, TVWUOU* |

divs
