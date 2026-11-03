---
article_id: 115010342108
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: fed6d50abdf0309c274ddd324722caffa25b977131ee840189bebea6ca5f6187
fetched_at: '2026-06-28T22:39:45.315472+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Tipo de conhecimento
  de transporte no siscomex web
type: support-article
updated_at: '2022-06-02T13:52:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010342108-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Tipo-de-conhecimento-de-transporte-no-siscomex-web
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Quais os tipos de conhecimento de transporte para envio de declaração de importação no siscomex *web*?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões  
  
**Solução**

Para o envio de declaração de importação, junto ao siscomex *web*, é necessário definir o código do tipo de conhecimento (W6\_TPCONHEC) onde depende do tipo da Via de Transporte.   
Os códigos são:

Quando via de transporte for **marítima/fluvial/lacustre**:

**10** - BL(*bill of lading*)

**12** - HBL(*house bill of lading*)

Quando via de transporte for **aérea**:

**01** - AWB (*airway bill*)

**03** - HAWB(*house airway bill*)

**14** - DSIC (documento subsidiário)

Quando via de transporte for **rodoviária**:

**13** - CRT

Quando via de transporte for **ferroviária**:

**17** - RWB(*railway bill*)

**18** - HRWB(*house railway bill*)

**19** - TIF/DTA
