---
content_hash: 74b65a0fcbbfd272e895544578fc94a6e4d50f1ce0d2b187372ee61e8670d2a6
fetched_at: '2026-06-29T00:12:09.410063+00:00'
page_id: '945419435'
product: rm
source: tdn-rm
title: Rescisão por transferência - Tabelas Aperfun,Amovfun,Acompfun e Asaldobancohor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=945419435
version: 12
---

## **01. DADOS GERAIS**

| **Produto:** | **RM** |
| --- | --- |
| **Linha de Produto:** | **Linha RM** |
| **Segmento:** | **RH** |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Função:** | Tabelas no processo de transferência |
| **País:** | **Brasil** |
| **Requisito/Story/Issue:** | **[DRHJORNRM-8054](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6953)** |

## **02. VERSÕES**

* A partir dos patches:
* 12.1.2406.279
* 12.1.2410.233
* 12.1.2502.147 e superiores.

## **03. SITUAÇÃO/REQUISITO**

No processo de transferência entre coligadas  é demonstrada  uma mensagem impedindo a conclusão do processo nas tabelas AMOVFUN e ASALDOBANCOHOR .

## **04****. SOLUÇÃO**

No processo de transferência entre coligadas , o  produto irá copiar as informações das tabelas APERFUN, ACOMPFUN, AMOVFUN, ASALDOBANCOHOR apenas para os registros com data fim anterior à data de transferência.

Importante:

* Esse novo comportamento, será apenas quando for realizada a transferência entre coligadas.
* Os dados serão transferidos para a tabela ASALDOBANCOHOR, se o tipo de rescisão for igual a 5- Transferência sem ônus p/ Cedente .
* Os dados serão transferidos para a tabela AMOVFUN, se estiver marcado o parâmetro "Permite cópia da ficha financeira na transferência entre coligadas" no Folha de Pagamento em : Configurações-Parametrizador-Rescisão- Etapa 5-Rescisão-Transferência.

## **05. EXEMPLO 1 :**

Período: 01/05/2025 a 15/05/2025

Data de Transferência 13/05/2025

Tabela APERFUN

Tabela AMOVFUN

 Tabela ACOMPFUN

Tabela ASALDOBANCOHOR

## **06. EXEMPLO 2:**

Período: 01/05/2025 a 15/05/2025

Data de Transferência 15/05/2025

Tabela APERFUN

Tabela AMOVFUN

Tabela ACOMPFUN

Tabela ASALDOBANCOHOR
