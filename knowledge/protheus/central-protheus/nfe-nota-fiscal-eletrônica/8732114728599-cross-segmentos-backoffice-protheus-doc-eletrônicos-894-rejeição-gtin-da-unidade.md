---
article_id: 8732114728599
category: NFe - Nota Fiscal Eletrônica
content_hash: b8364b58684c5b5d3695c9cc127066f504d3e67070792fe0e8cd8e50043c4786
fetched_at: '2026-06-28T22:40:05.480662+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 894 Rejeição: GTIN
  da unidade tributável inexistente no Cadastro Centralizado de GTIN (CCG)'
type: support-article
updated_at: '2024-09-02T17:48:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8732114728599-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-894-Rejei%C3%A7%C3%A3o-GTIN-da-unidade-tribut%C3%A1vel-inexistente-no-Cadastro-Centralizado-de-GTIN-CCG
---

**Dúvida**Como corrigir a 894 Rejeição: GTIN da unidade tributável inexistente no Cadastro Centralizado de GTIN (CCG) ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se Acesso CCG-Cadastro Centralizado de GTIN da unidade tributável informado na NF-e ***(tag: cEANTrib)*** inexistente no CCG.

[https://cnp.gs1br.org/](https://cnp.gs1br.org/.%20)

<https://dfe-portal.svrs.rs.gov.br/Nfe/Gtin>

É possível confirmar qual o último dígito ***deve ter no padrão conforme o site:***

[www.gs1.org/check-digit-calculator](http://www.gs1.org/check-digit-calculator)

1. Para alterar o NCM diferente do grupo do Anexo I preencha no campo do cadastro de produto ***Pos.IPI/NCM** "**B1\_POSIPI". para um NCM válido pela Sefaz.***

![20220411_141510.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26078509300503)

2. Para alterar para o Código de barras correto, verificar [https://cnp.gs1br.org/](https://cnp.gs1br.org/.%20)É possível confirmar qual o último dígito ***deve ter no padrão conforme o site:*** [www.gs1.org/check-digit-calculator](http://www.gs1.org/check-digit-calculator)

3. Preencher a **TAG** **cEANTrib**se a nota possuir **duas unidades de medida** conforme o link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar Segunda unidade de medida no XML ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044212253)

* Preencher o campo B5\_2CODBAR **"2 UN Cod Bar"** (esse pra quando a empresa possui duas unidades de medida cadastrada no complemento de produto)

![2_UN_Cod_bar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26078484170391)

5. Se tiver apenas um Unidade de medida preencher nos campos  B1\_CODGTIN ou B1\_CODBAR o código de barras com **GTIN 8, 12, 13 ou 14:**

**Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26078509304343)

**Ou** **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/26078509306903)

**Ao digitar o código de barras nos campos:**

* B1\_CODGTIN  "**Cod. Gtin"**
* B1\_CODBAR "**Cod. Barras"**
* B5\_2CODBAR  "**2 Un Cod. Bar"**

**O campo possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**

**Saiba mais:**

Caso o dado informado no campo **B1\_CODBAR** não for exclusivo para NFe, foi incluído o campo **B1\_CODGTIN** com as seguintes regras:  
- Se o campo **B1\_CODGTIN** estiver preenchido com o código de GTIN (CCG - Cadastro Centralizado de GTIN), será gerado na tag <cEAN>.  
- Se o campo **B1\_CODGTIN** estiver preenchido com a string '000000000000000' (15), será gerado a tag <cEAN> com a descrição  "SEM GTIN".  
- Se o campo **B1\_CODGTIN** não for preenchido,  será gerado com a informação preenchida no campo B1\_CODBAR para a tag <cEAN>.

***Validação da Sefaz:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26078509308567)
