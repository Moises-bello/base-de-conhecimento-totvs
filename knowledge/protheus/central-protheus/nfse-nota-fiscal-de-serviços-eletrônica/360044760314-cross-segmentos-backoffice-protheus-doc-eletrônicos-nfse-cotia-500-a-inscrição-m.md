---
article_id: 360044760314
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6bd39ad5ba861a82aefb76ba6165ad98adb7f60f588a73a57e919bf4d36c0515
fetched_at: '2026-06-28T22:39:56.409352+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - COTIA: 500
  - A Inscrição Municipal do Prestador informado no xml, não corresponde a Inscrição
  municipal logada.'
type: support-article
updated_at: '2025-07-14T21:11:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044760314-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-COTIA-500-A-Inscri%C3%A7%C3%A3o-Municipal-do-Prestador-informado-no-xml-n%C3%A3o-corresponde-a-Inscri%C3%A7%C3%A3o-municipal-logada
---

**Dúvida**Qual a tratativa para a rejeição abaixo?  
500 - A Inscrição Municipal do Prestador informado no xml, não corresponde a Inscrição municipal logada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A prefeitura de Cotia-SP exige algumas informações para autentificação junto ao webservice.  
Essa informações são preenchidas no wizard.config da rotina FISA022.  
O campo Usuário deve ser preenchido com a I.M do prestador, a mesma do cadastro da filial que é destacada no XML.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061481514/mceclip0.png)

Obs.: Vale lembrar que essa Inscrição Municipal (campo Usuário) precisa ser a mesma que foi previamente habilitada para transmissões via Web Services pela prefeitura.
