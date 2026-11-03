---
article_id: 360039677433
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7f6297ffe0cc0924b57b7e8ba20f04cc2dd6ad97d26851744e8fb1671418680a
fetched_at: '2026-06-28T22:38:41.247137+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Pedido de Vendas permite incluir duas vezes o produto com o mesmo
  número de série (C6_NUMSERI)
type: support-article
updated_at: '2021-04-28T15:50:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039677433-MP-FAT-Pedido-de-Vendas-permite-incluir-duas-vezes-o-produto-com-o-mesmo-n%C3%BAmero-de-s%C3%A9rie-C6-NUMSERI
---

**Dúvida**  
Pedido de Vendas permite incluir duas vezes o produto com o mesmo número de série (**C6\_NUMSERI**).  
  
**Ambiente**Microsiga Protheus -  todas as versões.

**Solução**

O bloqueio ocorrerá somente na liberação do Pedido Vendas(**MATA440**) e não na inclusão.   
  
Isto porque não haverá saldo físico do produto para usar duas vezes o mesmo número de série, gerando assim bloqueio de estoque
