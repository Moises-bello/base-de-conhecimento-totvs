---
content_hash: 16255858f68fe3de09dbf0d57782074f42aa34d0254ca1ff4f130008a7960d68
fetched_at: '2026-06-29T00:06:23.010818+00:00'
page_id: '223928075'
product: rm
source: tdn-rm
title: TTXAPV_DT_Desconto_Arredondamento_Ordenacao_Periodo
type: documentation
url: https://tdn.totvs.com/display/LRM/TTXAPV_DT_Desconto_Arredondamento_Ordenacao_Periodo
version: 2
---

# DESCONTO DO ARREDONDAMENTO CONSIDERANDO ORDENAÇÃO DE PERIODO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Desconto de Arredondamento* |
| **Situação/Requisito:** | *O desconto do arredondamento no evento de código de cálculo 21 está buscando o valor considerando a ordenação numérica do periodo do envelope.*  *Com isto, quando existe um envelope com data de pagamento anterior ao envelope corrente, mas com número do periodo maior, o valor do arredondamento está ficando incorreto.* |
| **Solução/Implementação:** | *A ordenação numérica do periodo só deve ser considerada no caso de existir mais de um envelope com a mesma data de pagamento.*  *Será ajustado no cálculo do CC 21 para primeiro buscar o(s) envelope(s) com a data de pagamento mais recente, anterior ou igual à data do envelope corrente.*  *Caso encontre outro envelope com a mesma data de pagamento do atual, será verificado se o número do periodo do outro envelope é anterior ao periodo corrente.*  *Caso contrário, será considerado o envelope com a primeira data de pagamento anterior à atual.*  *E se também for encontrado mais de um envelope com esta mesma data de pagamento, será considerado o envelope com o número maior de período.* |
| **Chamados   relacionados:** | *TTXAPV, TUA413* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
