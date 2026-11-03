---
article_id: 1500006728761
category: TAF - REINF
content_hash: ccfd28c664c27600e81145912fc99eccaa440ac0ef75b3d0211de80a2a884da4
fetched_at: '2026-06-28T22:41:33.550637+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Erro de Schema ao transmitir
  REINF
type: support-article
updated_at: '2023-03-31T16:33:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006728761-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-de-Schema-ao-transmitir-REINF
---

**Dúvida**

Ao realizar a transmissão de um evento ocorre a seguinte rejeição:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009020961/mceclip0.png)

**Ambiente**

TAF - SIGATAF  - A partir da versão 12.1.23  
  
**Solução**

Para correção é necessário aplicar pacote de atualização da pasta Schemas do TSS utilizado na transmissão da Reinf.

<https://suporte.totvs.com/portal/p/10098/download?e=761857>

Após atualizar a pasta de Schema da REINF, exclua a apuração inconsistente e transmita novamente o evento.
