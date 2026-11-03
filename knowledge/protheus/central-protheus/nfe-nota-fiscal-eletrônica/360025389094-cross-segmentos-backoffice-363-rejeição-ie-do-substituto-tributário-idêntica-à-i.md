---
article_id: 360025389094
category: NFe - Nota Fiscal Eletrônica
content_hash: 40e57d62fffe1fe653ddd4356cef21115270a087ce5f57e01749b5bcd8c4b221
fetched_at: '2026-06-28T22:40:03.026278+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice 363 Rejeição: IE do substituto tributário idêntica
  à IE do emitente ou do destinatário'
type: support-article
updated_at: '2025-07-25T18:41:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025389094-Cross-Segmentos-Backoffice-363-Rejei%C3%A7%C3%A3o-IE-do-substituto-tribut%C3%A1rio-id%C3%AAntica-%C3%A0-IE-do-emitente-ou-do-destinat%C3%A1rio
---

**Dúvida**Como solucionar a rejeição 363 Rejeição: IE do substituto tributário idêntica à IE do emitente ou do destinatário ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Caso informe a TAG **IEST** idêntica ao **IE do emitente** ou do **IE destinatário** gera rejeição **363**.

Sendo assim, há um tratamento no fonte do **NFESEFAZ** para que não seja gerado a TAG **IEST** caso **IE** do emitente ou do destinatário seja idêntico ao do **emitente** ou do **destinatário.**

1. **Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

     2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

* **Validação da Sefaz:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039360954)**
