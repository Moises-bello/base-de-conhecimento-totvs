---
content_hash: 7f747255014c595df3f2f040b34a01bb2c6b5763029d586615e630d9502bef6e
fetched_at: '2026-06-29T00:10:53.072712+00:00'
page_id: '574885134'
product: rm
source: tdn-rm
title: Cálculo do lançamento de batidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574885134
version: 6
---

O novo cálculo do lançamento de batidas considera a proximidade das batidas já existentes no espelho com as batidas horário planejado do funcionário.

**Regra Principal**

Serão consideradas as batidas faltantes para lançamento aquelas que restarem do horário planejado após validação das marcações importadas por **aproximação**.

Regras:

1. Caso a primeira batida coletada seja de hora inferior à primeira hora do horário planejado, ela será associada à esta primeira batida do horário planejado.
2. As demais batidas coletadas serão verificadas por proximidade das batidas planejadas e feito o lançamento das demais conforme planejado.
3. Caso uma batida possua a mesma distância entre duas batidas planejadas, será associada à primeira das duas batidas.

**Exemplo:** Horário 08h | 12h | 14h | 18h - Coletada 16h (está a 2h de 14h e 2h de 18h), será associada a batida de 14h por ela ser a primeira, caso a mesma já não esteja associada à outra batida coletada.

**Exemplo 1:**

Horário Planejado: 

1637946725430\_-235227820

|  |  |  |  |
| --- | --- | --- | --- |
| 08:00 | 12:00 | 14:00 | 18:00 |

Batidas Coletadas:

|  |  |
| --- | --- |
| 06:00 | 09:00 |

Regras:

1. Caso a primeira batida coletada (06:00) seja inferior à primeira hora do horário planejado (08:00), ela será considerada como a primeira hora a ser desprezada no lançamento, ou seja, 06:00 corresponderá à entrada e não será lançada a batida 08:00.
2. A próxima batida coletada (09:00) está mais próxima de qual hora planejada (12:00)? Neste caso será desconsiderada a batida de 12:00h no lançamento.

Como fica o espelho do dia:

|  |  |  |  |
| --- | --- | --- | --- |
| 06:00 | 09:00 | 14:00 | 18:00 |

\*\*Em amarelo são as batidas lançadas.

**Exemplo 2:**

Horário Planejado: 

|  |  |  |  |
| --- | --- | --- | --- |
| 08:00 | 12:00 | 14:00 | 18:00 |

Batidas Coletadas:

|  |  |  |
| --- | --- | --- |
| 08:40 | 11:50 | 15:00 |

Regras:

1. A próxima batida coletada (08:40) está mais próxima de 08:00h do horário planejado, logo será desconsiderada a batida de 08:00h no lançamento.
2. A próxima batida coletada (11:50) está mais próxima de 12:00h do horário planejado, logo será desconsiderada a batida de 12:00h no lançamento.
3. A próxima batida coletada (15:00) está mais próxima de 14:00h do horário planejado, logo será desconsiderada a batida de 14:00h no lançamento.

Como fica o espelho do dia:

|  |  |  |  |
| --- | --- | --- | --- |
| 08:40 | 11:50 | 15:00 | 18:00 |

\*\*Em amarelo são as batidas lançadas.

**Exemplo 3:**

Horário Planejado: 

|  |  |  |  |
| --- | --- | --- | --- |
| 08:00 | 12:00 | 14:00 | 18:00 |

Batidas Coletadas:

|  |  |  |
| --- | --- | --- |
| 12:30 | 13:12 | 16:00 |

Regras:

1. A próxima batida coletada (12:30) está mais próxima de 12:00h do horário planejado, logo será desconsiderada a batida de 12:00h no lançamento.
2. A próxima batida coletada (13:12) está mais próxima de 14:00h do horário planejado, logo será desconsiderada a batida de 14:00h no lançamento.
3. A próxima batida coletada (16:00) está mais próxima de 18:00h do horário planejado, logo será desconsiderada a batida de 18:00h no lançamento.

**Observação:** a batida de 16h está com a mesma distância da batida de 14h e 18h, como a batida de 14h já foi desconsiderada por aproximação de outra batida coletada, foi feita associação com a batida de 18h.

Como fica o espelho do dia:

|  |  |  |  |
| --- | --- | --- | --- |
| 08:00 | 12:30 | 13:12 | 16:00 |

Em amarelo são as batidas lançadas.

**Exemplo 4:**

Horário Planejado: 

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 08:00 | 09:00 | 09:15 | 12:00 | 13:00 | 15:00 | 15:15 | 17:00 |

Batidas Coletadas:

|  |  |  |
| --- | --- | --- |
| 12:40 | 15:05 | 15:20 |

Regras:

1. A próxima batida coletada (12:40) está mais próxima de 13:00h do horário planejado, logo será desconsiderada a batida de 13:00h no lançamento.
2. A próxima batida coletada (15:05) está mais próxima de 15:00h do horário planejado, logo será desconsiderada a batida de 15:00h no lançamento.
3. A próxima batida coletada (15:20) está mais próxima de 15:15h do horário planejado, logo será desconsiderada a batida de 15:15h no lançamento.

Como fica o espelho do dia:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 08:00 | 09:00 | 09:15 | 12:00 | 12:40 | 15:05 | 15:20 | 17:00 |

\*\*Em amarelo são as batidas lançadas.

**Observações**: 

Quando se utiliza horário por jornada, no dia que não existir batidas sendo o tipo trabalho, o sistema vai considerar o início das jornadas as 08:00.

 O início e fim da jornada é considerado para calcular a proximidade das batidas com o horário planejado, esse comportamento é utilizado em horário por jornada e por intervalo.
