---
article_id: 360040937334
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 223173bdbe13f94569ffbc051b5fc1f68c21a59406df938a33012c4daa7b16cf
fetched_at: '2026-06-28T22:38:38.498891+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como vincular
  um Pedido de Venda com uma Ordem de Produção
type: support-article
updated_at: '2024-03-07T18:08:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040937334-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-vincular-um-Pedido-de-Venda-com-uma-Ordem-de-Produ%C3%A7%C3%A3o
---

**Dúvida**

Como vincular um pedido de vendas com uma Ordem de Produção?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

É possível realizar o vínculo de duas formas:

**1. Vincular ordem de produção ao pedido pela rotina MATA650 (Ordens de Produção)**

Este processo é utilizado quando um produto precisa ser produzido para atender a demanda de venda gerada pelo pedido. Disponibilizamos uma vídeo sobre a realização desse processo: **[How To | MP -SIGAFAT - Gerar Ordem de Produção vinculada ao Pedido de Venda](https://youtu.be/SYm3NERaFf0)**

**2.** **Vincular ordem de produção ao pedido pelo botão** **“BENEFICIA”**

Este processo é utilizado quando uma empresa necessita enviar um material, para um fornecedor, para que este sofra algum processo de Transformação/Produção.

Na **inclusão** do pedido de vendas, quando atendidos os **requisitos** abaixo:

* O tipo do Pedido (**C5\_TIPO**) é **B-Utiliza Fornecedor**;
* O produto do pedido possui o campo “Tipo” (**B1\_TIPO**) configurado como **BN-Beneficiamento**;
* O TES possui movimento de estoque (**F4\_ESTOQUE = S-Sim**) e Controla Poder de Terceiros (**F4\_PODER3 = R-Remessa**);
* O parâmetro **MV\_EMPBN** deve estar configurado como **.T.**

**3. Gerar ordem de produção de um produto que já possua saldo.****Para gerar uma ordem de produção de um produto que já possui saldo, é necessário ajustar o parâmetro MV\_CONSEST e deixá-lo como "N". Dessa forma, uma ordem de produção será gerada para o pedido de venda.   
  
Saiba Mais: [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Estorno de Endereçamento na Exclusão do Documento de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019869032-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Estorno-de-Endere%C3%A7amento-na-Exclus%C3%A3o-do-Documento-de-Sa%C3%ADda)** **Saiba Mais**: **[FAT0293 Ordem de Produção x Pedido de Vendas](https://tdn.totvs.com/x/YW52Hw)**
