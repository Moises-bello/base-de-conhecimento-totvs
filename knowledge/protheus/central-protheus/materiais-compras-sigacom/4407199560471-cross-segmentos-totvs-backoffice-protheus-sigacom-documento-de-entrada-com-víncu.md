---
article_id: 4407199560471
category: Materiais - Compras (SIGACOM)
content_hash: 742132ade8f2678234c1674f25465a888b35a2bca7951b9b53cff4023c182b45
fetched_at: '2026-06-28T22:41:17.384666+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada
  com vínculo de Pedido de Compra com Valor de Frete
type: support-article
updated_at: '2022-11-29T10:46:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407199560471-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-com-v%C3%ADnculo-de-Pedido-de-Compra-com-Valor-de-Frete
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Qual o comportamento que o sistema possui, quando lança Nota Fiscal de Entrada com vínculo de Pedido de Compras com valor de frete informado (**C7\_FRETE**), e este Pedido não é atendido em sua totalidade ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Todas as versões  
  
**Solução**

Ao efetuar lançamento de Documento de Entrada com vínculo de Pedido de Compras, onde no momento não será atendido em sua totalidade, ou seja, o campo de quantidade (**D1\_QUANT**) é alterado, o valor de frete (**D1\_VALFRE**) é recalculado em sua proporção.

Isso acontece para que em um segundo momento, quando foi feito o lançamento de notas fiscais que atendem o saldo remanescente do pedido de compras, o valor de frete seja apresentado com base na quantidade que ainda resta para para o Pedido.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
