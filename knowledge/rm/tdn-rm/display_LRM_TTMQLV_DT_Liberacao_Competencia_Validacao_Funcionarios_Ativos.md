---
content_hash: 277f3d173bf19becef4b377634ff0ab95658ea8cc097e1f5606a02dfefba9a39
fetched_at: '2026-06-29T00:06:16.241735+00:00'
page_id: '212894032'
product: rm
source: tdn-rm
title: TTMQLV_DT_Liberacao_Competencia_Validacao_Funcionarios_Ativos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMQLV_DT_Liberacao_Competencia_Validacao_Funcionarios_Ativos
version: 1
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
| **Chamados relacionados:** | TTMQLV |
| **Versões/Release:** | *12.1.9* |

divs
