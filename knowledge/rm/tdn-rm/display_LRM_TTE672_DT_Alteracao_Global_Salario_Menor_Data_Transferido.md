---
content_hash: fd8a7fb413a92ee9d29e7924102b81aa9063c01191e6faf9500749f7314b1a2f
fetched_at: '2026-06-29T00:08:09.090319+00:00'
page_id: '239023285'
product: rm
source: tdn-rm
title: TTE672_DT_Alteracao_Global_Salario_Menor_Data_Transferido
type: documentation
url: https://tdn.totvs.com/display/LRM/TTE672_DT_Alteracao_Global_Salario_Menor_Data_Transferido
version: 116
---

# ALTERAÇÃO GLOBAL DE SALÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alteração Global de Salários* |
| **Situação/Requisito:** | *Quando tenho um funcionário que foi transferido com ônus (tipo 6) e logo após executo a alteração global de salário com uma data anterior a transferência, o processo não faz a mesma consistência quando o funcionário só tem um registro no histórico de alteração salarial, inserindo dois registros, um com a data da mudança e motivo igual ao informado no processo e outro com a data da transferência acrescentada de 10 minutos e o motivo cadastrado no parametrizador referente a alteração de salário retroativo.* |
| **Solução/Implementação:** | *Novo tratamento referente a data de mudança para funcionários transferidos. Sistema passa considerar a data de transferência, antes considerava a data de admissão.* |
| **Chamados relacionados:** | *TTE672* |

divs
