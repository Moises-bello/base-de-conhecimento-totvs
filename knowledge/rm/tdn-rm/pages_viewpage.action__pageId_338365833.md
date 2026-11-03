---
content_hash: 60d2374a9b50b3b984dc63b1e016f1034a0c4dde96c6f9cc8c78394c1c2788c7
fetched_at: '2026-06-29T00:08:51.718680+00:00'
page_id: '338365833'
product: rm
source: tdn-rm
title: 1835499 EDUCACIONAL01-4014 DT Vazamento de memória na tela de movimentações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338365833
version: 86
---

# MOVIMENTAÇÃO - VAZAMENTO DE MEMÓRIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | *****Totvs Educacional***** |
| **Função:** | *Movimentações* |
| **Situação/Requisito:** | Foi detectado que ao tentar acessar a visão de lançamentos financeiros várias vezes na movimentação de um mesmo usuário, o sistema se fecha. |
| **Solução/Implementação:** | Foi identificado que todas as vezes q ao acessar a aba de lançamentos financeiros o sistema a carregava novamente.  Após a inclusão de um tratamento, o sistema passou a carregar apenas uma vez a visão com os lançamentos gerados, acabando com o consumo excessivo de memória na movimentação. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
