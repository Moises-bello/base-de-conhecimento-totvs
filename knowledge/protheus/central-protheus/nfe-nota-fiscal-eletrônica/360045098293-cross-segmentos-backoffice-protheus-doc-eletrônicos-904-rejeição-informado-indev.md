---
article_id: 360045098293
category: NFe - Nota Fiscal Eletrônica
content_hash: 10723ff10ac11df487162a799c079e57247ec125303bc6d7e0d23c896a096e86
fetched_at: '2026-06-28T22:40:03.328013+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  904 Rejeição:
  Informado indevidamente campo valor de pagamento'
type: support-article
updated_at: '2025-07-14T14:21:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045098293-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-904-Rejei%C3%A7%C3%A3o-Informado-indevidamente-campo-valor-de-pagamento
---

**Dúvida**Como corrigir a rejeição 904 : Informado indevidamente campo valor de pagamento

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

* Para notas com **FINNFE = 3 ou 4,** mesmo que tenha gerado **duplicata no Protheus.** Essa nota não pode gerar a TAG Vpag **diferente de 0.**

1. Para a correção **aplicar a patch** e **compilar o NFESEFAZ** que consta no link abaixo de acordo com a **sua release do Protheus:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

2. Após isso, **exclua a nota e gere** novamente.

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003050001)
