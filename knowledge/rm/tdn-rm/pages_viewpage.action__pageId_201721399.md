---
content_hash: 2df36602d6dd0f0ad71efa69ffa0f3ad5a7021ddd5e2c145aef34d0ea560e62a
fetched_at: '2026-06-29T00:06:05.407146+00:00'
page_id: '201721399'
product: rm
source: tdn-rm
title: TSW546_DT_Parametrização_e_Campos_no_Movimento_Para_NFCE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201721399
version: 3
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | PAR.008 | PARAMETRIZACAO - INTEGRACOES | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | TSW546 |
| **Requisito (ISSUE):** | MOV000058 - Parametrizador do Nucleus e  MOV000003 - Movimento |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas utilizadas:** | TPARFILIAL, TTMVEXT e TMOV |
| **Sistema(s) operacional(is):** |  |
| **Versões/Release:** | *12.1.7* |

## Descrição

A emissão da NFC-e requer a parametrização do processo no ERP TOTVS Gestão de Estoque, Compras e Faturamento do Tipo de Movimento a ser utilizado bem como de qual Filial a usar a integração.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações **12.1.7** deste chamado.

## Procedimento para Utilização

* No Totvs Gestão de Estoque, Compras e Faturamento acesse a aba **Ambiente**, clique em **Parâmetros -> Gestão de Estoque, Compras e Faturamento**e Clique em avançar**.**
* Selecione a opção **Integrações -> Fiscal -> Dados Fiscais** e selecione a filial
* A aba NFC-e será apresentada com os campos a serem parametrizados.
* No Totvs Gestão de Estoque, Compras e Faturamento acesse a aba **Ambiente**, clique em **Parâmetros -> Gestão de Estoque, Compras e Faturamento**e Clique em avançar**.**
* Selecione o Tipo de Movimento a ser configurado.
* Na aba **Fis-Dados** serão apresentados os novos campos
* Acesse o Tipo de Movimento configurado para Emitir NFC-e
* Nesse Movimento verifique que a aba **Dados da NFC-e** será apresentada com os campos a serem preenchidos.
