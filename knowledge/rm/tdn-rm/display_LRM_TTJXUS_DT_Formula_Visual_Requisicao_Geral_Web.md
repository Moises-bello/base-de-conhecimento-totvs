---
content_hash: a47737282ee5d6d475288b06486853871f6d3207af1a9ca237e828c2d3d8babe
fetched_at: '2026-06-29T00:06:14.713134+00:00'
page_id: '210049941'
product: rm
source: tdn-rm
title: TTJXUS_DT_Formula_Visual_Requisicao_Geral_Web
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJXUS_DT_Formula_Visual_Requisicao_Geral_Web
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
| **Chamados relacionados:** | TTJXUS |
| **Versões/Release:** | *11.82.42* |

divs
