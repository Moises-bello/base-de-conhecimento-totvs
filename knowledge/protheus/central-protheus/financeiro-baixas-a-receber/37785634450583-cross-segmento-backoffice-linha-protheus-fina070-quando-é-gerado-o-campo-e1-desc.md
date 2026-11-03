---
article_id: 37785634450583
category: Financeiro - Baixas a Receber
content_hash: 62c36dbbe1e7ed06a2f0da3284e2a817c948b2a2060c6f97ecb93a176551e71e
fetched_at: '2026-06-28T22:37:43.673263+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA070 -  Quando é gerado o campo
  E1_DESCONT?
type: support-article
updated_at: '2026-01-19T20:23:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37785634450583-Cross-Segmento-Backoffice-Linha-Protheus-FINA070-Quando-%C3%A9-gerado-o-campo-E1-DESCONT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37785634443159) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
 Dúvida: campos E1\_DESCONT e E5\_VLDESCO quando são alimentados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA070 - Todas as versões.  
  
**Solução**  
O campo **E1\_DESCONT** é utilizado pelo sistema como um **campo de validação interna**. O preenchimento desse campo ocorre exclusivamente no momento da **baixa do registro**.

Como parte desse processo, o sistema também alimenta o campo **E5\_VLDESCO**, que corresponde ao valor do desconto efetivamente aplicado ao título no momento da baixa ou do preenchimento do campo E1\_DESCFIN incluído no título.
