---
content_hash: 7c1e81c998e4e037da25aad53e5ef095de48076e9fd1ae3b8ba3a50d200fdb59
fetched_at: '2026-06-29T00:09:00.479270+00:00'
page_id: '368904717'
product: rm
source: tdn-rm
title: 3054269 EDUCACIONAL01-5300 DT Importador - Concessão Bolsa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=368904717
version: 84
---

# IMPORTADOR - CONCESSÃO BOLSA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Importador - Concessão Bolsa* |
| **Situação/Requisito:** | *Ao tentar importar a tabela SCONCESSAOBOLSAHABALUNO, o importador dando erro informando que: "A coluna 'IDCONCESSAOBOLSA' não permite DBNull.Value.".* |
| **Solução/Implementação:** | *Ajuste nas tabelas SCONCESSAOBOLSAHABALUNO, SCONCESSAOBOLSAHABFILIAL e SCONCESSAOBOLSASERVICO com a inclusão do campo IDCONCESSAOBOLSA, sendo este autoinc na tabela SCONCESSAOBOLSA.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
