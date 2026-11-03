---
content_hash: f7e2f581048af8e13c214828ff8d248b61e560c11892de3784cbdebc1e3a714d
fetched_at: '2026-06-29T00:08:25.733478+00:00'
page_id: '270925023'
product: rm
source: tdn-rm
title: 347345_Calculo_Valor_Liquido
type: documentation
url: https://tdn.totvs.com/display/LRM/347345_Calculo_Valor_Liquido
version: 107
---

# Cálculo Valor Líquido na Visão de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Função:** | *Cálculo Valor Liquido na Visão de Lançamentos* |
| **Situação/Requisito:** | Quando no lançamento o juros e a multa são calculados por formula e na fórmula de juros utiliza a função TABLAN("VALORMULTA"), ao tentar calcular o valor liquido na tela de lançamentos, o host esta sendo encerrado devido ao processo entrar em loop. |
| **Solução/Implementação:** | Evitar que o Host seja encerrado quando no lançamento o juros e a multa são calculados por formula e na fórmula de juros utiliza a função TABLAN("VALORMULTA"), ao tentar calcular o valor liquido na tela de lançamentos. |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | FIN000254 |

divs
