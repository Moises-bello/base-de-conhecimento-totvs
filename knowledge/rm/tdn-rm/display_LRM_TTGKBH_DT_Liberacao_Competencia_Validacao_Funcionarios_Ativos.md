---
content_hash: 086cfb3a93e3281d0fe6ceb33ee900857405300c4e0d491127b28077f33d5664
fetched_at: '2026-06-29T00:06:14.289003+00:00'
page_id: '210043064'
product: rm
source: tdn-rm
title: TTGKBH_DT_Liberacao_Competencia_Validacao_Funcionarios_Ativos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGKBH_DT_Liberacao_Competencia_Validacao_Funcionarios_Ativos
version: 2
---

# LIBERAÇÃO DE COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Liberação de Competência* |
| **Situação/Requisito:** | Ao validar/realizar a liberação de competência, a validação com o License Server de total de funcionários ativos está considerando o total por coligada, quando o correto é considerar o total geral. |
| **Solução/Implementação:** | Foi alterada a validação para verificar com o license server o total de funcionários ativos em todas as coligadas. Inicialmente liberado apenas para empresas que possuam pelo menos uma coligada em Belo Horizonte. |
| **Chamados relacionados:** | TTGKBH |
| **Versões/Release:** | *11.82.42* |

divs
