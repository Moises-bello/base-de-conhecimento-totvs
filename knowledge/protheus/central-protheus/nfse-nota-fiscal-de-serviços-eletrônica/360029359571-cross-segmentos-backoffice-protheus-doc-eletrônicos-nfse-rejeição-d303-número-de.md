---
article_id: 360029359571
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: fb1829e3ebb676e26a8e736f6f2fc686080b811a7d42c742fecba3afe1f8519c
fetched_at: '2026-06-28T22:39:58.445473+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  D303: Número de rps não está na faixa de números autorizados.'
type: support-article
updated_at: '2021-10-06T18:11:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029359571-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-D303-N%C3%BAmero-de-rps-n%C3%A3o-est%C3%A1-na-faixa-de-n%C3%BAmeros-autorizados
---

**Dúvida** Na transmissão de rps/nfse, como corrigir a rejeição D303: Número de rps não está na faixa de números autorizados?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**

Esta rejeição, geralmente, é retornada pela prefeitura quando está utilizando um rps fora do range liberado por ela.  
Por exemplo: Foi liberado para uso na prefeitura o range de notas do número 1 até 5000, e está sendo transmitido o rps 6000.

Acesse o site da respectiva prefeitura com os dados de usuário e senha, e verifique o range liberado. Esta informação deve estar na parte dos dados cadastrais da empresa.
