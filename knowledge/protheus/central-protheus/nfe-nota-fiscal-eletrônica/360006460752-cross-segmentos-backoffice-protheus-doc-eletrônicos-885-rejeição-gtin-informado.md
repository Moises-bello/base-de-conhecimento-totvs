---
article_id: 360006460752
category: NFe - Nota Fiscal Eletrônica
content_hash: 69c1dd7ddd61d91cde30cd2c1ce51d0c31826b427c8ce8bb84aa1e20724ab75b
fetched_at: '2026-06-28T22:40:00.050497+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 885 Rejeição :
  GTIN informado, mas não informado o GTIN da unidade tributável'
type: support-article
updated_at: '2025-07-09T12:20:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006460752-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-885-Rejei%C3%A7%C3%A3o-GTIN-informado-mas-n%C3%A3o-informado-o-GTIN-da-unidade-tribut%C3%A1vel
---

**Dúvida**

Como solucionar a rejeição abaixo ?

885 Rejeição : GTIN informado, mas não informado o GTIN da unidade tributável

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Conforme a nota técnica **2017.001**o código **GTIN-8, GTIN-12, GTIN-13 ou GTIN-14** são os antigos códigos **EAN, UPC e DUN-14.**

1- Se no cadastro do produto conter apenas uma **Unidade de medida** **(B1\_UM)**na nota preencher os campos no **cadastro de Produto:**

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412283201943)

**Ou**

* **Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412277102231)

2- Se no cadastro de produto conter **duas Unidades de medida uma no produto (B1\_UM)**e outra no **complemento de produto (B5\_UMDIPI)** preencher:

* **2 Un Cod. Bar "B5\_2CODBAR"**

![2_UN_Cod_bar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412283302935)

3 - Após isso, exclua a nota e **gere novamente.**

* **Saiba mais:**

Se tiver duas **unidades de medida e o código  Cean e Ceantrib forem os mesmos** será necessário preencher os dois campos **B1\_CODGTIN ou B1\_CODBAR e B5\_2CODBAR.**

**IMPORTANTE:**

Caso seja **SEM GTIN** na duas TAGS basta preencher apenas.

**B1\_CODGTIN** = 000000000000000 (15 zeros)

Será levado **SEM GTIN** para a **Cean e Ceantrib**

**Importante:**

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN  "**Cod. Gtin"**
* B1\_CODBAR "**Cod. Barras"**
* B5\_2CODBAR  "**2 Un Cod. Bar"**

**O campo possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**
