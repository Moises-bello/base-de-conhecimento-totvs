---
content_hash: d6168ec1dc931be91a4385de94e7e47da105a3963528ad993b8a1f888c18942d
fetched_at: '2026-06-29T00:08:22.213682+00:00'
page_id: '269085446'
product: rm
source: tdn-rm
title: MEDU-713_Geração_Movimento_Por_Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269085446
version: 114
---

# Geração de Movimento Por Competência

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Movimento Por Competência |
| **Situação/Requisito:** | Quando temos em um mesmo contrato serviços distintos associados ao mesmo produto,   Exemplo:  Parcela 1 - Serviço 1 - Matricula -> Produto 09.91 – Serviços  Parcela 1 - Serviço 2 - Mensalidade -> Produto 09.91 – Serviços     Na geração do segundo período da competência está sendo apresentada a mensagem de não conformidade abaixo:     Não foi possível gerar o movimento. O valor gerado para os serviços, é maior que o valor total. |
| **Solução/Implementação:** | Como regra essa parametrização não será permitida, pois o educacional não está preparado para tratar este cenário, ou seja, se existir esse cenário será apresentada uma mensagem de validação, explicando que serviços distintos devem ser associados a produtos distintos. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | MEDU-713 |
| **Requisito (ISSUE):** | *N/A* |

divs
