---
article_id: 360052077394
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5a71b968de8dd03971e17f2b0f013d90fc36854b7c0a69c8772f254d19c89875
fetched_at: '2026-06-28T22:42:44.614304+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Necessidade do MRP diferente de diário
type: support-article
updated_at: '2021-07-30T13:16:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052077394-Manufatura-Linha-Protheus-SIGAPCP-Necessidade-do-MRP-diferente-de-di%C3%A1rio
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Ao selecionar um período diferente de diário no **MRP - Manufacturing Resources Planning**, como a rotina considera as informações registradas como **previsão de venda** ou **plano mestre de produção** no cálculo da necessidade?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Se for selecionado um período de diferente de diário, o Sistema somará todas as necessidades identificadas dentro do período selecionado e atribuirá para a primeira data do período em questão.  
  
**Exemplo**  
**Previsões de venda** registradas para os dias 01, 07, 10, 15 e 20, se a rotina for parametrizada para uma periodicidade quinzenal, o Sistema somará no dia 01 as previsões dos dias 01, 07, 10 e no dia 15, as previsões dos dias 15 e 20.
