---
article_id: 1500001948841
category: SIGAEST - CÁLCULOS
content_hash: 633e0d5e9540501ccfbdd1971cd06537d4d630e37509dcfe365c871758c0584e
fetched_at: '2026-06-28T22:39:04.162952+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATC010 - Como é calculado
  o índice de Perda na Formação de Preços?
type: support-article
updated_at: '2025-03-12T12:26:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001948841-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATC010-Como-%C3%A9-calculado-o-%C3%ADndice-de-Perda-na-Forma%C3%A7%C3%A3o-de-Pre%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503304156567) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**A rotina de Formação de Preço não está respeitando o percentual de perca informado na estrutura do produto. Como ajustar este problema?  
  
**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17  
  
**Solução**

Neste artigo mostraremos como é feito o cálculo para um exemplo prático de como é feito índice com perda 

**Equação:**

QuantItem := ((nQuant \* nG1Quant) / (100 - nQtdPerda)) \* 100

**Exemplo:**

(( 1 \* 10) / (100 - 50)) \* 100  
(10 / 50) \* 100  
0,2 \* 100 = 20

**Onde**:

**nQuant:= Quantidade Produzida**  
**nG1Quant:= Quantidade necessária para produção**  
**nQtdPerda:= Quantidade da perda**  
**QuantItem:= Resultado Final**

**Na prática:**

**Inserindo os parâmetros:**

![](https://totvssuporte.zendesk.com/attachments/token/XBy7ZknH1LOgiyDvI3La2O3ph/?name=inline-1281596781.png)

**Dados na prática:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102936313)

**Resultado:**

![](https://totvssuporte.zendesk.com/attachments/token/VTh6W20FP68fwgV9QyqWh0vxg/?name=inline-252879457.png)

**Saiba mais:**

*[MP - SIGAEST - Rotina Formação de Preço (MATC010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022184251)*

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199493-SIGAEST-C%C3%81LCULOS)*
