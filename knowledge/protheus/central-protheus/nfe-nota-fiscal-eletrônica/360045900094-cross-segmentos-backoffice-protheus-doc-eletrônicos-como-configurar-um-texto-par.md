---
article_id: 360045900094
category: NFe - Nota Fiscal Eletrônica
content_hash: ac5026ac739afbaccf670eccd1f8ff9c797fc2abf845d68458d3b4faef4a5a95
fetched_at: '2026-06-28T22:40:01.806373+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como configurar
  um texto para ser gravado no campo F3_OBSERV para os documentos eletrônicos inutilizados'
type: support-article
updated_at: '2021-08-10T20:16:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045900094--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-configurar-um-texto-para-ser-gravado-no-campo-F3-OBSERV-para-os-documentos-eletr%C3%B4nicos-inutilizados
---

**Dúvida**

Como configurar um texto para ser gravado no campo F3\_OBSERV para os documentos eletrônicos inutilizados ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para configurar um texto para ser gravado no campo **F3\_OBSERV** para os documentos eletrônicos inutilizados esta funcionalidade deve utilizar o parâmetro **MV\_TXTINUT** = **NF INUTILIZADA (texto de exemplo livre, sem aspas).**

* **Exemplo:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065749033/mceclip0.png)**

* **Saiba Mais:**

Este parâmetro tem o objetivo de informar um texto para ser gravado no campo **F3\_OBSERV** para os documentos eletrônicos inutilizados.

Caso esteja em branco será mantido o texto original do campo.
