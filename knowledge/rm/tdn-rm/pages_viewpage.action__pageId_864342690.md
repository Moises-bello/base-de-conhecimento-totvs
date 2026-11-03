---
content_hash: 7832e886f61fc6bb620f80a1defaf2c7724f12c4586957221f91fb1ef97d8dc2
fetched_at: '2026-06-29T00:11:55.838779+00:00'
page_id: '864342690'
product: rm
source: tdn-rm
title: DT - Rescisão e Pendências demissionais - Considerar cadastro de estabilidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864342690
version: 14
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Estabilidade |
| País: | Brasil |
| Ticket: | [16431664](https://totvssuporte.zendesk.com/agent/tickets/16431664 "View ticket on the Zendesk portal"); [14096622](https://totvssuporte.zendesk.com/agent/tickets/14096622 "View ticket on the Zendesk portal") |
| Issue | [DRHCALCRM-2749](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2749) ; [DRHCALCRM-3780](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-3780) |

## **02. Versões**

A solução está disponível a partir das versões/patchs abaixo:

* 12.1.2310.250
* 12.1.2402.216
* 12.1.2406.144
* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Quando o funcionário é transferido e possui estabilidade por ser membro da CIPA, ao realizar a uma rescisão com a chapa transferida, não está retornando a mensagem de alerta que o funcionário possui estabilidade. O mesmo cenário ocorre quando o cadastro CIPA é realizado em sistemas terceiros/parceiros, como  Quirons por exemplo, onde o registro é envido somente para o cadastro de estabilidades.

## **04. SOLUÇÃO**

Foi criado o parâmetro 'Considerar o cadastro de estabilidades do funcionário' em Parametrizador | Rescisão | Restrições Cadastrais, que passa a verificar se o funcionário possui alguma estabilidade cadastrada e retorna mensagem de informação quando for realizar demissão do funcionário. Também foi adequado o cadastro de funcionários na aba Pendências demissionais para retornar as estabilidades vigentes na competência atual da base.

Desta forma, com o parâmetro marcado, não é mais verificado o cadastro CIPA e Representantes de funcionários no módulo TOTVS Segurança e Saúde Ocupacional.

Mais informações: [Restrições Cadastrais da Rescisão](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718763)

## **05. ASSUNTOS RELACIONADOS**

* [Rescisão Coletiva](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719318)
