---
article_id: 360022409111
category: TAF - REINF
content_hash: 65ce8a67734a8b761c945dd5577c1e4b0f6f6d8f771e9d53593a4e24463d1798
fetched_at: '2026-06-28T22:41:34.841207+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Rejeição MS1185
type: support-article
updated_at: '2023-04-04T12:20:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022409111-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Rejei%C3%A7%C3%A3o-MS1185
---

**Dúvida**Como corrigir a rejeição MS1185

<dscResp>O grupo infoEFR é obrigatório se a Natureza Jurídica = [102-3, 103-1, 105-8, 106-6, 108-2, 117-1, 118-0, 123-6, 124-4]. Não deverá ser informado nos demais casos.</dscResp>

**Ambiente**TAF- REINF-  A partir da versão 12.01.17

**Solução**

Validar o preenchimento do campo Cod Nat Juri.![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019332051/mceclip0.png)

Após alterar o cadastros, acesse a rotina TABELA (TAFA494) e exclua o R-1000, conforme o vídeo abaixo.

Após excluir o registro com problema, apure novamente o Evento R-1000.

![excluir_R-1000.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360019333471/excluir_R-1000.gif)
