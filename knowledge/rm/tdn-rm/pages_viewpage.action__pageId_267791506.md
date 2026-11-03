---
content_hash: 071709ed02026d0fe9246144a683156f944e1439cf3fd5de29cb37bf1b2d30c2
fetched_at: '2026-06-29T00:08:19.515649+00:00'
page_id: '267791506'
product: rm
source: tdn-rm
title: TVYACO_DT_Baixa_Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267791506
version: 113
---

# Baixa de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Finanaceira* |
| **Função:** | *Baixa de Lançamentos* |
| **Situação/Requisito:** | Ao realizar baixa de lançamento financeiro o sistema acusa erro em fórmula, como se estivesse buscando na tabela da FLAN dados da tabela FLANBAIXA.  Mensagem de erro: A fórmula XXXXXX não pode ser executada! A coluna 'IDBAIXA' não pertence à tabela FLAN |
| **Solução/Implementação:** | *Feito melhoria para que ao executar uma fórmula do evento contábil, não ocorra erro informando que a coluna 'IDBAIXA' não pertence à tabela FLAN* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVYDTE |
| **Requisito (ISSUE):** | FIN000040 |

divs
