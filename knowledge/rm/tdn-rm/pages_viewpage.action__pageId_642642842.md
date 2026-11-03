---
content_hash: ceef3c1c89e1787c846504b9bf11f2e7cd24d60c8ac886601050ae7f38a0354e
fetched_at: '2026-06-29T00:11:10.227981+00:00'
page_id: '642642842'
product: rm
source: tdn-rm
title: DT – Base INSS Dissídio 13º Salário Incidência Exclusiva Empresa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642642842
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | **Linha RM** |
| Segmento: | **RH** |
| Módulo: | **Totvs Folha de Pagamento** |
| Função: | Eventos de Folha |
| País: | Brasil |
| Ticket: | 11596656 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-853](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-853) |

## **02. SITUAÇÃO/REQUISITO**

Para funcionário que teve um evento com incidência exclusiva do segurado, ao lançar a folha foi calculado apenas o valor descontado do segurado.

Ao calcular a diferença 13º salário por Dissídio é lançado o evento de código de cálculo [115 - Estorno Base INSS Dissídio Ret. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718646) com o valor total dos eventos que incidem em INSS 13º.

Ao lançar o evento de salário mensal do mês atual o valor do evento tem a dedução do valor do código de cálculo 115, ou seja, deduz o valor de diferença do evento que era com incidência exclusiva do segurado da base de cálculo empresa.

Para que o cálculo do valor empresa fique com o valor total é necessário lançar o código de cálculo [457 - Base INSS Dissidio 13º salário Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375538), sendo esse lançamento automático pelo cálculo da diferença de 13º Salário Por Dissidio.

O mesmo ocorre para o lançamento da rescisão complementar com o código de cálculo [458 - Base INSS Dissidio 13º Rescis. Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375549).

## **03. SOLUÇÃO**

Para que o cálculo do valor empresa fique com o valor total é necessário lançar o código de cálculo [457 - Base INSS Dissidio 13º salário Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375538), sendo esse lançamento automático pelo cálculo da diferença de 13º Salário Por Dissidio.

O mesmo ocorre para o lançamento da rescisão complementar com o código de cálculo [458 - Base INSS Dissidio 13º Rescis. Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375549).

## **04. DEMAIS INFORMAÇÕES**

[457 - Base INSS Dissídio 13º Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=642960331)

[458 - Base INSS Dissídio 13º Rescis. Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=642961707)

[Exemplo Base INSS Dissídio Folha Exclusiva Empresa e Base INSS Dissídio Folha Rescis. Exclusiva Empresa](https://tdn.totvs.com.br/pages/editpage.action?pageId=642960341)
