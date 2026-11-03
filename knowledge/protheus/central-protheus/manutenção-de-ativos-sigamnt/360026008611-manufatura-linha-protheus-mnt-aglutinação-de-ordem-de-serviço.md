---
article_id: 360026008611
category: Manutenção de Ativos (SIGAMNT)
content_hash: 3dd58c311d8c767d0f7f9fddd2ff84ccb988de068e4d441565f322ca492e07f1
fetched_at: '2026-06-28T22:42:32.713693+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Aglutinação de Ordem de Serviço
type: support-article
updated_at: '2024-09-16T11:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026008611-Manufatura-Linha-Protheus-MNT-Aglutina%C3%A7%C3%A3o-de-Ordem-de-Servi%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26395735153687)*** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como funciona a **Aglutinação de OS - Ordem de Serviço**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**O principal objetivo da **Aglutinação de OS** é a redução de custos com horas de máquina parada, insumos - mão de obra, produto, ferramenta, terceiros; e prover maior a disponibilidade do equipamento.  
  
São utilizadas em:  
**Aglutinação de O.S** - **MNTA365**  
**Aglutinação via geração de O.S. automática**.  
  
A aglutinação funciona da seguinte maneira: O Sistema une as **O.S's** fazendo com que a resultante tenha suas tarefas, etapas e insumos e as da **O.S. aglutinada**, caso já não possua.  
  
**Exemplo**O bem CAM001 possui neste momento a posição de contador 100 quilômetros e o contador acumulado 100 quilômetros.  
  
**Manutenções do Bem**  
O contador da última manutenção era 1 quilômetro

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome da manut.** | **Substit.** | **Incremento** | **Insumo** | **Quant.** | **Tarefa** |
| Manut. 120km |  | 120 quilômetros | Produto 12 | 2 | Tarefa 12 |
| Manut. 140km | 1 | 140 quilômetros | Produto 14 | 4 | Tarefa 14 |
| Manut. 160km | 1, 2 | 160 quilômetros | produto 16 | 6 | Tarefa 16 |

**Reporte de Contador**Foi informado um novo contador de 150 quilômetros posterior ao primeiro.  
Resultado: **Geração de uma Ordem de Serviço** e cancelamento da anterior que sofreu aglutinação.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Número da OS** | **Insumo** | **Tarefa** | **Quantidade** | **Contador** |
| 000002 | Produto 12 | Tarefa 12 | 2 | 150 quilômetros |
| 000002 | Produto 14 | Tarefa 14 | 4 | 150 quilômetros |

**Reporte de Contador**Foi informado um novo contador de 170 quilômetros posterior ao primeiro.Resultado: **Geração de uma Ordem de Serviço** e cancelamento da anterior que sofreu aglutinação.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Número da OS** | **Insumo** | **Tarefa** | **Quantidade** | **Contador** |
| 000003 | Produto 12 | Tarefa 12 | 2 | 170 quilômetros |
| 000003 | Produto 14 | Tarefa 14 | 4 | 170 quilômetros |
| 000003 | Produto 16 | Tarefa 16 | 6 | 170 quilômetros |

**Importante**Não são consideradas as **Dependências - STM** da **O.S.** aglutinada.  
Só podem ser aglutinadas **O.S** do mesmo **bem**, **serviço** e que sejam **preventivas**.
