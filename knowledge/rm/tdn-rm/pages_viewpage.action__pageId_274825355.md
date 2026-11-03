---
content_hash: 5580194fb70b7068d267bc3ebe790b447ac0625941f170efd3e68e9e3ed08b74
fetched_at: '2026-06-29T00:08:34.616901+00:00'
page_id: '274825355'
product: rm
source: tdn-rm
title: 846804 EDUCACIONAL01-906 DT Geração de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274825355
version: 97
---

# GERAÇÃO DE LANÇAMENTOS FINANCEIROS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos do tipo contábil. |
| **Situação/Requisito:** | Ao gerar um lançamento financeiro para uma parcela que possua duas bolsas, sendo uma delas com 100%, com o sistema parametrizado para aplicar a maior bolsa, o sistema financeiro, ao retornar as contas contábeis das bolsas aplicadas a parcela, também retorna as contas contábeis da bolsa que não possui valor, o que pode causar divergência caso o valor contábil da bolsa seja atribuída por fórmula dentro do evento contábil, apesar da situação poder ser tratada através de funções de fórmula para bolsas. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos financeiros do tipo contábil para que, ao buscar as contas contábeis das bolsas aplicadas a parcela, considere apenas as bolsas que compõe o lançamento financeiro, ou seja, as que possuem valor. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
