---
article_id: 360005487532
category: NFe - Nota Fiscal Eletrônica
content_hash: 748cbaa609fe11b575353d8c4cf7da4a2665694f87f45af6c4f7313587684d96
fetched_at: '2026-06-28T22:40:00.007628+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema na Tag cEAN cEANTrib'
type: support-article
updated_at: '2026-01-27T21:59:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005487532-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-cEAN-cEANTrib
---

**Dúvida**  
Como solucionar a Falha de schema na Tag cEan  cEanTrib ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

**![Cean_e_Ceantrib_possibilidades.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006874091)**

* Se preenchida as TAGS <cEan> <cEanTrib> o código de barras deve possuir 8, 12, 13 ou 14 posições ou deve haver o literal Sem Gtin

* Conforme a nota técnica **2017.001**o código **GTIN-8, GTIN-12, GTIN-13 ou GTIN-14** são os antigos códigos **EAN, UPC e DUN-14.**

1- Se no cadastro do produto conter apenas uma **Unidade de medida** **(B1\_UM)**na nota preencher os campos no **cadastro de Produto:**

* **Cod. Gtin "B1\_CODGTIN"**

![Cod._Gtin.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071552005271)

**Ou**

* **Cod. Barras "B1\_CODBAR"**

![Cod._Barras.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071515978263)

2- Se no cadastro de produto conter **duas Unidades de medida uma no produto (B1\_UM)**e outra no **complemento de produto (B5\_UMDIPI)** preencher:

* **2 Un Cod. Bar "B5\_2CODBAR"**

![2_UN_Cod_bar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071552007319)

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

**Os campos B1\_CODGTIN e B1\_CODBAR possui um gatilho:**

* Se tiver 12 deverão ser **preenchidos 11 e o gatilho irá preencher o 12.**
* Se tiver 13 deverão ser **preenchidos 12 e o gatilho irá preencher o 13.**
* Se tiver 14 deverão ser **preenchidos 13 e o gatilho irá preencher o 14.**

* **As listas de prefixos aceitos estão disponíveis nos sites:**

[www.gs1.org/company-prefix”.](http://www.gs1.org/company-prefix)

<http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=Iy/5Qol1YbE=>

[Tabela Prefixo GS1](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=mpYVEbsVRuE=)

* **Validação da SEFAZ:**

**![NT_GTIN.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006836652)**
