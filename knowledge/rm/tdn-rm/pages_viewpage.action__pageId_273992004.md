---
content_hash: 2a07ea2416e72311370fd1bffde0c44bc724bfbe353c9df651c28061eef6efd9
fetched_at: '2026-06-29T00:08:32.580791+00:00'
page_id: '273992004'
product: rm
source: tdn-rm
title: DT Valor Total do Lançamento em Conta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273992004
version: 105
---

# Valor Total do Lançamento em Conta

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Gestão de Custos Hospitalares |
| **Rotina:** | |  | | --- | | **Rotina** | | Lançamento em Conta de Custo | | Esquemas de Apuração | | Lançamento de Custo Indireto |  |  | | --- | | **Rotina(s) envolvida(s)** | | Lançamento a Centro de Custo | | Cenários | |
| **Requisito/Story/Issue:** | SAUGCH01-45 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER®  Oracle® |
| **Tabelas Utilizadas:** | SZ0LANCAMENTOCONTA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementado campo "Total Lançamento" na tela "Lançamento a Centro de Custo". Esse campo irá somar todos os valores dos lançamentos a centro de custo para a conta quando o cenário do lançamento não for informado e quando o cenário for o cenário principal.

O processo de "Esquemas de Apuração" foi atualizado para preencher o novo campo quando processar esquemas com Destino "Lançamento Conta Direta" e "Lançamento Conta Indireta". O processo de "Lançamento de Custo Indireto" também foi atualizado para preencher o campo "Total Lançamento" com o valor do lançamento informado ao executar o processo.

## Procedimento para Utilização

**Esquema de Apuração**

1. No Gestão de Custos Hospitalares, acesse Cadastros / Período de Competência.
2. Selecione o período a processar.
3. Escolha os esquemas a serem processados e clique em executar.  
   Se forem executados esquemas com o destino "Lançamento Conta Direta" ou "Lançamento Conta Indireta", o campo "Total Lançamento" da tela "Lançamento em Conta de Custo" será preenchido com o total do lançamento a conta de custo.

**Lançamento de Custo Indireto**

1. No Gestão de Custos Hospitalares, acesse Lançamentos / Contas de Custo.
2. Realize o lançamento da conta indireta, informando o período de competência e o código da conta de custo.
3. Selecione o lançamento realizado e acesse Processos / Lançamento de Custo Indireto.
4. Informe o valor total do lançamento e clique em executar.  
   O sistema realizará os lançamentos a centro de custo pelo critério de rateio associado à conta de custo.

divs
