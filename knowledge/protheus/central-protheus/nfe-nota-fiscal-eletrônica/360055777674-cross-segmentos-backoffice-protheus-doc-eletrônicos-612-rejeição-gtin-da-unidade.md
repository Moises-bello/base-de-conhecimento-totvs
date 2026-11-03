---
article_id: 360055777674
category: NFe - Nota Fiscal Eletrônica
content_hash: f6d907a656ed2fcae1574f487946cc44ba402a8c381e3fc941d9b66cfe381ee8
fetched_at: '2026-06-28T22:40:05.179337+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 612 Rejeição :
  GTIN da unidade tributável (cEANTrib) inválido'
type: support-article
updated_at: '2025-07-09T11:55:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055777674-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-612-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-cEANTrib-inv%C3%A1lido
---

**Dúvida**Como solucionar a rejeição 612  Rejeição : GTIN da unidade tributável (cEANTrib) inválido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Conforme a nota técnica **2017.001** o código **GTIN-8, GTIN-12, GTIN-13 ou GTIN-14** são os antigos códigos **EAN, UPC e DUN-14.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347184886935)

1- Preencher nos campos  **B1\_CODGTIN ou B1\_CODBAR** ou **B5\_2CODBAR** ou no campo  o código de barras com **GTIN 8, 12, 13 ou 14:**

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347184887703)

**Ou**

* **Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347181618071)

**Ou**

* **2 Un Cod. Bar "B5\_2CODBAR"**

![2_UN_Cod_bar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412351030039)

2- Após isso, **exclua a nota e gere novamente.**

* **Saiba mais:**

Se tiver duas **unidades de medida e o código  Cean e Ceantrib forem os mesmos** será necessário preencher os dois campos **B1\_CODGTIN ou B1\_CODBAR e B5\_2CODBAR.**

* **Importante:**

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN  "**Cod. Gtin"**
* B1\_CODBAR "**Cod. Barras"**
* B5\_2CODBAR  "**2 Un Cod. Bar"**

**O campo possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**

* Conforme a nota técnica **2017.001** o código **GTIN-8, GTIN-12, GTIN-13 ou GTIN-14** são os antigos códigos **EAN, UPC e DUN-14.**

É possível confirmar qual o último dígito **deve ter no padrão conforme o site:**

[www.gs1.org/check-digit-calculator](http://www.gs1.org/check-digit-calculator)

Caso seja **SEM GTIN** na duas TAGS basta preencher apenas.

**B1\_CODGTIN "Cod. Gtin"**= com até 14 zeros neste campo

Será levado **SEM GTIN** para a **Cean e Ceantrib**

![GTIN.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33347181618839)
