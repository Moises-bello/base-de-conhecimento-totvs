---
article_id: 360035244374
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4b3b2f1390a881ce15aa56b79f89dc59fec29459313016460b305d27b8294668
fetched_at: '2026-06-28T22:38:33.131704+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - Mensagem de Bloqueio ao tentar preparar doc de saída na rotina Pedido
  de venda ( MATA410 )
type: support-article
updated_at: '2021-04-28T15:54:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035244374-MP-FAT-Mensagem-de-Bloqueio-ao-tentar-preparar-doc-de-sa%C3%ADda-na-rotina-Pedido-de-venda-MATA410
---

**Ocorrência**  
 No módulo **Faturamento**, ao tentar faturar um **Pedido de Venda ( MATA410 )** pela opção P**reparar Doc. de Saída**, o sistema **apresenta** a mensagem:

**" Os itens abaixo encontram-se bloqueados, caso continue os mesmos serão desprezados "**

**Ambiente**  
Protheus – **Faturamento** – A partir da versão 11.80

**Causa**   
 Esse incidente ocorre, pelo fato dos itens **encontrarem-se bloqueados por crédito e/ou estoque**.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Antes de realizar a **preparação do doc de saída**, será preciso realizar a **liberação** do itens, através da rotina **MATA456- liberação de crédito e estoque**;

2. **Somente após a liberação** será possível prosseguir com o **faturamento**.
