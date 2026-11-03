---
content_hash: b6f5a5451d1ed8bf4f2d01bbc30e131c18143a1f8ad1cacf6f2703c46d09d7d9
fetched_at: '2026-06-29T00:06:01.121421+00:00'
page_id: '198936391'
product: rm
source: tdn-rm
title: TSUSBF_DT_Salario_Familia
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUSBF_DT_Salario_Familia
version: 2
---

# Salario Família CC 5

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo do Salário Família - CC 5* |
| **Situação/Requisito:** | *O cálculo do evento de salário família (CC 5) está duplicando a base quando é lançado em um envelope de salário maternidade, e está marcado o parâmetro "Considera Salário nominal".* |
| **Solução/Implementação:** | *Ajustar o cálculo do evento de Salário Família (CC 5). No envelope de Salário Maternidade o evento de Salário Família é calculado duas vezes, por causa do cálculo de média. Quando está marcado o parâmetro "Considera Salário Nominal", no 1º cálculo a base do Salário Família é abastecida com o salário do funcionário. Desta forma, antes de realizar o recalculo é necessário abater o salário nominal da base, para não duplicar o valor.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSUSBF* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.39* |
