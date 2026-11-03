---
content_hash: 02151fe6b84b6b1602ca3e6141aa9c51ee889e69ae32600a33ad41944e7f78a3
fetched_at: '2026-06-29T00:08:15.139928+00:00'
page_id: '244732315'
product: rm
source: tdn-rm
title: TVKWJX_DT_Diferimento_Parcela_Arredondamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TVKWJX_DT_Diferimento_Parcela_Arredondamento
version: 113
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Apropriação mensal através do novo modelo de contabilização por competência* |
| **Situação/Requisito:** | *Devido um comportamento indevido do sistema que existiu há um tempo atrás, no novo modelo de contabilização por competência, foram geradas contabilizações de aumentos e cancelamentos de poucos centavos sem o diferimento desses ajustes. Para esses casos, com a versão mais recente, pode ocorrer do sistema diferir todo o ajuste antes do fim do período de contabilização, fazendo com que o sistema tente diferir o aumento ou cancelamento com valor zero, causando erro de inclusão de lançamentos sem partidas contábeis.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de contabilização por competência, para o novo modelo, de foma que o sistema não tente incluir contabilizações de aumentos e cancelamentos com valor zerado.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.13* |
| **Versão Corrigida:** | *12.1.13* |
| **Versão Expedida:** | *12.1.13* |

divs
