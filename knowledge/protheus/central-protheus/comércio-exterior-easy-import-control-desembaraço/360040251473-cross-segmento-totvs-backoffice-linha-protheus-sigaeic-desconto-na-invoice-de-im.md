---
article_id: 360040251473
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 307f05e925815548ad48c00fba37af9cd492dcc376c09afbf6b75d66a622c800
fetched_at: '2026-06-28T22:39:51.031157+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAEIC - Desconto na Invoice
  de Importação
type: support-article
updated_at: '2021-08-19T21:02:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040251473-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Desconto-na-Invoice-de-Importa%C3%A7%C3%A3o
---

**Dúvida**Como conceder desconto na **Invoice** de Importação?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.

**Solução** Para solucionar essa dúvida, realize os seguintes passos:  
1. Acesse SIGAEIC - Atualizações - Desembaraço - Manutenção(EICDI502).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052772754/mceclip0.png)

2.  Posicione na **sobre o processo** e selecione ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049444933/mceclip2.png)

3. Selecione Outras Ações e Inoices.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053673613/mceclip1.png)

4. Selecione Outras Ações novamente e Alterar.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053673653/mceclip2.png)

5. Posicione no campo Desconto 'W9\_DESCONT'  e informe o valor do desconto do processo e confirme.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053673693/mceclip3.png)

Para que o módulo Easy Import Control considere o desconto informado na(s) Invoice(s) do processo na formação do valor FOB e, consequentemente, da base dos impostos, é necessário que o *parâmetro MV\_IN327 seja desabilitado (.F.)*([Easy Import Control - 11.80 - Agosto/15](https://tdn.totvs.com/pages/releaseview.action?pageId=196813704)). Esse parâmetro, *True* (.T.) por padrão, desconsidera o desconto informado na Invoice, não refletindo no valor FOB informado em diversos momentos no processo de desembaraço, como da pasta Valores da DI e despesas, bem como no recebimento de importação.
