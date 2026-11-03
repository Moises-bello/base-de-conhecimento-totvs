---
article_id: 360027229434
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 012261aaf3aaed6bc0981205386a15985cac4193c96b0f589de13fbc8f4e8fc4
fetched_at: '2026-06-28T22:42:47.100140+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Utilidade campo C2_PRIOR '
type: support-article
updated_at: '2021-11-03T13:11:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027229434-Manufatura-Linha-Protheus-SIGAPCP-Utilidade-campo-C2-PRIOR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:40 min****Dúvida**Para que serve o campo **C2\_PRIOR - Prioridade** no **MATA650 - Ordem de Produção**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
É por meio desse campo que o Sistema considera a sequência que executará as **OPs - Ordens de Produção** no **MATA690 - Carga Máquina**. Se nada for informado, o Sistema considera a Ordem de Produção que está sendo cadastrada como prioridade 500. As prioridades vão de 001 a 999, sendo que o Sistema dá maior prioridade aos números mais baixos, assim uma **OP** com prioridade 300 será executada antes de um **OP** com prioridade 400.
