---
article_id: 1500002593562
category: NFe - Nota Fiscal Eletrônica
content_hash: 939c843ef50b8412cc98cf113d400933ca225e579e811840e50e035c74a000ff
fetched_at: '2026-06-28T22:40:05.044840+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 439 Rejeição :
  Informações do intermediador da transação para operação por site de terceiros preenchido
  indevidamente '
type: support-article
updated_at: '2021-07-05T19:37:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002593562-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-439-Rejei%C3%A7%C3%A3o-Informa%C3%A7%C3%B5es-do-intermediador-da-transa%C3%A7%C3%A3o-para-opera%C3%A7%C3%A3o-por-site-de-terceiros-preenchido-indevidamente
---

**Dúvida**Como solucionar a rejeição abaixo:

439 Rejeição : Informações do intermediador da transação para operação por site de terceiros preenchido indevidamente ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Realizar **atualizações do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.006](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052959634)

* Se informado Indicador do Intermediador **DIFERENTE de “1=Operação em**  
  **site ou plataforma de terceiros (intermediadores/marketplace)”**  
  (indIntermed<>1) **Não é permitido o preenchimento** das Informações do Intermediador  
  da Transação (tag: infIntermed)

1- Se informado **diferente de** **Indicador do Intermediador IGUAL a “1=Operação em site ou plataforma de terceiros** (intermediadores/marketplace)”

Campo  vinculado o intermediador através do campo no pedido de vendas  Código do intermediador **C5\_CODA1U** no Documento de entrada **F1\_CODA1U**

 2- O intermediador não pode ser preenchido Informações do**Intermediador da Transação no Menu e campos abaixo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007818861/mceclip0.png)

![intermediador_campos.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007819861/intermediador_campos.JPG)

* **Saiba mais:**

Esta NT, possui as**alteração abaixo:**

**![indIntermed.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101205814/indIntermed.JPG)**

* **Validação da Sefaz:**

![439_rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007654522/439_rejei__o.JPG)
