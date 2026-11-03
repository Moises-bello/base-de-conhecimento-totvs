---
content_hash: 2c01ba1a12fc3fc9af33abb6ae488e95a0ee43406146876918a397582fedd98b
fetched_at: '2026-06-29T00:09:00.334552+00:00'
page_id: '367234837'
product: rm
source: tdn-rm
title: 1930729 DSAUGHCOM-14 DT Importação Matriz no Controle de Pedidos de Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=367234837
version: 1
---

# Importação Matriz no Controle de Pedidos de Exames

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Controle de Pedidos de Exames |
| **Situação/Requisito:** | Ao importar uma matriz para o controle de pedidos de exame com um valor com ponto, a função retirava o ponto e diminuía o valor, ex.: 240.000 mil ficava 240 |
| **Solução/Implementação:** | A função responsável por persistir os valores do resultado estava retirando o ponto e substituindo esse valor por virgula, esse trecho do código foi retirado. |
| **Documento de Referência:** | [Ticket #1930729](https://totvssuporte.zendesk.com/agent/tickets/1930729 "Open ticket in Zendesk Support") |
