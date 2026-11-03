---
content_hash: 5846d4c9ebcdb2627dbdf8f2144ddae78a73d4666598e50a6737820d7b3bb8d2
fetched_at: '2026-06-29T00:09:12.272342+00:00'
page_id: '416843922'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-357 DT CRIAÇÃO DO SERVIÇO DE DEVOLUÇÃO DE PRODUTOS ORIGINADOS
  DE PEDIDOS DO TOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416843922
version: 3
---

# CRIAÇÃO DO SERVIÇO DE DEVOLUÇÃO DE PRODUTOS ORIGINADOS DE PEDIDOS DO TOP

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MOV.001 | INCLUSÃO DE MOVIMENTO | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | - |
| **Tickets relacionados** | - |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-357 |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | TMOVRELAC |
| **Sistema(s) Operacional(is):** | - |
| **Pacote:** | - |

## Descrição

Ao realizar a devolução de um produto originado de pedidos do TOP, o mesmo irá realizar o estorno dos Itens de Movimento gerado pelo TOP.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação de um dos seguintes pacotes de atualizações:

* 12.1.21 ou superiores

## Procedimento para Utilização

* Para o correto funcionamento do Estorno dos Itens de Movimento gerado pelo TOP e necessário que o tipo de movimento originado pelo TOP esteja parametrizado para utilizar "Integração Projetos".
