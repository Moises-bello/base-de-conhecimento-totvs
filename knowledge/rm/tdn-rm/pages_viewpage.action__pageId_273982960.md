---
content_hash: bb84ecfe7778ec5714fa53baf5473fe60afbf7340f0ac6d711703f00af9a60b6
fetched_at: '2026-06-29T00:08:32.358434+00:00'
page_id: '273982960'
product: rm
source: tdn-rm
title: DT Validação Período Fechado nos Processos de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273982960
version: 121
---

# Validação Período Fechado nos Processos de Cálculo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão de Custos Hospitalares |
| **Rotina:** | |  | | --- | | **Rotina** | | Esquemas de Apuração  Lançamento de Custo Indireto  Inclusão da Composição na Base de Rateio  Cópia da Base de Rateio |  |  | | --- | | **Rotina(s) envolvida(s)** | | Fechamento do Período | |
| **Requisito/S****tory/Issue:** | SAUGCH01-32 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER®  Oracle® |
| **Tabelas Utilizadas:** | SZ0PERIODOCOMPETENCIA |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Foi Implementada uma validação na execução de processos relacionados aos lançamentos e ao cadastro do período. Essa nova validação irá impedir o processamento caso o período de competência esteja encerrado.

Os processos alterados foram:

* Esquemas de Apuração (Período de Competência);
* Lançamento de Custo Indireto (Lançamento em Conta);
* Inclusão da Composição na Base de Rateio (Base de Rateio);
* Cópia da Base de Rateio (Base de Rateio).

Importante

O período de competência será encerrado quando todos os processos obrigatórios e opcionais utilizados forem executados com sucesso. Para poder executar novamente os processos, o período deve ser reaberto, que pode ser realizado pelo processo Reabertura de Período disponível no cadastro do Período de Competência.

## Procedimento para Utilização

**Processamentos dos esquemas de apuração**

1. No Gestão de Custos Hospitalares, acesse Cadastros / Apuração / Período de Competência.
2. Selecione o período de competência. É permitido somente a seleção de um período por vez.
3. Clique em Processos / Esquemas de Apuração.
4. Selecione os esquemas desejados e clique em executar.  
   Se o período estiver encerrado, será exibida uma mensagem de alerta e o processo será cancelado.

**Lançamento de Custo Indireto**

1. No Gestão de Custos Hospitalares, acesse Lançamentos / Contas de Custo.
2. Selecione um lançamento.
3. Clique em Processos / Lançamento de Custo Indireto.
4. Informe o total da conta indireta e clique em executar.  
   Se o período estiver encerrado, será exibida uma mensagem de alerta e o processo será cancelado.

**Inclusão da Composição na Base de Rateio**

1. No Gestão de Custos Hospitalares, acesse Lançamentos / Base de Rateio.
2. Selecione um lançamento.
3. Clique em Processos / Inclusão da Composição na Base de Rateio.
4. Informe a quantidade da base de rateio para cada um dos centros de custo apresentados e clique em executar.  
   Se o período estiver encerrado, será exibida uma mensagem de alerta e o processo será cancelado.

**Cópia da Base de Rateio**

1. No Gestão de Custos Hospitalares, acesse Lançamentos / Base de Rateio.
2. Selecione um lançamento.
3. Clique em Processos / Lançamento de Custo Indireto.
4. Informe o novo período de competência e clique em executar.  
   Se o período estiver encerrado, será exibida uma mensagem de alerta e o processo será cancelado.

divs
