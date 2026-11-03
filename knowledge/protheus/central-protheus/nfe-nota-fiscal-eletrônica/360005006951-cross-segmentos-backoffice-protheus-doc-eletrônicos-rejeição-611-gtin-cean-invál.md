---
article_id: 360005006951
category: NFe - Nota Fiscal Eletrônica
content_hash: fc3dce6df8afa0f5250bf4b7dca67b5f132b43521787416aa247ed6f6f3b0e40
fetched_at: '2026-06-28T22:39:59.962565+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 611 :
  GTIN (cEAN) inválido '
type: support-article
updated_at: '2021-11-05T13:24:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005006951--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-611-GTIN-cEAN-inv%C3%A1lido
---

**Dúvida**Como solucionar a rejeição 611 - Rejeição: GTIN (cEAN) inválido ?  
  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043870034/mceclip0.png)

1- Preencher nos campos  B1\_CODGTIN ou B1\_CODBAR o código de barras com **GTIN 8, 12, 13 ou 14:**

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412283201943/Cod._Gtin.gif)

**Ou**

* **Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412277102231/Cod._Barras.gif)

2- Após isso, **exclua a nota e gere novamente.**

* **Importante:**

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN  "**Cod. Gtin"**
* B1\_CODBAR "**Cod. Barras"**

**O campo possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**

* Conforme a nota técnica **2017.001** o código **GTIN-8, GTIN-12, GTIN-13 ou GTIN-14** são os antigos códigos **EAN, UPC e DUN-14.**

É possível confirmar qual o último dígito **deve ter no padrão conforme o site:**

[www.gs1.org/check-digit-calculator](http://www.gs1.org/check-digit-calculator)

* **Saiba mais:**

![GTIN.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006945652/GTIN.PNG)

***Segue o vídeo em anexo abaixo de exemplo:***
