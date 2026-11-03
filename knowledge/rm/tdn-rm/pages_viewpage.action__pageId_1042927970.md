---
content_hash: cd1ab864218fd4155380b2f4e287d01efa7cab2fec93d7b39115ca1410e04739
fetched_at: '2026-06-29T00:05:49.921995+00:00'
page_id: '1042927970'
product: rm
source: tdn-rm
title: DT - Provisionamento Crédito Trabalhador - Lançar simultâneo para Férias e
  Adiantamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1042927970
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Cálculo |
| País: | Brasil |
| Ticket: | [#25067879](https://totvssuporte.zendesk.com/agent/tickets/25067879) |
| Issue: | [DRHCALCRM-10233](https://tdn.totvs.com/Requisito/Story/Issue (informe o requisito relacionado) : https:/jiraproducao.totvs.com.br/browse/DRHCALCRM-10233) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2502.285
  + 12.1.2506.251
  + 12.1.2510.174
  + 12.1.2602.100
  + 12.1.2606 e superiores

## **03. SITUAÇÃO/REQUISITO**

Foi solicitado apoio à equipe de Consultoria de Segmento para esclarecer se o provisionamento do Crédito do Trabalhador deve ser realizado apenas uma única vez ao mês ou se é necessário efetuar o provisionamento em todos os pagamentos distintos da folha.

Segue abaixo a documentação contendo a resposta obtida: 

<https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.8Provis%C3%A3odevaloressuperioresaovalordaparcela>

A partir do item **3.8** , constam as informações referentes a esse provisionamento. Em especial, o **segundo parágrafo** do referido item esclarece que o provisionamento deve ser realizado em **todos os pagamentos efetuados** , conforme transcrição abaixo: 

“Para evitar riscos de falta de saldo no fechamento da folha, recomenda-se que a empresa adote uma reserva operacional, ou seja, provisione, dentro do cálculo da folha, o valor estimado da parcela do consignado em todos os pagamentos realizados dentro do mês. Essa prática vale tanto para o adiantamento salarial, antecipação de férias, folhas complementares ou qualquer outra forma de pagamento que reduza o valor líquido disponível antes do fechamento da folha principal.”

## **03. SOLUÇÃO**

Quando houver cálculos de adiantamento e de férias na mesma competência, ambos deverão conter o devido provisionamento, a fim de evitar insuficiência de saldo para descontos posteriores.

Foi criado o parâmetro “Lança provisionamento no adiantamento e no recibo de férias da mesma competência” no Parametrizador | Férias | Empréstimo que ficará disponível se o parâmetro “Lança provisionamento do empréstimo do Crédito Trabalhador nas férias” estiver marcado.

## **04.** **ASSUNTOS RELACIONADOS**

* [Empréstimo - Folha de pagamento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719223)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
