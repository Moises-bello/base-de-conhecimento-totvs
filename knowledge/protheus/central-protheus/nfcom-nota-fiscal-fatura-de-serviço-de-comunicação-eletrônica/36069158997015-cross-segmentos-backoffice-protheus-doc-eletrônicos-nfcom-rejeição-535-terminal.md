---
article_id: 36069158997015
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: f587ff627c09444b4cef869efaa726f0470c7997151cb86f75ec53c98a82a11b
fetched_at: '2026-06-28T22:39:55.189731+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Rejeição
  535 (Terminal principal em UF diferente da UF de autorização da NFCom)
type: support-article
updated_at: '2025-11-03T17:06:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36069158997015-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Rejei%C3%A7%C3%A3o-535-Terminal-principal-em-UF-diferente-da-UF-de-autoriza%C3%A7%C3%A3o-da-NFCom
---

**Ocorrência**  
Ao realizar a transmissão de uma NFCOM ocorre a rejeição **535 - Terminal principal em UF diferente da UF de autorização da NFCom.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Se informado terminal principal (tag: NroTermPrinc) a UF do terminal (tag: cUFPrinc) deve ser a mesma UF de autorização da NFCom.  
Portanto, para correção, o campo **FX\_AREATER**no Complemento Fiscal deverá possuir a **mesma UF emissora da nota.**
