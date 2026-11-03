---
article_id: 1500000099562
category: Call Center - Telecobrança
content_hash: a6c6a278e35b53b4e2fce948da62481a58fc64f0cb3b8f394405795c10d62ec4
fetched_at: '2026-06-28T22:41:28.635177+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Ao realizar a Quitação
  de Cobranças (TMKA290), o sistema não preenche o campo E5_OPERAD.
type: support-article
updated_at: '2022-06-22T17:30:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000099562-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ao-realizar-a-Quita%C3%A7%C3%A3o-de-Cobran%C3%A7as-TMKA290-o-sistema-n%C3%A3o-preenche-o-campo-E5-OPERAD
---

**Dúvida**

Ao realizar a Quitação de Cobranças (TMKA290), o sistema não preenche o campo E5\_OPERAD.

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-Todas as versões.

**Solução**

Quando está sendo utilizado uma Regra de Negociação com Liquidação ativada, portanto quando o operador coloca o título do cliente com status de "Negociado", a rotina do Telecobrança efetua a baixa do título negociado e cria um novo título com o prefixo "**REN**" com uma nova data de vencimento. Estas movimentações da **SE5** que pertencem ao título renegociado não terão o campo **E5\_OPERAD** gravado, pois este campo só será gravado na movimentação referente a baixa do título principal.

Saiba Mais:

**Quitação de Cobrança (TMKA290 - SIGATMK) - [https://tdn.totvs.com/x/YrZWFhttps://tdn.totvs.com/x/YrZWF](https://tdn.totvs.com/x/YrZWF)**
