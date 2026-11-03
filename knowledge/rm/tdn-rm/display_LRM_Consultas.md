---
content_hash: 592102ad3809257a48799741a48dc509fb275323661b95485b17ee78a691c1b2
fetched_at: '2026-06-29T00:08:56.567437+00:00'
page_id: '351382539'
product: rm
source: tdn-rm
title: Consultas
type: documentation
url: https://tdn.totvs.com/display/LRM/Consultas
version: 9
---

As operações de consulta retornam o estado referentes aos JobServers do ambiente conforme abaixo:

| Objeto Json | Descrição |
| --- | --- |
| **{** "Alias": "local", "JobServer": "BHD0003455:12120", "LastChange": "2018-04-06T13:40:59-03:00",  "SecsFromLastPooling": 0, "Status": "Stoped" **}** | **Alias:** Alias onde o JobServer está rodando  **JobServer:** Nome e porta do JobServer  **LastChange:** Data da última atividade na GKNOWNJOBSERVER  **SecsFromLastPooling:** Segundos desde à última atividade de pooling  **Status**  ***Started***: JobServer está iniciado  ***Stoped***: JobServer está parado  ***Delayed***: Está iniciado mas com atraso no pooling  ***Unknown***: Não é possível identificar a condição do JobServer |

# Operação list

Esta operação retornará todos os JobServers integrantes dos ambientes cujos Alias estejam presentes no servidor de aplicação que recebeu a requisição.

**Endpoint:** [http://host:port/RMSJobServerApi/list](http://hostport)

Exemplo:

<http://server1:8051/RMSJobServerApi/list>

retorno:

[  
   {  
      "Alias": "local",  
       "JobServer": "server0003455:12120",  
       "LastChange": "2018-04-06T13:40:59-03:00",  
       "SecsFromLastPooling": 0,  
       "Status": "Stoped"  
   },  
   {  
       "Alias": "local",  
       "JobServer": "server050100289:1219",  
       "LastChange": "2018-04-09T14:54:05-03:00",  
       "SecsFromLastPooling": 4,  
       "Status": "Started"  
   },  
   {  
       "Alias": "ex12119",  
       "JobServer": "server0003980",  
       "LastChange": "2018-04-09T14:53:59-03:00",  
       "SecsFromLastPooling": 240,  
       "Status": "Delayed"  
   },  
   {  
       "Alias": "ex12119",  
       "JobServer": "T000000931",  
       "LastChange": "2013-05-25T16:11:48-03:00",  
       "SecsFromLastPooling": 0,  
       "Status": "Unknown"  
   }  
]

# Operação list/{jobServer}/{alias}

Esta operação retornará o status do jobServer a alias informados.

**Endpoint:** http://host:port/RMSJobServerApi/list/{jobServer}/{alias}

Exemplo:

<http://server1:8051/RMSJobServerApi/list/BHD050100289:1219/local>

retorno:

{  
   "Alias": "local",  
   "JobServer": "BHD050100289:1219",  
   "LastChange": "2018-04-09T17:10:34-03:00",  
   "SecsFromLastPooling": 1,  
   "Status": "Started"  
}
