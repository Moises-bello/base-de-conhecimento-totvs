---
content_hash: 30880eea439fea88e091450c1d1324fa713d57ecf3edb85e738e168a0be3df5b
fetched_at: '2026-06-29T00:08:33.955135+00:00'
page_id: '274635470'
product: rm
source: tdn-rm
title: 559447 FINANCEIRO01-325 - Valor líquido lançamento com retenções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274635470
version: 106
---

# CÁLCULO DO VALOR LÍQUIDO COM RETENÇÕES DA BAIXA SEM CÓDIGO DE RETENÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Cálculo do Valor Líquido. |
| **Situação/Requisito:** | Para lançamentos parcialmente baixados que possuem retenções (tributos) com o campo Código de Retenção nulo o cálculo do valor líquido não calculava corretamente o valor das retenções já baixadas. |
| **Solução/Implementação:** | Foi ajustado o serviço de cálculo do valor líquido para considerar os registros de tributos da baixa que possuem o campo Código de Retenção com valor nulo. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 559447. |
| **Requisito:** | FINANCEIRO01-325. |

divs
