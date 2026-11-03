---
content_hash: a48680cdfaece037869288da6eef883583f7da33eb2c7c3b1b6323e9c4ba5e90
fetched_at: '2026-06-29T00:12:00.135026+00:00'
page_id: '880064597'
product: rm
source: tdn-rm
title: DT - Integração RM X Quírons - API Exclusão de Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=880064597
version: 5
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM x Quírons - API Exclusão de Funcionários |
|  | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11042](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11042) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.240
* 12.1.2406.174
* 12.1.2410.111 e superiores

## **03. SITUAÇÃO/REQUISITO**

Permitir a exclusão de Funcionário e Pessoa na integração RM x Quírons.

## **04. SOLUÇÃO**

Foram desenvolvidas as APIs de exclusão de Funcionário e Pessoa na integração RM x Quírons. O TOTVS Folha de Pagamento RM agora realizará as chamadas dessas APIs através do processo já existente de Exclusão de Funcionários, quando houver integração com a Quírons.

**Importante:** Não será possível excluir Funcionários que possuam movimentações associadas, como Ficha Financeira, Batidas no Ponto, entre outros.

**Passo 1:** Realizado o processo de exclusão do funcionário no sistema.

**Passo 2:** O processo fará o envio da mensageria para o Quírons automaticamente.

## **05. DEMAIS INFORMAÇÕES**

[Integração NG - RH - RM](https://tdn.totvs.com/pages/viewpage.action?pageId=558246499)
