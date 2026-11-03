---
article_id: 1500007708682
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 0f73a0dc83747e213f13576cf23e05c86c3ead503a081ad03f080668e1c01791
fetched_at: '2026-06-28T22:42:44.727100+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Parâmetro MV_LOTVENC no cálculo do
  MRP
type: support-article
updated_at: '2022-11-01T15:29:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007708682-Manufatura-Linha-Protheus-SIGAPCP-Par%C3%A2metro-MV-LOTVENC-no-c%C3%A1lculo-do-MRP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:30 min  
  
Dúvida**Qual a funcionalidade do parâmetro **MV\_LOTVENC - Indica se devem ser utilizados Lotes/Sub-Lotes com a data de validade vencida** no cálculo do **MRP - Manufacturing Resource Planning**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Quando há **lote** de produtos vencidos dentro do período do **MRP,** o Sistema verifica o conteúdo parâmetro **MV\_LOTVENC**. Se o parâmetro está igual a **S** o Sistema considera os lotes vencidos para o cálculo do **MRP.**
