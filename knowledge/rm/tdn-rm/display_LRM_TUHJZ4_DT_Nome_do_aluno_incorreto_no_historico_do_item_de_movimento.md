---
content_hash: e13191a610583a9d6a354adfcc3e5b7ed4362481a275d5700157f27982d847d2
fetched_at: '2026-06-29T00:06:26.996971+00:00'
page_id: '229146676'
product: rm
source: tdn-rm
title: TUHJZ4_DT_Nome_do_aluno_incorreto_no_historico_do_item_de_movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHJZ4_DT_Nome_do_aluno_incorreto_no_historico_do_item_de_movimento
version: 115
---

# NOME DO ALUNO INCORRETO NA FORMATAÇÃO DO HISTÓRICO DO ITEM DE MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Contabilização por competência* |
| **Situação/Requisito:** | *Sistema está formatando o histórico do item do movimento com o aluno incorreto quando temos mais de um aluno com o mesmo código de contrato e coligadas distintas* |
| **Solução/Implementação:** | *Alterada a query principal de formatação de histórico na geração de movimentos por competência a qual não estava considerando a chave completa da tabela de contratos (SCONTRATO) fazendo com que dados de um contrato incorreto fosse considerado.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | TUIPQ0 |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.42 / 11.82.43* |
| **Versão Expedida:** | *11.82.42 / 11.82.43* |

divs
