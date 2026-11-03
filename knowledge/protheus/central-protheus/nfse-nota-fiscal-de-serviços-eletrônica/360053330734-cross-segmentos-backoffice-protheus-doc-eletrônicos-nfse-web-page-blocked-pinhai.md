---
article_id: 360053330734
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 2efd0c31d71c62fbf84d9fd51433185bc75473a66f3ccef35fe51ec33d3ee9ff
fetched_at: '2026-06-28T22:39:58.631156+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Web Page
  Blocked (Pinhais)
type: support-article
updated_at: '2021-10-04T19:17:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053330734-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Web-Page-Blocked-Pinhais
---

**Dúvida:**NFSE Pinhais APESENTANDO A MENSAGEM WEB PAGE BLOCKED

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
 **Solução**Verificar internamente a URL abaixo se tem alguma porta que está barrando, pois pode ser que precisa liberação dessa URL.

- [sync.nfs-e.net/datacenter/include/nfw/importa\_nfw/nfw\_import\_upload.php?eletron=1](http://sync.nfs-e.net/datacenter/include/nfw/importa_nfw/nfw_import_upload.php?eletron=1)

**Observação:**  
Habilitar o comando SPED\_SAVEWSDL=1 na seção da ENVIRONMENT utilizada.  
  
Assim que gerar o arquivo RCV na pasta system do TSS, verifique se apresenta a mensagem:  
  
*Web Page Blocked;*  
*Access to the web page you were trying to visit has been blocked in accordance with company policy. Please contact your system administrator if you believe this is in error.*  
*sync.nfs-e.net/datacenter/include/nfw/importa\_nfw/nfw\_import\_upload.php?eletron=1*
