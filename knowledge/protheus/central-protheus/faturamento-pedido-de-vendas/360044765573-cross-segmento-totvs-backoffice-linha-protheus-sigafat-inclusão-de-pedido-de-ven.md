---
article_id: 360044765573
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 39cce78f2adf8d381d9b0f6842450b4e2ff42a7e2c99c3cd67a017614b118ea7
fetched_at: '2026-06-28T22:38:38.548571+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Inclusão de
  Pedido de Vendas do Tipo Complemento de Quantidade
type: support-article
updated_at: '2022-12-09T12:09:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044765573-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Inclus%C3%A3o-de-Pedido-de-Vendas-do-Tipo-Complemento-de-Quantidade
---

**Dúvida**

Inclusão de Pedido de Vendas do Tipo Complemento de Quantidade.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Veja nosso vídeo How To sobre o tema: **[How To | MP - SIGAFAT - Complemento de Preço/Quantidade](https://youtu.be/cBr9Jf93TGI)**

Para incluir um Pedido de Venda do tipo Complemento de Quantidade, siga estes procedimentos:

**1.** Inclua um novo pedido com o campo **"Tipo Pedido (C5\_TIPO)"** = **"C - Compl. Preco/Quantidade"**;

**2.** No campo **"Tipo Compl. (C5\_TPCOMPL)"** informe **"2-Quantidade"**;

**3.** No campo **"Produto (C6\_PRODUTO)"** informe o produto utilizado na **NF original**;

**4.** Informe a **quantidade** e **valor** para complementar;

**5.** Informe um **TES** (Tipo de Entrada e Saída) **tributando** como na NF original;

**6.** Localize a **NF** **original** por meio do campo **"N.F. Original (C6\_NFORI)"**, no campo tecle **<ENTER>** e depois **[F4]** para localizar a nota;

**Saiba mais**: **[FAT0112 - Complemento de Preço / Quantidade](https://tdn.totvs.com/x/ghGWDg)**
