---
article_id: 360045564933
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 017c361d173f0543b89caff4e7e37e9cf62e1e2e63e130f4ce37800a4d6afacc
fetched_at: '2026-06-28T22:39:56.260189+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - 0000 Parâmetro
  Authorization fora do formato especificado (Inscrição Municipal-TOKEN) - Provedor
  GIAP
type: support-article
updated_at: '2025-06-02T12:16:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045564933-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-0000-Par%C3%A2metro-Authorization-fora-do-formato-especificado-Inscri%C3%A7%C3%A3o-Municipal-TOKEN-Provedor-GIAP
---

**Ocorrência**Ao realizar a transmissão para uma prefeitura do provedor GIAP ocorre a rejeição abaixo:  
  
*0000 - Parâmetro Authorization fora do formato especificado (Inscrição Municipal-TOKEN) exemplo: 123456-AGHJOPBEFFRE3Z4VIRZKZKIIY9ILLOOP. Qualquer duvida consulte o manual no site: https://nfseembudasartes.urbion.com.br/apex/embu01/f?p=935 Start tag expected, '<' not found***Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre quando está sendo utilizado um **TOKEN inválido ou expirado** pela prefeitura.  
Geralmente quando era utilizado um token X, porém algum usuário solicitou que fosse gerado um novo token, no caso, invalidando o antigo.  
  
**Solução**Nesse caso deverá utilizar o último TOKEN gerado através do portal da prefeitura e refazer o Wizard.cfg por completo informando esse código no campo específico.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9201284770967/mceclip0.png)
