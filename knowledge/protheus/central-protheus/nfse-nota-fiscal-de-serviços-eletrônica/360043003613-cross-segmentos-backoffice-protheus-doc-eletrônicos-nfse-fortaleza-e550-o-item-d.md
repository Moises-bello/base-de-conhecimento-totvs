---
article_id: 360043003613
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1c20af7dbebee5e8cb977f4f1a53867ec522f352eb9b332ea58968c4390bc38b
fetched_at: '2026-06-28T22:39:57.453116+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Fortaleza:
  E550 - O Item da Lista Informado não está vinculado ao CNAE informado'
type: support-article
updated_at: '2025-07-18T14:36:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043003613-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Fortaleza-E550-O-Item-da-Lista-Informado-n%C3%A3o-est%C3%A1-vinculado-ao-CNAE-informado
---

**Dúvida**Como solucionar a rejeição?  
E550 - O Item da Lista Informado não está vinculado à CNAE informado.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A prefeitura de Fortaleza vincula o serviço prestado ao CNAE.  
Consulte o CNAE e Item Lista vinculado na pagina [Sefin Fortaleza.](https://issadmin.sefin.fortaleza.ce.gov.br/grpfor/pagesPublic/atividadeCPBS/consultarAtividadeCPBS.seam)

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056836894/mceclip0.png)**

O item lista deve ser informado no campo **B1\_CODISS**: 1702.  
O CNAE deve ser informado no **B1\_CNAE**: 8220200 (Com 7 dígitos).  
O CNAE completo deve ser informado no campo **B1\_TRIBMUN**: 822020001 (Com 9 dígitos).  
  
O xml será gerado com as tags conforme exemplo abaixo:

<tipos:ItemListaServico>1702</tipos:ItemListaServico>  
<tipos:CodigoCnae>8220200</tipos:CodigoCnae>  
<tipos:CodigoTributacaoMunicipio>822020001</tipos:CodigoTributacaoMunicipio>
