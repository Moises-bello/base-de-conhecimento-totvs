---
article_id: 29660159758871
category: Materiais - Compras (SIGACOM)
content_hash: 8bb3fd700faf9ce9bae77557253a89ccd32ba583fc7ec5e8cff8c6b4e784a129
fetched_at: '2026-06-28T22:41:17.381699+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada
  com quantidade maior ao vinculado do PC.
type: support-article
updated_at: '2025-01-31T18:07:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29660159758871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-com-quantidade-maior-ao-vinculado-do-PC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29660144029975) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Documento de Entrada com quantidade maior ao vinculado do PC.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus compras - Todas as versões

**Solução**

Qual o comportamento que o sistema adota para a atualização do campo quantidade entregue (C7\_QUJE), quando lançado Nota Fiscal de Entrada com vínculo de Pedido de Compras com quantidade da NF (D1\_QUANT) maior que a quantidade (C7\_QUANT) informada no pedido de compra.

Por padrão a rotina de documento de entrada (MATA103) com recebimento de quantidade à mais do que a vinculada no pedido de Compra terá o comportamento conforme o exemplo abaixo :

Exemplo:  
1) Pedido de Compras de **10** unidades em aberto **(C7\_QUANT=10).**  
2) Documento de entrada **(NF)** com quantidade **15 (D1\_QUANT=15).**  
3) Quando a NF entrar vai baixar o pedido que foi realizado com a quantidade solicitada**(D1\_QUANT)**, atualizando a quantidade entregue **(C7\_QUJE)** conforme a quantidade **(C7\_QUANT)** do pedido , ou seja, **C7\_QUJE =10** e não haverá vinculo com o pedido do volume a mais, porém vai atualizar o saldo do produto de acordo com a quantidade entregue **(D1\_QUANT).**

*****Saiba Mais :*****

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
