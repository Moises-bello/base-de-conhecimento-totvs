---
content_hash: b441837fb57946af28e48d0fa7828fb36d08be814578cb4b344a1d5382abfd8d
fetched_at: '2026-06-29T00:08:45.754748+00:00'
page_id: '315887629'
product: rm
source: tdn-rm
title: 1486638 FINANCEIRO01-3630 Geração Cod. Barras boleto valor negativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315887629
version: 92
---

# GERAÇÃO CÓDIGO DE BARRAS PARA BOLETO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Geração de código de barras. |
| **Situação/Requisito:** | Ao gerar remessa de cobrança eletrônica para boleto cujo lançamento está parcialmente baixado sistema apresentava a mensagem "A cadeia de caracteres de entrada não estava em um formato incorreto". |
| **Solução/Implementação:** | Ajustado o serviço de geração de código de barras do boleto para não executar o serviço caso o valor calculado para o boleto tenha valor negativo. Isso pode ocorrer, por exemplo, se existe algum valor opcional calculado por fórmula e parametrizado como ação "Descontar". Como a fórmula para valor opcional sempre é executada no cálculo do valor líquido o seu conteúdo deve prever se o valor retornado deve ser cheio ou parcial (considerar o valor já baixado). |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1486638. |
| **Requisito:** | FINANCEIRO01-3630. |

divs
