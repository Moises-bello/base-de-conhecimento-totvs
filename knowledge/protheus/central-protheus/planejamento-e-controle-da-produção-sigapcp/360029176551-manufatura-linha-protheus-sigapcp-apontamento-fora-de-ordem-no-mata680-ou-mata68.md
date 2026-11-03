---
article_id: 360029176551
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 071fbc098d135f3ff49d6ac9096aea39c0bfca75cbddfb9347e8a4909c12fc78
fetched_at: '2026-06-28T22:42:40.820630+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apontamento fora de ordem no MATA680
  ou MATA681
type: support-article
updated_at: '2024-05-09T17:22:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029176551-Manufatura-Linha-Protheus-SIGAPCP-Apontamento-fora-de-ordem-no-MATA680-ou-MATA681
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:35 min****Dúvida**É possível apontar as operações fora de ordem por meio da rotina **MATA680 - Produção PCP Mod1** ou **MATA681- Produção PCP Mod2**?  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para que as operações possam ser apontadas de forma aleatória, altere o parâmetro **Verif. Sld Oper Anterior?** do **F12** do **MATA680/MATA681** para **Não Verifica**. Esse parâmetro é indicado quando a ordem de execução das operações pode ser diferente do roteiro de operações.
