---
article_id: 8687242057879
category: NFe - Nota Fiscal Eletrônica
content_hash: 912012f5a8506775ead805e293c29b425047bd6c0a48b27e5b06cc5bf03714cb
fetched_at: '2026-06-28T22:40:05.437821+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 883 Rejeição: GTIN
  (cEAN) sem informação'
type: support-article
updated_at: '2025-07-09T12:17:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8687242057879-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-883-Rejei%C3%A7%C3%A3o-GTIN-cEAN-sem-informa%C3%A7%C3%A3o
---

**Dúvida**Como corrigir a 883 Rejeição: GTIN (cEAN) sem informação ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para levar a **TAG cEAN** referente a **primeira unidade**  a **TAG** **cEANTrib :**

1- Preencher nos campos  B1\_CODGTIN ou B1\_CODBAR o código de barras com **GTIN 8, 12, 13 ou 14:**

* **Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347576029463)

**Ou**

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347611316631)

* **Saiba mais:**

Caso o dado informado no campo **B1\_CODBAR** não for exclusivo para NFe, foi incluído o campo **B1\_CODGTIN** com as seguintes regras:  
- Se o campo **B1\_CODGTIN** estiver preenchido com o código de GTIN (CCG - Cadastro Centralizado de GTIN), será gerado na tag <cEAN>.  
- Se o campo **B1\_CODGTIN** estiver preenchido com a string '000000000000000' (15), será gerado a tag <cEAN> com a descrição  "SEM GTIN".  
- Se o campo **B1\_CODGTIN** não for preenchido,  será gerado com a informação preenchida no campo B1\_CODBAR para a tag <cEAN>.

* **Importante:**

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN  "**Cod. Gtin"**
* B1\_CODBAR "**Cod. Barras"**

**O campo possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**

* ***Validação da Sefaz:***

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8687231277847)***
