---
content_hash: 6bd386343ab21c0d12971bca59249db33387fb48714ba1cbc59daec5d15ef8f9
fetched_at: '2026-06-29T00:08:03.780901+00:00'
page_id: '235325069'
product: rm
source: tdn-rm
title: TUOFBL_DT_GERACAO_SEFIP_TOMADORES
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOFBL_DT_GERACAO_SEFIP_TOMADORES
version: 116
---

# GERAÇÃO DE SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | *Ao gerar o SEFIP por tomadores com mais de um registro com o mesmo CEI, é gerada uma exceção que interrompe o processo.* |
| **Solução/Implementação:** | *Foi corrigida a unificação de registros com mesmo CEI para não acessar registros removidos.* |
| **Chamados relacionados:** | TUOFBL, TUPBI0 |

divs
