---
article_id: 13316189225751
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8878df9a48ea9bd8a95572c3d8f2e7e98e15a1a39d54660f49ca0904ce8d8fd9
fetched_at: '2026-06-28T22:38:42.644268+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Alterar/salvar
  pedido de venda sem perder a liberação
type: support-article
updated_at: '2023-03-23T20:39:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13316189225751-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Alterar-salvar-pedido-de-venda-sem-perder-a-libera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Quais as formas de alterar o pedido de venda e ainda assim não perder a liberação?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

1 - Vá na rotina Liberação de Pedidos de Venda (MATA440).

2 - Altere para abrir a janela do pedido de venda.

Campos que podem ser alterado sem perder a liberação:

* Campos de despesas acessórias: C5\_FRETE  |  C5\_SEGURO  |  C5\_DESPESA  |  C5\_FRETAUT
* Campos de transporte/transportadoras: C5\_TRANSP  |  C5\_REDESP
* Campos de peso e medida: C5\_PESOL  |  C5\_PBRUT
* Campos de volume e espécie: C5\_VOLUME1/2/3/4  |  C5\_ESPECI1/2/3/4

3 - Altere os campos desejados que estiverem na lista acima e salve a tela.

**OBSERVAÇÃO 1:** Fique atento ao campo **"Qtd.Liberada (C6\_QTDLIB)"** antes de salvar. Dependendo de como o pedido estava anteriormente, pode ser que seja liberado parcialmente ou total, deixando o pedido com legenda "verde" ou "amarela" (parcial ou totalmente liberado), possivelmente diferente de antes.

**OBSERVAÇÃO 2:** Ao liberar qualquer campo pela rotina pedido de venda (MATA410) irá desfazer a liberação, o processo acima tem de ser feito na rotina de Liberação de Pedidos de Venda (MATA440).

**Saiba Mais  
TDN: [FAT0242 Liberação / Bloqueio do Pedido de Vendas](https://tdn.totvs.com/x/RjS4Ew)**
