---
content_hash: 420303ee69b8933ca3255975ad634d64b974d06232c98263edd6984f87202ac1
fetched_at: '2026-06-29T00:08:19.525583+00:00'
page_id: '267791670'
product: rm
source: tdn-rm
title: TVXWA4_DT_Periodo_Incorreto_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVXWA4_DT_Periodo_Incorreto_Rescisao
version: 111
---

# RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | Está definido nos parâmetros locais o período 10, competência 08 e caixa 08. Existe o período 1 que está totalmente bloqueado. Ao cadastrar uma rescisão com data de 01/08/2016 o sistema muda o período de 10 para 1, e não permite calcular a rescisão pois o período encontra-se bloqueado. |
| **Solução/Implementação:** | *Ajustado período da rescisão quando o período local é diferente do período global.*  Estava sendo considerado sempre o período global. |
| **Chamados relacionados:** | *TVXWA4* |

divs
