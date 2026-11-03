---
article_id: 360052556953
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: da04882ba4629477ec2f4e87411859c8d5470bdf83874b11ffd4328b436c7019
fetched_at: '2026-06-28T22:42:42.272548+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro array out of bounds ( 0 of 23
  ) on PERDALINOK(SIGACUSA.PRX)
type: support-article
updated_at: '2022-07-01T14:35:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052556953-Manufatura-Linha-Protheus-SIGAPCP-Erro-array-out-of-bounds-0-of-23-on-PERDALINOK-SIGACUSA-PRX
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:00:45 min****Ocorrência**No módulo do **PCP - Planejamento e Controle da Produção**, ao tentar realizar o apontamento de perda através da rotina **MATA685 - Apontamento de Perda** apresenta o erro **array out of bounds ( 0 of 23 ) on PERDALINOK(SIGACUSA.PRX)**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Os campos **BC\_NUMLOTE - Sub-Lote**, **BC\_LOTECTL - Lote**, **BC\_LOCALIZ - Endereço** e **BC\_NUMSERI - Num. de Serie** não estão na tela para o usuário.  
  
**Solução**Ajustar os campos  **BC\_NUMLOTE**, **BC\_LOTECTL**, **BC\_LOCALIZ** e **BC\_NUMSERI** no **SIGACFG - Configurador** para que elessejam apresentados na tela do usuário.
