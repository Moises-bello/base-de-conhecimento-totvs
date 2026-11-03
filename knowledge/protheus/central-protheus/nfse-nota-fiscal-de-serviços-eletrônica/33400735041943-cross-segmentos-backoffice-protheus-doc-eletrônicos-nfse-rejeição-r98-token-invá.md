---
article_id: 33400735041943
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: dead7f6baaa1a7617bbeebae7f3ab05304eb50c73c761933724e52db60673c9a
fetched_at: '2026-06-28T22:39:58.476471+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Rejeição
  R98: Token Inválido (Santana de Parnaíba)'
type: support-article
updated_at: '2025-07-11T14:12:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33400735041943-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Rejei%C3%A7%C3%A3o-R98-Token-Inv%C3%A1lido-Santana-de-Parna%C3%ADba
---

**Ocorrência**  
Ao realizar a transmissão de um RPS para a prefeitura de Santana de Parnaíba, ocorre a rejeição '**R98 - Token Inválido'.** Como corrigi-la?  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33400747575063)  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Causa**  
Isso ocorre pela ausência das tags <ws:token\_nick> e ws:token\_pass> no xml ou estarem incorretas/desatualizadas.  
  
Para correção, deverá se certificar de estar usando as informações válidas de token\_nick e token\_pass, que devem ser extraídas diretamente pelo portal da prefeitura: <http://nf-eletronica.com.br/info_contrib/index.asp>.  
  
Uma vez acessado, deverá ir até o menu 'Web Service -> Gerar Token':  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33400735023383)  
  
Onde serão apresentadas as credenciais abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33400747578903)  
  
Com essas informações em mãos, basta preenche-las no Wizard.cfg da rotina FISA022.  
Onde, campos Usuário deverá receber o conteúdo do token\_nick e o campo Senha o conteúdo do token\_pass:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33400735025815)  
  
Após isso, basta retransmitir a nota.
