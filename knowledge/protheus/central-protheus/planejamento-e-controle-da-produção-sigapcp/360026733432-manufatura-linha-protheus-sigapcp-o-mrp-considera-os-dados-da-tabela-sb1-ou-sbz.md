---
article_id: 360026733432
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e87c729789ecafe84820cff15ec768f33c34bf93640f6c1ec8179da4c8958c3f
fetched_at: '2026-06-28T22:42:44.636770+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - O MRP considera os dados da tabela
  SB1  ou SBZ para o cálculo das necessidades
type: support-article
updated_at: '2021-07-30T11:54:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026733432-Manufatura-Linha-Protheus-SIGAPCP-O-MRP-considera-os-dados-da-tabela-SB1-ou-SBZ-para-o-c%C3%A1lculo-das-necessidades
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:50 min****Dúvida**O **MRP - Material Requiriments Planning** considera as informações da tabela **SB1 - Cadastro de Produtos** ou **SBZ - Indicadores de Produtos** para o cálculo das necessidades?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O **MRP** considera o conteúdo do parâmetro **MV\_ARQPROD - O parâmetro configura se os dados de indicadores de produtos serão considerados pela tabela SB1 ou se serão considerados pela da tabela SBZ**, para determinar a leitura da tabela **SB1** ou **SBZ**, se o conteúdo desse parâmetro for **SBZ** e existe registro correspondente ao produto na tabela **SBZ** o **MRP** utiliza as informações desta tabela, caso contrário utiliza as informações da tabela **SB1**.
