---
content_hash: 3ff79d1eb517308d1e336e60efd3b2529b26119ce1269d9c622a42c5105daa61
fetched_at: '2026-06-29T00:08:16.357330+00:00'
page_id: '244939137'
product: rm
source: tdn-rm
title: TVEJE6_DT_Importação_Campo_Concentração_Antibiótico_com_Casa_Decimal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244939137
version: 118
---

# Importação do Campo Concentração de Antibiótico com Casa Decimal

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Controle de Infecção Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Importação de Antibiótico | | Paciente - Pedido de Antibióticos | |
| **Cadastros Iniciais:** | Cadastro de Antibióticos |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZJIMPORTANTIBIOTICO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Realizada alteração na importação e a exibição do campo concentração do antibiótico no cadastro do paciente para conter uma casa decimal.

## Procedimento para Utilização

       1.            No **TOTVS Controle de Infecção Hospitalar** (RM Janus), acesse **Paciente / Internação / Pedido de Antibiótico**.

O sistema apresentará a tela com os pedidos de antibióticos realizados para o Paciente.

       2.            Dê um duplo clique sobre um antibiótico, após apresentar a tela clique no botão "**Dispensações**".

       3.            Verifique que a coluna Concentração (mg) apresenta agora os valores com uma casa decimal conforme imagem abaixo:

divs
