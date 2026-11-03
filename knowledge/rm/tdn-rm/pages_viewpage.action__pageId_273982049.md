---
content_hash: 88bc3895a271487fc7bd03e11c3f16f954aa8749a06579a1b50a30e79adeac88
fetched_at: '2026-06-29T00:08:32.023275+00:00'
page_id: '273982049'
product: rm
source: tdn-rm
title: DT Parametrização dos Processos de Fechamento do Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273982049
version: 114
---

# Parametrização dos Processos de Fechamento do Período

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão de Custos Hospitalares |
| **Rotina:** | |  | | --- | | **Rotina** | | Fechamento do Período |  |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros  Período de Competência | |
| **Parâmetro(s):** | Utiliza cálculo de Doação e Desconto  Utiliza cálculo da Refeição  Utiliza cálculo do Repasse |
| **Requisito/S****tory/Issue:** | SAUGCH01-33 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER®  Oracle® |
| **Tabelas Utilizadas:** | SZ0PARAMETRO |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Implementados quatro parâmetros para indicação dos processos opcionais do fechamento do período são utilizados no sistema. Os parâmetros criados são:

* Utiliza cálculo de Doação e Desconto: Indica se utiliza o processo de Cálculo da Doação e Desconto;
* Utiliza cálculo da Refeição: Indica se utiliza o processo de Cálculo da Refeição;
* Utiliza cálculo do Repasse: Indica se utiliza o processo de Cálculo do Repasse;

Com a configuração dos parâmetros realizada, o cadastro do Período de Competência bem como o processo de Fechamento do Período se adaptarão às configurações realizadas, ou seja, caso um dos processos opcionais seja indicado como não utilizado, as informações do mesmo não aparecerão em nenhum dos processos citados.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No módulo **Gestão de Custos Hospitalares** acesse Sistema > Ambiente > Parâmetros > **Gestão de Custos**. Configure os parâmetros a seguir:

|  |  |
| --- | --- |
|  | **Descrição** |
| **Nome:** | Utiliza cálculo de Doação e Desconto |
| **Valores:** | S (default) ou N |
| **Descrição:** | Indica se o cálculo de Doação e Desconto será utilizado no sistema. |

|  |  |
| --- | --- |
|  | **Descrição** |
| **Nome:** | Utiliza cálculo da Refeição |
| **Valores:** | S (default) ou N |
| **Descrição:** | Indica se o cálculo da Refeição será utilizado no sistema. |

|  |  |
| --- | --- |
|  | **Descrição** |
| **Nome:** | Utiliza cálculo do Repasse |
| **Valores:** | S (default) ou N |
| **Descrição:** | Indica se o cálculo do Repasse será utilizado no sistema. |

## Procedimento para Utilização

1. No módulo Gestão de Custos Hospitalares acesse Sistema > Ambiente > Parâmetros > Gestão de Custos.
2. Acesse a opção 52.00.02 - Fechamento do Período / Parâmetros Gerais do Fechamento do Período.
3. Configure os parâmetros "Utiliza cálculo de Doação e Desconto", "Utiliza cálculo da Refeição" e "Utiliza cálculo do Repasse".
4. Acesse o cadastro do período de competência, através do menu Cadastros / Períodos de Competência.  
   Serão exibidas as datas de processamentos dos cálculos obrigatórios e somente as datas dos processos opcionais configurados na etapa 3.
5. Abra o processo Fechamento do Período, através do cadastro do período do competência / Processos / Fechamento do Período.  
   Serão exibidas as datas de processamentos dos cálculos obrigatórios e somente as datas dos processos opcionais configurados na etapa 3.

divs
