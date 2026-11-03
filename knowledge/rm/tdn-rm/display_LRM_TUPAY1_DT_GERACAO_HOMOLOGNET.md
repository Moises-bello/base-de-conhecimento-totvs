---
content_hash: 8e27125b6465d442f8ae40b0f8178fe13d3cf84dcf3c42cb6f2ba6e67325c6a7
fetched_at: '2026-06-29T00:08:05.138944+00:00'
page_id: '235585291'
product: rm
source: tdn-rm
title: TUPAY1_DT_GERACAO_HOMOLOGNET
type: documentation
url: https://tdn.totvs.com/display/LRM/TUPAY1_DT_GERACAO_HOMOLOGNET
version: 116
---

# GERAÇÃO HOMOLOGNET

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Homolognet* |
| **Situação/Requisito:** | Erro ao gerar arquivo Homolognet: "Valor era muito grande ou muito pequeno para Decimal.Não foi possível armazenar <+Infinito> na coluna VLRubrica. O tipo esperado é Decimal." |
| **Solução/Implementação:** | Ajuste na rotina Homolognet para emitir mensagem de erro quando valor de referência para determinado evento estiver vazio ou zerado, afim de auxiliar o usuário no correto preenchimento dos parâmetros para geração. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUPAY1 TUSKKG |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.11* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
