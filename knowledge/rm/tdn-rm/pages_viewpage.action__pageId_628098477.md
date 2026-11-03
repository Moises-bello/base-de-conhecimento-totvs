---
content_hash: 124e1bdfe7dc2f4cf7b17839dd06d6bff39d06086c78665fd03c003d3f869411
fetched_at: '2026-06-29T00:11:05.033330+00:00'
page_id: '628098477'
product: rm
source: tdn-rm
title: Aprovar ou Reprovar Solicitação de SobreAviso do Time
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628098477
version: 1
---

Este serviço aprova ou reprova as solicitações de SobreAviso do time.

PUT - /team/oncall/{coordinatorId}

Como parâmetro do serviço é necessário informar a coligada do gestor, chapa do gestor.

Exemplo:

<http://localhost/MeuRH/rm/api/rest/team/oncall/1%7C00047>

Para aprovar ou reprovar a solicitação de SobreAviso é necessário preencher no boby do serviço as informações abaixo:

{  
"approved": true,  
"date": "2021-07-07T18:48:26.401Z",  
"justify": "string",  
"requisitions": [  
"string"  
]  
}

| Campo | Informação do serviço |
| --- | --- |
| approved | Aprovar: true  Reprovar: false |
| justify | Justificativa da aprovação ou reprovação da solicitação de SobreAviso |
| requisitions | Informar coligada do funcionário e o id da IDFLUXO da solicitação do funcionário. O campo IDFLUXO está  na tabela AFLUXOSOBREAV. |

Exemplo:

{  
  "approved":false,  
  "date": "2021-04-19T08:05:17.303Z",  
  "justify": "Reprovar solicitação do funcionário 00005",  
  "requisitions": [  
   "1|45"  
  ]  
}
