---
content_hash: 96d9480a681e179cfa1d635ca164962ec793fcaa1c73f61d6a0d0814f38ad394
fetched_at: '2026-06-29T00:11:56.968407+00:00'
page_id: '873209051'
product: rm
source: tdn-rm
title: Código de Cálculo 473 - Pagamento da Restituição de INSS 13º Retificado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=873209051
version: 9
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Evento provento, do tipo valor e sem incidência.

Este evento será lançado no período da rescisão quando foi identificado o pagamento de restituição de INSS de 13º Salário na rescisão, o desligamento do colaborador for na competência de Dezembro e o mesmo já tiver recebido a 2ª parcela do 13º Salário. Este evento será lançado mediante a marcação do parâmetro 'Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão' criado em [13º salário - Rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719912). 

Quando ocorrer o lançamento do evento com este código de cálculo na rescisão, o evento com o código de cálculo 153 -  Restituição INSS 13º Salário será lançado período 10000 que será gerado automaticamente pelo processo de cálculo mediante a parametrização acima. 

## **02. EXEMPLO DE UTILIZAÇÃO**

[FAQ - Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=873208316)

## **03.** **TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
* PFRETIFICACAOPERIODO
