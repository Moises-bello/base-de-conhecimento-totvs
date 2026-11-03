---
article_id: 38355084565655
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 89b90055b1b29821494c817259a99aed4d6fcab83ea442485765a34d3da7a331
fetched_at: '2026-06-28T22:37:22.943751+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CXNPROMED para
  marcar a planilha recorrente é necessário mudar a competência na medição
type: support-article
updated_at: '2026-02-12T14:55:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38355084565655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CXNPROMED-para-marcar-a-planilha-recorrente-%C3%A9-necess%C3%A1rio-mudar-a-compet%C3%AAncia-na-medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38355084539415) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**

Ao selecionar a competência na medição ocorre o Help:

Help CXNPROMED para marcar a planilha recorrente é necessário mudar a competência XX/XXXX

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38355084539927)

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS  Gestão de Contratos - A partir da versão 12.

**Causa**  
  
Esse incidente ocorre, pois a competência selecionada na medição está divergente do campo **Próx. Med (CNA\_PROMED)** na Planilha do contrato.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38355076518551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38355076521879)

**Solução**

Para que o sistema não apresente o Help:

1. Na rotina Manutenção CNTA300 visualize na planilha do contrato e veja qual é o mês da "Próx. Med", no campo da imagem acima.

2. Inclua a Medição na mês competência do campo **Prox.Med (CNA\_PROMED)**

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Contrato ou Planilha Recorrente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9015993098775-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Contrato-ou-Planilha-Recorrente)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
