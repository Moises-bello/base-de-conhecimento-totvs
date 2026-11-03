---
article_id: 8687601681687
category: NFe - Nota Fiscal Eletrônica
content_hash: 8253feeb1c7f868aea065213bdbc60f5b3b64bb32855f2a8c09b01ca742d9d6c
fetched_at: '2026-06-28T22:40:05.450761+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 888 Rejeição: GTIN
  da unidade tributável (cEANTrib) sem informação'
type: support-article
updated_at: '2025-07-09T12:15:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8687601681687-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-888-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-cEANTrib-sem-informa%C3%A7%C3%A3o
---

**Dúvida**Como corrigir a rejeição 888 Rejeição: GTIN da unidade tributável (cEANTrib) sem informação ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Para levar a **TAG** **cEANTrib**se a nota possuir **duas unidades de medida** conforme o link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar Segunda unidade de medida no XML ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044212253)

* Preencher o campo B5\_2CODBAR **"2 UN Cod Bar"** (esse pra quando a empresa possui duas unidades de medida cadastrada no complemento de produto)

![2_UN_Cod_bar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347569100183)

2. Se tiver apenas um Unidade de medida preencher nos campos  B1\_CODGTIN ou B1\_CODBAR o código de barras com **GTIN 8, 12, 13 ou 14:**

* **Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347569101335)

**Ou**

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347554062103)

* **Importante:**

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN  "**Cod. Gtin"**
* B1\_CODBAR "**Cod. Barras"**
* B5\_2CODBAR  "**2 Un Cod. Bar"**

**O campo possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**

* **Saiba mais:**

Caso o dado informado no campo **B1\_CODBAR** não for exclusivo para NFe, foi incluído o campo **B1\_CODGTIN** com as seguintes regras:  
- Se o campo **B1\_CODGTIN** estiver preenchido com o código de GTIN (CCG - Cadastro Centralizado de GTIN), será gerado na tag <cEAN>.  
- Se o campo **B1\_CODGTIN** estiver preenchido com a string '000000000000000' (15), será gerado a tag <cEAN> com a descrição  "SEM GTIN".  
- Se o campo **B1\_CODGTIN** não for preenchido,  será gerado com a informação preenchida no campo B1\_CODBAR para a tag <cEAN>.
