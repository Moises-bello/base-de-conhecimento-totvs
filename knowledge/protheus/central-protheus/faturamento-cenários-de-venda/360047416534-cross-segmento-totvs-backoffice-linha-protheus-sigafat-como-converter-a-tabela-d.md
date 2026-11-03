---
article_id: 360047416534
category: Faturamento - Cenários de Venda
content_hash: 0046e49c314424b69ffc47e5742805d273c91d5527a562a7b46e4d82f65e92be
fetched_at: '2026-06-28T22:38:34.080221+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como converter
  a tabela de preço para outra moeda
type: support-article
updated_at: '2023-01-31T13:11:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047416534-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-converter-a-tabela-de-pre%C3%A7o-para-outra-moeda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como converter a tabela de preço para outra moeda?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento – A partir da versão 11.80.  
  
**Solução**1° Na tabela de preço (OMSA010)  deve conter a moeda que deseja realizar a conversão (campo DA1\_MOEDA);

2° Na tabela de preço deve conter o Preço de venda do produto (DA1\_PRCVEN);

3° O parâmetro MV\_MPRCBAS  deve estar configurado como 1. Deste modo o sistema realiza a conversão do valor da tabela;

4°  O pedido de venda deve estar na mesma moeda que deseja converter, exemplo: A Moeda 2 dólar deve estar na tabela de preço DA1\_MOEDA e no pedido de venda C5\_MOEDA;

5° Deve informar a taxa da moeda do dia através da rotina MATA090 (moedas);

6° Ao vincular a tabela de preço no pedido de venda e informar o produto o sistema converte o preço unitário na moeda que deseja.
