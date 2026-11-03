---
article_id: 360019243511
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b97c0f233949190f4d81fb3fe02564dbbb981d172dd9049862567652ac9abe5b
fetched_at: '2026-06-28T22:38:41.027703+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Funcionamento do parâmetro MV_NDESCTP
type: support-article
updated_at: '2026-02-12T17:14:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019243511-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Funcionamento-do-par%C3%A2metro-MV-NDESCTP
---

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7491988610583)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida:**Qual é a função do parâmetro **MV\_NDESCTP**?  
  
**Ambiente:**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) – Todas as versões

**Solução:**

O parâmetro **MV\_NDESCTP** define se desconsidera ou não a diferença entre o preço de lista e o valor unitário como desconto.

**Obs:** Caso seja feito uma alteração de valor para menor no item que possui preço de lista ou tabela de preço cadastrada, e o parâmetro **MV\_NDESCTP** estiver preenchido como **.F.**, os campos **C6\_VALDESC** e **C6\_DESCONT** serão preenchidos com a porcentagem e valor do desconto.

Para que os campos não sejam preenchidos com o valor do desconto, é necessário deixar o parâmetro como **.T.**

**Abaixo os exemplos:**

**MV\_NDESCTP = .T.**

A diferença entre o preço de lista (**C6\_PRUNIT**) e o Valor Unitário (**C6\_PRCVEN**) não será gravado como desconto no campo (**D2\_DESCON**). Exemplo:

* "Produto" - C6\_PRODUTO = Produto qualquer
* "Quantidade" - C6\_QTDVEN = 1
* "Prc Unitario" = C6\_PRCVEN = 50
* "Vlr.Total" = C6\_VALOR (Quantidade x Preço) = 50
* "Prc Lista" = C6\_PRUNIT = 100
* **"Desconto"** - D2\_DESCON = **0**

**MV\_NDESCTP = .F.**

A diferença entre o preço de lista (**C6\_PRUNIT**) e o Valor Unitário (**C6\_PRCVEN**) é gravado como desconto no campo (**D2\_DESCON**).

* "Produto" - C6\_PRODUTO = Produto qualquer
* "Quantidade" - C6\_QTDVEN = 1
* "Prc Unitario" = C6\_PRCVEN = 50
* "Vlr.Total" = C6\_VALOR (Quantidade x Preço) = 50
* "Prc Lista" = C6\_PRUNIT = 100
* **"Desconto"** - D2\_DESCON = **50**

**OBS 1:** Sempre que os campos específicos de desconto do Pedido de Vendas, como por exemplo (**C6\_DESCONT** ou **C6\_VALDESC**) possuírem conteúdo, então será inevitavelmente considerado o desconto na nota!

**OBS 2:** O parâmetro terá efeito apenas sobre a diferença que é naturalmente gerada quando o valor unitário fica inferior ao preço de lista. Não terá porém, efeito sobre descontos atribuídos no item do Pedido de Vendas.

**OBS 3:** No Pedido de Vendas continua sendo exibido o desconto, o parâmetro só impede que seja gravado o desconto no campo "**D2\_DESCON**".

**OBS 4:** O comportamento é devidamente obtido em cenário validado conforme os critérios aqui especificados. Caso não obtenha o comportamento, é necessário validar a funcionalidade com um ambiente atualizado e sem customizações.

**Saiba mais:**

[Recálculo do preço de venda no ambiente Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042778873-MP-FAT-Recalculo-do-pre%C3%A7o-de-venda-no-ambiente-de-faturamento)
