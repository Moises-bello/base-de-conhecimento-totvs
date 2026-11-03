---
content_hash: 2b72ff67993114240067da44e287e9c6d03a30ebc316f2820b9aca5da0e69162
fetched_at: '2026-06-29T00:10:30.159479+00:00'
page_id: '519206640'
product: rm
source: tdn-rm
title: DT - Associação de item Tarefa/Insumo com preço unitário diferente no mesmo
  aditivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519206640
version: 6
---

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Construção e Projetos |
| Módulo: | Gestão de Obras e Projetos |
| Função: | Associação de item no aditivo |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [TOPEXECONTROL01-8057](https://jiraproducao.totvs.com.br/browse/TOPEXECONTROL01-8057) |

## **SITUAÇÃO/REQUISITO**

Sistema permitir associar um mesmo item no aditivo com preço unitário diferente .

## SOLUÇÃO

Criação de um parâmeto que permite a associação de um item com preços unitários diferentes.

**Associar mesmo Insumo/Tarefa  com valor diferente**

Sistema permitirá associar um mesmo Insumo/Tarefa  contratado  com preço unitário  diferente no aditivo.

Desde que o parâmetro  **"Permitir que itens Tarefas/Insumos  contratados sejam associados com outo preço unitário no aditivo "**seja habilitado. [Contratos Parâmetros de Projeto (F6)](https://tdn.totvs.com/pages/viewpage.action?pageId=421385359)

**Importante:** Quando esse parâmetro estiver marcado, não será possível o Consumo de Objetos nos contratos de insumo através do Lookup do grid de consumo. Será exibida a seguinte mensagem:
