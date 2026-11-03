---
content_hash: e9715013941cc0514506bda225a15d46900242d67672ea0de1522d403132b81f
fetched_at: '2026-06-29T00:08:12.970510+00:00'
page_id: '243656031'
product: rm
source: tdn-rm
title: TUAXMQ_DT_Traducao_Produtos_Unidade_Recebimento_Automatico_NFe
type: documentation
url: https://tdn.totvs.com/display/LRM/TUAXMQ_DT_Traducao_Produtos_Unidade_Recebimento_Automatico_NFe
version: 114
---

# Recebimento Automático de NF-e

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Tradução de Produtos e Unidades* |
| **Situação/Requisito:** | *Durante o recebimento automático de NF-e, o sistema exibe uma mensagem de erro para cada produto não traduzido, o ideal seria que o Log do processo exibisse uma mensagem com todas as inconsistências.* |
| **Solução/Implementação:** | Ajustamos a rotina responsável por traduzir o produto e a unidade de medida, agora são analisados todos os itens do XML e caso sejam identificadas inconsistências, todas são exibidas no log do processo. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
