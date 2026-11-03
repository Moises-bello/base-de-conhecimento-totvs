---
content_hash: 3c74e2e8456479dd03affac50aaa27aa432dc01127f16cd5cd1f286097ece3ac
fetched_at: '2026-06-29T00:11:56.462719+00:00'
page_id: '866527182'
product: rm
source: tdn-rm
title: DT - Contabilização - Criação de campos para Controle de Registros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866527182
version: 10
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Contabilização - Criação de campos para Controle de Registros |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11214](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11214) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir da release:

* 12.1.2410 e superiores

## **03. SITUAÇÃO/REQUISITO**

Atualmente, enfrentamos no Orçamento problemas recorrentes com a integração do lote contábil mensal. As inconsistências nos registros que não são integrados corretamente nos forçam a recorrer ao cliente para obter a quantidade de registros no lote original (no RM). Isso causa atrasos e aumenta nossa dependência do cliente para resolver problemas de integração. Para melhorar o processo e reduzir nossa dependência do cliente, é necessário adicionar campos que registrem a quantidade de registros por lote diretamente na tabela PCONTABILIZACAO.

## **04. SOLUÇÃO**

O processo Encargos | Contabilização | Geração dos Lançamentos passou a alimentar os campos abaixo após a geração da contabilização.

* **PCONTABILIZACAO.TOTALPARTIDA:** Armazenar o total de registros gerados na tabela PPARTIDA para o lote após a finalização do cálculo da contabilização.
* **PCONTABILIZACAO.TOTALITEMPARTIDA:** Armazenar o total de registros gerados na tabela PITEMPARTIDA para o lote após a finalização do cálculo da contabilização.

## **05. DEMAIS INFORMAÇÕES**
