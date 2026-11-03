---
content_hash: 655f5175f77d8bd05bf86fca37d0a290ee774df4d6a2fe874c9376d8bbaeb373
fetched_at: '2026-06-29T00:11:05.228983+00:00'
page_id: '628376585'
product: rm
source: tdn-rm
title: DT – Base INSS Dissídio Folha Exclusiva Empresa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628376585
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Eventos da Folha |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-853](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-853) |

## **02. SITUAÇÃO/REQUISITO**

Para funcionário que teve um evento de licença maternidade, por exemplo, com incidência exclusiva do segurado, ao lançar a folha foi calculado apenas o valor descontado do segurado.

Ao calcular a diferença salarial é lançado o evento de código de cálculo 114 – Estorno base INSS dissidio retroativo folha com o valor total dos eventos que incidem em INSS.

Ao lançar o evento de salário mensal do mês atual o valor do evento tem a dedução do valor do código de cálculo 114, ou seja, deduz o valor de diferença do evento que era com incidência exclusiva do segurado da base de cálculo empresa.

## **03. SOLUÇÃO**

Para que o cálculo do valor empresa fique com o valor total é necessário lançar o código de cálculo 451 – Base INSS Dissídio Folha Exclusiva Empresa, sendo esse lançamento automático pelo cálculo da diferença salarial.

O evento deve ser base de cálculo, valor e com incidência exclusiva do empregador.

Para o lançamento da rescisão complementar foi criado o código de cálculo 452 - Base INSS Dissídio Folha Rescis. Exclusiva Empresa que também deve ser base de cálculo, valor e com incidência exclusiva do empregador.

## **04. DEMAIS INFORMAÇÕES**

[Código de Cálculo 451 - BASE INSS DISSÍDIO FOLHA EXCLUSIVA EMPRESA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375538)

[Código de Cálculo 452 - BASE INSS DISSÍDIO FOLHA RESCIS. EXCLUSIVA EMPRESA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375549)

[Exemplo Base INSS Dissídio Folha Exclusiva Empresa e Base INSS Dissídio Folha Rescis. Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375896)
