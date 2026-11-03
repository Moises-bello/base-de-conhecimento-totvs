---
content_hash: a8e304e8dc8601bc4a9ef624a38f34ca7a3650ee312acceca4c1f30d737b616a
fetched_at: '2026-06-29T00:08:20.273326+00:00'
page_id: '268576066'
product: rm
source: tdn-rm
title: TWACIS_DT_Exportacao_CCN_Filtros_Invalidos
type: documentation
url: https://tdn.totvs.com/display/LRM/TWACIS_DT_Exportacao_CCN_Filtros_Invalidos
version: 111
---

# EXPORTAÇÃO DE DADOS DE PERIÓDICOS PARA CCN

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Exportação de dados de periódicos para CCN* |
| **Situação/Requisito:** | **Ao executar o processo "Exportação de dados de periódicos para CCN" ao selecionar um dos filtros "descrição tipo de publicação", "descrição grupo publicação" ou "Autor", o sistema retorna um erro informando que a coluna não existe e não conclui a pesquisa das publicações periódicas.** |
| **Solução/Implementação:** | *Foi identificado uma inconsistência na consulta que utiliza os filtros, pois na junção das tabelas, algumas tabelas não foram informadas. Foi feito o ajuste na consulta e todos os filtros passaram a ser executados corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TWAKGT* |
| **Requisito (ISSUE):** | *N/A* |

divs
