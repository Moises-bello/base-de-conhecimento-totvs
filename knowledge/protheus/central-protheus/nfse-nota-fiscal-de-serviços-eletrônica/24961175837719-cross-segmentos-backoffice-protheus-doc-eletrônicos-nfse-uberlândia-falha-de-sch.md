---
article_id: 24961175837719
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3a414f7352a75ad889382e2346e2bc4924aa42281e78de6fcc3df5f77e14f54d
fetched_at: '2026-06-28T22:39:58.674713+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE Uberlândia
  - Falha de schema: Expected is ( {http://www.abrasf.org.br/nfse.xsd}Competencia
  )'
type: support-article
updated_at: '2025-05-27T12:51:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24961175837719-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Uberl%C3%A2ndia-Falha-de-schema-Expected-is-http-www-abrasf-org-br-nfse-xsd-Competencia
---

**Ocorrência**  
Ao realizar a transmissão de um RPS para Uberlândia, ocorre a falha de schema abaixo:  
  
***Element '{http://www.abrasf.org.br/nfse.xsd}Servico': This element is not expected. Expected is ( {http://www.abrasf.org.br/nfse.xsd}Competencia ).***  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Causa**Essa falha de schema ocorre por conta da falta de uma tag obrigatória pela prefeitura: **Competência:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24961161425687)**  
  
**Solução**Para correção, deverá ser configurado o parâmetro MV\_NFSECOM e informar a data de competência.  
Lembrando que há uma particularidade para essa prefeitura, [essa data obrigatoriamente deverá ser o primeiro dia do mês.](https://tdn.totvs.com/pages/releaseview.action?pageId=853925741)  
  
Segue documentação de como configurar o parâmetro MV\_NFSECOM:  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Data de Competência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026235551-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Data-de-Compet%C3%AAncia?source=search)  
  
**Importante:** Via Módulo de Faturamento, obrigatoriamente o parâmetro MV\_INTTMS deve estar como F, caso contrário o campo não será acatado e será utilizado como base a data atual do Protheus.
