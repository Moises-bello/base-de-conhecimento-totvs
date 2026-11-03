---
article_id: 360045027334
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 81183cc7bd6ca7834e673d5dbcb563ebe1179a1fb64ddc472816915cbcecd984
fetched_at: '2026-06-28T22:39:56.257894+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - 0000 Erro:Não
  há um número do Token informado (Provedor GIAP)
type: support-article
updated_at: '2026-01-26T20:05:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045027334-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-0000-Erro-N%C3%A3o-h%C3%A1-um-n%C3%BAmero-do-Token-informado-Provedor-GIAP
---

**Ocorrência**  
Ao realizar a transmissão para prefeituras do provedor GIAP ocorre a rejeição abaixo:  
  
***0000 - Erro:Não há um número do Token informado. Start tag expected, '<' not found***  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**  
Essa rejeição ocorre quando não está sendo informado um **TOKEN** válido dentro do Wizard.cfg, o qual é disponibilizado pela própria pela prefeitura.  
  
**Solução**  
Nesse caso deverá utilizar o último TOKEN gerado através do portal da prefeitura e refazer o Wizard.cfg por completo, informando esse código no campo específico.
