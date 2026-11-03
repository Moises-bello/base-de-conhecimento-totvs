---
content_hash: d1a4cddacd58e59100007cf3fae7e456069193c063aacb28c3f472862e52cd8c
fetched_at: '2026-06-29T00:06:16.431427+00:00'
page_id: '212897983'
product: rm
source: tdn-rm
title: TTNKZ3_DT_Formula_Visual_Requisicao_Geral_Web
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNKZ3_DT_Formula_Visual_Requisicao_Geral_Web
version: 1
---

# FÓRMULA VISUAL EM REQUISIÇÕES (PORTAL)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Pessoas* |
| **Função:** | *Requisições Portal* |
| **Situação/Requisito:** | Ao tentar adicionar uma fórmula visual à action RhuReqGeralActionWeb estava sendo gerada uma exceção, impedindo o processo. |
| **Solução/Implementação:** | Foi adicionada uma validação para quando não houvesse requisição a ser validada no inicio da action. |
| **Chamados relacionados:** | TTNKZ3 |
| **Versões/Release:** | *12.1.9* |

divs
