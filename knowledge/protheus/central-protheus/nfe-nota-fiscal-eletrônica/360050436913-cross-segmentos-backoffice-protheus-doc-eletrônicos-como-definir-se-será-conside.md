---
article_id: 360050436913
category: NFe - Nota Fiscal Eletrônica
content_hash: 61300a6de74b70ee24bf5d68337f3512b59f86ec1ea97b6cbffe6b367bee51e0
fetched_at: '2026-06-28T22:40:01.641809+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como definir se
  será considerado o endereço de cobrança ou entrega no Danfe para o emitente '
type: support-article
updated_at: '2021-10-11T18:45:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050436913--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-definir-se-ser%C3%A1-considerado-o-endere%C3%A7o-de-cobran%C3%A7a-ou-entrega-no-Danfe-para-o-emitente
---

**Dúvida**Como definir se será considerado o endereço de cobrança ou entrega no Danfe para o emitente ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

É possível definir se será impresso no Danfe o **endereço de entrega** ou o **endereço de cobrança** do emitente através do parâmetro MV\_SPEDEND.

1 - Para sair o **endereço de entreg**a habilitar o parâmetro **MV\_SPEDEND = .T.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074760314/mceclip2.png)

2-  Para sair o **endereço de cobrança** habilitar o parâmetro **MV\_SPEDEND = .F.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075980753/mceclip1.png)**

* **Saiba mais:**

Os dados de **endereço de entrega e cobrança** são os dados cadastrados no configurador pela empresa.
