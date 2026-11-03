---
content_hash: 3ba361c2fae524d2aba977358fd34e344221b2ad995068baac8ac6fac2597adc
fetched_at: '2026-06-29T00:08:39.043511+00:00'
page_id: '286005696'
product: rm
source: tdn-rm
title: 714734 MSAU-10404 DT Opção de Tipo de Gerador para Relatório Padrão de Pedido
  de Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286005696
version: 103
---

# Opção de tipo de gerador para relatório padrão de Pedido de exames

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Controle de Pedido de exames | Emissão de pedido de exame | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server® e Oracle® |
| **Tabelas Utilizadas:** | SZUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta melhoria tem por objetivo, disponibilizar a seleção do tipo de gerador de relatórios, para o relatório padrão de Pedido de exames da unidade de atendimento.

Relatório esse que tem como parâmetros os seguintes campos: CODCOLIGADA, CODSETOR E NUMEROPEDIDO.

* Para utilizar o relatório padrão do novo gerador, deve-se ajustar o cadastro da unidade de atendimento conforme imagem abaixo:

* Feita esta configuração, é possível validar a impressão em Unidades de Diagnóstico -> Controle de pedidos de exames e então selecione o exame e solicite a reimpressão do mesmo.

* Após clicar em sim, o sistema gera a visualização através do novo gerador.

divs
