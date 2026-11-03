---
article_id: 360028184151
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 53efbd1a57d5c232fd6fde531da9eb256840000185db8556bb0b28c5af7dcc0b
fetched_at: '2026-06-28T22:36:39.120952+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Campo: EEC_DTDUE
  e EEC_NRODUE bloqueados para edição'
type: support-article
updated_at: '2025-04-08T19:12:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028184151-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Campo-EEC-DTDUE-e-EEC-NRODUE-bloqueados-para-edi%C3%A7%C3%A3o
---

**Ocorrência**Campos: EEC\_DTDUE e EEC\_NRODUE bloqueados para edição  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
  
**Causa**Esse incidente ocorre devido o parâmetro **MV\_EEC0053** estar habilitado.   
  
**Solução**Para permitir edição dos campos, realize a configuração abaixo:  
- No Configurador (SIGACFG), o parâmetro **MV\_EEC0053** deve estar com o conteúdo .F.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028062252)

**Saiba mais:**[Declaração Única de Exportação (DUE) no SIGAEEC](https://tdn.totvs.com/pages/releaseview.action?pageId=274854794)
