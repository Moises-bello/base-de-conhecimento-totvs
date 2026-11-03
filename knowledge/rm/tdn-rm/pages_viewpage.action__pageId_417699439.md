---
content_hash: 0649fbf4ed5a4f8c4c2a81dd3c46d5c27cddcd6539f00f71cc1f8fb3a4371d56
fetched_at: '2026-06-29T00:09:12.400968+00:00'
page_id: '417699439'
product: rm
source: tdn-rm
title: 3786708 FOPCALCULO01-4741 INSS Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417699439
version: 1
---

# INSS Férias

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Diferença de Férias |
| **Situação/Requisito:** | Funcionário gozou férias do período 18/08/2018 à 06/09/2018, 20 dias com 10 de abono, na competência agosto/2018. O sistema calculou o INSS de férias no mês e no próximo mês corretamente, porém ao lançar as férias para o envelope e calcular diferença de férias, o sistema recalculou o INSS de férias próximo mês, calculando um valor de INSS menor do que o recibo de férias. |
| **Solução/Implementação:** | Ajuste na diferença de INSS Férias do segundo mês, quando a Diferença de Férias é calculada na competência de inicio das férias. |
| **Tickets relacionados:** | 3786708 |
