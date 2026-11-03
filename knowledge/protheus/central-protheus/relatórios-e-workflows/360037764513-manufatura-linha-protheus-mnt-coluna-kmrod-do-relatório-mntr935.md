---
article_id: 360037764513
category: Relatórios e Workflows
content_hash: 46faadee9772bd60a71a82af44a4e45dc06091879bb3f4ee102be91663a6822b
fetched_at: '2026-06-28T22:42:31.604290+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: 'Manufatura - Linha Protheus - MNT - Coluna KmRod do relatório MNTR935 '
type: support-article
updated_at: '2021-06-17T19:05:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037764513-Manufatura-Linha-Protheus-MNT-Coluna-KmRod-do-relat%C3%B3rio-MNTR935
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**O que é a coluna **KmRod** do relatório **MNTR935 - Indicadores de Rendimento Combust.?**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios e Workflows - Todas as versões  
  
**Solução**A coluna **KmRod**  representa o quanto foi rodado no período.   
O cálculo é realizado da seguinte forma:  
**X = (PCF - PCI) - KMO.**Sendo:  
**PCF:** Posição final do contador - acumulado.  
**PCI:** Posição inicial do contador - acumulado.  
**KMO:** Quilometragem de outro combustível.  
  
Exemplo:  
01/01/15 -> Abast 100 litros Diesel 100 /100  
10/01/15 -> Abast 100 litros Etanol 1100/1100  
20/01/15 -> Reporte 2100/2100  
Tiramos um relatório pelo combustível Diesel  
X = (PCF - PCI) - KMO\*  
X = (2100 - 100) - 1000  
X = 2000-1000  
X = 1000 Km  
  
**Importante**  
Para os cálculos são usadas as tabela **STP - Ordens Serviço Acompanhamento** e **TQN - Entrada Manual de Abastecimento**.
