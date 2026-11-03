---
article_id: 22540344770967
category: PMS - Integrações
content_hash: c81efe2ef8cb56207fa3f0086ab53daf986ee61a54ae44ace526f5d75d3b6998
fetched_at: '2026-06-28T22:37:16.697582+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Cálculo de horas (AF9_HDURAC)
  na tarefa do projeto
type: support-article
updated_at: '2024-04-05T12:18:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22540344770967-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-C%C3%A1lculo-de-horas-AF9-HDURAC-na-tarefa-do-projeto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22540330698007) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como funcional o cálculo de horas (AF9\_HDURAC) na tarefa do projeto  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões.  
  
**Solução**

Funcionamento dos campos da tarefa do projeto na inclusão/alteração:

* "Duracao Hrs (AF9\_HDURAC)"
* "Calendario (AF9\_CALEND)"
* "Dt.Ini.Prv\* (AF9\_START)"
* "Dt.Fin. Prv. (AF9\_FINISH)"
* "Hr.Inic.Prv. (AF9\_HORAI)"
* "Hr.Fin. Prv (AF9\_HORAF)"

Se informado uma quantia de horas (AF9\_HDURAC) maior que a carga horária do calendário (AEG\_HUTEIS), o sistema joga para os próximos dias as horas excedentes, os campos que se alteram com isso: "Dt.Fin. Prv. (AF9\_FINISH)" e "Hr.Fin. Prv (AF9\_HORAF)".

**Exemplo conceitual:**

Carga horário do calendário são 9 horas (AEG\_HUTEIS), De inicio as 09:00 (AEG\_HORAI) e fim as 17:00 (AEG\_HORAF). Eu informo na duração da tarefa (AF9\_HDURAC) 12 horas.  
Como o calendário admite o máximo de 9 horas ao dia, ele subtrairá até dar zero a hora final (AF9\_HORAF) menos a inicial (AF9\_HORAI). Cada subtração que ainda sobrar horas, é acrescentado 1 dia a mais na tarefa (AF9\_FINISH).

**Exemplo prático:**

Na tarefa iniciada no dia 01/01/2024 será colocado o calendário "001" tem a 9 horas de total de carga horária (08:00 até 17:00), então temos no começo:

* "Duracao Hrs (AF9\_HDURAC)" = 9
* "Calendario (AF9\_CALEND)" = 001
* "Dt.Ini.Prv\* (AF9\_START)" = 01/01/2024
* "Dt.Fin. Prv. (AF9\_FINISH)" = 01/01/2024
* "Hr.Inic.Prv. (AF9\_HORAI)" = 08:00
* "Hr.Fin. Prv (AF9\_HORAF)" = 17:00  
    
  Ao alterar a duração de "9" para "22" teremos:

O sistema subtrairá dentro do intervalo (AF9\_HORAI até AF9\_HORAF) definido, as 22 horas informadas (AF9\_HDURAC):

* 22 - 9 (horas do intervalo) = 13 (SUBTRAÇÃO 1)
* 13 - 9 (horas do intervalo) = 4 (SUBTRAÇÃO 2)
* 4 - 9 (horas do intervalo) = ZERAM AS HORAS (não fica negativo) (SUBTRAÇÃO 3)

O sistema efetuou 3 subtrações, então a data final da tarefa (AF9\_FINISH) será reajustado há 3 dias a frente (01/01/2024 + 3 dias = 03/01/2024) (dia 1 completo (9 horas) = 01/01/2024, dia 2 completo (9 horas) = 02/01/2024, dia 3 parcial (4 horas) = 03/01/2024).

No último dia novo calculado ("AF9\_FINISH" = 03/01/2024), o intervalo serão as últimas horas subtraídas, ou seja, o último dia (AF9\_FINISH) começara as 09:00 (AF9\_HORAI) e terminará as 13:00 (AF9\_HORAF)   
  
**Resultado final:**

* "Duracao Hrs (AF9\_HDURAC)" = 22
* "Calendario (AF9\_CALEND)" = 001
* "Dt.Ini.Prv\* (AF9\_START)" = 01/01/2024
* "Dt.Fin. Prv. (AF9\_FINISH)" = 03/01/2024
* "Hr.Inic.Prv. (AF9\_HORAI)" = 08:00
* "Hr.Fin. Prv (AF9\_HORAF)" = 12:00

**Supondo que o cabeçalho da tarefa esteja assim:**

* "Duracao Hrs (AF9\_HDURAC)" = 9
* "Calendario (AF9\_CALEND)" = 001
* "Dt.Ini.Prv\* (AF9\_START)" = 01/01/2024
* "Dt.Fin. Prv. (AF9\_FINISH)" = 01/01/2024
* "Hr.Inic.Prv. (AF9\_HORAI)" = 08:00
* "Hr.Fin. Prv (AF9\_HORAF)" = 17:00

**Se for alterado o (AF9\_FINISH) manualmente para 3 dias acima aparecerá a mensagem:**

![](https://totvssuporte.zendesk.com/attachments/token/46fgZg9jVFbt0sXxqtyIWOdQ9/?name=image.png)  
  
**Resultado se escolher data inicial:**  
(AF9\_HORAF) = 03/04/2024

(AF9\_HORAI) = 03/04/2024

**Resultado se escolher duração:**  
(AF9\_HORAF) = 01/04/2024

(AF9\_HORAI) = 03/04/2024

(AF9\_HDURAC)" = 27 (3 [dias a frente colocado] \* 9 [intervalo])
