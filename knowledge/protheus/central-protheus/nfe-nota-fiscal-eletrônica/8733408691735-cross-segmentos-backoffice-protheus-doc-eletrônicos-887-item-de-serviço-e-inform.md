---
article_id: 8733408691735
category: NFe - Nota Fiscal Eletrônica
content_hash: 691aaee088085831a7fc16a85fa2a53d52eaf18860e137a3cade281eabf2854b
fetched_at: '2026-06-28T22:40:05.443735+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 887 Item de Serviço
  e informado GTIN diferente de SEM GTIN
type: support-article
updated_at: '2025-07-09T12:12:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8733408691735-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-887-Item-de-Servi%C3%A7o-e-informado-GTIN-diferente-de-SEM-GTIN
---

**Dúvida**Como corrigir a 887 Item de Serviço e informado GTIN diferente de SEM GTIN ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informado ***grupo de tributação do ISSQN (id:U01),*** deve ser informado GTIN ***(tag:***  
***cEAN) e GTIN da unidade tributável (tag: cEANTrib) igual a “SEM GTIN”***

1. Se tiver apenas uma unidade de medida preencher o campo **B1\_CODGTIN**  com a '000000000000000' (15), será gerado a tag <cEAN> e <cEANTrib> com a descrição  "SEM GTIN".

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347476495127)

2. Se tiver duas unidades de medida, além do preenchimento do campo acima retirar o código de barras do campo B5\_2CODBAR **"2 UN Cod Bar"** (esse pra quando a empresa possui duas unidades de medida cadastrada no complemento de produto)

![2_UN_Cod_bar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347476497943)

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

* ***Validação da Sefaz:***

***![887_rejeicao.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8732965541143)***
