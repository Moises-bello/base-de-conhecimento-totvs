---
article_id: 360025543272
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 63556bab8ab3eb58e6290326567e4c7dc048e96a694409ab388ade0b459bce8b
fetched_at: '2026-06-28T22:42:40.715455+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - A OP intermediária não tem a mesma
  quantidade do empenho
type: support-article
updated_at: '2025-07-09T11:45:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025543272-Manufatura-Linha-Protheus-SIGAPCP-A-OP-intermedi%C3%A1ria-n%C3%A3o-tem-a-mesma-quantidade-do-empenho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min****Dúvida**Por que o Sistema está gerando **OP - Ordem de Produção** intermediária e a quantidade é menor da quantidade do empenho?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Isso ocorre quando o parâmetro **MV\_CONSEST - Considera estoque na geração de Ordem de produção** está com o valor igual a **S**, desse modo o Sistema verifica a disponibilidade de estoque e abre a **OP** intermediária somente com o saldo faltante para atender a necessidade.  
  
**Por exemplo:**   
Se a necessidade for de 10 unidades, mas o estoque tiver 8 unidades disponíveis, a **OP** intermediária será de 2 unidades.
