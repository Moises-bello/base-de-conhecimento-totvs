---
article_id: 21251077436695
category: ADVPL - Web Service
content_hash: 267c96feb80954f69fee059eaff7efa078026b9995ea0c1290bd549f5947aca2
fetched_at: '2026-06-28T22:40:10.580346+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - É possível realizar
  a autenticação via active directory para receber o Token pela API?
type: support-article
updated_at: '2024-02-09T19:40:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21251077436695-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-realizar-a-autentica%C3%A7%C3%A3o-via-active-directory-para-receber-o-Token-pela-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21251082254743) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**É possível realizar a autenticação via active directory para receber o Token pela API?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80

**Solução**

1 - Realizar a configuração do login pelo [Active Directory](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026238652-MP-FRAME-Login-no-Protheus-com-Active-Directory) para o usuário em questão, que irá realizar a solicitação do Token pela API.

2 - Realizar o POST na API de obtenção de token usando o usuário configurado para login pelo Active Directory.

|  |  |
| --- | --- |
| **Parâmetro** | **Valor** |
| grant\_type | password |
| password | Senha do usuário |
| username | Usuário para autenticação |

  

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21251077421079)  
   
**Saiba mais**

[API Token](https://totvssuporte.zendesk.com/agent/tickets/19275345)
