---
article_id: 4410034743319
category: NFe - Nota Fiscal Eletrônica
content_hash: 7587e67c31465ccc232a89c5a92270354c13f1fa9b63efb76f620b132ce224f7
fetched_at: '2026-06-28T22:40:03.729546+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema na TAG UF da placa '
type: support-article
updated_at: '2021-10-04T18:18:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410034743319-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-TAG-UF-da-placa
---

**Dúvida**Como solucionar a falha de Schema na TAG UF da placa  ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

*1 - Ao gerar falha de Schema **referente a TAG UF no grupo veicTransp** verifique se o seu XML gerou conforme o **exemplo abaixo:***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410021065879/mceclip1.png)

2- Para que não apresente falha de Schema na **transmissão é necessário aplicar os pacotes da documentação abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

O Fonte do ***NFESEFAZ, RPO do TSS e Schema do TSS*** devem estar atualizados.

3- Após isso **exclua a nota e gere novamente.**
