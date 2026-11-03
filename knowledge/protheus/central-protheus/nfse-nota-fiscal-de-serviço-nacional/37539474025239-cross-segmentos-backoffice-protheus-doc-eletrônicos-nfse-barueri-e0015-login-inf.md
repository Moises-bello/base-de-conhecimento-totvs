---
article_id: 37539474025239
category: NFSE - Nota Fiscal de Serviço Nacional
content_hash: 59192a5338a6c15a65cbce0bebf58228342caaa66ef8f29ca12e0b6dce7cae6a
fetched_at: '2026-06-28T22:39:54.403849+00:00'
product: protheus
section_id: 33955617231639
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE Barueri -
  E0015 - Login informado não tem permissão de acesso a inscrição do CPF/CNPJ do prestador
  - CNPJ informado: 00000000000000'
type: support-article
updated_at: '2026-01-08T19:07:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37539474025239-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Barueri-E0015-Login-informado-n%C3%A3o-tem-permiss%C3%A3o-de-acesso-a-inscri%C3%A7%C3%A3o-do-CPF-CNPJ-do-prestador-CNPJ-informado-00000000000000
---

**Ocorrência**  
Ao realizar a transmissão de um RPS, ocorre a rejeição **"E0015 - Login informado não tem permissão de acesso a inscrição do CPF/CNPJ do prestador - CNPJ informado: 00000000000000".**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Causa**  
Para correção, deverá acessar o Wizard.cfg e preencher o campo CNPJ com o **mesmo que está vinculado ao certificado digital utilizado** e importado na rotina:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37539453951639)

Após isso, basta retransmitir ou gerar uma nova nota.
