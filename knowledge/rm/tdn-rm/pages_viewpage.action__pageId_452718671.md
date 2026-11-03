---
content_hash: 47ab0058ee706cf52b5901e40f0a641bc8e957edd5a52402ef0b044962b7340c
fetched_at: '2026-06-29T00:10:00.994919+00:00'
page_id: '452718671'
product: rm
source: tdn-rm
title: Código de Cálculo 200 - Estorno de Pensão Alimentícia Sobre 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718671
version: 4
---

Evento Provento, tipo valor e com incidência em 'IRRF 13º salário'. Este código de cálculo possui um tratamento especial para estornar valores referentes à Pensão Alimentícia sobre 13º Salário no eSocial.  
Este evento é inserido na movimentação de pensão do dependente com o tipo 6 - Dif. 13º Salário.

**Exemplo**

Supondo que o valor lançado de Pensão Alimentícia sobre 13º Salário seja de 500,00 e assumindo que o valor correto seja 400,00, ao lançar o evento com CC 200 com o valor de 100,00 esse é deduzido do total mensal para Pensão Alimentícia.

Evento de Pensão Alimentícia sobre 13º CC120 = 500,00

Evento de Estorno de Pensão Alimentícia sobre 13º Salário CC200 = 100,00

Total mensal para Pensão Alimentícia 13º Salário = 400,00

Dica

Veja mais informações em [DT - S-1010 - Adequação da tag <codIncIRRF> para estorno de pensão](https://tdn.totvs.com/pages/viewpage.action?pageId=1054121536#1-1606214831)

Códigos de Cálculo
