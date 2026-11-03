---
article_id: 4412157028631
category: Manutenção de Ativos (SIGAMNT)
content_hash: 5e4e182987179493fb325c31f883538b22614644b89dfd082cee256dd4ed6d6c
fetched_at: '2026-06-28T22:42:32.973014+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Composição das datas de Insumo para Ordens
  de Serviço Preventivas
type: support-article
updated_at: '2021-11-12T14:11:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412157028631-Manufatura-Linha-Protheus-MNT-Composi%C3%A7%C3%A3o-das-datas-de-Insumo-para-Ordens-de-Servi%C3%A7o-Preventivas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:45 min****Dúvida**Qual é o conceito da composição das **Datas** e **Horas** de início e fim em uma **O.S. - Ordem de Serviço** do tipo **Preventiva**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Ao incluir uma **O.S.** **Preventiva** é informado uma data, podendo no ato de inclusão informar insumos. No reporte de insumos os campos **Data** e **Hora** não são apresentados, pois os mesmos assumem a data referente a **O.S** e o horário conforme a hora atual da inclusão da **O.S**. nos casos que esta data coincide com a **Data da OS - TJ\_DTORIGI**. Nos casos que a **Data da OS - TJ\_DTORIGI** é distinta da data do ato de inclusão o horário se adequa conforme o primeiro disponível conforme o calendário do dia.  
  
**Exemplo**Considerando uma manutenção preventiva com calendário de segunda a sexta das 08:00 as 18:00. Incluir uma **O.S. Preventiva** informando um insumo. Note o comportamento de **previsão** de realização destes insumos:

| Data no ato da inclusão | Hora no ato da inclusão | Data da OS -  TJ\_DTORIGI | Quantidade - TL\_QUANTID | Data Inicio - TL\_DTINICI | Hora Inicio - TL\_HOINICI | Data Fim - TL\_DTFIM | Hora Fim - TL\_HOFIM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12/11/2021 | 14:00 | 12/11/2021 | 1h | 12/11/2021 | 14:00 | 12/11/2021 | 15:00 |
| 12/11/2021 | 14:00 | 13/11/2021 | 2h | 13/11/2021 | 08:00 | 13/11/2021 | 10:00 |

Conforme o exemplo, quando a data de inclusão da **O.S.** coincide com a **Data da OS - TJ\_DTORIGI**, o insumo é gerado com a mesma data e com o horário de inclusão da **O.S.** Para os casos que a data de inclusão da **O.S.** for anterior a **Data da OS - TJ\_DTORIGI**. O insumo é gerado com a data da **O.S.** e alocando a hora com a primeira disponível em consideração ao calendário da manutenção utilizada. Vale ressaltar que para uma **O.S** **Preventiva**, os insumos reportados e suas receptivas datas e horários devem respeitar o calendário pré-estabelecido em sua manutenção.
