---
article_id: 360025626093
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 07570aee57daacd200b80715091d56d137c130708ae951136141535fc9d0f218
fetched_at: '2026-06-28T22:42:47.003079+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Seleção dos opcionais na geração da
  ordem de produção por vendas
type: support-article
updated_at: '2021-05-27T11:16:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025626093-Manufatura-Linha-Protheus-SIGAPCP-Sele%C3%A7%C3%A3o-dos-opcionais-na-gera%C3%A7%C3%A3o-da-ordem-de-produ%C3%A7%C3%A3o-por-vendas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**É possível selecionar os opcionais da estrutura ao gerar a **OP - Ordem de Produção** por meio da rotina **MATA650 - Ordens de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**A seleção dos opcionais deve ser feita ao incluir o item no **pedido de venda**, no momento da geração da **OP** através do **MATA650** é considerada essa informação, que deve estar registrada no campo **C6\_OPC - Opcionais Utilizados p/ PV** ou **C6\_MOPC - Mesmo Opcional**, não sendo possível nova seleção.
