---
article_id: 360021841331
category: Contabilidade Gerencial - Reprocessamento
content_hash: 219787d41d42bef1066ba8159f4580acdcf16a5155a255a52cf3de595877508c
fetched_at: '2026-06-28T22:40:41.932437+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA190 e CTBA193 de
  forma simultânea em schedule
type: support-article
updated_at: '2022-06-02T20:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841331-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-e-CTBA193-de-forma-simult%C3%A2nea-em-schedule
---

**Ocorrência**Quando a rotina CTBA190 é executa via Schedule com a CTBA193, de forma simultânea, a rotina CTBA193 trava tendo que ser reinicializada.  
   
 **Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12  
   
 **Causa**As duas rotinas não poderão ser executadas de forma simultânea devido a concorrência ao locar as tabelas de saldos, CQ0 a CQ9 e CQA.

**Solução**

Como solução/alternativa, sugerimos ajustar o agendamento das duas rotinas, para que quando uma estiver sendo executada a outra esteja parada, assim poderemos garantir que não vai haver concorrência entre elas.

Como agendamento abaixo, iremos garantir que até a 24h o CTBA193 esteja parado e retornando somente as 06h00.

![](https://totvssuporte.zendesk.com/attachments/token/GGXySMgYiCB6uQvYI6uiw3kBt/?name=inline-330524273.png)​

E para a CTBA190, que precisa ser executada somente uma vez ao dia, seja agendado da forma abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/zct83ZmEPicWVqqYBzBPEiQHz/?name=inline1795705805.png)​

Dessa forma não terá processo concorrente e a rotina não vai travar.
