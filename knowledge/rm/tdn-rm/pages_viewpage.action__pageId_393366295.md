---
content_hash: 151e15bd334b7817822340c00baa188fbe843d3c633edf946ad0cc7b11f70b9f
fetched_at: '2026-06-29T00:09:09.740796+00:00'
page_id: '393366295'
product: rm
source: tdn-rm
title: 3404396 FOPCALCULO01-4440 Média Licença Maternidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393366295
version: 1
---

# Cálculo da Média de Licença Maternidade

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Cálculo da Média de Licença Maternidade |
| **Situação/Requisito:** | Ao efetuar o lançamento de Salário maternidade para funcionária com afastamento do tipo ‘E – Licença Maternidade’ de ‘05/06/2018’ à ‘02/10/2018’, afastamento anterior do tipo ‘P - Af.Previdência’ de ‘31/10/2017’ à ‘30/11/2017’ e período de gozo de férias de ‘02/01/2018’ à ‘31/01/2018’, a parametrização realizada no Sindicato para desconsiderar o mês do afastamento e substituí-lo por mês anterior não é considerada. Desta forma ao calcular as médias de Salário Maternidade o mês 11/2017 é considerado na apuração e composição do cálculo. |
| **Solução/Implementação:** | Ajuste no cálculo da média de salário maternidade quando existem períodos de afastamentos e ferias intercalados durante os meses de apuração da médias. |
| **Tickets relacionados:** | 3404396 |
