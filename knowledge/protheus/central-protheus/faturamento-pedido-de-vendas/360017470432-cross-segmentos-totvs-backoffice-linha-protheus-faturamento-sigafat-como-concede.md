---
article_id: 360017470432
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 26ce59a1cb749d1a85074aeb0dee8d78f9295e19aecb31fd2208dbe9997acd6f
fetched_at: '2026-06-28T22:38:38.337334+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: ' Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Como conceder descontos no Pedido de Venda'
type: support-article
updated_at: '2024-04-02T12:38:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017470432--Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Como-conceder-descontos-no-Pedido-de-Venda
---

**Dúvida**

Como funciona a aplicação de descontos nos Pedidos de Venda?  
  
**Ambiente**

 Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - a partir da versão 12.  
  
**Solução**

Veja o vídeo How To sobre esse processo: [**How To | MP - SIGAFAT - Descontos no processo de venda**](https://youtu.be/JwG34Vyv3qQ)

O desconto no Pedido de Venda é aplicado sempre sobre o Preço de Lista (**C6\_PRUNIT**) para se obter o Valor Unitário já com desconto (**C6\_PRCVEN**). Quando não há Preço de lista, é aplicado diretamente no Valor unitário recalculando-o para comportar o desconto.

Esta é uma característica estrutural do Protheus para devidos cálculos fiscais e não é opcional. O desconto sempre irá refletir no Valor unitário. Porém, na **DANFE** irá exibir separadamente. Valor Unitário / Desconto / Valor Total.

Uma exceção dessa regra é o Desconto Financeiro (**C5\_DESCFI**  |  **E4\_DESCFIN**) pois, neste caso, o desconto não é levado para a Nota. É concedido apenas na baixa do título.

***OBS:** O título gerado de uma nota que contém a informação de desconto financeiro, seja pela condição de pagamento ou pelo pedido, será gerado com o valor cheio e apresentará a informação do desconto no campo **E1\_DESCFIN**.*

**Saiba Mais:**

**[Descontos no Pedido de Venda](https://tdn.totvs.com/x/KE1tDQ)**
