---
content_hash: 653f5d1ae6fe46a51f6898508313bacda209552624f990b05d9c131aae5652eb
fetched_at: '2026-06-29T00:08:15.044298+00:00'
page_id: '244726400'
product: rm
source: tdn-rm
title: TVLQOJ_DT_Historico_SEFIP
type: documentation
url: https://tdn.totvs.com/display/LRM/TVLQOJ_DT_Historico_SEFIP
version: 112
---

# HISTÓRICO DE OCORRÊNCIA SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Histórico de Ocorrência SEFIP |
| **Situação/Requisito:** | Ao realizar a transferência de um funcionário para outra seção (mesma coligada) quando o funcionário possuía mais de um registro no histórico de ocorrência, o sistema exibia um erro de violação de chave. |
| **Solução/Implementação:** | Retirado código que atualizava data de mudança da tabela PHSTOCORRENCIA quando existem mais de um registro de ocorrência, evitando chave duplicada. |
| **Chamados relacionados:** | TVLQOJ |

divs
