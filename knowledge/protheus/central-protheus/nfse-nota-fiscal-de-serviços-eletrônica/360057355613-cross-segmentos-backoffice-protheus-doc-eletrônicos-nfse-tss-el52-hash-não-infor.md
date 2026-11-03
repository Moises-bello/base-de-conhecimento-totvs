---
article_id: 360057355613
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 2f7fc54304898422cf55c38f98b322569502ad3f882f4f72693928ca6ad13079
fetched_at: '2026-06-28T22:39:58.572547+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: EL52
  - HASH NÃO INFORMADO - INFORME O HASH DE AUTENTIFICACAO DO PRESTADOR (Simões Filho/BA)'
type: support-article
updated_at: '2025-06-04T14:55:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057355613-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-EL52-HASH-N%C3%83O-INFORMADO-INFORME-O-HASH-DE-AUTENTIFICACAO-DO-PRESTADOR-Sim%C3%B5es-Filho-BA
---

**Ocorrência**Como corrigir a rejeição "EL52 - HASH NÃO INFORMADO - INFORME O HASH DE AUTENTIFICACAO DO PRESTADOR"?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre quando o emissor não está informando na transmissão as credenciais (Usuário e Senha) Web Services exigidas pela prefeitura.  
  
**Solução**Para correção deverá dentro do Wizard.cfg na rotina **FISA022** informar ambos os campos destacados abaixo.  
Vale lembrar que é de total responsabilidade da prefeitura fornecer esses dados.  
Não necessariamente são os mesmos dados para os ambientes de Produção e Homologação, o que precisa ser também verificado junto a prefeitura.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096119993/mceclip0.png)
