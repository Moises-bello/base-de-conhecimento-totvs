---
article_id: 1500007026482
category: TAF - REINF
content_hash: ab7d9fa5910b891adfaf777737aadd36a0cb8abdd5ccd8a97bc3e4c01946c553
fetched_at: '2026-06-28T22:41:34.803735+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - R-2050 Indicativo de
  comercialização
type: support-article
updated_at: '2023-04-04T12:09:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007026482-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-R-2050-Indicativo-de-comercializa%C3%A7%C3%A3o
---

**Dúvida**

**Como Configurar o Indicativo de comercialização referente ao evento R-2050**  
  
**Ambiente**

A Partir: 12.1.17  
  
**Solução**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009624361/mceclip4.png)

**Como Gerar Indicativo de comercialização com o numero 1.**

Campo C1H\_PAA no cadastro de participantes **NÃO PODE** estar como sim(numero 1) e CFOP **NÃO PODE** começar com 1.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009622541/mceclip0.png)

**Como Gerar Indicativo de comercialização com o numero 7.**

o Layout no parâmetro MV\_TAFVLRE precisa estar com o conteúdo 1\_04\_00 e o campo C30\_INDISE precisa estar como **SIM**(numero 1).

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009371042/mceclip2.png)

**Como Gerar Indicativo de comercialização com o numero 8.**

C1H\_PAA precisa estar como **SIM**(numero 1).

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009371602/mceclip3.png)

**Como Gerar Indicativo de comercialização com o numero 9.**

C1H\_PAA **NÃO PODE** estar como como **SIM**(numero 1) e CFOP precisa começar com 7.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009624601/mceclip5.png)
