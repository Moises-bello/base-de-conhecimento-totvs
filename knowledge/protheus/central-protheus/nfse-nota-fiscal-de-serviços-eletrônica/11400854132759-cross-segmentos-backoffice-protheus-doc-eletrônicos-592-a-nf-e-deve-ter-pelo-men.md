---
article_id: 11400854132759
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: bda6879637d78e6c11f42eada800c8e5d037908b90e5b9f4b12d15ae3deb8131
fetched_at: '2026-06-28T22:39:56.227076+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 592 - A NF-e deve
  ter pelo menos um item de produto sujeito ao ICMS (Brasília)
type: support-article
updated_at: '2023-01-03T14:47:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11400854132759-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-592-A-NF-e-deve-ter-pelo-menos-um-item-de-produto-sujeito-ao-ICMS-Bras%C3%ADlia
---

**Ocorrência**Ao realizar a transmissão ocorre a rejeição: 592 - A NF-e deve ter pelo menos um item de produto sujeito ao ICMS.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11400934240919)  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição ocorre pelo fato de Brasília ter sofrido alterações, onde notas que possuem somente itens de serviço devem ser obrigatoriamente transmitidas via provedor IssNetOnline ao invés da Sefaz.  
  
**Solução**Para correção as notas deverão ser transmitidas de acordo com a necessidade:  
  
**NFS-e (contendo apenas itens de serviço): Através da rotina FISA022.**  
NF-e (contendo apenas itens de produto): Através da rotina SPEDNFE.  
Nota Conjugada (contendo itens de serviço e produto): Através da rotina SPEDNFE.  
  
Dúvidas nessas alterações que houveram recentemente? Clique abaixo:  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE BRASÍLIA/DF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053669914-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-BRAS%C3%8DLIA-DF)
