---
content_hash: 60d0063b79181e51e7223ce1bbe1571a70c4f67d90a1c687a85ce7906d98baf4
fetched_at: '2026-06-29T00:10:03.310931+00:00'
page_id: '452719098'
product: rm
source: tdn-rm
title: Compensação de horas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719098
version: 24
---

**Compensação**

**Realiza a compensação de cálculo antes da autorização das extras:** Marcando este parâmetro será realizado a compensação de Atrasos/Faltas com as Horas Extras não autorizadas. Caso este parâmetro esteja desmarcado serão compensadas somente as Horas Extras autorizadas.

**Realiza a compensação de cálculo antes de abonar:** Marcando este parâmetro será realizado a compensação de Atrasos/Faltas com as Horas Extras, e será possível abonar somente as horas resultantes desta compensação. Caso este parâmetro esteja desmarcado será possível abonar as ocorrências antes que sejam compensadas.

**Considera a compensação do cálculo por evento:** Ao marcar esse parâmetro será considerado o número de horas do evento ( o número é definido com base na distribuição de   e as extras executadas ), para determinar quais os intervalos de extras serão considerados como compensáveis. Se o intervalo de horas extras que é considerado para compor o evento não for superior ao número de horas do evento, ele será totalmente considerado como intervalo compensável.

Caso contrário o sistema irá modificar os intervalos e considerar como compensável apenas *as extras* que ocorrerem dentro deste intervalo, que terá como limite de horas o número de horas do evento.

***Observação***: Para que o evento seja considerado no calculo das extras compensáveis é necessário que o evento vinculado no sindicato | etapa eventos | seja definida como Compensar em Informações adicionais | Compensação do Cálculo.

11Exemplo 1

**Exemplo de intervalos compensáveis:**

 Horário Planejado Flexível:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| 25/01/2025 | 07:00 | 10:00 | 10:15 | 13:00 |

Horário Executado:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| 25/01/2025 | 06:58 | 12:12 | 13:11 | 16:20 |

Intervalos de extras executadas no dia 25/01:

* 1º ocorrência de extras - 06:58 as 07:00 = 00:02 minutos
* 2º ocorrência de extras - 10:00 as 10:15 = 00:15 minutos
* 3º ocorrência de extras - 13:11 as 16:20 = 03:09 minutos

Distribuição de faixas de extras:

* Tipo de faixa: Diária.
* 1º faixa = 3:00 horas;
* 2º faixa = 2:00 horas;

Distribuição das Extras executadas para definir o **número de horas dos eventos** correspondentes à faixa.

* 1º faixa = 3:00 horas;
* 2º faixa = 00:26 minutos;

Para compor a base de cálculo da 1º faixa é considerado os intervalos de extras.

* 1º ocorrência de extras - 06:58 as 07:00 = 00:02 minutos
* 2º ocorrência de extras - 10:00 as 10:15 = 00:15 minutos
* 3º ocorrência de extras - 13:11 as 16:20 = 03:09 minutos

A primeira e segunda ocorrência de extras serão consideradas como compensável, mas como a terceira ocorrência tem um intervalo com total de horas superior ao número de horas da 1º faixa, ele vai reconhecer como extras compensáveis apenas as extras existentes no intervalo das 10:15 a 12:58 (o total de horas desse intervalo, 02:43, é o que falta para totalizar o número de horas do evento).

 Para compor a base de cálculo da 2º faixa é considerado o intervalo de extras.

* 3º ocorrência de extras - 13:11 as 16:20 = 03:09 minutos

Como o total de horas dessa ocorrência é superior ao número de horas da faixa será considerado como compensável apenas as horas extras existentes no intervalo das 12:58 a 13:24 totalizando os 26 minutos do número de horas do evento/faixa.

Portanto as horas extras executadas após as 13:24 *não serão consideradas como compensáveis.*

2Exemplo 2

**Exemplo de intervalos compensáveis:**

Horário Planejado Flexível:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| 25/01/2025 | 07:00 | 10:00 | 10:15 | 13:00 |

Horário Executado:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| 25/01/2025 | 14:00 | 15:00 | 16:00 | 22:00 |

Intervalos de extras executadas no dia 25/01:

