---
content_hash: 689da49c6811a98157b77f4f70500efc7339aae1a4e371a8d4aa782adcb79122
fetched_at: '2026-06-29T00:11:05.224829+00:00'
page_id: '628375896'
product: rm
source: tdn-rm
title: Exemplo Base INSS Dissídio Folha Exclusiva Empresa e Base INSS Dissídio Folha
  Rescis. Exclusiva Empresa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628375896
version: 2
---

Para funcionário que teve um evento de licença maternidade, por exemplo, com incidência exclusiva do segurado, ao lançar a folha foi calculado apenas o valor descontado do segurado.

Ao calcular a diferença salarial é lançado o evento de código de cálculo [114 – Estorno base INSS dissidio retroativo folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718664) com o valor total dos eventos que incidem em INSS.

Ao lançar o evento de salário mensal do mês atual o valor do evento tem a dedução do valor do código de cálculo 114, ou seja, deduz o valor de diferença do evento que era com incidência exclusiva do segurado da base de cálculo empresa

Para que o cálculo do valor empresa fique com o valor total é necessário lançar o código de cálculo [451 - Base INSS Dissidio Folha Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375538), sendo esse lançamento automático pelo cálculo da diferença salarial.

O mesmo ocorre para o lançamento da rescisão complementar com o código de cálculo [452 - Base INSS Dissidio Folha Rescis. Exclusiva Empresa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=628375549).

**Veja simulação nos prints abaixo:**

VALORES DA DIFERENÇA SALARIAL E RESCISÃO COMPLEMENTAR SEM OS CÓDIGOS DE CÁLCULO

Valor da guia de INSS - 3677,42 + 800 + 250(13º sal) + 42,61Média HE 13º sal) = 4770,03

ENCARGOS INSS EMPRESA

FOLHA 5000 – 1322,58 = 3677,42

RESCISÃO 1000 – 200 = 800

VALORES DA DIFERENÇA SALARIAL E RESCISÃO COMPLEMENTAR COM OS CÓDIGOS DE CÁLCULO

Valor da guia de INSS - 5000 + 1000 + 250(13º sal) + 42,61Média HE 13º sal) = 6292,61

ENCARGOS INSS EMPRESA

FOLHA 5000

RESCISÃO 1000
