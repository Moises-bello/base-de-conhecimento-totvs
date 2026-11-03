---
article_id: 360055777954
category: NFe - Nota Fiscal Eletrônica
content_hash: f5195efd42e3379b551ca24ee588b5d2c64295ede59f1ac887e480fd672b4e50
fetched_at: '2026-06-28T22:40:05.431846+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 882 Rejeição: GTIN
  (cEAN) com prefixo inválido'
type: support-article
updated_at: '2025-06-04T18:58:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055777954-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-882-Rejei%C3%A7%C3%A3o-GTIN-cEAN-com-prefixo-inv%C3%A1lido
---

**Dúvida**Como solucionar a rejeição 882: GTIN (cEAN) com prefixo inválido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Conforme a nota técnica ***2021.003*** o código ***GTIN-8, GTIN-12, GTIN-13 ou GTIN-14*** são os antigos códigos ***EAN, UPC e DUN-14.***

1- Preencher nos campos B1\_CODGTIN ou  B1\_CODBAR  o prefixo correto [Tabela Prefixo GS1](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=mpYVEbsVRuE=) do ***código de barras que são os três primeiros algoritmos do GTIN.***

***Cód. Gtin "B1\_CODGTIN"***

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29072430045207)

**Ou** ***Cód. Barras "B1\_CODBAR"***

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29072430049431)

2- Após isso, ***exclua a nota e gere novamente.***

**Importante:**

***A lista de prefixos aceitos está disponível no link abaixo em Documentos -> Diversos:***

[Tabela Prefixo GS1](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=Oc%20fygAxwmc=)

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN  "**Cód. Gtin"**
* B1\_CODBAR "**Cód. Barras"**

**O campo possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**

Conforme a nota técnica **2021.003** o código **GTIN-8, GTIN-12, GTIN-13 ou GTIN-14** são os antigos códigos **EAN, UPC e DUN-14.**

O GTIN ***de 14 posições, só pode ser utilizado quando há duas unidades de medida*** no XML a primeira por exemplo e 13 UN e a segunda 14 KG.  
Uma ***por exemplo*** é referente a lata e outra a caixa. Se as duas forem iguais deve ter ***8, 12 ou 13*** é válido pela Sefaz, o XML.

**Saiba mais:**

A rejeição pode ocorrer devido as TAGS **cEAN e cEANTrib** gerarem com um código de barras de 14 dígitos. Porém com a unidade de medida **comercial uCom e tributável uTrib iguais.**

![GTIN.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/29072435648919)

***Validação da Sefaz:***

![882.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/7163798352407)
