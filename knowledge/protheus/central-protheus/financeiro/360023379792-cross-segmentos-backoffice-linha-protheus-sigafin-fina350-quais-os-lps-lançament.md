---
article_id: 360023379792
category: Financeiro
content_hash: 2e4f067e0546a1e901b9543987cc4a208fefc4605f70e6f5e74adf4a967631c9
fetched_at: '2026-06-28T22:38:03.006446+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA350 - Quais os
  Lp''s (Lançamento Padrão) utilizados na Correção Monetário '
type: support-article
updated_at: '2022-06-15T02:02:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023379792-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA350-Quais-os-Lp-s-Lan%C3%A7amento-Padr%C3%A3o-utilizados-na-Corre%C3%A7%C3%A3o-Monet%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Quais os Lp's (Lançamento Padrão) utilizados e a configuração da Correção Monetário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA350 - Todas as versões  
  
  
**Solução****LP598 - Var.Monet.Ctas a Rec**| SA1->A1\_CONTA |Cta Espec (R) \*\*|Utilizar o campo valor a variável ABS(VALOR)

**LP599 - Var.Monet.Ctas a Pag**|Cta Espec (D) \*\*|SA2->A2\_CONTA|Utilizar o campo valor a variável ABS(VALOR)

**Saiba mais:**  
[FIN0012\_LPAD\_CONTABILIZAÇÃO \_VARIAÇÃO\_CONTABIL](http://tdn.totvs.com/pages/releaseview.action?pageId=244934660)
