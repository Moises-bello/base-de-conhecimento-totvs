---
article_id: 360039130653
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 199f00be54ea3cdb98ef2871d812b116a389642d0946a7827dfbc2be2a63bc41
fetched_at: '2026-06-28T22:39:44.291452+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC -  Data de compensação
  adiantamento com invoice (e2_baixa)
type: support-article
updated_at: '2021-08-09T13:37:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039130653-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Data-de-compensa%C3%A7%C3%A3o-adiantamento-com-invoice-e2-baixa
---

**Dúvida**Qual data é preenchida (E2\_BAIXA) ao realizar a compensação do PA com o título INV?  
   
 **Ambiente**Protheus – Easy Import Control – A partir da versão 11.80  
  
**Solução**A gravação do campo E2\_BAIXA é definido através do parâmetro MV\_EIC0040. Quando o parâmetro estiver .T., irá levar a data base para baixa do título, caso esteja .F. será enviado a data de emissão da invoice.
