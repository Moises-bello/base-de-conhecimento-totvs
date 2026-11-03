---
article_id: 4409604155159
category: Faturamento - Cenários de Venda
content_hash: 50dd04f2dcdae293262850f60e749e8ff5c6b5c6546bf38f30fa3b7c01b73f93
fetched_at: '2026-06-28T22:38:34.068624+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Preço Base
  e Preço de Venda na integração da Tabela de Preços Protheus x Vtex
type: support-article
updated_at: '2021-09-28T14:25:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409604155159-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pre%C3%A7o-Base-e-Pre%C3%A7o-de-Venda-na-integra%C3%A7%C3%A3o-da-Tabela-de-Pre%C3%A7os-Protheus-x-Vtex
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como funciona a integração do Preço Base e do Preço de Venda na Tabela de Preços (OMSA010) entre o Protheus e o Vtex?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - A partir da Versão 12  
  
**Solução**A integração entre o Protheus e o Vtex permite que sejam utilizados os preços estabelecidos na Tabela de Preços (OMSA010) nas vendas do e-commerce.

O "Preço Base" (DA1\_PRCBAS) é enviado ao Vtex através da tag "**price**", ele representa o Preço de Custo do produto vendido.

Quanto ao "Preço de Venda" (DA1\_PRCVEN) é enviado ao Vtex pela tag "**minimunSalePrice**", ele representa o valor de venda do produto no e-commerce.

Além desses, caso seja especificado um desconto no campo "Vlr.Desconto" (DA1\_VLRDES), o mesmo será enviado ao Vtex pela tag "**discountFactor**", representando o valor de desconto aplicado ao "Preço Base" para gerar o "Preço de Venda".
