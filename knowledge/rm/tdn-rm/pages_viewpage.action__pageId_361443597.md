---
content_hash: 9a4e6e209a05330289ac9212ab801b0d318ba31f2b7704f7855b43955d365fc3
fetched_at: '2026-06-29T00:08:58.839041+00:00'
page_id: '361443597'
product: rm
source: tdn-rm
title: 2598645 DEDUINTEGRACOES-2302 DT Simulação de parcelas com faixas de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=361443597
version: 87
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Ao alterar o valor de um contrato, com a matrícula em uma disciplina, e em seguida simular o valor de todas as parcelas do contrato, o sistema encontra valores diferentes para as parcelas não geradas se a simulação for feita com todas as parcelas em aberto, com algumas parcelas geradas ou com algumas parcelas geradas e baixadas. Situação ocorre quando utilizada faixa de crédito com valor fixo. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, de forma que o comportamento do sistema, com relação ao cálculo das parcelas do contrato, seja homogêneo, com relação a existência ou não de parcelas geradas e baixadas e com a utilização de faixa de crédito fixa, para quando ocorre alteração no valor do contrato a ser considerado após a data de alteração. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
