---
content_hash: d5306871beea23f37ecf32761224d37fd2ee2ea9d4f89fa003b2bf28d655db30
fetched_at: '2026-06-29T00:11:10.273526+00:00'
page_id: '642960341'
product: rm
source: tdn-rm
title: Exemplo Base INSS 13º Dissídio Exclusiva Empresa e Base INSS Dissídio 13º Rescisão
  Exclusiva Empresa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642960341
version: 9
---

Para funcionário que teve um evento com incidência exclusiva do segurado, ao lançar a folha foi calculado apenas o valor descontado do segurado.

Ao calcular a diferença 13º salário por Dissídio é lançado o evento de código de cálculo [115 - Estorno Base INSS Dissídio Ret. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718646) com o valor total dos eventos que incidem em INSS 13º.

Ao lançar o evento de salário mensal do mês atual o valor do evento tem a dedução do valor do código de cálculo 115, ou seja, deduz o valor de diferença do evento que era com incidência exclusiva do segurado da base de cálculo empresa.

Para que o cálculo do valor empresa fique com o valor total é necessário lançar o código de cálculo  sendo esse lançamento automático pelo cálculo da diferença de 13º Salário Por Dissidio.

O mesmo ocorre para o lançamento da rescisão complementar com o código de cálculo .

**Veja simulação nos prints abaixo:**

VALORES DA DIFERENÇA DE 13º SALÁRIO POR DISSIDIO E RESCISÃO COMPLEMENTAR SEM OS CÓDIGOS DE CÁLCULO

Valor da guia de INSS - 3677,42 + 800 + 250(13º sal) + 42,61Média HE 13º sal) = 4770,03

ENCARGOS INSS EMPRESA

FOLHA 5000 – 1322,58 = 3677,42

RESCISÃO 1000 – 200 = 800

VALORES DA DIFERENÇA SALARIAL E RESCISÃO COMPLEMENTAR COM OS CÓDIGOS DE CÁLCULO

Valor da guia de INSS - 5000 + 1000 + 250(13º sal) + 42,61Média HE 13º sal) = 6292,61

ENCARGOS INSS EMPRESA

FOLHA 5000

RESCISÃO 1000
