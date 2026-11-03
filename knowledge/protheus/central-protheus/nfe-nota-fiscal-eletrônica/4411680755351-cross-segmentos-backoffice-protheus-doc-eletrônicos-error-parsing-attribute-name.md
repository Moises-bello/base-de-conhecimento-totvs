---
article_id: 4411680755351
category: NFe - Nota Fiscal Eletrônica
content_hash: 6a8071d8ac819da25c273cac7abba3914a76bb5c2da316cbb36d056a26bc31cc
fetched_at: '2026-06-28T22:40:01.850799+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Error parsing
  attribute name attributes construct error xmlParseStartTag: problem parsing attributes
  Couldn''t find end of Start Tag compacto1000 '
type: support-article
updated_at: '2025-12-15T19:28:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411680755351--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Error-parsing-attribute-name-attributes-construct-error-xmlParseStartTag-problem-parsing-attributes-Couldn-t-find-end-of-Start-Tag-compacto1000
---

**Dúvida**

Como solucionar Error parsing attribute name attributes construct error xmlParseStartTag: problem parsing attributes Couldn't find end of Start Tag compacto1000  ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411686686871/mceclip0.png)

1- Este erro ocorre devido **(error parsing attribute name)** existir algum **caractere especial** que não é permitido na montagem do XML para envio a SEFAZ.  Verificar em todos os cadastro relacionados a esta nota se você encontra os seguintes caracteres:

**# $ ¨ & \* > < ° | ou palavras com acento**

2- Retire os caracteres especiais do cadastro no qual foi encontrado **cadastro de cliente, transportadora, no pedido de venda no campo Mensagem da nota, no cadastro do produto.**

* **Importante:**

Se for utilizado um dos campos abaixo para gerar mensagem em informações complementares das documentações abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

Esta mensagem precisa ser digitada manualmente nos campos, pois se a nota for copiada de algum outro arquivo, por exemplo um arquivo .DOC, **pode conter formatações e estas formações levar caractere especial para os campos.**

3- **Exclua a nota, refaça a nota novamente** e realize uma nova transmissão.
