---
article_id: 360050889413
category: Relatórios e Workflows
content_hash: 59e3e0a942f19c8ac22cdfda9653431abcfcb29e39d697fdb6b6d25a2abdcb28
fetched_at: '2026-06-28T22:42:31.597787+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Cálculo do indicador MTTR
type: support-article
updated_at: '2021-06-17T19:03:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050889413-Manufatura-Linha-Protheus-MNT-C%C3%A1lculo-do-indicador-MTTR
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:02:30 min.**  
**Dúvida**Como funciona e como é realizado o cálculo do indicador **MTTR - M****ean Time To Repair**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios e Workflows - Todas as versões  
  
**Solução**O indicador **MTTR - Mean****Time To Repair**apresenta o tempo médio para reparo, sendo que para este somente são consideradas as **ordens de serviço** finalizadas e do tipo **corretiva**. O valor resultante deste indicador equivale ao tempo médio de duração de reparo de um equipamento.  
  
Para a realização do cálculo é utilizada a fórmula de padrão mundial do **MTTR**, sendo esta:  
  
**Fórmula do MTTR:** **TR** / **NI**

* **Tempo de Reparo - TR:** O tempo total de reparo trata-se do tempo em que o equipamento ficou parado devido as **ordens de serviço** do tipo **corretiva** abertas para o mesmo. Para os cenários onde a **ordem de serviço** encerra fora do período consultado, será contabilizado apenas parte da duração do reparo, ou seja, o tempo contido dentro do período consultado.  
    
  Ressaltar que para esta variável da fórmula somente são consideradas as **O.S.** **finalizadas** e do tipo **corretiva**, levando em consideração o período consultado pelo indicador.  As mesma considerações valem para as **O.S. de histórico - STS**. Outro ponto são os campos considerados para definição do período de manutenção, que leva é definido a partir do parâmetro **considera tempo de**.   
  Neste que possui três opções que são apresentadas abaixo:

| Tipo | Nome | Detalhes | Campos Considerados |
| --- | --- | --- | --- |
| **1** | Tempo de Parada | O tempo compreendido entre a parada do equipamento até retornar à operação. | **TJ\_DTPRINI, TJ\_HOPRINI, TJ\_DTPRFIM, TJ\_HOPRFIM, TS\_DTPRINI, TS\_HOPRINI, TS\_DTPRFIM, TS\_HOPRFIM** |
| **2** | Tempo de Execução da Manutenção | O tempo compreendido entre o inicio da execução da manutenção até seu fim. | **TJ\_DTMRINI, TJ\_HOMRINI, TJ\_DTMRFIM, TJ\_HOMRFIM, TS\_DTMRINI, TS\_HOMRINI, TS\_DTMRFIM, TS\_HOMRFIM** |
| **3** | Ambos | Prevalesse o tempo de parada, caso não haja, considera-se o tempo de execução da manutenção. | Todos anteriores. |

* **Número de Intervenções - NI:** Quantidade de **O.S.** do tipo **corretiva** e **finalizadas** para o equipamento durante o período. Mesmo que a **O.S. - Ordem de Serviço** seja realizada em um período fora do calendário do equipamento. Para a variável de **número de falhas** ela será contabilizada, visto que independentemente se o equipamento afetou sua produção em relação a seu calendário, existiu uma falha no mesmo.

**Exemplo:****O.S. 1 = 1 Hora         - 14/04 17:00 às 14/04 18:00   
O.S. 2 = 1 Hora         - 20/04 13:00 às 20/04 14:00  
O.S. 3 = 33:58 Horas - 29/04 14:00 às 30/04 23:59****MTTR => ( 1 + 1 + 33,966666 ) / 3 = 11,98888 = 12 horas**
