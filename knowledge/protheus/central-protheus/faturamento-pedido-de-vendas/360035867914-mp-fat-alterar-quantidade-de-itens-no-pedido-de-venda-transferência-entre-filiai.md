---
article_id: 360035867914
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: bd8ab17118ff34ee02cd615c3f9c2414582fac1eaf3d8b1d98f95ce6d516c79a
fetched_at: '2026-06-28T22:38:41.214356+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Alterar quantidade de itens no Pedido de Venda Transferência entre
  filiais - MV_QTITENS
type: support-article
updated_at: '2021-04-28T15:50:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035867914-MP-FAT-Alterar-quantidade-de-itens-no-Pedido-de-Venda-Transfer%C3%AAncia-entre-filiais-MV-QTITENS
---

**Ocorrência**

Alterar quantidade de itens no Pedido de Venda Transferência entre filiais - MV\_QTITENS  
  
**Ambiente**

Microsiga Protheus – **Até a versão 11.**  
**Solução**

O parâmetro **MV\_QTITENS** era utilizado somente para o processo de transferência entre filiais na rotina Central de Compras.

A rotina **MATA177**, que utilizava o parâmetro foi descontinuada. A rotina atual não utiliza o parâmetro em questão.

Observação: Caso seja imprescindível a verificação dos Itens do Pedido de Venda, utilizar o ponto de entrada "**MTA410T**" - **[Ponto de Entrada MTA410T](https://tdn.totvs.com/display/public/PROT/MTA410T)**
