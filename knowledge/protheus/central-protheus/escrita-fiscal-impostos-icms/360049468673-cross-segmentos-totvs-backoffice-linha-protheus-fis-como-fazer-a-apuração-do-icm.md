---
article_id: 360049468673
category: Escrita Fiscal - Impostos - ICMS
content_hash: 579a7e6dfa97d88ec7c056698c937e25edda11f450f0d776409d07fc94a25095
fetched_at: '2026-06-28T22:39:24.190380+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como fazer a apuração
  do ICMS da restituição ICMS-ST do RS ? '
type: support-article
updated_at: '2021-07-28T02:58:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049468673-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-fazer-a-apura%C3%A7%C3%A3o-do-ICMS-da-restitui%C3%A7%C3%A3o-ICMS-ST-do-RS
---

**Dúvida** Como fazer a apuração do ICMS da restituição ICMS -ST do RS ?   
  
**Ambiente**Protheus - fiscal - a partir da versão 11.80

**Solução**

Após gerado a apuração do Fisa196, conforme boletim

<https://tdn.totvs.com/pages/releaseview.action?pageId=463811572>

Para a apuração verificar os parâmetros:

Parâmetros  
MV\_usasped = .T.  
MV\_p9sped = .T.  
MV\_p9auto = T

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073692953/mceclip0.png)

exemplo , de configuração na TES livro = 1

 (F4\_NRLIVRO) = 1

1) Gerar primeiro a sub-apuração

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072518234/mceclip1.png)

os valores serão gerados na sub-apuração e transportados para a apuração centralizada através do arquivo P9autotext.RS na pasta system do Protheus

Apuração centralizada

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072519314/mceclip2.png)
