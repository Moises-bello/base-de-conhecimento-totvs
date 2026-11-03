---
content_hash: b53daaabd792d158539cde30d225e41b2b8eec88e1554cb1baa0a96fcf06bd7d
fetched_at: '2026-06-29T00:09:12.234527+00:00'
page_id: '416842939'
product: rm
source: tdn-rm
title: 3943112 DSAUGHCOM-1333 DT Ajuste no erro ao exibir histórico de pedido de exames.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416842939
version: 1
---

# Ajuste no erro ao exibir histórico de pedido de exames.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Acessamos Unidades Diagnóstico > Controle de Pedidos de Exames |
| **Situação/Requisito:** | Ao abrir qualquer pedido emitido e clicar em exibir histórico a tela gerava uma exceção que só era possível fechar o RM pelo gerenciador de tarefas. |
| **Solução/Implementação:** | Ajuste na função responsável pelo histórico do pedido, que estava acessando mais de uma vez os mesmos dados e assim gerando o erro. |
| **Tickets relacionados:** | [Ticket #3943112](https://totvssuporte.zendesk.com/agent/tickets/3943112 "Open ticket in Zendesk Support") |
| **Requisito:** | Informe o requisito relacionado. |
