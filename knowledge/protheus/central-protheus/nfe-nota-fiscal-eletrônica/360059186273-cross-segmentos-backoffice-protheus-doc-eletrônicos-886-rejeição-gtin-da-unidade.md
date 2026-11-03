---
article_id: 360059186273
category: NFe - Nota Fiscal Eletrônica
content_hash: c846e1017c6d24f8c80a00a70bc0bb625a949317aacd07a901cfed9b060477b8
fetched_at: '2026-06-28T22:40:03.320772+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  886 Rejeição :
  GTIN da unidade tributável informado, mas não informado o GTIN'
type: support-article
updated_at: '2025-06-17T19:01:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059186273-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-886-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-informado-mas-n%C3%A3o-informado-o-GTIN
---

**Dúvida**Como corrigir a rejeição abaixo:

886 Rejeição : GTIN da unidade tributável informado, mas não informado o GTIN  ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para levar a **TAG cEAN** referente a **primeira unidade** e **segunda unidade medida** caso sejam iguais a **TAG** **cEANTrib :**

1- Preencher nos campos  B1\_CODGTIN ou B1\_CODBAR o código de barras com **GTIN 8, 12, 13 ou 14:**

* **Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15313687787031)

**Ou**

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15313687789463)

* **Saiba mais:**

Caso o dado informado no campo **B1\_CODBAR** não for exclusivo para NFe, foi incluído o campo **B1\_CODGTIN** com as seguintes regras:  
- Se o campo **B1\_CODGTIN** estiver preenchido com o código de GTIN (CCG - Cadastro Centralizado de GTIN), será gerado na tag <cEAN>.  
- Se o campo **B1\_CODGTIN** estiver preenchido com a string '000000000000000' (15), será gerado a tag <cEAN> com a descrição  "SEM GTIN".  
- Se o campo **B1\_CODGTIN** não for preenchido,  será gerado com a informação preenchida no campo B1\_CODBAR para a tag <cEAN>.

2- Para levar a **TAG** **cEANTrib**se a nota possuir **duas unidades de medida** conforme o link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar Segunda unidade de medida no XML ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044212253)

* Preencher o campo B5\_2CODBAR **"2 UN Cod Bar"** (esse pra quando a empresa possui duas unidades de medida cadastrada no complemento de produto)

![2_UN_Cod_bar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15313662645911)

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

* **Validação da Sefaz:**

**![rejei__o_886.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360099501853)**
