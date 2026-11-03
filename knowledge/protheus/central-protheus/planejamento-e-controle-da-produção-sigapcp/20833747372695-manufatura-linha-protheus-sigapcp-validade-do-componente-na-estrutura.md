---
article_id: 20833747372695
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 27fe89fddb84d1499fb13d3036edf243d3691544dba9ae1b7e788d91731099e0
fetched_at: '2026-06-28T22:42:47.122998+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Validade do componente na estrutura
type: support-article
updated_at: '2024-01-24T20:30:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20833747372695-Manufatura-Linha-Protheus-SIGAPCP-Validade-do-componente-na-estrutura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20833747351831) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Como os campos **G1\_INI - Data Inicial da Validade** e **G1\_FIM  - Data Final da Validade** são considerados para determinar se um componente será empenhado ou não?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O Sistema avalia se o conteúdo do campo **C2\_DATPRI - Data prevista de início** da **Ordem de Produção - OP** está no intervalo especificado nos campo **G1\_INI** e **G1\_FIM**. Se estiver neste intervalo, por essa regra o item é empenhado mas, se estiver fora desse intervalo não é empenhado.
