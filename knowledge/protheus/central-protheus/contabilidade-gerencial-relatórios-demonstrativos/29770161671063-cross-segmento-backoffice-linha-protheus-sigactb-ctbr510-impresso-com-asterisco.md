---
article_id: 29770161671063
category: Contabilidade Gerencial - Relatórios Demonstrativos
content_hash: 18fd7f801fe974dd9afd9800ebd7829a5e496cdfadb04f42550b13213b4c5904
fetched_at: '2026-06-28T22:40:38.876729+00:00'
product: protheus
section_id: 1500001548882
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR510 IMPRESSO COM
  ASTERISCO
type: support-article
updated_at: '2025-02-06T12:24:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29770161671063-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR510-IMPRESSO-COM-ASTERISCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29770161645335) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**

Relatório DRE CTBR510 está sendo impresso com ASTERISCO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29770161645975)  
**Ambiente:**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – a partir da versão 12.  
  
**Causa:**

O cenário ocorre ao imprimir com o parâmetro [MV\_TPVALOR = P](https://tdn.totvs.com/pages/releaseview.action?pageId=146966519)   
  
**Solução:**

Através da Issue (DSERCTR1-38411), foi informado que para utilizar o parâmetro **MV\_TPVALOR = P** sem que o asterisco seja exibido, é necessário ativar a opção[**Divide Por ?**](https://tdn.totvs.com/pages/releaseview.action?pageId=519201889)**.**
