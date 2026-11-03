---
article_id: 4418868690455
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d92483ebb93921619c57d562d324b4f02a64f7735931ea8be9257c9f008dfc09
fetched_at: '2026-06-28T22:42:45.817708+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quantidade Rejeitada pelo CQ no MRP
type: support-article
updated_at: '2022-01-13T10:37:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418868690455-Manufatura-Linha-Protheus-SIGAPCP-Quantidade-Rejeitada-pelo-CQ-no-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Como o **MRP - Material Requiriment Planning** identifica a quantidade rejeitada pelo **CQ - Controle de Qualidade**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando o parâmetro **Estoque Rejeitado pelo CQ** possui o conteúdo **1 - Subtrai**, o **MRP** faz a busca na tabela **SD7 - Movimentações de CQ** por todas as rejeições do produto - **D7\_TIPO - Tipo de Movimento** com conteúdo **2** -, e procura dessas rejeições aquelas que não foram devolvidas ao fornecedor através da emissão de nota fiscal de devolução. A diferença entre a quantidade rejeita e a quantidade devolvida é a quantidade que será subtraída do estoque no cálculo do **MRP**.
