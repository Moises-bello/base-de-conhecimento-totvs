---
article_id: 28280936026135
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 8a4e4e2c18c55e2ef4de5eb92062b9607fed54c74d393409107ce50f20127571
fetched_at: '2026-06-28T22:37:49.236951+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Onde fica
  gravado o QRCode do PIX impresso no boleto gerado via API
type: support-article
updated_at: '2026-01-07T18:31:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28280936026135-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Onde-fica-gravado-o-QRCode-do-PIX-impresso-no-boleto-gerado-via-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28280922117783) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
Onde fica gravado o QRCode do PIX impresso no boleto gerado via API?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**Para o **boleto+PIX** por meio da API, o **QRCode** é gerado pelo **banco**. No sistema, as informações do PIX podem ser obtidas através do JSON na **SEA**, no campo **EA\_APIMSG**. Não existe um campo específico na tabela que contenha essa informação, **somente no JSON.**  
   
![](https://totvssuporte.zendesk.com/attachments/token/4VVPGFQfU53pfqXUUZ1dDI8ed/?name=image.png)  
 

**Saiba mais**

[Comunicação bancária online - FINA710](https://tdn.totvs.com/pages/viewpage.action?pageId=734394374)  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - Configurar layout do Boleto via API - Novo painel gestor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413850994711/live_preview/01JE9KAFZR4ZHRXQHM4E7EECAG)
