---
article_id: 360052520313
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d9eab7d37dd67ac3c0caecc1809d321154e108f8f00c7adf67965b04135b45d9
fetched_at: '2026-06-28T22:38:31.217956+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-Help: FTQTDMIN'
type: support-article
updated_at: '2025-08-08T20:16:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052520313-MP-FAT-Help-FTQTDMIN
---

**Dúvida**

Help: **FTQTDMIN** : "A quantidade digitada não pode ser menor que a quantidade de lote mínimo permitido."  
  
 **Ambiente**

Microsiga Protheus - todas as versões.  
  
**Solução**

A validação ocorre por que no campo **B1\_LOTVEN** está determinado uma quantidade a ser vendida, se ela for menor que o estipulado neste campo, gera o help: **FTQTDMIN**  
  
![](https://totvssuporte.zendesk.com/attachments/token/m2F61c6jmrK5cpWDPzHqdYDQU/?name=inline113502684.png)​  
  
Uma opção seria não determinar uma quantidade neste campo para que o help não ocorra, caso não seja possível, segue o ponto de entrada que está neste processo:  
  
**FTQTDMIN  - <https://tdn.totvs.com/display/public/PROT/FTQTDMIN+-+Verifica+quantidade+de+produto>**
