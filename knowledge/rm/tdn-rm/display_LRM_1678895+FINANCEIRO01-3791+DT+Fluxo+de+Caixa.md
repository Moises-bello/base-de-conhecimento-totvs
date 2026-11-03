---
content_hash: e0ae6b644a719de5a37b9522e81b1dcb96da1599c13e12d0d38c192d15f20017
fetched_at: '2026-06-29T00:08:47.068015+00:00'
page_id: '318603891'
product: rm
source: tdn-rm
title: 1678895 FINANCEIRO01-3791 DT Fluxo de Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/1678895+FINANCEIRO01-3791+DT+Fluxo+de+Caixa
version: 1
---

# Fluxo de Caixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Fluxo de Caixa |
| **Situação/Requisito:** | Quando existe uma aplicação do tipo CDB pós-fixado que ainda não venceu  e solicita um fluxo de caixa no qual o período compreende a data de vencimento da aplicação e não existe cotação para algumas data futura, sistema estava exibindo mensagem de cotação não encontrada |
| **Solução/Implementação:** | Para aplicação do tipo CDB pós fixado, origem do cálculo seja fluxo de caixa e caso não exista cotação em uma determinada data, então cálculo irá considerar última cotação do índice anterior à data no qual está tentando efetuar o cálculo. Sendo assim, mensagem de “Cotação não encontrada para data ??/??/????” só será apresentada quando não existir nenhuma cotação anterior a data verificada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000255 |
