---
article_id: 12107362041495
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 1e26b5d4ac855abb23f1bf155d7fa246cec85d5bda6ccb7d3620c347860dfa0a
fetched_at: '2026-06-28T22:42:00.912929+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o campo 15 - Débitos Especiais  do E110 no Sped Fiscal?
type: support-article
updated_at: '2025-08-13T17:43:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12107362041495-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-15-D%C3%A9bitos-Especiais-do-E110-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar o campo **15 Débitos Especiais** do **E110 - Apuração do ICMS - Operações Próprias**  no **Sped Fiscal**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Existem duas formas de gerar o **campo 15** do **E110** com os valores a recolher do **DIFAL**:  
  
1. Manualmente, incluindo uma linha na aba **Débitos Especiais** da **Apuração do ICMS**, conforme processo abaixo:

Através da rotina **Apuração do ICMS - MATA953,** processe a apuração do período e na aba **Débitos Especiais** inclua uma nova linha:  
  
![](https://totvssuporte.zendesk.com/attachments/token/6VWNPN6adNz9RBlhHqSVWwUC5/?name=image.png)

Na linha deve ser informado o número da guia à que se refere o **DIFAL** e  **código de ajuste** à que se refere à operação. 

![](https://totvssuporte.zendesk.com/attachments/token/bpzIMZ06NgCnvUNmOKhWYhebc/?name=image.png)  
  
OU   
  
2. Automaticamente, amarrando o **código de ajuste** e um **código de reflexo** configurado com regra que calcule o **DIFAL** amarrado ao cadastro de **TES** utilizado na escrituração.  
  
![](https://totvssuporte.zendesk.com/attachments/token/3JkOyLsztkOGnkokKQbu8ioTr/?name=image.png)  
  
Com essa amarração na **TES**, o **código de ajuste** será apresentado automaticamente aba "**Debitos Especiais"** na **Apuração do ICMS**, conforme abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/1HD62AWymNyFtTn9kcuEzn2Hf/?name=image.png)  
  
Ao confirmar a **Apuração do ICMS** será apresentada a guia de recolhimento.  
  
![](https://totvssuporte.zendesk.com/attachments/token/2gOr6Llx5RlyEwvQ8aT1f4I6y/?name=image.png)  
  
Ao gerar o arquivo txt do **Sped Fiscal**, o valor será apresentado no **campo 15** do Registro **E110.**  
  
![](https://totvssuporte.zendesk.com/attachments/token/8j8Yq15JK0VZ8uJJjPNi5xlUu/?name=image.png)
