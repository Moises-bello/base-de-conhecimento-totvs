---
article_id: 4405064250391
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 638c7a8cfcba36c72e1686cf49f38595b972f3b431cc729b16e9963cdbdcd661
fetched_at: '2026-06-28T22:42:44.535953+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem PERBQTD
type: support-article
updated_at: '2021-07-27T13:09:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405064250391-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-PERBQTD
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:56 min****Ocorrência**Ao realizar o apontamento de perda através da rotina **MATA685 - Apontar Perda** é apresentado o **Help PERBQTD**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A mensagem é apresentada quando a quantidade apontada para o produto da perda excede o consumo previsto para a **OP - Ordem de Produção**.  
  
**Solução**Para que a mensagem não seja apresentada ao realizar uma apontamento com quantidade maior que a previsto para a **OP** é necessário que o parâmetro **MV\_PERBQTD - Bloqueia apontamentos de perda com quantidade superior ao consumo previsto para a ordem de produção?** e/ou **MV\_PERDINF - Identifica se a quantidade de perda informada nos apontamentos de produção será tratada de forma informativa** estejam desativados.
