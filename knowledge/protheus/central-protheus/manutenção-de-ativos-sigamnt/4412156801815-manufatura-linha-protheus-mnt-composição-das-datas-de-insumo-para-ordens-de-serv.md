---
article_id: 4412156801815
category: Manutenção de Ativos (SIGAMNT)
content_hash: 736aa52c585c15fc78db36eae2e77d9cb1ca03a1cdc72b257a359202a20fa3b6
fetched_at: '2026-06-28T22:42:32.965320+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Composição das datas de Insumo para Ordens
  de Serviço Corretiva
type: support-article
updated_at: '2021-11-03T17:02:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412156801815-Manufatura-Linha-Protheus-MNT-Composi%C3%A7%C3%A3o-das-datas-de-Insumo-para-Ordens-de-Servi%C3%A7o-Corretiva
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:30 min****Dúvida**Qual é o conceito da composição das **Datas** e **Horas** de **Início** e **Fim** em uma **Ordem de Serviço Corretiva - O.S**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Basicamente em um insumo é possível controlar sua **Data** e **Hora** **início** e **Data** e **Hora fim**. Porém existem conceitos diferentes para as **O.S's** **Preventivas** e **Corretivas**.  
Ao incluir uma **O.S. corretiva** é informada uma data para esta **O.S**, podendo no ato de inclusão informar insumos. No reporte de insumos os campos data e hora não são apresentados, pois os mesmos assumem a data referente a **O.S** e o horário conforme a hora atual da inclusão da **O.S**.  
   
**Exemplo**Considerando uma ordem de serviço corretiva informando um insumo. Note o comportamento de **previsão** de realização destes insumos:

| Data no ato da inclusão | Hora no ato da inclusão | Data da OS - TJ\_DTORIGI | Utiliza Calendário - TL\_USACALE | Quantidade - TL\_QUANTID | Data Início - TL\_DTINICI | Hora Início - TL\_HOINICI | Data Fim  - TL\_DTFIM | Hora Fim  - TL\_HOFIM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12/11/2021 | 14:00 | 12/11/2021 | Não | 1h | 12/11/2021 | 14:00 | 12/11/2021 | 15:00 |
| 12/11/2021 | 14:00 | 13/11/2021 | Não | 2h | 13/11/2021 | 14:00 | 13/11/2021 | 16:00 |
| 12/11/2021 | 14:00 | 12/11/2021 | Sim | 1h | Preenchido pelo Usuário | Preenchido pelo Usuário | Preenchido pelo Usuário | Preenchido pelo Usuário |

Conforme o exemplo, as **Datas de início** sempre acompanham o campo **Data da OS - TJ\_DTORIGI**e o **Horário** acompanha o horário do ato de inclusão. Quando o insumo **Utiliza Calendário** o preenchimento das datas e horários fica a cargo do usuário.
