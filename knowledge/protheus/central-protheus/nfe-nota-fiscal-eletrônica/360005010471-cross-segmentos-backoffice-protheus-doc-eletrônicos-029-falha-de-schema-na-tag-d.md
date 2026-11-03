---
article_id: 360005010471
category: NFe - Nota Fiscal Eletrônica
content_hash: a468bef306b49c79f1f4e1beb958632646d6e36ce2283e6b5090d436a67e69d5
fetched_at: '2026-06-28T22:39:59.979774+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  029 : Falha de
  schema na Tag descanp'
type: support-article
updated_at: '2025-06-26T14:48:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005010471-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-descanp
---

**Dúvida**Como solucionar a Falha de schema na Tag descANP ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

A TAG descANP é nova na versão 4.0 da NF-e, anteriormente não existia no layout da 3.10 para fazer nota de combustível na 3.10 a Sefaz solicitava a inclusão apenas:

* CD6\_CODANP
* CD6\_UFCONS

* **Na versão 4.00 será necessário informar os três campos:**

**![COMBUSTIVEL.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006824491)**

* **Para habilitar a opção de complemento de combustível nos Livros Fiscais, deverá:**

Para habilitar a opção de complemento de combustível nos Livros Fiscais, você deverá:  
  
1. Incluir um grupo de produto (**Combustíveis**);

![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071697537815)

2. Alterar o cadastro do produto e vincular o grupo no campo **B1\_GRUPO;**

**![GRUPO_DE_PRODUTO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071697537815)**

3. Informar o grupo no parâmetro **MV\_COMBUS;**

**![MV_COMBUST.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071728783639)**

4. Após gerar a nota, acessar: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos;**

**![COMP._COMBUSTIVEL.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071697546007)**

**Na versão 4.00 da NF-e será necessário informar os quatro campos abaixo:  
  
· CD6\_CODANP**

**· CD6\_DESANP**

**. CD6\_UFCONS**

**. CDD\_IFCOMP**
