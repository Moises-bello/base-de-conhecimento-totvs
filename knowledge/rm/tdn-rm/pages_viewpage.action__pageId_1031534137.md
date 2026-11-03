---
content_hash: 6f96f6d9f43452feaf7f56db62bfb9e0bde5784355295bda172564df51427b0f
fetched_at: '2026-06-29T00:05:48.852573+00:00'
page_id: '1031534137'
product: rm
source: tdn-rm
title: DT - Calculo Pensão Nova Tabela IRRF Redução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1031534137
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Calculo Pensão Nova Tabela IRRF Redução |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHCALCRM-11256](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-11256) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2410.319
  + 12.1.2502.229
  + 12.1.2506.179
  + 12.1.2510.112
  + 12.1.2602 e superiores

## **03. SITUAÇÃO/REQUISITO**

Implementar a redução de IRRF para o cálculo da pensão alimentícia

## **04. SOLUÇÃO**

Foi implementado na fórmula do calculo da pensão alimentícia a redução do IRRF como nos exemplos abaixo:

*Dados fictícios*

Para os casos onde o **Valor aplicado na tabela de Redução de IRRF**for menor que o Limite superior da primeira faixa ( R$ 5.000,00 ), será exibido o detalhamento no log do cálculo dos eventos de pensão alimentícia  
  
  
Caso o funcionário atinja a segunda faixa da nova tabela de IRRF  ( R$ 5.000,01 a  R$ 7.350,00 ), será exibido no log o detalhamento da Redução 

## **05. ASSUNTOS RELACIONADOS**

* [Como calcular a Isenção do Imposto de Renda para quem ganha até 5.000,00 e redução gradual até 7.350,00 - LEI 15.270/2025](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1021212238)
