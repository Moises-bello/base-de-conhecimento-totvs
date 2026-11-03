---
content_hash: 855ba6227b578112ded354bdad259ba0d820b837ada6f95760a5acfca3e0f4f3
fetched_at: '2026-06-29T00:06:21.884952+00:00'
page_id: '223904454'
product: rm
source: tdn-rm
title: TTVS26_DT_INSS_Ferias_Outro_Emprego_Desconto_Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVS26_DT_INSS_Ferias_Outro_Emprego_Desconto_Complementar
version: 2
---

# LANÇAMENTO E INSS FÉRIAS OUTRO EMPREGO COM DESCONTO COMPLEMENTAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *INSS Férias* |
| **Situação/Requisito:** | *Quando são lançados no Recibo de Férias os eventos de INSS Férias Outro Emprego (CC 159) e Base INSS Férias Outro Emprego Desconto Complementar (CC 186), o valor do INSS Férias lançado no CC 82 não está ficando correto, fazendo com que o total de INSS Férias no mês fique acima do teto.* |
| **Solução/Implementação:** | *Ajuste no código de cálculo 82 para tratar o lançamento da Base de INSS Férias Outro Emprego Desconto Complementar, para abater o INSS descontado no outro emprego do valor do teto proporcionalizado pelo número de dias de férias no mês, ao invés de abater do valor total do teto.* |
| **Chamados   relacionados:** | *TTVS26, TTYAUW* |
| **Versões/Release:** | *11.82.43* |
