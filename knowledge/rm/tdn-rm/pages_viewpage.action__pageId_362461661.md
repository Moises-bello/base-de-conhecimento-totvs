---
content_hash: 35abb5a2ad1df15449a79a4998a85ae55804734e2600dc2075511c41d490b7da
fetched_at: '2026-06-29T00:08:59.513419+00:00'
page_id: '362461661'
product: rm
source: tdn-rm
title: 2897045 FOPCALCULO01-3744 Cálculo da Média do Abono Pecuniário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362461661
version: 2
---

# Férias

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Férias |
| **Situação/Requisito:** | Ao calcular férias com média de abono pecuniário com o código de cálculo 47, o sistema apresenta os valores corretamente no recibo, porém ao lanças as ferias para a movimentação do funcionário, o sistema não está somando o valor do evento do código de cálculo 47 no evento de código de cálculo 43. |
| **Solução/Implementação:** | Ajustado o cálculo do liquido de férias para considerar o valor do evento de código de cálculo 47, quando existe evento de média de abono pecuniário. |
| **Tickets relacionados:** | 2897045 |
