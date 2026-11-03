---
article_id: 360026730652
category: Escrita Fiscal - Impostos - ICMS
content_hash: d32c10f436d951ec0ef2e918be7995ce01f7fcaf105dea0b84e9d812002d614b
fetched_at: '2026-06-28T22:39:23.994900+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Considerar o CST
  Informado no TES da Nota de Devolução'
type: support-article
updated_at: '2021-07-20T14:07:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026730652--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Considerar-o-CST-Informado-no-TES-da-Nota-de-Devolu%C3%A7%C3%A3o
---

**Dúvida**

Configurar o sistema para considerar o CST Informado no TES da Nota de Devolução?  
   
 **Ambiente**

Protheus – Livros Fiscais– A partir da versão 11.80  
  
**Solução**

Para que o sistema considere o CST informado no TES de uma nota devolução o e não o CST da nota de origem é necessário configurar o parâmetro:

**MV\_CSTORI = T** - Irá considerar o CST informado no documento de origem   
  
**MV\_CSTORI = F** - Irá considerar o CST informado no TES de devolução
