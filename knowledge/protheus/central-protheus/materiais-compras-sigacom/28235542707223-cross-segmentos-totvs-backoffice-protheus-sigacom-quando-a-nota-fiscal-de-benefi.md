---
article_id: 28235542707223
category: Materiais - Compras (SIGACOM)
content_hash: ed0b162158716b073f7c97bde5bd0aaadf1c3adca7aeab6315853dd8eb66d3c2
fetched_at: '2026-06-28T22:41:24.329579+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Quando a nota fiscal
  de Beneficiamento é retornada, os campos D2_VALDEV e D2_QTDEDEV não são preenchidos
type: support-article
updated_at: '2024-12-03T13:10:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28235542707223-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Quando-a-nota-fiscal-de-Beneficiamento-%C3%A9-retornada-os-campos-D2-VALDEV-e-D2-QTDEDEV-n%C3%A3o-s%C3%A3o-preenchidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28235558134167) Tempo aproximado para leitura: **00:02:00 min****Dúvida**

Ao retornar nota fiscal de beneficiamento os campos D2\_VALDEV e D2\_QTDEDEV  não são preenchidos  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - VERSÃO 12

**Solução**

Quando a nota fiscal for do tipo B (Beneficiamento), o sistema permite o lançamento de notas de entrada desse tipo apenas quando há controle de poder de terceiros. Por padrão, os campos D2\_VALDEV e D2\_QTDEDEV não são preenchidos, mesmo após o retorno, pois, o poder de terceiros movimenta a tabela SB6, e não a SD2.

Ao realizar o retorno, o campo F2\_FLAGDEV será preenchido conforme descrito na documentação.

[SIGACOM - Campo F2\_FLAGDEV Devolução de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413919149079-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Campo-F2-FLAGDEV-Devolu%C3%A7%C3%A3o-de-Vendas)

**Saiba mais em :**

[SIGACOM - Retorno de beneficiamento com vínculo de pedido de compra](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4683680372503-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Retorno-de-beneficiamento-com-v%C3%ADnculo-de-pedido-de-compra)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
