---
article_id: 360058757574
category: NFe - Nota Fiscal Eletrônica
content_hash: 9cf4cc17f33e566e4eccbff42399ba06f81757611b675438056417cf19abb414
fetched_at: '2026-06-28T22:40:05.217681+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 630 Rejeição: Valor
  do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável'
type: support-article
updated_at: '2025-06-13T11:50:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058757574-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-630-Rejei%C3%A7%C3%A3o-Valor-do-Produto-difere-do-produto-Valor-Unit%C3%A1rio-de-Tributa%C3%A7%C3%A3o-e-Quantidade-Tribut%C3%A1vel
---

**Dúvida**

Como corrigir a rejeição abaixo:

630 Rejeição: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Sefaz  faz a seguinte validação nas TAGS ***vProd  difere de vUnTrib  \* qTrib***

* **Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000296682)

1 - Caso a unidade de medida ***<uCom>*** e ***<uTrib>***sejam iguais:

**As TAGS <vUnCom> e a <vUnTrib>** deve ter o mesmo conteúdo.

Para unidades de medidas iguais, não deve ser preenchido os ***campos na SB5:***

**B5\_CONVDIP e B5\_UMDIPI**

* Para saber, como o sistema chega no **vUnCom segue o artigo abaixo:**

*[MP - NFE - Qual o conteúdo é levado para a TAG vUnCom ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028071034)*

2 - Caso a unidade de medida ***<uCom>*** e ***<uTrib>***sejam diferentes:

* **Configurar o parâmetro do link abaixo para operações nacionais:**

[NFE0118\_Parâmetro\_MV\_NIMP2UM](http://tdn.totvs.com/pages/viewpage.action?pageId=284866258)

**MV\_NIMP2UM = .F.   ( Se não houver necessidade de apresentar as duas unidades no XML)**

**![20201201_172751.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16513556216983)**

Após isso, ***exclua a nota e gere*** novamente.

**Para emitir a nota com duas unidades de medida no XML:**

**1-** Ir em complemento **do produto:**

![20201201_172957.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16513571703063)

**2-** Cadastrar o **produto e preencher os campos B5\_CONVDIP e B5\_UMDIPI** ( Verificar se o valor de **conversão** informado neste campo, **está correta**)

![20201201_173116.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16513571704215)

**3-** Após isso, **incluir o pedido de venda e realizar a transmissão da nota:**

* **Saiba mais:**

<uCom>**UN**</uCom>***primeira unidade (cadastro de produto)***

<uTrib>**DZ**</uTrib>***segunda unidade (complemento de produto)***

* **Validação da Sefaz :**

**![rejei__o_630.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000296322)**
