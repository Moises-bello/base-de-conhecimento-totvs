---
content_hash: 17223dd0bdd67092cbf5b504c93008d15181f0d665a02a7a1ea66e8bdf9df04b
fetched_at: '2026-06-29T00:11:36.921744+00:00'
page_id: '773520795'
product: rm
source: tdn-rm
title: APIs -  Comissões....
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773520795
version: 1
---

### Apis de Comissões

API : POST: [http://localhost:8051/api/imb/v1/commission/view](http://localhost:8021/api/imb/v1/commission/view)

API Comissão View

Exemplo API

{  
    "TipoUsuarioComissionado": "0",  
    "CpfOuCnpjUsuarioComissionado": {  
        "CpfCnpj": "XXX.XXX.XXX.XX"  
    },  
    "CpfOuCnpjSubordinados": [  
        { "CpfCnpj": "" },  
        { "CpfCnpj": "" }  
    ],  
    "CnpjImobiliaria": {  
        "CpfCnpj": ""  
    },  
    "DataInicial": "2022-03-01",  
    "DataFinal": "2022-03-11",  
    "CodigoEmpreendimento": null  
}
