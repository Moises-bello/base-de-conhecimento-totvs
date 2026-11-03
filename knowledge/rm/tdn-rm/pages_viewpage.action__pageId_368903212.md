---
content_hash: 329c313329983f704fb19bd135bc7854eb4c37547dd58c08d50989ac03804873
fetched_at: '2026-06-29T00:09:00.440449+00:00'
page_id: '368903212'
product: rm
source: tdn-rm
title: 2338144 DSAUGHCOM-93 DT Tela de validação de liberação de resultados no Controle
  de Pedidos de Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=368903212
version: 2
---

# Tela de validação de liberação de resultados no Controle de Pedidos de Exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hositalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Unidades Diagnóstico / Controle de Pedidos de Exames | Controle de Pedidos de Exames |  |  |  | | --- | --- | | **Rotina envolvida** | **Nome Técnico** | | Opções / Parâmetros / Parâmetros Gerais / Unidades Diagnóstico | Valida Liberação de Resultados | |
| **Parâmetro(s):** | Valida Liberação de Resultados (aba Unidades Diagnóstico dos parâmetros gerais) |
| **Tickets relacionados** | [Ticket #2338144](https://totvssuporte.zendesk.com/agent/tickets/2338144 "Open ticket in Zendesk Support") |
| **Requisito****:** | DSAUGHCOM-93 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZPARAM |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado parâmetro para desabilitar/habilitar a tela de validação de liberação de resultados no controle de pedido de exames.

## Procedimento para Utilização

1. Acesse Unidades Diagnóstico / Controle de Pedidos de Exames

          2. Selecione um pedido de exame com estado inicial e de duplo clique.

         3. No preenchimento de resultados altere o combo Executar ação na seguinte forma:

             Digitar Exame / Concluir digitação / Liberar Resultado /

             Escolher o responsável técnico Após esse passo será mostrada a tela de Validação de liberação de resultados

            Então a tela de Validação de Liberação de Resultados será mostrada.

Observação

Somente liberação com alguma regra para validar se a tela de validação será apresentada

            4. Para a tela de Validação de liberação de resultados não ser mostrada e liberar o resultado, é necessário desmarcar a opção Valida Liberação de Resultados que encontra-se em Opções / Parâmetros / Parâmetros Gerais / Aba Unidades Diagnóstico.
