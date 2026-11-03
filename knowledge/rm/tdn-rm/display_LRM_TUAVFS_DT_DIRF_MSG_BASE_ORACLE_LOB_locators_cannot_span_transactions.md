---
content_hash: a87f601b2c114d511b0e13b07ebae51c940dbd55982e11949171de72bc5cffe1
fetched_at: '2026-06-29T00:06:23.308772+00:00'
page_id: '223935856'
product: rm
source: tdn-rm
title: TUAVFS_DT_DIRF_MSG_BASE_ORACLE_LOB_locators_cannot_span_transactions
type: documentation
url: https://tdn.totvs.com/display/LRM/TUAVFS_DT_DIRF_MSG_BASE_ORACLE_LOB_locators_cannot_span_transactions
version: 125
---

# DIRF em Arquivo Delphi

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gravação dos parâmetros da DIRF em Arquivo* |
| **Situação/Requisito:** | Ao gerar a DIRF em Delphi está retornando a mensagem abaixo em algumas bases oracleORA-22990: LOB locators cannot span transactions |
| **Solução/Implementação:** | Foi otimizado o tratamento para gravação de campos CLOB oracle. Separando a instrução de atualização do campo CLOB da tabela pparamrelat.parametros |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TUAVFS* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
