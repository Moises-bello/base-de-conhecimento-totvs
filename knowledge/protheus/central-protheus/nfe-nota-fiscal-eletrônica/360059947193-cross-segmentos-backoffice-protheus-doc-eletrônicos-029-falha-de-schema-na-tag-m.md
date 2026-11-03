---
article_id: 360059947193
category: NFe - Nota Fiscal Eletrônica
content_hash: 6c26439a8e69a06ac1d8272d2ba2a1631419a7ac05c4cff313f9542ff85407c0
fetched_at: '2026-06-28T22:40:00.391862+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema na Tag motDesICMS'
type: support-article
updated_at: '2021-10-11T15:13:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059947193--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-motDesICMS
---

**Dúvida**Como corrigir a 029: Falha de schema na Tag motDesICMS ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se gerada a TAG ***motDesICMS*** é obrigatório gerar a TAG ***vICMSDeson.***

* ***Exemplo do XML errado:***

![moticms.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360098478534/moticms.JPG)

* ***Exemplo do XML correto:***

![corretissimo.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360098479494/corretissimo.JPG)

1 - Caso não tenha valor desonerado, retire do TES o motivo de desoneração do campo ***F4\_MOTICMS  "Mot. Desone."***

![F4_MOTICM__7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098480114/F4_MOTICM__7.png)

2- Após isso, exclua a nota e gere novamente.

3- Para gerar o ***valor desonerado, corretamente*** configurar a nota conforme o artigo abaixo:

[MP - NFE - 934 - Rejeição: Não informado valor do ICMS desonerado ou o Motivo de desoneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025687693-MP-NFE-934-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-valor-do-ICMS-desonerado-ou-o-Motivo-de-desonera%C3%A7%C3%A3o?source=search)
