---
article_id: 23152217798295
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8b13fdcb91f4bedc9f9cfd412bc9c442389709391546d10e12b2440a8353845b
fetched_at: '2026-06-28T22:42:47.007909+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Sequência das OPs intermediárias geradas
  pelo MRP
type: support-article
updated_at: '2024-04-30T13:47:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23152217798295-Manufatura-Linha-Protheus-SIGAPCP-Sequ%C3%AAncia-das-OPs-intermedi%C3%A1rias-geradas-pelo-MRP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23152217793303) Tempo aproximado para leitura: **00:00:48 min** **Dúvida**As **OPIs - Ordens de Produção Intermediárias** geradas pelo **PCPA712 - MRP Memória** tem a mesma sequência das **OPIs** geradas pelo **MATA650 - Cadastro de Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Não, a sequência das **OPIs** geradas pelo **PCPA712** pode ser diferente das sequências das **OPIs** **geradas** pelo **MATA650**, isso porque o critério de ordenação dos registros e as tabelas avaliadas diferem entre os processos.  
O mesmo pode ocorrer se gerar os documentos pela rotina **RESULTADOM - Resultado MRP** ou **PCPA144 - Geração de documentos MRP**
