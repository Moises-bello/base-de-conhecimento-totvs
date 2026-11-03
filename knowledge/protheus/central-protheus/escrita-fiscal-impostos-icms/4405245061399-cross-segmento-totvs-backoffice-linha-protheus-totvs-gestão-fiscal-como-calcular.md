---
article_id: 4405245061399
category: Escrita Fiscal - Impostos - ICMS
content_hash: 19d891b0ee8f076537e1d4c2829740abb228ec68e5800b10dc207b85c796b08b
fetched_at: '2026-06-28T22:39:24.097688+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal-Como
  calcular ICMS Desonerado com redução de base de icms ?
type: support-article
updated_at: '2021-07-29T18:17:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405245061399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-Como-calcular-ICMS-Desonerado-com-redu%C3%A7%C3%A3o-de-base-de-icms
---

Tempo aproximado para leitura: 00:01:00**min** **Dúvida**Como calcular ICMS Desonerado com redução de base de icms ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Como calcular ICMS desonerado com redução de base de icms para descontar do valor total da nota fiscal

TES  
Calcula icms = sim  
l fiscal icms = outros  
% red icms = 70  
Agrega valor = D  
Cst = 20  
Mot desone = 9

Exemplo = valor da mercadoria = 1.000,00

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405254231191/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405254201239/mceclip0.png)

valor do icms desonerado = 54,00

Verificar o parametro MV\_DBRDIF = .T.

<https://tdn.totvs.com/pages/releaseview.action?pageId=334342114>
