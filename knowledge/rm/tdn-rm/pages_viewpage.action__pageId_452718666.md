---
content_hash: 4734dfdb84dcf7b11a1cc5d8ea8373da1ffb0c354e4c8a9ed76c0bcd294d854e
fetched_at: '2026-06-29T00:10:00.986287+00:00'
page_id: '452718666'
product: rm
source: tdn-rm
title: Código de Cálculo 199 - Estorno de Pensão Alimentícia Sobre Folha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718666
version: 7
---

Evento Provento, tipo valor e com incidência em 'IRRF'. Este código de cálculo possui um tratamento especial para estornar valores referentes à Pensão Alimentícia sobre Folha no eSocial.

Este evento é inserido na movimentação de pensão do dependente com o tipo 4 - Dif. Movimento e o Valor negativo.

**Exemplo**

Supondo que o valor lançado de Pensão Alimentícia seja de 500,00 e considerando que o valor correto seja 400,00, ao lançar o evento com CC199 com o valor de 100,00 esse é deduzido do total mensal para pensão alimentícia.

Evento de Pensão Alimentícia sobre Folha CC 13 = 500,00

Evento de Estorno de Pensão Alimentícia sobre Folha CC 199 = 100,00

Total mensal para Pensão Alimentícia = 400,00

Dica

Veja mais informações em [DT - S-1010 - Adequação da tag <codIncIRRF> para estorno de pensão](https://tdn.totvs.com/pages/viewpage.action?pageId=1054121536#1-1606214831)

Códigos de Cálculo
