---
content_hash: 8e0e9009c1d3d1e640bf16de890dac4d374f6e11544e6e5a8cd3f56acdc0cb86
fetched_at: '2026-06-29T00:09:52.965384+00:00'
page_id: '439706579'
product: rm
source: tdn-rm
title: 4384696 TOPEXECONTROL01-4947 - DT Valor Calculado Reajuste não está trazendo
  valores de reajustes de itens que não foram medidos.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439706579
version: 6
---

# CÁLCULO DO REAJUSTE PREVISTO - PI + R (PREÇO INICIAL + REAJUSTE)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Função:** | Contrato |
| **Situação/Requisito:** | Valor Calculado Reajuste não está trazendo valores de reajustes de itens que não foram medidos. Não existia coluna que informasse qual reajuste previsto do contrato. E a coluna reajuste calculado, gerava dupla interpretação. |
| **Solução/Implementação:** | Criada coluna na visão e edição de contrato, chamada "Reajuste Previsto" que calcula qual o reajuste total do contrato previsto baseado no último fator de reajuste aplicado, considerando o acumulado anterior. Também foi alterado a coluna "Valor Calculado Reajuste" para "Reajuste Devido" na visão de contratos e sua edição.  **Reajuste Devido:** Apresenta a soma dos valores de reajustes calculados sobre o valor medido (PI). **Reajuste Previsto:** Apresenta a soma dos valores de reajuste calculados sobre o valor medido (PI), menos os valores medidos de reajustes (R). |
| **Conversores e Parâmetros:** | Não se aplica. |
| **Tickets relacionados:** | 4384696 |
| **Requisito:** | TOPEXECONTROL01-4923 |
| **Documento de Referência:** | Não se aplica. |
| **Pacote:** | Não se aplica. |
