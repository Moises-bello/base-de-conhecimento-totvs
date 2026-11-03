---
article_id: 360026071534
category: NFe - Nota Fiscal Eletrônica
content_hash: 70b0887b00c0aefec2f7b8be0f664eea60daf0acb599408949baa3e32b67324e
fetched_at: '2026-06-28T22:40:00.277632+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  927 Rejeição
  : Número do item fora da ordem sequencial'
type: support-article
updated_at: '2021-07-05T14:35:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026071534--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-927-Rejei%C3%A7%C3%A3o-N%C3%BAmero-do-item-fora-da-ordem-sequencial
---

**Dúvida**Como solucionar a rejeição abaixo:

927 -Rejeição: Número do item fora da ordem sequencial ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Os **fontes** que realizam a **transmissão** da **NF-e**, a gravação do **XML** e a impressão do **DANFE**, não realizam alterações na ordem dos itens.

A **ordem** é definida na **Preparação do Documento de Saída** para gravação das linhas de itens na tabela **SD2.**

* **Para isso existe uma documentação completa no link abaixo:**

<http://tdn.totvs.com/pages/releaseview.action?pageId=338374819>

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040660494/mceclip0.png)
