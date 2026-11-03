---
content_hash: 39d5cbb0586bc7e788673f9b46d1de755f2a30a425470dfa1de2ce758c8b264d
fetched_at: '2026-06-29T00:06:29.480568+00:00'
page_id: '234610370'
product: rm
source: tdn-rm
title: TTTPV0_DT_Encargo_Provisao_13_Nao_Abate_Adiantamento_13_Salario
type: documentation
url: https://tdn.totvs.com/display/LRM/TTTPV0_DT_Encargo_Provisao_13_Nao_Abate_Adiantamento_13_Salario
version: 120
---

# GERAÇÃO DE ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração de Encargos* |
| **Situação/Requisito:** | Ao gerar o encargo do tipo 9 não considera o evento de código de cálculo 35 para o abatimento, assim fazendo com que o encargo fique negativo. |
| **Solução/Implementação:** | Ajustado o cálculo do encargo tipo 9 quando é provisão acumulado e existe desconto de adiantamento da primeira parcela do décimo terceiro. Sistema passa a considerar o código de cálculo 35 para considerar o valor correto da primeira parcela. |
| **Chamados relacionados:** | *TTTPV0,TUMVW8* |

divs
