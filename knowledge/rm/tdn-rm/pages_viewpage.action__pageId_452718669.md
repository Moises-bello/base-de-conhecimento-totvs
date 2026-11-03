---
content_hash: a7e931e4dd32323f1c42dcb204822047703695a5330c319884043a4fb8a360c1
fetched_at: '2026-06-29T00:10:00.991375+00:00'
page_id: '452718669'
product: rm
source: tdn-rm
title: Código de Cálculo 201 - Estorno de Pensão Alimentícia Sobre Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718669
version: 4
---

Evento Provento, tipo valor e com incidência em 'IRRF Férias'.  Este código de cálculo possui um tratamento especial para estornar valores referentes à Pensão Alimentícia sobre Férias no eSocial.

Este evento é inserido na movimentação de pensão do dependente com o tipo 5 - Dif. Férias e com valor negativo.

**Exemplo**

Supondo que o valor lançado de Pensão Alimentícia sobre Férias seja de 500,00 e considerando que o valor correto seja 400,00, ao lançar o evento com CC201 com o valor de 100,00 esse é deduzido do total mensal para pensão alimentícia.

Evento de Pensão Alimentícia sobre Férias CC 113 = 500,00

Evento de Estorno de Pensão Alimentícia sobre Férias CC 201 = 100,00

Total mensal para Pensão Alimentícia = 400,00

Dica

Este valor é deduzido do ultimo movimento de pensão de férias no ano corrente.  Caso não exista movimento de desconto de pensão de férias no ano corrente, o mesmo será deduzido do movimento de pensão de Folha.  
Veja também informações em [DT - S-1010 - Adequação da tag <codIncIRRF> para estorno de pensão](https://tdn.totvs.com/pages/viewpage.action?pageId=1054121536#1-1606214831)

Códigos de Cálculo
