---
article_id: 24316478087447
category: Gestão de Armazenagem (WMS)
content_hash: 3094d1aed4790ff3200160b7506ae3e3011e2a24b1b9ce8869ce4526ff2a0d0a
fetched_at: '2026-06-28T22:45:47.957025+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Distribuição - Linha Protheus - WMS - Produto não aparece no WMSA535
type: support-article
updated_at: '2024-06-24T18:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24316478087447-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-Produto-n%C3%A3o-aparece-no-WMSA535
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24316478074391) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que o produto não aparece no **WMSA535** - **Troca de Validade do Lote?**  
  
**Ambiente**TOTVS Distribuição - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Todas as versões  
  
**Solução**Para que o produto seja apresentado no **WMSA535**, o Sistema valida o parâmetro **MV\_ARQPROD - O parâmetro configura se os dados de indicadores de produto serão considerados pela tabela "SB1" ou se serão considerados pela da tabela "SBZ"**, na sequencia valida no produto o controle de enedereçamento, **B1\_LOCALIZ**, e o controle de endereçamento **WMS**, **B5\_CTRWMS**.  
Caso o produto não controle localização e não controle **WMS**, ele não será apresentado no **WMSA535**.
