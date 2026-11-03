---
article_id: 360026791212
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 2324af517081a816db70fd3708a2b42a69b04cef6a9815aeb6a8ae5dd71356ba
fetched_at: '2026-06-28T22:39:56.445334+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - DESTAQUE
  DO IRRF NO XML DO RPS
type: support-article
updated_at: '2021-10-04T18:56:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026791212-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DESTAQUE-DO-IRRF-NO-XML-DO-RPS
---

**Dúvida**O IR está sendo destacado no XML mesmo sem gerar SE1.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Nesse caso, verifique o conteúdo do parâmetro MV\_NFSEIR.  
MV\_NFSEIR = .T. o rdmake destaca o conteúdo do D2\_VALIRRF sempre que preenchido.  
MV\_NFSEIR = .F. o rdmake destaca o conteúdo do F2\_VALIRRF, ou seja somente quando houver a retenção.  
  
**O IR será destacado no XML apenas se a retenção ocorrer pelo cliente/tomador do serviço.**  
A1\_RECIRRF=1 + ED\_RECIRRF=1 ou ED\_RECIRRF=3 + A1\_RECIRRF=1 (IR retido pelo cliente).  
A1\_RECIRRF=2 + ED\_RECIRRF=2 ou ED\_RECIRRF=3 + A1\_RECIRRF=2 (IR retido pelo emitente).
