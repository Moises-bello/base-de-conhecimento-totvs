---
content_hash: 1527b95511b11c3cb5e9fd6039325b4c5ac57db0f4c5ca7eeaf6c2f4c11907b2
fetched_at: '2026-06-29T00:11:50.579903+00:00'
page_id: '843140979'
product: rm
source: tdn-rm
title: Como é o cálculo do adicional noturno na tag <qtdHrsSem> nos eventos S-2200
  e S-2206?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=843140979
version: 6
---

---

Vamos demonstrar nesta FAQ como o sistema realiza o cálculo da <qtdHrsSem> no XML, especialmente quando o funcionário possui adicional noturno.

## Temos as seguintes jornadas:

**Data:** 03/07/2023

**Intervalos de Trabalho:**

* **07:00 às 12:00:**

+ Duração: 5 horas
+ Total em minutos: 5 × 60 = 300 minutos (diurnos)

* **13:00 às 19:00:**

+ Duração: 6 horas
+ Total em minutos: 6 × 60 = 360 minutos (diurnos)

**Total de minutos trabalhados no dia 03/07/2023:**

* 300 minutos (manhã) + 360 minutos (tarde) = 660 minutos

**Data:** 07/07/2023 - 08/07/2023

**Intervalos de Trabalho:**

* **07/07/2023 19:00 às 22:00:**

+ Duração: 3 horas
+ Total em minutos: 3 × 60 = 180 minutos (diurnos)

* **07/07/2023 22:00 às 08/07/2023 02:30:**

+ Duração: 4 horas e 30 minutos
+ Total em minutos: 4,5 × 60 = 270 minutos (noturnos)
+ **Cálculo da hora noturna:**

- Multiplicador da hora noturna: 0,1429
- Noturna: 270 minutos × 0,1429 = 38,583 minutos (aproximadamente 39 minutos)
- Total ajustado: 270 minutos + 39 minutos = 309 minutos

* **08/07/2023 03:30 às 05:00:**

+ Duração: 1 hora e 30 minutos
+ Total em minutos: 1,5 × 60 = 90 minutos (noturnos)
+ **Cálculo da hora noturna:**

- Noturna: 90 minutos × 0,1429 = 12,861 minutos (aproximadamente 13 minutos)
- Total ajustado: 90 minutos + 13 minutos = 103 minutos

* **08/07/2023 05:00 às 07:00:**

+ Duração: 2 horas
+ Total em minutos: 2 × 60 = 120 minutos (diurnos)

**Total de minutos trabalhados nos dias 07/07/2023 - 08/07/2023:**

* 180 minutos (diurnos) + 309 minutos (noturnos ajustados) + 103 minutos (noturnos ajustados) + 120 minutos (diurnos) = 712 minutos

**Cálculo da** **<qtdHrsSem>****:**

* **Total de minutos trabalhados na semana:**

+ 660 minutos (03/07/2023) + 712 minutos (07/07/2023 - 08/07/2023) = 1.372 minutos

* **Conversão para horas:**

+ 1.372 minutos ÷ 60 = 22,867 horas
+ Arredondamento: 22,87 horas

<qtdHrsSem>22,87</qtdHrsSem>

**Observação**:

A representação de 1 hora e 30 minutos como 1,50 ocorre devido à conversão dos minutos em uma fração de hora. O cálculo é baseado no fato de que uma hora tem 60 minutos, e cada minuto equivale a 1/60 (fração)​ de uma hora. Assim:

1 hora e 30 minutos:

1 hora = 1,00 (em horas)

30 minutos = 30/60 (fração) = 0,50 (em horas)

Portanto, somando as partes:

1 + 0,50 = 1,50 horas.

Essa conversão é usada em contextos que exigem o cálculo em horas decimais.

## **DEMAIS INFORMAÇÕES**

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.2310 e superiores |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
