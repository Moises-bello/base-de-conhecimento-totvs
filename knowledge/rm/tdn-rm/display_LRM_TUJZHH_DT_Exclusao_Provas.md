---
content_hash: de2d1d512ff46b89b8341df50352a9aa5009a88de7311833aafa6f7987f1a66f
fetched_at: '2026-06-29T00:06:28.508712+00:00'
page_id: '233753750'
product: rm
source: tdn-rm
title: TUJZHH_DT_Exclusao_Provas
type: documentation
url: https://tdn.totvs.com/display/LRM/TUJZHH_DT_Exclusao_Provas
version: 121
---

# CADASTRO DE PROVAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Exclusão de provas* |
| **Situação/Requisito:** | *Ao excluir uma prova através da visão ou da tela de cadastro é gerado um erro de objeto não referenciado.* |
| **Solução/Implementação:** | *Foi identificado que estava sendo realizada uma validação, no tratamento de mensagens de erros, sem a verificação de um valor nulo. Juntamente com a correção da validação, foi realizada, também, a alteração das mensagens de erro em exclusões de provas, quando há dependências de seus anexos, para ficarem mais amigáveis.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** | *12.1.10* |
| **Versão Expedida:** | *12.1.10* |

divs
