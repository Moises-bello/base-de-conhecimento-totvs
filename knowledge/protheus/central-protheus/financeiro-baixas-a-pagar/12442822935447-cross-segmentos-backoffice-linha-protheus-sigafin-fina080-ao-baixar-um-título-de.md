---
article_id: 12442822935447
category: Financeiro - Baixas a Pagar
content_hash: a8fcb63d8a166241e842e7bb63249c90055ff912c9f7e10ade452b0d04bfe99b
fetched_at: '2026-06-28T22:37:24.881590+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 - Ao baixar
  um título de imposto no Financeiro não gera a tabela FKY
type: support-article
updated_at: '2026-03-25T20:24:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12442822935447-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Ao-baixar-um-t%C3%ADtulo-de-imposto-no-Financeiro-n%C3%A3o-gera-a-tabela-FKY
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39295443595927) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Ao baixar um título de imposto no Financeiro, não gera a tabela FKY?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Quando o sistema está configurado para reter os impostos de **PIS**/**COFINS**/**CSLL**/**IRRF** na emissão da nota fiscal ou inclusão de títulos avulsos (EX: inclusão manual), os dados que serão levados para **EFD**-**REINF** serão os gravados na tabela **FKW**; com isso, não é gerada a tabela **FKY** ao baixar um título.  
  
**Saiba mais**  
[Gravação dos Impostos x Natureza de rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=728637277)
