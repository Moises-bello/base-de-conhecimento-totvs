---
article_id: 4403736972439
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 59103f18798cdb3671caebc9137db4d806ae5ad7ecfdb395498ffb00feaf565b
fetched_at: '2026-06-28T22:39:51.025065+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Valor superior
  a quantidade disponível!
type: support-article
updated_at: '2021-11-11T17:44:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403736972439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Valor-superior-a-quantidade-dispon%C3%ADvel
---

**Dúvida**

Valor superior a quantidade disponível!

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403744087447/mceclip0.png)  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
**Solução**

Veirifique a configuração do parâmetro MV\_EIC0032

Com o parâmetro desabilitado (MV\_EIC0032 = .F.), não será permitido gerar as Notas Filhas com quantidade superior a 5% da mercadoria manifestada.

Com o parâmetro habilitado (MV\_EIC0032 = .T.), será permitido gerar as Notas Filhas com quantidade superior a 5% da mercadoria manifestada (Conforme legislação vigente - Artigo 706 §5º)
