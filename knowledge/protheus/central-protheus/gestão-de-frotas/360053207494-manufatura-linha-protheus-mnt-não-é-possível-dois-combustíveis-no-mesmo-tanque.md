---
article_id: 360053207494
category: Gestão de Frotas
content_hash: ccd7a66bdf39569f389e7202e3d559da50aec283a7905f082d4060e5130f6928
fetched_at: '2026-06-28T22:42:39.541296+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Não é possível dois combustíveis no mesmo
  tanque
type: support-article
updated_at: '2021-08-13T18:22:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053207494-Manufatura-Linha-Protheus-MNT-N%C3%A3o-%C3%A9-poss%C3%ADvel-dois-combust%C3%ADveis-no-mesmo-tanque
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Por que não é possível utilizar dois combustíveis no mesmo tanque?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - A partir da versão 12  
  
**Solução**Eram realizadas inserções de diversos combustíveis para um mesmo tanque na rotina de **Posto Interno** - **MNTA615**.   
  
A forma de armazenamento de dois combustíveis, fisicamente, não é possível dentro de apenas um tanque. Pensando em um tanque onde se guarda combustível, não seria possível, fisicamente, separar a **gasolina** de **álcool**, por exemplo.  
  
Em relatórios ou consultas, por exemplo, a busca feita por **Posto/Tanque/Bomba** ficaria incorreta com mais de um tanque com diferentes combustíveis. Não seria possível dividir os dados de mesmo tanque porém com combustíveis diferentes e por conta disto foi realizado um ajuste em **Setembro de 2019** na **ISSUE DNG-7976** com intuito de não mais permitir que esta situação se repetisse em ambiente padrão para se evitar inconsistências de base como integridade dos registros de **armazém/estoque**.
