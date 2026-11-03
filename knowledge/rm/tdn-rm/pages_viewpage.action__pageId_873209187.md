---
content_hash: 653a63decfd894fcc1e9793dbb54cb82ed378b7abefea383c164158c56fa2367
fetched_at: '2026-06-29T00:11:56.973683+00:00'
page_id: '873209187'
product: rm
source: tdn-rm
title: Código de Cálculo 475 - Pagamento da Restituição de IRRF 13º Retificado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=873209187
version: 7
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Evento provento, do tipo valor e sem incidência.

Este evento será lançado no período da rescisão quando foi identificado o pagamento de restituição de IRRF de 13º Salário na rescisão, o desligamento do colaborador for na competência de Dezembro e o mesmo já tiver recebido a 2ª parcela do 13º Salário. Este evento será lançado mediante a marcação do parâmetro 'Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão' criado em [13º salário - Rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719912). 

Quando ocorrer o lançamento do evento com este código de cálculo na rescisão, o evento com o código de cálculo 52 -  Restituição IRRF 13º Salário será lançado período 10000 que será gerado automaticamente pelo processo de cálculo mediante a parametrização acima. 

## **02. EXEMPLO DE UTILIZAÇÃO**

[FAQ - Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873208316)

## **03.** **TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
* PFRETIFICACAOPERIODO
