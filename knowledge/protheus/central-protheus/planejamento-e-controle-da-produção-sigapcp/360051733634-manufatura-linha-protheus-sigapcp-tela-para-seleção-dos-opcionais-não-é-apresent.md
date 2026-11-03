---
article_id: 360051733634
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8c8893d27d3366300a3c4b595a263406e1e681b3f8114e3722599f346cc34ae0
fetched_at: '2026-06-28T22:42:47.064886+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Tela para seleção dos opcionais não
  é apresentada na geração da ordem de produção
type: support-article
updated_at: '2021-05-26T19:43:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051733634-Manufatura-Linha-Protheus-SIGAPCP-Tela-para-sele%C3%A7%C3%A3o-dos-opcionais-n%C3%A3o-%C3%A9-apresentada-na-gera%C3%A7%C3%A3o-da-ordem-de-produ%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:40 min****Dúvida**Por que a tela para seleção dos opcionais da estrutura, não é apresentada ao gerar a **OP - Ordem de Produção** por meio da rotina **MATA650 - Ordens de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Essa situação ocorre porque o parâmetro **MV\_SELEOPC** **- Indica se Sistema utiliza seleção de Opcionais na abertura de OPs, SCs, Prev. Vendas, Plano Mestre de Produção, etc** está igual a **N - Não**.
