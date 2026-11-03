---
article_id: 360019749211
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5623a44c86d6d6f9eebe4f45b2f7f8a158889c57ef38d93cffba3a649e8fe49b
fetched_at: '2026-06-28T22:38:41.244994+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Pedido de Vendas está com Bloqueio de Crédito ou de Estoque, porém,
  na rotina de Pedido de Vendas demonstra Status Liberado (legenda verde)
type: support-article
updated_at: '2021-04-28T15:51:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019749211-MP-FAT-Pedido-de-Vendas-est%C3%A1-com-Bloqueio-de-Cr%C3%A9dito-ou-de-Estoque-por%C3%A9m-na-rotina-de-Pedido-de-Vendas-demonstra-Status-Liberado-legenda-verde
---

**Ocorrência**

Pedido de Vendas está com Bloqueio de Crédito ou de Estoque, porém, na rotina do Pedido de Vendas demonstra Status Liberado (legenda verde).  
  
**Ambiente**

Microsiga Protheus– a partir da versão 12.

**Solução**

Na rotina **MATA410** - Pedidos de Venda não há legenda que indique status de bloqueio de Crédito e Bloqueio de Estoque.

Como se pode verificar em:

* Ações relacionadas;
* Legenda.

Essa Rotina indica bloqueios apenas de:

![image2018-4-23_11-27-15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015295052/image2018-4-23_11-27-15.png)

**Pontos de Entrada que possibilitam tratar as Legendas na MATA410**:

MA410LEG - <http://tdn.totvs.com/display/public/PROT/MA410LEG+-+Alterar+textos+da+legenda+de+status+do+pedido>

MA450COR - <http://tdn.totvs.com/display/public/PROT/MA450COR+-+Alterar+textos+da+legenda+de+status+do+pedido>

**Saiba Mais:  
[Legendas exibidas na rotina MATA410 - Pedido de Vendas](http://tdn.totvs.com/display/public/PROT/FAT0121_Legendas_Status_do_Pedido_de_Vendas)**
