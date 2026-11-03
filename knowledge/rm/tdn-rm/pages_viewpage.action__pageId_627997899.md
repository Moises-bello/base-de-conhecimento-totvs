---
content_hash: 1b8dae7a11c597af1cb343b5b41ba3efb28ac2abd25f688cbf2582a15bbdbdaa
fetched_at: '2026-06-29T00:11:05.018174+00:00'
page_id: '627997899'
product: rm
source: tdn-rm
title: Gravar Solicitações de SobreAviso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=627997899
version: 3
---

Por este serviço é possível incluir uma solicitação de sobre aviso por dia, por semana, por mês, e com repetição de datas.

POST - /timesheet/onCall/{employeeId}

Boby:

{  
"initDate": "2021-02-10T09:30Z",  
"endDate": "2021-02-11T09:30Z",  
"recurrence": {  
"repetitions": 2,  
"repetitionType": "day",  
"weekDays": [  
{  
"id": "some text",  
"label": "some text"  
},  
{  
"id": "some text",  
"label": "some text"  
}  
],  
"monthlyRule": 2  
},  
"initHour": 540,  
"endHour": 720,  
"considerDays": [  
{  
"id": "some text",  
"label": "some text"  
},  
{  
"id": "some text",  
"label": "some text"  
}  
],  
"justification": "some text"  
}

Passo a passo para preencher as informações do serviço:

| Campo | Informação do Campo |
| --- | --- |
| initDate | Informe neste campo a data de início do período que será solicitado o SobreAviso |
| endDate | Informe neste campo a data final do período que será solicitado o SobreAviso |
| repetitions | Informe a quantidade de vezes que a solicitação irá repetir |
| repetitionType | day, week ou month |
| weekDays | Informe o id de cada dia da semana que deseja solicitar o SobreAviso  id: 1 = Segunda-feira  id: 2 = Terça-feira  id: 4 = Quarta-feira  id: 5 = Quinta-feira  id: 6 = Sexta-feira  id: 7 = Sábado  id: 0 = Domingo |
| initHour | Informe neste campo o início do horário em minutos que será iniciado o intervalo de SobreAviso.  Exemplo: Para 01:00 informar no campo 60 minutos  initHour":60, |
| endHour | Informe neste campo término em minutos do intervalo de SobreAviso.  Exemplo: Para 18:00 informar no campo 1080 minutos  initHour":1080, |
| considerDays | Informe o id do horário que será lançado o SobreAviso  id: 1 = Horário Planejado  id: 2 = Horário Compensado  id: 3 = Horário de Descanso  id: 4 = Feriado |
| justification | Informe a justificativa da solicitação do SobreAviso do funcionário |

O caminho do serviço deve conter:

<http://localhost/MeuRH/rm/api/rest/timesheet/oncall/1%7C00005>

[http://servido](http://servidor)r / Nome do serviço criado no iis / [rm/api/rest/timesheet/oncall/](http://localhost/MeuRH/rm/api/rest/timesheet/oncall/1%7C00005) Coligada do funcionário %7C Chapa do funcionário

Observação:

Para rodar o serviço é necessário informar o cookie gerado pelo portal MeuRH.
