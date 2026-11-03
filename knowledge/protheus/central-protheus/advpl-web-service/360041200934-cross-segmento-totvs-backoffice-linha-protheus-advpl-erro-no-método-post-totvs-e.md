---
article_id: 360041200934
category: ADVPL - Web Service
content_hash: 65b6c4f814bdf798bdd958d8de78feac3bcb001298bd0f58b8967b63d87e4e92
fetched_at: '2026-06-28T22:40:10.445341+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro no método Post
  Totvs Eai CostCenter
type: support-article
updated_at: '2021-12-29T13:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041200934-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-no-m%C3%A9todo-Post-Totvs-Eai-CostCenter
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min**

**Ocorrência**Ao fazer uma requisição "*http://localhost:xxxx/REST/01/TOTVSEAI/standardmessage/v1/transactions****"*** no **TOTVS EAI**, utilizando o **METODO POST**, é retornado o erro abaixo:

```
argument #0 error, expected C->O,  function XmlParser on CTBI030
```

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12  
  
**Causa**Esse erro pode ocorrer pela configuração incorreta do **Adapter**, o não preenchimento do parâmetro **MV\_EAICONV,** ou inconsistência nos dados enviados no "**body**" da requisição  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize as configurações conforme o **Saiba Mais**;  
2. Verifique o parâmetro **MV\_EAICONV**, conforme o **Saiba Mais**;  
3. Valide o body da requisição conforme o exemplo abaixo:

```
METODO: POST  
URL: http://localhost:1285/REST/01/TOTVSEAI/standardmessage/v1/transactions
```

```
{  
 "Header" : {  
 "UUID" : "d6bbfa63-ca27-e2ac-0b14-101970f59a32",  
 "Type" : "BusinessMessage",  
 "SubType" : "event",  
 "Event" : "upsert",  
 "Transaction" : "CostCenter",  
 "Version" : "2.002",  
 "SourceApplication": "P122599",  
 "ProductName" : "PROTHEUS",  
 "ProductVersion" : "12.1.25",  
 "CompanyId" : "99",  
 "BranchId" : "01",  
 "GeneratedOn" : "2020-01-08T19:00:00-03:00",  
 "DeliveryType" : "sync"  
  
},  
 "Content" : {  
 "CompanyId" : "99",  
 "BranchId" : "01",  
 "CompanyInternalId" : "99",  
 "Code" : "ABC005",  
 "InternalId" : "99|ABC005",  
 "RegisterSituation" : "Active",  
 "Name" : "Centro de Custo ABC005",  
 "ShortCode" : "ABC005",  
 "SPED" : true,  
 "Class" : 2  
 }  
}
```

**Saiba Mais:  
[Configuração EAI REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041198974)  
[Parametro MV\_EAICONV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041687413)**
