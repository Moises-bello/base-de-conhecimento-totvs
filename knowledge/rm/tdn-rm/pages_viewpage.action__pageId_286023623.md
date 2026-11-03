---
content_hash: 47f5a0449b6d7f41f1b128ce3a6b7a38ce5c782640a056435d57385d38202707
fetched_at: '2026-06-29T00:08:39.876656+00:00'
page_id: '286023623'
product: rm
source: tdn-rm
title: 1136851 FINANCEIRO01-1596-Fechamento valores baixa por proporção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286023623
version: 102
---

# FECHAMENTOS DO VALORES DE BAIXA QUANDO POR PROPORÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa de lançamentos financeiros. |
| **Situação/Requisito:** | Quando executada baixa parametrizada para calcular por proporção com múltiplas formas de pagamento, para alguns campos cujos valores continham casas decimais, o somatório do rateio do valor do campo entre os itens de baixa não fechava com o valor calculo do mesmo no lançamento. Os campos passíveis desse problema são: Valor Original, Desconto, Multa, Juros, Capitalização, Juros Vendor, Acréscimo Acordo, Juros Acordo, Desconto Acordo, Valores Opcionais e Valores de Integração. |
| **Solução/Implementação:** | Quando o rateio do valor do campo produzir, devido ao arredondamento de valores, uma diferença entre o valor do campo no lançamento calculado e o somatório dos itens de baixa gerados esta será atualizada no último item de baixa. Esse comportamento ocorre somente quando o tipo de prioridade de baixa por **Proporção** e os itens de baixa gerados corresponderem a uma baixa total. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1136851. |
| **Requisito:** | FINANCEIRO01-1596. |

divs
