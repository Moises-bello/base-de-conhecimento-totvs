---
article_id: 18697344859415
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6a1dfe9a3072de8da0db69e9e657ef31663f95c8100d7d7948f6059d9c94008d
fetched_at: '2026-06-28T22:42:40.842001+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apresentação dos dados no MRP memória
type: support-article
updated_at: '2023-10-31T17:49:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18697344859415-Manufatura-Linha-Protheus-SIGAPCP-Apresenta%C3%A7%C3%A3o-dos-dados-no-MRP-mem%C3%B3ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18697317985559) Tempo aproximado para leitura: **00:00:46 min** **Dúvida**Por que a rotina **PCPA144 - Geração de Documentos MRP** ou a rotina **RESULTADOM - Resultado do MRP** não apresenta as colunas referentes a todos os períodos calculados pelo **PCPA712 - MRP Memória**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Diferentemente do **MATA710 - MRP** ou **MATA712 - MRP**, que apresenta todos os períodos calculados, mesmo que o produto não tenha movimentos nesses períodos, as rotinas **PCPA144** e **RESULTADOM** apresentam somente os períodos nos quais o produto tem movimento, isso é, entradas, saídas ou saídas por estrutura.
