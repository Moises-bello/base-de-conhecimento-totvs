---
article_id: 11150265031703
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1c9daf403dd2d8a434963be6314216e732b1515c8e40938d42bae98235eb9fc2
fetched_at: '2026-06-28T22:38:41.143244+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help NFEMITIDA
type: support-article
updated_at: '2022-12-22T18:00:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11150265031703-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-NFEMITIDA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar estornar o documento na rotina de preparação de documento de saída apresenta o **Help NFEMITIDA**.  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**Os campos **C9\_BLEST** e **C9\_BLCRED** estão preenchidos como Faturados (10)  
  
**Solução**O help ocorre pois os campos **C9\_BLEST** e **C9\_BLCRED** estão com status faturado (10) sendo necessário excluir primeiro o Documento de Saída através da rotina de Exclusão de Documento de Saída.
