---
article_id: 360044662754
category: NFe - Nota Fiscal Eletrônica
content_hash: 1a2dd5be6169eda30c6f14ff95295775853f09ece3c33bfb04557159f3acae7e
fetched_at: '2026-06-28T22:40:01.649619+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como é preenchida
  a tag IEST, para operação que possui cliente de entrega de outra UF'
type: support-article
updated_at: '2024-06-20T13:58:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044662754--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-%C3%A9-preenchida-a-tag-IEST-para-opera%C3%A7%C3%A3o-que-possui-cliente-de-entrega-de-outra-UF
---

**Dúvida**

Como é preenchida a tag IEST, para operação que possui cliente de entrega de outra UF ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**A tag <IEST> considera a UF do cliente de Destino, e não a UF do cliente de entrega, e será preenchida com conteúdo da IE informado no parâmetro MV\_SUBTRIB.

Exemplo :  
MV\_SUBTRIB=RS9000032828/PR          /SP     
Venda para UF=RS  
Entrega para UF=SP    

Veja no xml abaixo que a tag IEST  considerou a UF cliente de Destino, e preencheu a IEST referente a UF=RS

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061164734/mceclip0.png)

* **Saiba Mais:**  
  [MP - NFE - Como gerar a TAG IEST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025537353)
