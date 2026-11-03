---
content_hash: ce8a2bfcc9d85dbea9dc30de3a792c14f84dd134b624b43d74885d3a5276a724
fetched_at: '2026-06-29T00:08:51.629367+00:00'
page_id: '337352847'
product: rm
source: tdn-rm
title: RMFIN-1320 DT Tela de cadastro do Pacote
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIN-1320+DT+Tela+de+cadastro+do+Pacote
version: 2
---

# Criação da tela de cadastro de Pacote

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão de Custos Hospitalares |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastros | Outros Cadastros → Pacote |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Consumo Pacote | Lançamentos → Consumo Pacote | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMFIN-1320 |
| **Banco(s) de Dados:** | *SQL Server®, Oracle*® |
| **Tabelas Utilizadas:** | SZ0PACOTE |
| **Sistema(s) Operacional(is):** | *Windows®* |

## Descrição

Criação da Tabela SZ0PACOTE e da tela de cadastro de Pacotes cuja finalidade é normalizar o cadastro de pacotes para a rotina Consumo Pacotes.

## Procedimento para Utilização

### Cadastros

       1.            No sistema TOTVS Gestão de Custos Hospitalares acesse o menu Cadastros → Outros Cadastros → Pacote

O sistema apresenta a view de Pacotes:

2.            Clique no botão de inclusão para incluir um novo pacote. Insira o Código e Descrição e salve.

3.       Verifique que o Pacote foi incluído:

### Rotina Consumo Pacote

       1.         Acesse o menu Lançamentos → Consumo Pacote

       2.            Dê duplo clique em algum registro e visualize o campo pacote (Lookup):

    3.            É possível clicar no link e visualizar o registro do Pacote:
