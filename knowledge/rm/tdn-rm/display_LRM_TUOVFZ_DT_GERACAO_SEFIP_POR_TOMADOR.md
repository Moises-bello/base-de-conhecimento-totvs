---
content_hash: c8f61fa5cc5e61b4e1083377ffcbc896cdf3f8125f643fd3d1921841b855894b
fetched_at: '2026-06-29T00:08:03.925556+00:00'
page_id: '235329729'
product: rm
source: tdn-rm
title: TUOVFZ_DT_GERACAO_SEFIP_POR_TOMADOR
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOVFZ_DT_GERACAO_SEFIP_POR_TOMADOR
version: 113
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | Ao gerar SEFIP por tomadores com mais de um tomador com o mesmo CEI, os tomadores subsequentes eram ignorados pelo fato de a key da collection de tomadores ser o CEI, podendo incluir apenas o primeiro. Sendo assim, na hora de buscar os funcionários, buscava apenas através do primeiro tomador e não verificava os subsequentes. |
| **Solução/Implementação:** | *Foi alterada a consulta SQL para não utilizar o código do tomador, mas apenas o CEI para buscar os funcionários que possuíam rateio para aquele tomador.* |
| **Chamados relacionados:** | TUOVFZ, TUPPDK |

divs
