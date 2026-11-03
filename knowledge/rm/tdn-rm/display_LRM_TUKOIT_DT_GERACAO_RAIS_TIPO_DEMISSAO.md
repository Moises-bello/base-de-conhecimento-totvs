---
content_hash: 99eefc502d77ee142be4ec08352edfbbda38b1e76b0cd4ae9f24beba82b10355
fetched_at: '2026-06-29T00:06:28.532582+00:00'
page_id: '233754082'
product: rm
source: tdn-rm
title: TUKOIT_DT_GERACAO_RAIS_TIPO_DEMISSAO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKOIT_DT_GERACAO_RAIS_TIPO_DEMISSAO
version: 118
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Tipo de demissão sendo levada errada no arquivo RAIS |
| **Solução/Implementação:** | Ajuste na rotina RAIS para ordenar lista de histórico de situação do funcionário afim de buscar a situação atual (histórico mais recente). Em Alguns casos a rotina buscava o histórico desordenado e por este motivo não recuperava situação atual do funcionário. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUKOIT TULJEB |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.11* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
