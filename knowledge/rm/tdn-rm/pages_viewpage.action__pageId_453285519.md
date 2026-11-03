---
content_hash: 5fbc47ac6474cc36ba534909fbf148ea6856bb2d5f327e0a52dbe80444c2cc0c
fetched_at: '2026-06-29T00:10:11.802097+00:00'
page_id: '453285519'
product: rm
source: tdn-rm
title: FISCAL01-7762 DT Parametrizador do Nucleus -  NFS-e - Observações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453285519
version: 3
---

# Parametrizador do Nucleus

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Backoffice. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MOV000058 | Parametrizador do Nucleus | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** |  |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FISCAL01-7762 |
| **País(es):** | - |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | TPARFILIAL |
| **Sistema(s) Operacional(is):** | - |
| **Pacote:** |  |

## Descrição

Implementação do parâmetro em  Movimento -> Parâmetro -> Gestão de Estoque - Compras e Faturamento -> Integrações -> Fiscal -> Dados Fiscais -> Parâmetros por Filial -> Observações NFS-e, para flexibilização da geração das tags de observações no envio da NFS-e .

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação de um dos pacote de atualizações abaixo:

* 12.1.24 ou superiores.

## **1) PARAMETRIZAÇÃO**

**No contexto do Movimento Selecionar:****Parâmetro -> Gestão de Estoque - Compras e Faturamento -> Integrações -> Fiscal -> Dados Fiscais -> Parâmetros por Filial -> Observações NFS-e**

Parametrizar conforme necessidade do preenchimento das tags de observações  para emissão da NFS-e.

Observações: Os campos de Histórico e Descrição do Produto serão preenchidos na NFS-e conforme parametrização do Movimento.
