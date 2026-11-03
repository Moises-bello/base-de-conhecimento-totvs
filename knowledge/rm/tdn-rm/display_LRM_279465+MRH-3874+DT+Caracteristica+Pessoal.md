---
content_hash: e91e02b72dc162ff3ab675ee3b886a84dce50ffe4b29b6f8e2ae73f6371552c1
fetched_at: '2026-06-29T00:08:26.360012+00:00'
page_id: '271176879'
product: rm
source: tdn-rm
title: 279465 MRH-3874 DT Caracteristica Pessoal
type: documentation
url: https://tdn.totvs.com/display/LRM/279465+MRH-3874+DT+Caracteristica+Pessoal
version: 108
---

# CARACTERÍSTICA PESSOAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Característica Pessoal |
| **Situação/Requisito:** | Após excluir uma característica pessoal do funcionário (Anexos Gestão de Pessoas | Características Pessoais), o histórico que fica na tabela VHISTHABPESS não é excluído. |
| **Solução/Implementação:** | Foi criado uma condição que valida se o registro ja foi inserido na tabela e decide se vai inserir um novo ou atualizar o existente. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | MRH-3874 |
| **Requisito (ISSUE):** |  |

divs
