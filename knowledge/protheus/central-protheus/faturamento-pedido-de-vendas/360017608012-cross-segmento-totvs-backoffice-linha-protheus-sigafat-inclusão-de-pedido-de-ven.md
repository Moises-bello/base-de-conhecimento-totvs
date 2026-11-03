---
article_id: 360017608012
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d2cccc039ba60fe733999557c4ac205d9ea6294941370576768444966e1363f9
fetched_at: '2026-06-28T22:38:38.545114+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Inclusão de
  Pedido de Vendas do Tipo Complemento de Preço
type: support-article
updated_at: '2022-12-08T14:59:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017608012-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Inclus%C3%A3o-de-Pedido-de-Vendas-do-Tipo-Complemento-de-Pre%C3%A7o
---

**Dúvida**

Inclusão de Pedido de Vendas do Tipo Complemento de Preço.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Veja nosso vídeo How To sobre o tema: [How To | MP - SIGAFAT - Complemento de Preço/Quantidade](https://youtu.be/cBr9Jf93TGI)

Para incluir um Pedido de Venda do tipo Complemento de Preço, siga estes procedimentos:

**1.** Inclua um novo pedido com o campo **"Tipo Pedido (C5\_TIPO)"** = **"C - Compl. Preco/Quantidade"**;

**2.** No campo **"Tipo Compl. (C5\_TPCOMPL)"** informe **"1-Preço"**;

**3.** No campo **"Produto (C6\_PRODUTO)"** informe o produto utilizado na **NF original**;

**4.** Nos campos **"Prc Unitario (C6\_PRCVEN)"** e **"Vlr. Total (C6\_VALOR)"** informe o valor do **Complemento de Preço**;

**5.** Informe um **TES** (Tipo de Entrada e Saída) **tributando** como na NF original;

**6.** Localize a **NF** **original** por meio do campo **"N.F. Original (C6\_NFORI)"**, no campo tecle **<ENTER>** e depois **[F4]** para localizar a nota;

**Observações:**

Não é preenchida quantidade para este complemento.

1-) Para emissão de Pedido de Venda do Tipo "C" (Complemento) informando conteúdo no campo de quantidade (**C6\_QTDVEN**) é necessário informar o ***tipo de complemento "1- Preço"***  no campo **"Tipo Compl." (C5\_TPCOMPL / F1\_TPCOMPL).**

2-) Condição de pagamento com adiantamento (campo E4\_CTRDAT = Sim ) não é utilizado para Pedido de Venda com Tipo = C - Compl.Preço/Quantidade. O Adiamentamento é utilizado apenas para Pedido de Vena Tipo = N- Normal.

**Saiba mais**: [FAT0112 - Complemento de Preço / Quantidade](https://tdn.totvs.com/x/ghGWDg)
