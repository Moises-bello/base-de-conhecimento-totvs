---
content_hash: 3ced28d7e4ca289354eee87da0ca9b4a206486f9b23841577ebb5617e0fef541
fetched_at: '2026-06-29T00:08:26.414029+00:00'
page_id: '271178555'
product: rm
source: tdn-rm
title: 297168 MCP-1412 DT Buscar Unidade Pedido TOTVS Colaboração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271178555
version: 113
---

# BUSCAR UNIDADE DO PEDIDO - TOTVS COLABORAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | **Totvs Gestão de Estoque Compras e Faturamento*.* |
| **Função:** | Tradução de itens no Totvs Colaboração / Unidade de Medida |
| **Situação/Requisito:** | Abrindo o lookup para selecionar a unidade de medida, era apresentada todas as unidades de medida presentes no sistema |
| **Solução/Implementação:** | Ajuste no processo de tradução de itens no Totvs Colaboração para a unidade de medida.Quando o produto do pedido ou produto tradução estiverem preenchidos, o  Lookup de unidade respeitará a parametrização do tipo de movimento (Item – Identificação 2/2 -> Critério para alteração), alem disso, é possível preencher a unidade de tradução antes ou depois de selecionar o produto do pedido, neste caso, o sistema irá recalcular o saldo do pedido apenas quando ambos os campos estiverem preenchidos; criadas também novas consistências para garantir que o usuário preencha a unidade de tradução corretamente; foram criados avisos para que o usuário seja alertado no caso do recebimento para MAIS, situação onde a quantidade do produto da Nota Fiscal é maior que a do item do pedido |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
