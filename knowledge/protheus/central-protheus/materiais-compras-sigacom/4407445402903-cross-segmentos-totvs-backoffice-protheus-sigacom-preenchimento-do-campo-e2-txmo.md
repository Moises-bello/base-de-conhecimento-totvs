---
article_id: 4407445402903
category: Materiais - Compras (SIGACOM)
content_hash: bb1557f645ac71d5c0b7d397d62e0dd0a322ed9565690a07f6eadd007504dc21
fetched_at: '2026-06-28T22:41:24.049944+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Preenchimento do campo
  E2_TXMOEDA com data diferente do dia da inclusão do documento de entrada.
type: support-article
updated_at: '2022-05-16T22:34:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407445402903-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Preenchimento-do-campo-E2-TXMOEDA-com-data-diferente-do-dia-da-inclus%C3%A3o-do-documento-de-entrada
---

**Ocorrência**Ao lançar um documento de entrada cuja a data da emissão da nota seja igual a data da taxa cadastrada na rotina MATA090 após a confirmação da nota na gravação do título do financeiro o campo E2\_TXMOEDA não é preenchido.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões.  
  
**Solução**Quando se tem no cadastro de moeda uma taxa por dia, o campo E2\_TXMOEDA não será gravado. Será considerado o preenchimento desse campo de acordo com a taxa da data da baixa do título.  
Ao colocar a taxa na aba duplicatas do documento de entrada o sistema vai priorizar o que foi informado no documento e ignorar o cadastro da moeda (SM2).  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407446394519/mceclip1.png)

**Observações:**

Quando não há cadastro de taxa de moeda para o dia e ao fazer o documento de entrada seja informado manualmente a taxa, o campo E2\_TXMOEDA fica preenchido com a informação.  
  
O campo E2\_TXMOEDA somente será preenchido quando houver uma taxa prévia acordada que é colocada no documento de entrada pois entende-se que efetivando a entrada do documento fiscal a taxa foi negociada e está firmando a compra.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
