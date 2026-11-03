---
article_id: 1500003413302
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 4f8f1334fa6d90837bcfb40f70dea599b2582717cf474b32988ab0fa28254c9b
fetched_at: '2026-06-28T22:39:57.392317+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Element
  ''faturas'': This element is not expected. Expected is one of (pagamentos, deducoes,
  infcompl, contrucao ).'
type: support-article
updated_at: '2025-07-08T19:49:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003413302-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Element-faturas-This-element-is-not-expected-Expected-is-one-of-pagamentos-deducoes-infcompl-contrucao
---

**Dúvida**Ao transmitir um RPS ocorre o erro:  
Element 'faturas': This element is not expected. Expected is one of (pagamentos, deducoes, infcompl, contrucao ).

![ERRO_-_TSS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360102337874/ERRO_-_TSS.PNG)  
 **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Esse erro ocorre pois o rdmake NFSEXMLENV estruturou incorretamente as faturas no XML/remessa, exemplo:  
  
**Estrutura incorreta:**  
![Faturas.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360104509633/Faturas.PNG)

**Estrutura correta:**  
**![Faturas_correto.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003466122/Faturas_correto.PNG)**  
  
**A solução está disponível no rdmake NFSEXMLENV com data igual ou superior a 2020.**- [Download NFSEXMLENV](https://suporte.totvs.com/portal/p/10098/download#detail/992400)
