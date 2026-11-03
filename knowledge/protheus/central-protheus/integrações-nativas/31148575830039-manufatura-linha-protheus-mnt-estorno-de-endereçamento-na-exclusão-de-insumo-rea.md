---
article_id: 31148575830039
category: Integrações Nativas
content_hash: 782c7a68326b5c8bc92dae5369f03e6d909d1e7ba2a55f3165908b9e334d90b4
fetched_at: '2026-06-28T22:42:35.378456+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Estorno de endereçamento na exclusão de
  insumo realizado
type: support-article
updated_at: '2025-04-04T11:26:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31148575830039-Manufatura-Linha-Protheus-MNT-Estorno-de-endere%C3%A7amento-na-exclus%C3%A3o-de-insumo-realizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31148575806231) Tempo aproximado para leitura: **00:00:00 min** **Dúvida**Quais os tratamentos o que Sistema pode realizar ao devolver um produto com controle de endereçamento ao estoque, na exclusão de um **Insumo realizado**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Depende do conteúdo do parâmetro **MV\_PDEVLOC - Define se quando ocorrer um estorno de movimento com controle de localizacao**:

* **0 - Redistribuir**: O **produto** volta ao estoque para redistribuição, sendo necessário realizar um novo endereçamento;
* **1 - Localização Original**: O produto retorna ao **Endereço** que estava antes, dessa forma não é necessário realizar um novo endereçamento.
