---
article_id: 360045088054
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 5a63b8e2acb76cec33a0eee3e45dd5e9ef20eaff0ff076ecfbc09383c660ce1d
fetched_at: '2026-06-28T22:39:57.426072+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - ERROR.LOG
  AO ACESSAR ROTINA FISA020
type: support-article
updated_at: '2025-07-08T19:44:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045088054-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-ERROR-LOG-AO-ACESSAR-ROTINA-FISA020
---

**Dúvida**Ao acessar a rotina **FISA020 - NF Digital Serviço** ocorrem alguns erros conforme exemplos abaixo:

invalid class WSWSUTIL on FISA020PRT(FISA020.PRW) 02/06/2017 09:46:05 line : 265  
ou  
invalid class WSWSENTRADA on FISA020TRS(FISA020.PRW) 02/06/2017 09:46:05 line : 558  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A rotina **FISA020 - NF Digital Serviço** foi descontinuada.  
Utilize a rotina **FISA022 - Nfs-e** para transmissão de notas para prefeitura.  
  
Veja se o município do prestador está homologado no TSS para transmissão de notas via webservice:  
- [Municipios Homologados no TSS](http://tdn.totvs.com/pages/releaseview.action?pageId=4814340)