* 1º ocorrência de extras - 14:00 as 15:00 = 1:00 de extra.
* 2º ocorrência de extras - 16:00 as 22:00 = 6:00 de extras.

Distribuição de faixa de extras:

* Tipo de faixa: Diária.
* 1º faixa = 3:00 horas;
* 2º faixa = 2:00 horas;
* 3º faixa = 2:00 horas;

Distribuição das Extras executadas para definir o **número de horas dos eventos** correspondentes à faixa.

* 1º faixa = 3:00 horas;
* 2º faixa = 2:00 horas;
* 3º faixa = 2:00 horas;

Para compor a base de cálculo da 1º faixa é considerado os intervalos de extras.

* 1º ocorrência de extras - 14:00 as 15:00 = 1:00 de extra.
* 2º ocorrência de extras - 16:00 as 22:00 = 6:00 de extras.

Para compor a base de cálculo da 2º faixa é considerado o intervalo de extras.

* 2º ocorrência de extras - 16:00 as 22:00 = 6:00 de extras.

Para compor a base de cálculo da 3º faixa é considerado o intervalo de extras.

* 2º ocorrência de extras - 16:00 as 22:00 = 6:00 de extras.

 O intervalo da 1º ocorrência de extras - 14:00 as 15:00, será totalmente considerado como compensável.

Como o total de horas da segunda ocorrência é superior ao número de horas da 1º faixa será considerado como compensável somente as extras existentes no intervalo das 15:00 as 17:00.

Para a 2º faixa será considerado como compensável os intervalos de extras existentes das 17:00 as 19:00.

Para a 3º faixa será considerado como compensável os intervalos de extras existentes das 19:00 as 21:00.

Portanto a extra que ocorreu no intervalo de 21:00 as 22:00 *não será considerada como compensável.*

3Exemplo 3

**Exemplo de intervalos compensáveis:**

 Horário Planejado Flexível:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| 25/01/2025 | 07:00 | 10:00 | 10:15 | 13:00 |

Horário Executado:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data | Entrada 1 | Saída 1 | Entrada 2 | Saída 2 |
| 25/01/2025 | 06:58 | 12:12 | 13:11 | 16:20 |

Intervalos de extras executadas no dia 25/01:

* 1º ocorrência de extras - 06:58 as 07:00 = 00:02 minutos
* 2º ocorrência de extras - 10:00 as 10:15 = 00:15 minutos
* 3º ocorrência de extras - 13:11 as 16:20 = 03:09 minutos

Distribuição de faixas de extras:

* Tipo de faixa: Diária.
* 1º faixa = 2:00 horas;
* 2º faixa = 99:00 horas;

Distribuição das Extras executadas para definir o **número de horas dos eventos** correspondentes à faixa.

* 1º faixa = 2:00 horas;
* 2º faixa = 1:26 minutos;

Para compor a base de cálculo da 1º faixa é considerado os intervalos de extras.

* 1º ocorrência de extras - 06:58 as 07:00 = 00:02 minutos
* 2º ocorrência de extras - 10:00 as 10:15 = 00:15 minutos
* 3º ocorrência de extras - 13:11 as 16:20 = 03:09 minutos

A primeira e segunda ocorrência de extras serão consideradas como compensável, mas como a terceira ocorrência tem um intervalo com total de horas superior ao número de horas da 1º faixa, ele vai reconhecer como extras compensáveis apenas as extras existentes no intervalo das 10:15 a 11:58 (o total de horas desse intervalo, 01:43, é o que falta para totalizar o número de horas do evento).

 Para compor a base de cálculo da 2º faixa é considerado o intervalo de extras.

* 3º ocorrência de extras - 13:11 as 16:20 = 03:09 minutos

Como o total de horas dessa ocorrência é superior ao número de horas da faixa será considerado como compensável apenas as horas extras existentes no intervalo das 11:58 a 13:24 totalizando 01:26, que corresponde ao do número de horas do evento/faixa.

Portanto as horas extras executadas após as 13:24 *não serão consideradas como compensáveis.*

**Considera as extras que foram compensadas na distribuição das extras:** Marcando esse parâmetro, ao realizar a distribuição de faixas de extra, as extras que foram compensadas pelo horário flexível, serão consideradas no cálculo da distribuição.
