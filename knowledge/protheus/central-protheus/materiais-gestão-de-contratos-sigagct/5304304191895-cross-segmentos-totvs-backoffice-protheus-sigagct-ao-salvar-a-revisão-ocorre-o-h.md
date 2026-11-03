---
article_id: 5304304191895
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 2227587cd5f1c19a986c5abc2df6e5a55d1fc623e500ac662d5f695c020905a0
fetched_at: '2026-06-28T22:37:21.366631+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao salvar a Revisão  ocorre
  o Help CNTA100VIG
type: support-article
updated_at: '2025-04-17T11:57:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5304304191895-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-salvar-a-Revis%C3%A3o-ocorre-o-Help-CNTA100VIG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Ao salvar a Revisão ocorre o Help CNTA100VIG  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Gestão de Contratos - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a data do campo Dt. prev medição (CNF\_PRUMED) do Cronograma financeiro do contrato  está maior que a Data final do Contrato (CN9\_DTFIM).

**Solução**Verificar se o calculo da Data final do contrato (CN9\_DTFIM) está correto de acordo com o campo Data inicio(CN9\_DTINIC) + o campo Vigência (CN9\_VIGE) do cabeçalho do Contrato. Caso esteja correto será necessário realizar uma Revisão para adicionar um prazo maior no contrato para que o campo Data final do Contrato (CN9\_DTFIM) seja maior que o campo Dt. prev medição (CNF\_PRUMED).

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais são os tipos de Revisão disponíveis, para revisar contratos no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-s%C3%A3o-os-tipos-de-Revis%C3%A3o-dispon%C3%ADveis-para-revisar-contratos-no-Gest%C3%A3o-de-Contratos-?source=search)

[MP - SIGAGCT - Como aumentar ou reduzir os meses e redistribuição das parcelas de um contrato na Revisão de Aditivo ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028039532-MP-SIGAGCT-Como-aumentar-ou-reduzir-os-meses-e-redistribui%C3%A7%C3%A3o-das-parcelas-de-um-contrato-na-Revis%C3%A3o-de-Aditivo-?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Revisão de Renovação de Contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659713-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Revis%C3%A3o-de-Renova%C3%A7%C3%A3o-de-Contrato?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
