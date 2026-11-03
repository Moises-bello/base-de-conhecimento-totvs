---
content_hash: 5d769ecfc3268dc9e1d05882b5d60965f0819945fda93b80a9fc4aa00d275d10
fetched_at: '2026-06-29T00:08:38.240861+00:00'
page_id: '285642760'
product: rm
source: tdn-rm
title: 908999 FINANCEIRO01-824 Validação do tipo contábil no acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285642760
version: 101
---

# VALIDAÇÃO DO TIPO CONTÁBIL NO PROCESSO DE GERAR ACORDO MÚLTIPLO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Geração de acordo múltiplo. |
| **Situação/Requisito:** | O processo está validando o tipo contábil mas o mesmo não é informado na interface do processo. |
| **Solução/Implementação:** | O processo de acordo múltiplo não deve consistir o tipo contábil já que essa informação não está disponível na interface para seleção. A regra para preenchimento do campo será: se um único lançamento origem busca do mesmo, se o primeiro for "Contábil" ou "Baixa Contábil" usa esse último, caso contrário busca do primeiro lançamento.  A validação a ser realizada será sobre o tipo contábil dos lançamentos origem do acordo múltiplo. Não será permitido, para um mesmo cliente/fornecedor, lançamentos do tipo "Contábil" ou "Baixa contábil" juntos com outros que não possuam esse tipo. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 908999. |
| **Requisito:** | FINANCEIRO01-824. |

divs
