---
article_id: 4412149839895
category: Manutenção de Ativos (SIGAMNT)
content_hash: 7dea485d8027694a29854581bd466799d2120f80eea081cea8265d9b9d60e6be
fetched_at: '2026-06-28T22:42:32.874322+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Cálculo do Relatório MNTR360
type: support-article
updated_at: '2021-11-03T12:34:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412149839895-Manufatura-Linha-Protheus-MNT-C%C3%A1lculo-do-Relat%C3%B3rio-MNTR360
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:40 min****Dúvida**Como é realizado o cálculo do relatório **Análise MTNF/MTTR - MNTR360**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Para explicação do cálculo do relatório, será exemplificado utilizando um **Bem** com duas **O.S. - Ordens de serviço**, conforme dados abaixo.  
  
Período configurado de: 01/01/2021 até: 31/01/2021   
**Utiliza calendário** igual a **S - Sim**Calendário **24 horas** todos os dias

| Data da O.S | Hora Início | Hora Fim |
| --- | --- | --- |
| 11/01/2021 | 12:49 | 13:10 |
| 29/01/2021 | 09:30 | 09:50 |

| Chave | Valor | Definição | Observações |
| --- | --- | --- | --- |
| **A** | 2 | Quantidade de ordens de serviço no período |  |
| **B** | 252,82 | Quantidade de horas entre o início do período até o início da primeira ordem, quando configurado para considerar período anterior a primeira **O.S** | Do dia 01/01/2021 das 00:00 ao dia 11/01/2021 as 12:49 |
| **C** | 428,33 | Quantidade de horas desde o horário de término da ordem anterior | Do dia 11/01/2021 das 13:10 ao dia 29/01/2021 as 09:30 |
| **D** | 0 | Caso houver mais ordens segue a mesma regra do item anterior |  |
| **E** | 62,15 | Quantidade de horas entre fim da última ordem até o fim do período | Do dia 29/01 as 09:50 ao dia 31/01 as |
| **F** | 743,30 | Total de horas entre as ordens | **B + C + D + E** |
| **G** | 371,65 | Total entre as ordens / Quantidade de ordens no período | **F / A** |
| **H** | 0,21 | Total de horas realizadas |  |
| **I** | 371:39 | **MTBF -** **Mean Time Between Failures**, em português **Tempo médio entre falhas** | Média convertida para horas |
| **J** | 15,49 | **MTBF** Dias | Média convertida pra dias |
| **K** | 00:21 | **MTTR -** **Mean Time to Repair**, em português **Tempo Médio para Reparo** | Média de execução convertido para horas |
| **L** | 0,01 | **MTTR** Dias | Média de execução convertido para dias |
