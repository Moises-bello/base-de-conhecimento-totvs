---
content_hash: 49c39ca4c7e093f91fe417b249f979be566ab41fd267cccf3c85cf955ea0888e
fetched_at: '2026-06-29T00:11:13.141963+00:00'
page_id: '656808751'
product: rm
source: tdn-rm
title: DT – eSocial - Atualizar Recibo Entrega eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656808751
version: 11
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Atualizar Recibo Entrega eSocial |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-1863](https://jiraproducao.totvs.com.br/browse/DRHROTRM-1863 "Ver este problema") |

## **02. SITUAÇÃO/REQUISITO**

O sistema estava duplicando o valor do recibo do eSocial na fila de eventos sendo que no TAF o valor do recibo estava correto.

## **03. SOLUÇÃO**

 Foi criado o filtro ID (Identificador) e o flag" Sobrescrever Recibo" no processo de Atualizar recibo de entrega eSocial.

 Marcando o flag "Sobrescrever Recibo" o sistema irá atualizar os recibos existentes e os que estiverem em branco e com o status 10-Aceito RET.

## **04. DEMAIS INFORMAÇÕES**

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=435097908>
