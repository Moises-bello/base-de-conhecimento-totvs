---
article_id: 360043240593
category: NFe - Nota Fiscal Eletrônica
content_hash: f9a3d7be7f5892f691b9b1202eb1b2b550cb5c6772e67429916aafc79693f68b
fetched_at: '2026-06-28T22:40:06.885489+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Mensagem de erro:
  invalid property _PAGAMENTO TSSNFEV4: 80'
type: support-article
updated_at: '2025-06-11T18:53:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043240593-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Mensagem-de-erro-invalid-property-PAGAMENTO-TSSNFEV4-80
---

**Dúvida**Como solucionar o erro Mensagem de erro: invalid property \_PAGAMENTO TSSNFEV4: 80 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A TAG referente a pagamento  foi criada para o **layout 4.00 da NFe** para que não ocorra o erro o fonte do **NFESEFAZ** deve conter as novas informações.

1- Realize **atualização do NFESEFAZ** do link abaixo:

Atualizar o NFESEFAZ (Padrão da pasta NFE)

* Para aplicar o RDMAKE de **NFe, MDFe, NFSE há o link abaixo:**

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)

* Conforme o Print estão centralizados em **pastas separadas**, **SPED NF-e** os Rdmakes de Nota fiscal eletrônica e **NFSE** os RDMAKES de nota fiscal de serviço.

![PRINT_DO_RDMAKE.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000047121)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

2- Após isso, **exclua a nota** e gere novamente.
