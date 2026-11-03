---
content_hash: 30151679b01357780c21716074a15d257b37836a1b680fb873565882e0659930
fetched_at: '2026-06-29T00:11:03.361560+00:00'
page_id: '621209563'
product: rm
source: tdn-rm
title: DT – Atestado Médico nas Férias em Dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=621209563
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Totvs Folha de Pagamento |
| Função: | Parametrizador / Férias / Férias em Dobro |
| País: | Brasil |
| Ticket: | N /A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPCALCULO01-12733](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-12733) |

## **02. SITUAÇÃO/REQUISITO**

Ao incluir um atestado inferior a 15 dias é calculado o Limite para gozo de férias de acordo com o parâmetro marcado “Interrompe contagem do período para pagto de férias em dobro nos afastamentos I - L - M - P - T”, mas pelo entendimento não deveria contar o período de atestado.

Validação do retorno Jurídico:

<https://tdn.totvs.com/pages/viewpage.action?pageId=574684381>

Cliente não concorda com o comportamento do sistema.

## **03. SOLUÇÃO**

Criado no parametrizador em Férias, Férias em dobro, o parâmetro “Desconsidera período de atestado médico na interrupção”, que estará habilitado quando o parâmetro “Interrompe contagem do período para pagto de férias em dobro nos afastamentos I - L - M - P - T” estiver marcado.

## **04. DEMAIS INFORMAÇÕES**

Veja links para Documentos de Referência:

[Parametrizador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719558) [/ Férias / Férias em dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719558)
