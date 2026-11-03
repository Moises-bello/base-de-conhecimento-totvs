---
content_hash: 3ff4bd7178526ac09d378d88262c19ad79c2686d3863f98fc8c92cd336093a27
fetched_at: '2026-06-29T00:08:10.918096+00:00'
page_id: '241700635'
product: rm
source: tdn-rm
title: TUUK64_DT_Contabilizar_Segunda_Bolsa_na_Regeração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=241700635
version: 110
---

# GERAÇÃO DE LANÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Geração de Lançamento* |
| **Situação/Requisito:** | Em um lançamento do tipo contábil já existia contabilização de inclusão gerada, contendo partida para uma bolsa. Ao inserir uma segunda bolsa e Regerar o lançamento, o sistema não estava atualizando a contabilização de Inclusão com o valor da segunda bolsa, ou seja, mantinha incorretamente as partidas contábeis originais. |
| **Solução/Implementação:** | Alterado o processo de Geração de Lançamento, para lançamento do tipo contábil, ao regerar a contabilidade de inclusão todas as bolsas inseridas deverão ser contabilizadas (caso o item do evento contábil esteja para aplicar na bolsa). |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
