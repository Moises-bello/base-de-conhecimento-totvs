---
article_id: 360029162691
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8d56656de0f449f42595a600d12fa892847b4d61f81de9ae03f626d729f1b4b3
fetched_at: '2026-06-28T22:42:48.112471+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Saldo de e em terceiros no cálculo do MRP
type: support-article
updated_at: '2020-06-24T13:38:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029162691-MP-SIGAPCP-Saldo-de-e-em-terceiros-no-c%C3%A1lculo-do-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min****Dúvida**Como o **MRP - Manufacturing Resources Planning** considera o saldo do produto **De e Em Terceiros**?  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**A rotina leva em consideração o conteúdo do parâmetro **Qtd. Terc. em nosso Poder?** para subtrair ou não do saldo inicial a quantidade de terceiros, e o conteúdo do parâmetro **Qtd. nossa Poder. Terc.?** para somar ou não a quantidade que se encontra em terceiros. Ambos os parâmetros estão disponíveis nas rotinas **MATA712 - MRP** e **PCPA107 - MRP** por meio da opção **Parâmetros**.
