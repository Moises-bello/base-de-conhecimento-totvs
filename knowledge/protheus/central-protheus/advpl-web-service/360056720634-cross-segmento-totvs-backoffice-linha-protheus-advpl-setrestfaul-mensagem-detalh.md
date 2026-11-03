---
article_id: 360056720634
category: ADVPL - Web Service
content_hash: 418a27bb5159352b225e4c26853bafc342e8ae9eade03896c29d499fde94040c
fetched_at: '2026-06-28T22:40:10.518208+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - SetRestFaul Mensagem
  detalhada: Configuração '
type: support-article
updated_at: '2021-12-29T14:08:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056720634-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-SetRestFaul-Mensagem-detalhada-Configura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Qual a configuração para mostrar o quinto parâmetro do **SetRestFaul**?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão P12

**Solução**Para usar este parâmetro é necessário configurar o padrão **TTALK** no seu *c***Exemplo**

```
WSMETHOD GET admin DESCRIPTION "Teste GET REST" WSSYNTAX "/TESTREST/{myid}/{my2}" PATH "/TESTREST/{myid}/{my2}" TTALK "v1"
```

**Saiba mais:**

[Api Protheus com mensagens de erro no padrão Ttalk](https://tdn.totvs.com/pages/viewpage.action?pageId=453308173)  
[SetRestFault](https://tdn.totvs.com/display/framework/SetRestFault)
