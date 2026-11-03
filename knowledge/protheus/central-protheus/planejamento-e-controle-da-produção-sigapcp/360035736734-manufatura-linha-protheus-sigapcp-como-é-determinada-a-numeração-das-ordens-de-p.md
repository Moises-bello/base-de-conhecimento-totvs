---
article_id: 360035736734
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a4dc781354a0acdf4a00cea61ede04b239eec59affc314bd39afb8bd89ff5fbb
fetched_at: '2026-06-28T22:42:41.082543+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Como é determinada a numeração das
  Ordens de Produção geradas pelo MRP  '
type: support-article
updated_at: '2024-05-09T12:10:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035736734-Manufatura-Linha-Protheus-SIGAPCP-Como-%C3%A9-determinada-a-numera%C3%A7%C3%A3o-das-Ordens-de-Produ%C3%A7%C3%A3o-geradas-pelo-MRP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:25 min**  
**Dúvida**Como é determinada a numeração das **OP** **-** **Ordem de Produção**pais e **OPs** intermediárias geradas pelo **MRP** -**Material Requiriments Planning**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**No **MRP - MATA712**, o parâmetro **Geracao de OPs Prod. Interme?** determina como as **OPs** intermediárias serão geradas.  
Se o conteúdo selecionado for **Por OP**, para cada **OP** pai serão geradas suas correspondentes **OPs** intermediárias, em quantidade de acordo com a necessidade da **OP** pai e configurações de **lote econômico** e **mínimo**, seguindo a mesma numeração da **OP** pai, da mesma forma que ocorre na abertura manual das **OPs** através da rotina **MATA650 - Ordem de Produção.**Se o conteúdo selecionado for **Por** **Necessidade**, as **OPs** serão geradas de acordo com a necessidade de cada período, neste caso não haverá vínculo entre as **OPs** pai e intermediárias através dos números das **OPs.**No **MRP Memória - PCPA712**, o parâmetro que determina como as **OPs** **Intermediárias** serão geradas, é o parâmetro **Aglutina Ordem de Produção**. Se o conteúdo desse parâmetro for **Aglutina**, irá aglutinar todas as **OPs** por **produto + período**, neste caso não haverá vínculo entre as **OPs** pai e intermediárias através dos números das **OPs**.  
Se o conteúdo selecionado for **Não Aglutina**, as **OPs** intermediárias seguem a mesma numeração da **OP** pai.
