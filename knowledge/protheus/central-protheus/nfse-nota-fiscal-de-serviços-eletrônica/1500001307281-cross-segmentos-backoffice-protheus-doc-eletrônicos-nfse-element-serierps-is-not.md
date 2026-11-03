---
article_id: 1500001307281
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3b792373ae5dba150721f9c9514785796e25324a16382e6374c54975c77f6efe
fetched_at: '2026-06-28T22:39:57.398342+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Element 'serierps':"
  is not a valid
type: support-article
updated_at: '2025-07-08T19:47:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001307281-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Element-serierps-is-not-a-valid
---

**Dúvida**Ao transmitir um RPS ocorre o erro: **Element 'serierps': [facet 'minLength'] The value has a length of '0'; this underruns the allowed minimum length of '1'.**  
  
![Serie_RPS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360102386093/Serie_RPS.PNG)  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O Erro "Element 'serierps':"is not a valid" ocorre na transmissão da nota, quando no pedido de vendas o campo **C5\_NFSUBST** está preenchido e o campo **C5\_SERSUBS** está vazio, ou vice e versa.  
  
![NFSUBST.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001376481/NFSUBST.png)![sERIE.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001311962/sERIE.png)  
 **Faça o correto preenchimento dos dois campos, ou se essa nota não for de substituição, limpe os dois campos.**
