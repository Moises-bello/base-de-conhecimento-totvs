---
content_hash: aab0f7b63b42e57b84130b591002d478ac39373a7d2ca1a95044ee29cb3a4fc3
fetched_at: '2026-06-29T00:08:43.786383+00:00'
page_id: '306842141'
product: rm
source: tdn-rm
title: 681654 RMSAU-91 DT Inclusão automática na AIH de procedimento principal na
  aba procedimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=306842141
version: 104
---

# Inclusão automática na aba procedimentos ao lançar o procedimento principal na AIH

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM** |
| **Segmento:** | **Saúde** |
| **Módulo:** | **TOTVS Gestão Hospitalar** |
| **Rotina:** | |  | | --- | | **Rotina** | | *Faturamento* |  |  | | --- | | **Rotina(s) envolvida(s)** | | *Faturamento / Faturamento SUS / Elaboração de AIH* | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [RMSAU-91](http://jiraproducao.totvs.com.br/browse/RMSAU-91) |
| **País(es):** | **Brasil** |
| **Banco(s) de Dados:** | **SQL Server® e Oracle®** |
| **Tabelas Utilizadas:** | *SZSUSAIH* |
| **Sistema(s) Operacional(is):** | **Windows®** |

## Descrição

Replicar o procedimento principal na lista de procedimentos da tela de Elaboração de AIH

## Procedimento para Utilização

## Lançamento automático de procedimento principal na lista de procedimentos da tela de Elaboração de AIH

* Acesse Faturamento / Faturamento SUS / Elaboração de AIHs
* Na aba Identificação, ao preencher o procedimento principal o mesmo será validado e automaticamente incluído na aba Procedimentos
* Procedimento lançado automaticamente

  ObservaçõesAo inserir o procedimento principal na tela de elaboração de AIH, o sistema irá fazer com que este procedimento seja submetido às validações para inserção de itens na lista de procedimentos (aba procedimentos nesta tela). Não havendo impedimentos ou críticas que impeçam o faturamento do item, este será inserido na lista de procedimentos (aba de procedimentos).

divs
