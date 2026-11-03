---
article_id: 37734733141015
category: Rental by ItUp Business
content_hash: 7c45bedb2c273343d154d32c5e7993015bf6fb0aef01ec6239beda5651e8fcdb
fetched_at: '2026-06-28T22:36:20.617565+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Erro de Moeda Inválida (C5_MOEDA)
  no Faturamento Automático (SIGALOC).
type: support-article
updated_at: '2026-01-16T20:04:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37734733141015-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Erro-de-Moeda-Inv%C3%A1lida-C5-MOEDA-no-Faturamento-Autom%C3%A1tico-SIGALOC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37734733107991) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao processar a Fatura Automática, o sistema interrompe o fluxo apresentando erro de validação no campo Moeda (C5\_MOEDA).  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Causa**  
O incidente ocorre devido ao preenchimento incorreto do campo **Moeda - FP0\_MOEDA** com o valor **"0"**. Por padrão, o sistema exige que este campo esteja definido como **"1"** para validar o faturamento corretamente.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a rotina **Orçamento (LOCA001)**;
2. Localize o projeto desejado e selecione **Outras Ações > Alterar**;
3. No campo **Moeda (FP0\_MOEDA)**, altere o valor para **1**;
4. Salve as alterações e processe o faturamento novamente.
