---
content_hash: 82ee45d679ce534c1905ee3cf6be8b391fe3129b7b05db6457fcdd635794bd44
fetched_at: '2026-06-29T00:08:10.160698+00:00'
page_id: '240302397'
product: rm
source: tdn-rm
title: TVAJPT_DT_DataServerRateioFixo
type: documentation
url: https://tdn.totvs.com/display/LRM/TVAJPT_DT_DataServerRateioFixo
version: 115
---

# RATEIO FIXO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DataServer FopRateioFixoData* |
| **Situação/Requisito:** | *Ao tentar acessar o DoReadRecord com uma chave primária que não existe, o sistema retornava uma exceção de "Segurança Estendida ativa" mesmo quando a funcionalidade não estava ativa no sistema.* |
| **Solução/Implementação:** | *Removida a exceção do ReadRecord* |
| **Chamados relacionados:** | TVAJPT |

divs
