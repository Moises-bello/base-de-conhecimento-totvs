---
article_id: 360043360893
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: d95223f909fc6893111457a6653fbb090e951aa07aeb6d4721722183f8424387
fetched_at: '2026-06-28T22:36:39.198557+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Motivo de baixa
  MV_EEC0032
type: support-article
updated_at: '2021-08-18T17:17:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043360893-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Motivo-de-baixa-MV-EEC0032
---

**Dúvida**Como configurar o motivo de baixa do título NF originado da nota fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Verifique o parâmetro MV\_EEC0032 e defina um motivo de baixa cadastrado.   
O título gerado pela NF de saída é baixado ao preencher a data de embarque na rotina EECAE100, o motivo de baixa deste titulo pode ser informado no parâmetro MV\_EEC0032, o mesmo será enviado na TAG <AUTMOTBX> do xml AVLINK006.  
  
Obs.: O titulo gerado pela NF de saída é considerado um titulo Provisório.

**Saiba mais:**

[Criação do Parâmetro MV\_EEC0032 - TIESDM](https://tdn.totvs.com/pages/releaseview.action?pageId=108660654)
