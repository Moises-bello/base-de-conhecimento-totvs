---
article_id: 360027074531
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 499c78687f94af42dc77daa1a6f2f5199775cb9a35f7a24e772812a631c9907c
fetched_at: '2026-06-28T22:39:58.622249+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Valor Total
  com Desconto
type: support-article
updated_at: '2021-10-06T19:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027074531-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Valor-Total-com-Desconto
---

**Dúvida**A tag responsável por enviar o valor total no xml da nota, está subtraindo o desconto.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para solução, use o parâmetro MV\_NFSETOT=.T., dessa forma será somado o valor do desconto no valor total.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059394474/mceclip0.png)
