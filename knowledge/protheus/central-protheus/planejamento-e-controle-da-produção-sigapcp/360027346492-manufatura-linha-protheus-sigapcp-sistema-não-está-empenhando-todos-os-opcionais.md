---
article_id: 360027346492
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4a1370f9e0e4ff55a9137e0531d5c053ff6ad29bf29789ec3b92ca3cd9968bf8
fetched_at: '2026-06-28T22:42:47.024875+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Sistema não está empenhando todos
  os opcionais '
type: support-article
updated_at: '2021-05-27T10:53:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027346492-Manufatura-Linha-Protheus-SIGAPCP-Sistema-n%C3%A3o-est%C3%A1-empenhando-todos-os-opcionais
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**O que deve ser feito quando o Sistema não empenha todos os **opcionais**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Devido a quantidade, os dados referentes a todos os **opcionais** não são gravados no campo **C2\_OPC - Opcional OP**da rotina **MATA650 - Ordem de produção.**Para esses casos aconselhamos utilizar o campo **C2\_MOPC - M. Opcional** da rotina **MATA650**. Para isso, mude o valor do parâmetro**MV\_REPGOPC - Indica se deverá solicitar os opcionais em todos  os níveis da estrutura** para **S.**O campo**C2\_MOPC**é um campo do tipo *memo*,e permite o registro de um número ilimitado de **opcionais**.
