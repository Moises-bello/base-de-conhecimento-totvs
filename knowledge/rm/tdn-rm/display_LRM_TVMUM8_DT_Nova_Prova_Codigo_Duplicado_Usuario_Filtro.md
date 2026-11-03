---
content_hash: 8b202316dca606195facf9ab2696ab560b40bd303204a43b1351b3719aeec903
fetched_at: '2026-06-29T00:08:15.614257+00:00'
page_id: '244914827'
product: rm
source: tdn-rm
title: TVMUM8_DT_Nova_Prova_Codigo_Duplicado_Usuario_Filtro
type: documentation
url: https://tdn.totvs.com/display/LRM/TVMUM8_DT_Nova_Prova_Codigo_Duplicado_Usuario_Filtro
version: 112
---

# PROVAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Avaliação e Pesquisa* |
| **Função:** | *Provas* |
| **Situação/Requisito:** | *Quando o usuário possui filtro por perfil, o sistema está gerando um erro ao tentar criar uma prova.* |
| **Solução/Implementação:** | *Foi identificado que o erro é ocasionado por uma inconsistência no momento de criar o código da prova, o sistema tenta inserir o filtro do usuário para buscar o código e retorna um código de prova que já existe pra ser o código da nova prova, gerando assim o erro de chave duplicada. Para correção foi feito um ajuste e o sistema agora verifica se o novo código já existe, caso exista, irá incrementar até encontrar o próximo que não exista, evitando assim o erro de se criar uma prova com um código que já existe.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
