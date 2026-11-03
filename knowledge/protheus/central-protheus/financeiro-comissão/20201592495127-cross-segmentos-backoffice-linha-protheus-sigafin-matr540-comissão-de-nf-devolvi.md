---
article_id: 20201592495127
category: Financeiro - Comissão
content_hash: d4e9c63c93833ebd776b2243c7d3b652469eace0ed8a4100cf14d3c2fa99729b
fetched_at: '2026-06-28T22:37:50.797315+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - MATR540 - Comissão
  de NF devolvida
type: support-article
updated_at: '2026-03-25T14:39:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20201592495127-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATR540-Comiss%C3%A3o-de-NF-devolvida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20201564780951) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como gerar comissão para NF devolvida?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para gerar comissão para uma NF devolvida, ou seja, uma comissão com o valor negativo, devemos parametrizar os seguintes pontos:   
  
1° Parâmetro MV\_COMIDEV:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20201564783511)

2° Além do parâmetro, no momento da compensação da NCC com a NF, no F12 da rotina, devemos marcar a opção "Calc. Comiss. S/NCC?" como sim, para que desse modo, sejam apresentados no relatório os valores da devolução e da baixa da NF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20201592480919)

Saiba Mais

[MP - SIGALOJA - Parâmetro - MV\_COMIDEV](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053741913-MP-SIGALOJA-Par%C3%A2metro-MV-COMIDEV)
