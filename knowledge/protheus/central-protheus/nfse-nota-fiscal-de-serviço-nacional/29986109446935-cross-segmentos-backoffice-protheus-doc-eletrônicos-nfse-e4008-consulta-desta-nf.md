---
article_id: 29986109446935
category: NFSE - Nota Fiscal de Serviço Nacional
content_hash: 864ea383251981f3a75e9175aa8b0c271bb447d1121e2628e82dc6293b3b604e
fetched_at: '2026-06-28T22:39:54.390132+00:00'
product: protheus
section_id: 33955617231639
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E4008 - Consulta
  desta NFS-e não é permitida para este usuário.
type: support-article
updated_at: '2025-09-15T17:27:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29986109446935-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E4008-Consulta-desta-NFS-e-n%C3%A3o-%C3%A9-permitida-para-este-usu%C3%A1rio
---

**Dúvida**Ao consultar a chave da NFSE Nacional no documento de entrada ocorre o retorno:  
E4008 - Consulta desta NFS-e não é permitida para **este usuário**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Esse erro ocorre quando a chave consultada não pertence a empresa.  
Neste caso a mensagem vinda do ambiente Nacional é especifica avisando que não é permitida a consulta para esse CNPJ, **pois a nota pertencer a outro CNPJ tomador do serviço**.
