---
content_hash: 08aab9806a942187f8443ada77f35d1ed27e8a096727df1921ff1b98a6aa0a2b
fetched_at: '2026-06-29T00:11:05.051714+00:00'
page_id: '628108205'
product: rm
source: tdn-rm
title: Solicitar SobreAviso em Lote do Time
type: documentation
url: https://tdn.totvs.com/display/LRM/Solicitar+SobreAviso+em+Lote+do+Time
version: 1
---

Este serviço é utilizado para solicitar SobreAviso em Lote para os funcionários do time por dia, por semana, por mês, e com repetição de datas.

POST - ​/timesheet​/onCall​/Batch

Boby:

[  
{  
  "initDate": "2021-08-01T00:00Z",  
  "endDate": "2021-08-05T00:00Z",  
  "recurrence": {  
    "repetitions": 2,  
    "repetitionType": "month",  
     "weekDays": [  
        {  
         "id": "0",  
         "label": "sunday"  
       },  
       {  
         "id": "3",  
         "label": "wednesday"  
       },  
       {  
         "id": "6",  
         "label": "saturday"  
       }        
     ],  
     "monthlyRule": 2  
  },  
  "initHour": 0,  
  "endHour": 1440,  
  "considerDays": [  
    {  
      "id": "1",  
      "label": "working"  
    },  
    {  
      "id": "2",  
      "label": "compensated"  
    }  
  ],  
  "idName": "1|00022",  
  "justification": "Teste de solicitação de SobreAviso Funcionario 00022"  
},

{  
  "initDate": "2021-08-01T00:00Z",  
  "endDate": "2021-08-05T00:00Z",  
  "recurrence": {  
    "repetitions": 2,  
    "repetitionType": "month",  
     "weekDays": [  
        {  
         "id": "0",  
         "label": "sunday"  
       },  
       {  
         "id": "3",  
         "label": "wednesday"  
       },  
       {  
         "id": "6",  
         "label": "saturday"  
       }        
     ],  
     "monthlyRule": 2  
  },  
  "initHour": 0,  
  "endHour": 1440,  
  "considerDays": [  
    {  
      "id": "1",  
      "label": "working"  
    },  
    {  
      "id": "2",  
      "label": "compensated"  
    }  
  ],  
  "idName": "1|00018",  
  "justification": "Teste de solicitação de SobreAviso Funcionário 00018"  
},  
  
{  
  "initDate": "2021-08-01T00:00Z",  
  "endDate": "2021-08-05T00:00Z",  
  "recurrence": {  
    "repetitions": 2,  
    "repetitionType": "month",  
     "weekDays": [  
        {  
         "id": "0",  
         "label": "sunday"  
       },  
       {  
         "id": "3",  
         "label": "wednesday"  
       },  
       {  
         "id": "6",  
         "label": "saturday"  
       }        
     ],  
     "monthlyRule": 2  
  },  
  "initHour": 0,  
  "endHour": 1440,  
  "considerDays": [  
    {  
      "id": "1",  
      "label": "working"  
    },  
    {  
      "id": "2",  
      "label": "compensated"  
    }  
  ],  
  "idName": "1|03030",  
  "justification": "Teste de solicitação de SobreAviso funcionario 03030"  
}  
  
]

Passo a passo para preencher as informações do serviço:

| Campo | Informação do Campo |
| --- | --- |
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
| idName | Informe a coligada e a chapa do funcionário |
| justification | Informe a justificativa da solicitação do SobreAviso do funcionário |
