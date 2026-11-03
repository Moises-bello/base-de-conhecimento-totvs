---
article_id: 4405464991383
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 9592a931e3fd48badabdf92f5d87fb850d7ce22ee395680dd4a266fee10e7d48
fetched_at: '2026-06-28T22:39:36.965732+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Valor do Desconto
  esta Somando na Base do PIS, COFINS e CSLL de Retenção
type: support-article
updated_at: '2025-01-23T14:50:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405464991383-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Valor-do-Desconto-esta-Somando-na-Base-do-PIS-COFINS-e-CSLL-de-Reten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Dúvida**  
Como configurar o Protheus para na nota de saída o valor do desconto não somar na base do PIS, COFINS e CSLL de retenção?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Para o sistema não somar o valor do **desconto** na base do **PIS**, **COFINS** e **CSLL** na nota de saída é necessário configurar os parâmetros abaixo;

1. Configure no **Configurador** os **parâmetros** abaixo;

**MV\_PISBRU** = 2

**MV\_COFBRU** = 2

**MV\_CSLLBRU** = 2
