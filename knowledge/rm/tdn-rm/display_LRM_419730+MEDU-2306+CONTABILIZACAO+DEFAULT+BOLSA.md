---
content_hash: 74cde836088ede30b77d3a8e87b0475453a8a9252306cfc9c69a7fd97be45488
fetched_at: '2026-06-29T00:08:28.109914+00:00'
page_id: '271659686'
product: rm
source: tdn-rm
title: 419730 MEDU-2306 CONTABILIZACAO DEFAULT BOLSA
type: documentation
url: https://tdn.totvs.com/display/LRM/419730+MEDU-2306+CONTABILIZACAO+DEFAULT+BOLSA
version: 111
---

# Contabilização de Lançamentos do Educacional com Evento Contábil com Default em Bolsa.

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Função:** | *Gerar Lançamento* |
| **Situação/Requisito:** | Cliente possui lançamento com mais de uma bolsa, porém no contrato utiliza-se apenas a Bolsa Maior. Desta forma o evento contábil esta carregando o default da conta da bolsa que possui menor valor, dando erro de débito e crédito. |
| **Solução/Implementação:** | Otimizado evento contábil para carregar os Defaults Contábeis das Bolsas corretamente. |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | FIN000098 |

divs
