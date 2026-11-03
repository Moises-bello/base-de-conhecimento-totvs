---
article_id: 37785634413463
category: Financeiro - Contas a Receber
content_hash: 17d0e31e3885bbed5408da94b6754e621df9b3270269e863183476dcc35fc4e3
fetched_at: '2026-06-28T22:38:12.464362+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA070 -  Quando é gerado o campo
  E1_DESCONT?
type: support-article
updated_at: '2026-01-19T20:23:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37785634413463-Cross-Segmento-Backoffice-Linha-Protheus-FINA070-Quando-%C3%A9-gerado-o-campo-E1-DESCONT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37785634402071) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
 Dúvida: campos E1\_DESCONT e E5\_VLDESCO quando são alimentados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA070 - Todas as versões.  
  
**Solução**  
O campo **E1\_DESCONT** é utilizado pelo sistema como um **campo de validação interna**. O preenchimento desse campo ocorre exclusivamente no momento da **baixa do registro**.

Como parte desse processo, o sistema também alimenta o campo **E5\_VLDESCO**, que corresponde ao valor do desconto efetivamente aplicado ao título no momento da baixa ou do preenchimento do campo E1\_DESCFIN incluído no título.
