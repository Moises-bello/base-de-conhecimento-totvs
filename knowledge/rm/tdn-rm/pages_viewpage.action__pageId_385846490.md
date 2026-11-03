---
content_hash: 100f268f58a7debb5d0d1462d96dbaddcb70e454ac2aa77bc9c503c32e69f53e
fetched_at: '2026-06-29T00:09:07.774439+00:00'
page_id: '385846490'
product: rm
source: tdn-rm
title: 3426740 DSAUGHSCC-1032 Data de lançamento na conta com a data do aprazamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385846490
version: 3
---

# DATA DE LANÇAMENTO NA CONTA COM A DATA DO APRAZAMENTO (MAPA DE DISPENSAÇÃO)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Mapa de Dispensação | |
| **Parâmetro(s):** | Lançamento na conta com a data do aprazamento |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZATENDMATMED |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta melhoria tem a finalidade de realizar o lançamento do item de estoque na conta, com a mesma data do aprazamento. Para isso, é necessário parametrizar o sistema para se comportar desta maneira.

Este comportamento só será utilizado quando do processamento pela Mapa de Dispensação.

## Procedimento para Utilização

* Acessar o Menu Opções / Parâmetros / Parâmetros Gerais, aba Estoques II. Marcar o parâmetro "Lançamento na conta com a data do aprazamento"

* Criar uma prescrição médica com horários que se estendam para mais de um dia
* Acessar o Menu Estoques / Mapa de Dispensação, gerar um mapa com itens que possuam datas diferentes da data da requisição
* Confirmar os itens do mapa
* Processar o mapa e aguardar a sua conclusão

* Acessar a funcionalidade da Elaboração de Contas, pesquisar o atendimento e visualizar que a data de lançamento corresponde à data do aprazamento.
