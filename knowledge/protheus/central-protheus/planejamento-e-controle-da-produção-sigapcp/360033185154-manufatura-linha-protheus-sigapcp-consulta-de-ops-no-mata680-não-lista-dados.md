---
article_id: 360033185154
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5ccd56b24471fa056381d13346723bb225f8ef5a2171779b51ca14550a309fe3
fetched_at: '2026-06-28T22:42:42.127775+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Consulta de OPs no MATA680 não lista
  dados
type: support-article
updated_at: '2022-02-03T14:33:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033185154-Manufatura-Linha-Protheus-SIGAPCP-Consulta-de-OPs-no-MATA680-n%C3%A3o-lista-dados
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Por que ao consultar as **OPs - Ordens de Produção** a serem apontadas no **MATA680 - Apontamento Mod I** não são listados dados, diferentemente a rotina **MATA681 - Apontamento Mod II**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Na rotina **MATA680** a consulta das **OPs** lista somente as **OPs** alocadas através do **MATA690 - Carga Máquina**, enquanto a rotina **MATA681** lista todas as **OPs** cadastradas.  
Portanto, para apontar as **OPs** através do **MATA680** é necessário primeiramente realizar as alocações através do **MATA690**, somente assim elas serão listadas e será possível realizar o apontamento.
