---
article_id: 360026235551
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 43de53f6dd85f649ca7dd6a310ad986256bdbe4c8a8d803385f96fbc2a331f6d
fetched_at: '2026-06-28T22:39:56.431925+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Data de Competência
type: support-article
updated_at: '2025-05-27T12:57:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026235551-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Data-de-Compet%C3%AAncia
---

**Dúvida**Qual o procedimento para informar a Data de Competência no XML do RPS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões.  
  
**Solução**Crie um campo na tabela SC5 com o formato de data, esse campo será para informar a data de competência da NFS-e.  
Informe o nome desse campo dentro do parâmetro MV\_NFSECOM, que deverá ser criado como caractere.  
  
**Importante:**- O destaque da data de competência, ocorrerá apenas no XML das prefeituras que possuem essa informação no layout webservice;  
- Via Módulo de Faturamento, obrigatoriamente o parâmetro MV\_INTTMS deve estar como F, caso contrário o campo não será acatado e será utilizado como base a data atual do Protheus.
