---
article_id: 360026448171
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: b7cf9afcfb459ce7e85f625cbd9530603758f91b770c6222492253d28ec8fb2a
fetched_at: '2026-06-28T22:39:58.609792+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: XML_ERP
  e XML_TSS da SPED051'
type: support-article
updated_at: '2021-10-06T19:07:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026448171-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-XML-ERP-e-XML-TSS-da-SPED051
---

**Dúvida**Qual a diferença entre o XML\_ERP e XML\_TSS da tabela SPED051?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O XML\_TSS possui um XML gerado pelo rdmake, com um modelo único contemplando o máximo de informações (da nota) coletadas do ERP.   
O TSS utiliza o conteúdo do XML\_TSS para converter para o layout da prefeitura, e esse xml já convertido é gravado no XML\_ERP.
