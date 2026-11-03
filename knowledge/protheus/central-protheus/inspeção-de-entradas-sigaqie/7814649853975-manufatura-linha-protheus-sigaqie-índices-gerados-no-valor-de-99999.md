---
article_id: 7814649853975
category: Inspeção de Entradas (SIGAQIE)
content_hash: 04341861cf9408e1b9c3e75f6133ce83fbf508f657a6521c5bbc5eeb6a204e14
fetched_at: '2026-06-28T22:42:27.051690+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Índices gerados no valor de 999,99
type: support-article
updated_at: '2022-08-01T16:35:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7814649853975-Manufatura-Linha-Protheus-SIGAQIE-%C3%8Dndices-gerados-no-valor-de-999-99
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min** **Dúvida**Qual o motivo da rotina **QIEA230 - Geração de Índices** gerar um registro na tabela **QEV - Relatórios Índices Qualidade** com lote e dados zerados, mas os índices no valor de 999,99?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Isto ocorre quando não existem entradas no mês/ano, e neste caso, a tabela **QEV** é gerada com os campos **QEV\_LOTENT - Lotes Entregues**, **QEV\_LOTDEM - Lotes Demeritados**, **QEV\_LOTINS - Lotes Inspecionados** e **QEV\_LOTSKP - Lotes em Skip-lote** zerados, e os campos dos índices **QEV\_IQP - IQP**, **QEV\_IQD - IQD**, **QEV\_IQS - IQS**, **QEV\_IQI - IQI**, **QEV\_IPO - IPO**, **QEV\_ITR - ITR**, **QEV\_IES - IES**, **QEV\_IPR - IPR** e **QEV\_IQF - IQF** com os valores de 999,99.
