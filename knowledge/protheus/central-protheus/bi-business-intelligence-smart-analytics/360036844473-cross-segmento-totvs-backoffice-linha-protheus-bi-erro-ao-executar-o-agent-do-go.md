---
article_id: 360036844473
category: BI - Business Intelligence - Smart analytics
content_hash: 6dda9b8171e785634e1f4ab8cbc7fce1ccc1c637b9eb55da950bb30fed299e01
fetched_at: '2026-06-28T22:37:04.142740+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Erro ao executar o
  Agent do GoodData -  POST/gdc/account/login returned 404 not found
type: support-article
updated_at: '2022-07-27T18:06:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036844473-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Erro-ao-executar-o-Agent-do-GoodData-POST-gdc-account-login-returned-404-not-found
---

**Ocorrência**Ao executar o Agent do Analytics, é retornado a seguinte mensagem de erro:  
**POST/gdc/account/login returned 404 not found**  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - GoodData Analytics - Todas as versões  
**Causa**Este erro ocorre pois foi alterado pela TOTVS e GoodData o endereço de acesso ao servidor, visando maior segurança.  
  
**Solução**Neste caso, basta executar a seguinte alteração de endereço dentro da linha **gdc.etl.process\_url** do arquivo **properties**:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047492994/mceclip0.png)

**Saiba mais**[Erro 404 Not Found apresentado ao executar o Agent](https://tdn.totvs.com/pages/releaseview.action?pageId=235312485)
