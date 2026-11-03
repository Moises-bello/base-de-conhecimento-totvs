---
article_id: 360046060134
category: ADVPL - Web Service
content_hash: dbb642b062824dc2915cacbccdf9aaa128bf13d38cac6b370c45c5d0fdd50ee7
fetched_at: '2026-06-28T22:40:10.378386+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - API Totvs filial(Branch)
type: support-article
updated_at: '2022-01-05T18:00:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046060134-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-API-Totvs-filial-Branch
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao realizar o consumo da **API** , não retorna a resposta com os dados devido a um erro interno.  
   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Para utilização do serviço, é necessário estar com a chave **SECURITY** habilitada em seu arquivo **.ini.**

```
[HTTPREST]
Port=8080
URIs=HTTPURI
SECURITY=1
```

**Saiba mais**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Configuração básica REST do protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793)  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Codigos de erros HTTP mais comuns](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045402233)  
[API TOTVS Filial(Branch)](https://api.totvs.com.br/apidetails/Branch_v1_000.json)
