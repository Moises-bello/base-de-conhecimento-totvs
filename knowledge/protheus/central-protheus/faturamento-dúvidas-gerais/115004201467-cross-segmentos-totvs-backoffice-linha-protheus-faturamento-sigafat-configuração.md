---
article_id: 115004201467
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: c3cf6f682e4dcd0053ea7d3ec6f9d915bffc8221d67b610657b10a2d5363ca4c
fetched_at: '2026-06-28T22:38:29.899140+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Configuração correta do cadastro de TES para tratar  poder de terceiros
type: support-article
updated_at: '2021-08-06T19:59:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004201467-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Configura%C3%A7%C3%A3o-correta-do-cadastro-de-TES-para-tratar-poder-de-terceiros
---

**Ocorrência**

Qual a configuração do cadastro de TES para controle de poder De/Em terceiros?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) – A partir da versão 11.80.

**Solução**

Para que o sistema consiga gerar os controles de poder **De/Em terceiros**, primeiramente precisamos de **TES** (**MATA080**) devidamente configurados para tal.

Sendo assim, toda **Remessa** **geradora de Controle de/em Terceiro**s, independentemente de entrada ou saída, deve conter **"R" (remessa)** no campo **SF4->F4\_PODER3;**

E toda **Devolução de Remessa Geradora de Poder de/em Terceiros**, independentemente de entrada ou saída, deve conter **"D" (devolução)** no campo **SF4->F4\_PODER3**.

Para mais detalhes e exemplos de configuração, acesse: **[Cadastro de TES para Controle de Poder De/Em terceiros](https://tdn.totvs.com/x/eSswDg)**
