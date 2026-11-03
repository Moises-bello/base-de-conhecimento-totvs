---
article_id: 25811592205591
category: Relatórios e Workflows
content_hash: 860db9afdaa789c14112e44bab22ef0cbc442516a643f0d6cd904d3b476bb858
fetched_at: '2026-06-28T22:42:31.578896+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Cálculo do indicador MTBF
type: support-article
updated_at: '2024-08-21T19:03:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25811592205591-Manufatura-Linha-Protheus-MNT-C%C3%A1lculo-do-indicador-MTBF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25811592183191) Tempo aproximado para leitura:**00:01:30 min** **Dúvida**Como é realizado o cálculo do indicador **MTBF - Mean Time Between Failure**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios e Workflows - Todas as versões  
  
**Solução**O **MTBF - Tempo Médio Entre Falhas** é um índice utilizado para equipamentos reparados após a ocorrências de uma falha em **Ordem de Serviço Corretiva**. Corresponde a relação entre o produto do **NOIT - Número de equipamentos** e os seus **HROP - Tempos de Operação Produtivos**, e o **NTMC - Número de Ordem de Serviço Corretiva** identificadas nesses mesmos equipamentos, em período determinado. O índice serve para determinar a média dos tempos de funcionamento de cada equipamento reparável entre uma falha e outra, ou seja, entre uma manutenção corretiva e a manutenção corretiva seguinte nesse mesmo equipamento.  
  
**Fórmula:**  
**MBTF = (NOIT x HROP) / (∑ NTMC)**  
**NOIT** - Número total de equipamentos;  
**HROP** - Tempos de operação dos equipamentos em bom funcionamento - Desconsiderando horas paradas tempo total da ordem de serviço;  
**NTMC** - Número total de ordem de serviço corretiva identificadas nos equipamentos.  
  
**Funções:**  
**NOIT.HROP = MNTV001;**  
**NTMC = MNTV002  
  
Exemplo:**  
Equipamento: Máquina de solda.  
Tempo de operação: 24 horas por dia - Apenas em dias úteis.  
Tempo total de operação no mês: 528 horas.  
Ordem de serviço 01: Dia 13 com 1 hora de parada do equipamento.  
Ordem de serviço 02: Dia 20 com 1 hora de parada do equipamento.  
Período avaliado pelo indicador: Do dia 01 até o dia 30.  
Valor apresentado no indicador: 263 horas.
