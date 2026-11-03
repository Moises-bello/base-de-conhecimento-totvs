---
content_hash: 1484872ed844bbc2016645c88eee313466cbb7b78be393a57f56e88b6bdb0240
fetched_at: '2026-06-29T00:06:12.228435+00:00'
page_id: '205915371'
product: rm
source: tdn-rm
title: TTEKUG_DT_DataServer_RhuFormacaoAcadData
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEKUG_DT_DataServer_RhuFormacaoAcadData
version: 2
---

# DATASERVER RHUFORMACAOACADDATA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | DataServer RhuFormacaoAcadData |
| **Situação/Requisito:** | Ao tentar consumir o DataServer RhuFormacaoAcadData através do método SaveRecord, o sistema apresenta a mensagem "Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados.". |
| **Solução/Implementação:** | Foi otimizado o método SaveRecord no wsDataServer do TOTVS Business Connect (TBC) e adicionado atributo de segurança ao DataServer. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTEKUG |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | 12.1.8 |

divs
