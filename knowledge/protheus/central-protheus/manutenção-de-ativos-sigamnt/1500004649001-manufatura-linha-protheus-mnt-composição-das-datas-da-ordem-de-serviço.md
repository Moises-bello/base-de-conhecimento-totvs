---
article_id: 1500004649001
category: Manutenção de Ativos (SIGAMNT)
content_hash: ed626ca21da6df7d0c25a82a80c720a60050d3761fba1b48b1ac59563fd6fc9e
fetched_at: '2026-06-28T22:42:32.956377+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Composição das datas da ordem de serviço
type: support-article
updated_at: '2025-05-26T17:49:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004649001-Manufatura-Linha-Protheus-MNT-Composi%C3%A7%C3%A3o-das-datas-da-ordem-de-servi%C3%A7o
---

**![relogio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21054904364951)**Tempo aproximado para leitura: **00:04:40**  
**Dúvida**Qual o conceito da composição das datas de uma **O.S. - Ordem de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Basicamente em uma **O.S.** é possível controlar o **tempo de parada previsto e realizado** do equipamento,**tempo de execução previsto e realizado**da manutenção e a **data em que deveria ocorrer a manutenção**chamada de **Data Original**.  
Os campos que correspondem a essas datas são:  
  
**1) Data Original - TJ\_DTORIGI**: é a data em que deveria ocorrer a manutenção com base na data da última ocorrência, ou seja, da última **O.S.** executada. São considerados dias contínuos, desprezando qualquer feriado, exceções de calendário ou dias não uteis.  
**Exemplo**   
Considerando uma manutenção preventiva com periodicidade de 1 mês e sendo executada pela última vez em 10/02/2021.

| Projeção da Manutenção | 10/03 | 10/04 | 10/05 | 10/06 |
| --- | --- | --- | --- | --- |
| Dias da Semana | Sexta-feira | Segunda-Feira | Quarta-Feira | Sábado |

Seguindo no exemplo acima, podemos afirmar que as datas apresentadas correspondem a **Data original** da **O.S.**, ou seja, datas em que deveria ocorrer a manutenção.  
Supondo que no dia **10/06** seja um **dia não útil**, teremos a atuação do Sistema mudando a data prevista inicio, podendo antecipar ou adiar conforme cadastro da manutenção no campo **Dia não útil - TF\_NAOUTIL**.**2) Tempo de Parada Previsto do Equipamento**: Corresponde ao tempo previsto e necessário de parada do equipamento para início da manutenção até o retorno do mesmo em operação.  
Ao gerar a **O.S.** o Sistema verifica no cadastro na **Manutenção - STF** se existe a necessidade de **Parada do equipamento - TF\_PARADA**. Caso sim, verifica o período de parada que antecede e/ou seja posterior ao tempo previsto de execução da manutenção.  
  
**Exemplo**  
Em uma caldeira, para que seja realizado a manutenção preventiva com previsão de execução de 2 horas, será necessário o seu desligamento com antecedência, bem como após o término da manutenção o equipamento necessita de um tempo para aquecimento até retornar a operação normal.  
Seguindo o exemplo acima, supondo que o tempo previsto para a execução da manutenção corresponde ao período das 8h ás 10h de um determinado dia e necessita de 1h para resfriar e 2h para o seu aquecimento. O Sistema automaticamente gravará como tempo de parada prevista das 7h ás 12h.  
  
Campos relacionados:   
**Data prevista inicial - TJ\_DTPPINI**  
**Hora prevista inicial - TJ\_HOPPINI**  
**Data prevista final - TJ\_DTPPFIM**  
**Hora prevista final - TJ\_HOPPFIM**.  
  
**3) Tempo de Parada Real do Equipamento**:Corresponde ao tempo em que o equipamento realmente ficou parado, ou seja, desde o início da execução da manutenção ou falha até o retorno para sua atividade produtiva ou operacional. Com base nesta informação o Sistema poderá apresentar o prejuízo com lucro cessante.  
  
Dependendo da configuração é possível que impacte nos indicadores de **Disponibilidade**, **MTBF -** **Tempo Médio Entre Falhas** e **MTTR - Tempo Médio Para Reparo**. Esta informação da parada do equipamento poderá ser informada manualmente ao realizar a finalização da **O.S.**  
Campos relacionados:   
**Data parada real inicial - TJ\_DTPRINI****Hora parada real inicial - TJ\_HOPRINI****Data parada real final - TJ\_DTPRFIM****Hora parada real final - TJ\_HOPRFIM****4) Tempo Previsto para Execução da Manutenção**: Corresponde ao tempo previsto em que o equipamento ficará em manutenção, ou seja, é o tempo compreendido entre a menor data e hora até a maior data e hora dos **Insumos previstos** **- STL** na **O.S.**

| Tempo Previsto para Execução da Manutenção | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Tipo de Insumo** | **Quantidade** | **TJ\_DTMPINI** | **TJ\_HOMPINI** | **TJ\_DTMPFIM** | **TJ\_HOMPFIM** |
| Mão de Obra | 4H | 10/02/2021 | 08:00 | 10/02/2021 | 12:00 |
| Ferramenta | 1H | 10/02/2021 | 08:00 | 10/02/2021 | 09:00 |
| Terceiro | 2H | 10/02/2021 | 13:00 | 10/02/2021 | 15:00 |

No exemplo acima podemos concluir que o tempo previsto para execução da manutenção corresponde a **10/02/2021 as 08:00 até 10/02/2021 as 15:00**.

Campos relacionados:   
**Data Prevista Manutenção Inicial -** **TJ\_DTMPINI****Hora Prevista Manutenção Inicial -** **TJ\_HOMPINI****Data Prevista Manutenção Final -** **TJ\_DTMPFIM****Hora Prevista Manutenção Final - TJ\_HOMPFIM****5) Tempo Real para Execução da Manutenção**: Corresponde ao tempo real em que o equipamento ficou em manutenção, ou seja, é o tempo compreendido entre a menor data e hora até a maior data e hora dos **Insumos realizados** **- STL** na **O.S.**

Com base nesta informação o Sistema calculará os indicadores de **Disponibilidade**, **MTBF** e **MTTR**.

| Tempo Real para Execução da Manutenção | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Tipo de Insumo** | **Quantidade** | **TJ\_DTMRINI** | **TJ\_HOMRINI** | **TJ\_DTMRFIM** | **TJ\_HOMRFIM** |
| Mão de Obra | 4H | 10/02/2021 | 08:00 | 10/02/2021 | 12:00 |
| Ferramenta | 1H | 10/02/2021 | 08:00 | 10/02/2021 | 09:00 |
| Terceiro | 2H | 10/02/2021 | 13:00 | 10/02/2021 | 15:00 |

No exemplo acima podemos concluir que o tempo real para execução da manutenção corresponde a **10/02/2021 as 08:00 até 10/02/2021 as 15:00**.

Campos relacionados:   
**Data real inicial - TJ\_DTMRINI****Hora real inicial - TJ\_HOMRINI****Data real final - TJ\_DTMRFIM****Hora real final - TJ\_HOMRFIM**
