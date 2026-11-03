---
article_id: 1500012952982
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 67feaccb8798d577150612742319401771a564560312f073c03817e2a5534c4c
fetched_at: '2026-06-28T22:42:43.300036+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Funcionalidade do parâmetro Aglutina
  Ordem de Produção no PCPA712
type: support-article
updated_at: '2021-06-07T10:48:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012952982-Manufatura-Linha-Protheus-SIGAPCP-Funcionalidade-do-par%C3%A2metro-Aglutina-Ordem-de-Produ%C3%A7%C3%A3o-no-PCPA712
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**Como funciona o parâmetro **Aglutina Ordem de Produção** no **PCPA712 - MRP Material Requiriment Planning Memória**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O parâmetro **Aglutina Ordem de Produção** possui três alternativas sendo elas: **Aglutina Somente Demandas**, **Aglutina** e **Não Aglutina**.  
Quando o conteúdo do parâmetro é **Aglutina Somente Demandas**, todas as demandas registradas no **PCPA136 - Demandas do MRP** para esse mesmo produto e período serão aglutinadas e será gerada uma **OP - Ordem de Produção** para atender toda a sua demanda, já as demais necessidades terão **OPs - Ordens de Produção** geradas em separado, como por exemplo a **OP** de quantidade necessária para atender ponto de pedido.  
Quando este parâmetro possui o **Aglutina**, será gerada uma única **OP** para atender toda a necessidade do período, independente da sua origem, se uma demanda registrada no **PCPA136** ou ponto de pedido, por exemplo.  
E quando o parâmetro possui o valor **Não Aglutina**, serão geradas diversas **OPs**, cada uma para atender a uma necessidade.
