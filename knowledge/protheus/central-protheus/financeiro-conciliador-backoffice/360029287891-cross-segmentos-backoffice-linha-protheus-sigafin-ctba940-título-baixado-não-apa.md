---
article_id: 360029287891
category: Financeiro - Conciliador Backoffice
content_hash: c8e0be1fa28c61f200edd899cba0a77088d7d1524b0a42af0d1eca33d9e553b0
fetched_at: '2026-06-28T22:37:47.229849+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Título baixado
  não aparece para realizar a conciliação
type: support-article
updated_at: '2025-03-19T19:16:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029287891-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-T%C3%ADtulo-baixado-n%C3%A3o-aparece-para-realizar-a-concilia%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24337920869783)**Tempo aproximado para leitura: **00:05 min  
  
Dúvida**Título baixado não aparece para realizar a conciliação. O que fazer?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - CTBA940 - a partir 12.1.33  
  
**Solução**

Na conciliação bancária, são conciliados os movimentos provenientes da tabela SE5, que **geram movimentação bancária**. Para tanto, é necessário validar o campo **E5\_TIPODOC** a fim de identificar o tipo de movimento e verificar se há movimentação associada.

Os registros que apresentarem o campo **E5\_TIPODOC** sem movimentação bancária não serão incluídos na conciliação.

A documentação a seguir detalha os tipos de movimentos que geram ou não movimentação bancária.

[Tipo de movimentos bancários](http://tdn.totvs.com/pages/releaseview.action?pageId=207357394)

**Saiba mais**[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliador Backoffice Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23945644752279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conciliador-Backoffice-Financeiro)
