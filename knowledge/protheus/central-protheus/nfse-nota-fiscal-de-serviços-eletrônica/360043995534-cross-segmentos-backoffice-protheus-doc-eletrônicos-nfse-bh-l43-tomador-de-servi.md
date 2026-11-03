---
article_id: 360043995534
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f6198e0d56d01ea91a88340621deb8609c7170d2ff0809d09ded2630d39f67a8
fetched_at: '2026-06-28T22:39:56.325254+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - BH: L43
  - Tomador de serviço não possui inscrição municipal válida no município'
type: support-article
updated_at: '2025-07-14T21:36:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043995534-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-BH-L43-Tomador-de-servi%C3%A7o-n%C3%A3o-possui-inscri%C3%A7%C3%A3o-municipal-v%C3%A1lida-no-munic%C3%ADpio
---

**Dúvida**Como corrigir a rejeição abaixo na transmissão da NFS-e de Belo Horizonte?  
L43 - Tomador de serviço não possui inscrição municipal válida no município e não pode efetuar a retenção do ISSQN na fonte.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Essa rejeição ocorre, quando o tomador é o responsável pela retenção do ISS (A1\_RECISS ou C5\_RECISS = 1), e está estabelecido em outro município.  
Nesse caso a tributação não pode ser em BH, dessa forma o campo F4\_ISSST deve ser alterado para 2 e os campos C5\_ESTPRES e C5\_MUNPRES devem ficar em branco.
