---
article_id: 360050828014
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 196c3b461eec75da48398e0fc28f08a51f4dadcb2dae7a8182fc9bba88466aad
fetched_at: '2026-06-28T22:41:43.325125+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -SIGAATF - ATFA006 - Como é feito
  o calculo da taxa de índice em relação a Curva '
type: support-article
updated_at: '2021-09-01T10:29:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050828014-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA006-Como-%C3%A9-feito-o-calculo-da-taxa-de-%C3%ADndice-em-rela%C3%A7%C3%A3o-a-Curva
---

**Dúvida**ATFA006 Como é feito o calculo da taxa de índice em relação a Curva pelo Método de depreciação = A- Índice de Depreciação  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 11.80.  
  
**Soluçã:**

Rotina: ATFA005 (Cadastro de Índices)

* O sistema faz o calculo do Índice (FNT\_TAXA) apenas quando o campo FNI\_TIPO= 2 (CALCULADO)

          Período deve ser MENSAL.

* Nos campos Ini Curva (FNI\_CURVIN) e Fim Curva (FNI\_CURVFI), informamos a data inicial e final da CURVA de demanda.

\*Esse intervalo de período é importante, pois o sistema irá somar todas as "curvas" informadas no período e dividir pela curva atual (Farei um exemplo mais abaixo).

![](https://totvssuporte.zendesk.com/attachments/token/YLSCoqkC6iQgVi0FamEAxNi78/?name=inline-1645642538.png)​

Na rotina de Atualização de Índices (ATFA006).

Iremos relacionar o cadastro que criamos na ATFA005, Campo FNT\_CODIND.

Informaremos a data do índice (FNT\_DATA) e a curva de demanda (FNT\_CURVA) para o período.

Exemplo:

|  |  |
| --- | --- |
| DATA | CURVA |
| 01/02/2019 | 25,00 |
| 01/03/2019 | 25,00 |
| 01/04/2019 | 10,00 |

Para calcular o índice o sistema faz da seguinte forma:

Taxa = a / b onde:

 a = Curva de demanda do período (FNT\_CURVA).

 b = **Soma das curvas** do intervalo entre a data inicial **(FNI\_CURVIN)** e final da curva

**(FNI\_CURVFI).**

01/02/2019

25,00 / 25,00+25,00 + 10,00 = 0,41666667 (Índice)

01/03/2019

25,00 / 25,00+25,00 + 10,00 = 0,41666667 (Índice)

01/04/2019

10,00 / 25,00+25,00 + 10,00 = 0,16666666 (Índice)

![](https://totvssuporte.zendesk.com/attachments/token/W5d8DlPosnB9FRmg21ftMbMzN/?name=inline502357080.png)​

No cadastro do ativo (ATFA012)

1. Tipo de ativo: 10 – Depreciação Gerencial/Contabil
2. Método de depreciação:  A – Índice de Depreciação
3. Índ. Cálculo (N3\_CODIND)

![](https://totvssuporte.zendesk.com/attachments/token/MPpNaEhdSkatpTDlnaWMFUdK3/?name=inline-463368031.png)​

O calculo (ATFA050) da amortização/depreciação é o Valor Original do bem x Índice:

![](https://totvssuporte.zendesk.com/attachments/token/zl69dwm9aMXv2e8Sw1YDdPfS8/?name=inline978478094.png)​

**IMPORTANTE!** Toda vez que for incluído uma CURVA nova, na rotina de ATUALIZAÇÃO DE ÍNDICE dentro do período- FNI\_CURVIN e Fim Curva FNI\_CURVFI, o sistema reajustará os Índices do grupo.

Para exemplificar, Inclui mais uma CURVA de 15,00, no período, note que todo índice foi reajustado.

![](https://totvssuporte.zendesk.com/attachments/token/1kXcO3LWsvSS2hM4k5lpTaATH/?name=inline-1618469367.png)​

E como ficará o calculo mensal (ATFA050) que já foi processado?

O valor que esta gravado não é alterado.

Para que o calculo mensal fique conforme índices novos, deverá ser feito o descalculo mensal e posteriormente um novo calculo (ATFA050).
