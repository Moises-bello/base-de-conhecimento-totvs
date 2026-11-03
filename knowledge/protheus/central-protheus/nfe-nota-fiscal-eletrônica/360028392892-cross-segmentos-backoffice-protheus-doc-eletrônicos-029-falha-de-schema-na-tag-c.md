---
article_id: 360028392892
category: NFe - Nota Fiscal Eletrônica
content_hash: 665345ac66dc966ce7010ff82f1ae8f03a6a0bd8eddf9fffb1f87af7cba68c06
fetched_at: '2026-06-28T22:40:00.445730+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029: Falha de
  schema na Tag <cEAN> <cEANTrib>'
type: support-article
updated_at: '2021-11-05T17:00:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028392892--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-cEAN-cEANTrib
---

**Dúvida**Como solucionar a 029- Falha de schema na Tag <cEAN> <cEANTrib>  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para solucionar é importante verificar se está preenchida **as TAGS <cEan> <cEanTrib> o código de barras deve possuir 8, 12, 13 ou 14 posições ou deve haver o literal Sem Gtin**

* Se preenchida as TAGS <cEan> <cEanTrib> o código de barras deve possuir **8, 12, 13 ou 14** posições ou deve haver o literal Sem Gtin

* Se preenchida as TAGS <cEan> <cEanTrib> o código de barras deve possuir **8, 12, 13 ou 14** posições ou deve haver o literal Sem Gtin

1- Se no cadastro do produto conter apenas uma **Unidade de medida** **(B1\_UM)**na nota preencher os campos no **cadastro de Produto:**

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412283201943/Cod._Gtin.gif)

**Ou**

* **Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412277102231/Cod._Barras.gif)

2- Se no cadastro de produto conter **duas Unidades de medida uma no produto (B1\_UM)**e outra no **complemento de produto (B5\_UMDIPI)** preencher:

* **2 Un Cod. Bar "B5\_2CODBAR"**

![2_UN_Cod_bar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412283302935/2_UN_Cod_bar.gif)

3 - Após isso, exclua a nota e **gere novamente.**

* **Saiba mais:**

Se tiver duas **unidades de medida e o código  Cean e Ceantrib forem os mesmos** será necessário preencher os dois campos **B1\_CODGTIN ou B1\_CODBAR e B5\_2CODBAR.**

**Importante:**

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN  "**Cod. Gtin"**
* B1\_CODBAR "**Cod. Barras"**
* B5\_2CODBAR  "**2 Un Cod. Bar"**

**O campo possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**

* **Saiba mais:**

![GTIN.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006945652/GTIN.PNG)
