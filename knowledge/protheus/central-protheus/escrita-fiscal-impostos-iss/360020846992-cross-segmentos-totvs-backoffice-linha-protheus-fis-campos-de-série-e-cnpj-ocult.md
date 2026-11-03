---
article_id: 360020846992
category: Escrita Fiscal - Impostos - ISS
content_hash: d5b88ba6acaff85676a9899bb1ff264bbad4d86d020aa406fff519b7a9881a43
fetched_at: '2026-06-28T22:39:35.106108+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Campos de série
  e CNPJ ocultos no relatório 53 do ISS.
type: support-article
updated_at: '2021-06-17T12:30:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020846992-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Campos-de-s%C3%A9rie-e-CNPJ-ocultos-no-relat%C3%B3rio-53-do-ISS
---

**Dúvida**

KCS - Como resolver o problema dos campos ocultos no relatório 53 do ISS?

**Ambiente**

Protheus - Livros Fiscais – A partir da versão 11.80.

**Solução:**

Para que não ocorra a ocultação dos campos de série e CNPJ, é necessário tirar aspas do conteúdo do parâmetro: MV\_MOD53, com isso o problema é resolvido na geração do relatório:

Errado = MV\_MOD53 = "1"

Correto = MV\_MOD53 = 1.
