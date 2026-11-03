---
article_id: 4407647052695
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9cb6c0c7c0ec1af2f3352a467679bc3fdc6f2b29828b4ce816e31d000bdd0736
fetched_at: '2026-06-28T22:42:45.695933+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo  D4_OPORIG
type: support-article
updated_at: '2021-09-02T16:44:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407647052695-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-D4-OPORIG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min** **Dúvida**Quando e com que informação é preenchido o campo **D4\_OPORIG** na rotina **MATA381**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O campo **D4\_OPORIG** é preenchido com a **O****rdem de Produção** responsável pela produção do material empenhado, ou seja, quando é aberta uma **OP** intermediária automaticamente para o produto do empenho.  
  
O campo é composto por: **C2\_NUM+C2\_ITEM+C2\_SEQUEN**  
Se tiver **grade** é composto: **C2\_NUM+C2\_ITEM+C2\_SEQUEN+C2\_ITEMGRD**  
  
**Glossário**  
**D4\_OPORIG** - Ordem de produção Origem  
**OP** - Ordem de Produção **C2\_NUM** - Número da OP **C2\_ITEM** - Item **C2\_SEQUEN** - Sequencia **C2\_ITEMGRD** - Item Grade  
**MATA381** - Empenho Múltiplo
