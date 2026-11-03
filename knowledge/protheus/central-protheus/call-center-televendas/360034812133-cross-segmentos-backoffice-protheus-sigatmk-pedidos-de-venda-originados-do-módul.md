---
article_id: 360034812133
category: Call Center - Televendas
content_hash: ea0ba14ce0a9e01fccc412f9ff6ad993fc9bf720e2201d4cd04040e66142d373
fetched_at: '2026-06-28T22:41:30.263746+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Pedidos de venda originados
  do módulo Call Center, não respeitam os parâmetros de liberação
type: support-article
updated_at: '2024-04-25T14:14:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034812133-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Pedidos-de-venda-originados-do-m%C3%B3dulo-Call-Center-n%C3%A3o-respeitam-os-par%C3%A2metros-de-libera%C3%A7%C3%A3o
---

**Dúvida**

Como parametrizar o módulo Call Center, para respeitar as mesmas regras de liberação do módulo Faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**

O Pedido do Televendas para o Pedido de Vendas, sempre será gerado como Aberto.  
Salvo se utilizar os pontos de Entrada abaixo para gravar como liberado:

* [TKGRPED - Gravação do Televendas](https://tdn.totvs.com/x/GZNn)
* [TMKVFIM - Pós-gravação do pedido de vendas](https://tdn.totvs.com/x/z5Jn)

**Saiba mais**: [Atendimentos Call Center (Televendas)](https://tdn.totvs.com/x/fHF2Jw)
