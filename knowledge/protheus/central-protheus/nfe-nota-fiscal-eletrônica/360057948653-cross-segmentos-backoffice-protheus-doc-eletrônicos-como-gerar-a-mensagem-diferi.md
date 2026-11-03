---
article_id: 360057948653
category: NFe - Nota Fiscal Eletrônica
content_hash: 1e46a05e62d5227940d1a37c0f7b48ef05219790731dbebc21a7c79d1c8ee263
fetched_at: '2026-06-28T22:40:01.672626+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a mensagem
  "Diferimento do ICMS que exceder 12% - Base Legal Item II da Subseção III da Seção
  IV do Apêndice II do RICMS/RS. Valor do ICMS Diferido R$ "'
type: support-article
updated_at: '2022-07-05T16:53:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057948653--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-mensagem-Diferimento-do-ICMS-que-exceder-12-Base-Legal-Item-II-da-Subse%C3%A7%C3%A3o-III-da-Se%C3%A7%C3%A3o-IV-do-Ap%C3%AAndice-II-do-RICMS-RS-Valor-do-ICMS-Diferido-R
---

**Dúvida**Como gerar a mensagem "Diferimento do ICMS que exceder 12% - Base Legal Item II da Subseção III da Seção IV do Apêndice II do RICMS/RS. Valor do ICMS Diferido R$ " ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Para gerar a mensagem **"Diferimento do ICMS que exceder 12% - Base Legal Item II da Subseção III da Seção IV do Apêndice II do RICMS/RS. Valor do ICMS Diferido R$ "** é necessário que o fonte do NFESEFAZ esteja atualizado conforme o link abaixo:

* Para aplicar o RDMAKE de **NFe, MDFe, NFSE há o link abaixo:**

<https://suporte.totvs.com/portal/p/10098/download#detail/947505>

* Conforme o Print estão centralizados em **pastas separadas**, **SPED NF-e** os Rdmakes de Nota fiscal eletrônica.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098613193/mceclip0.png)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

2- Configure a nota com diferimento:

* **No Protheus há 7 tipos de configuração de ICMS diferido conforme o link abaixo:**

<http://tdn.totvs.com/display/public/PROT/FIS0069_DIFERIMENTO_ICMS>
