---
article_id: 360056872354
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 90ac6c899f4dcbd3556ae17a4ea293b81960762b8679394d947b0018bb4b5e05
fetched_at: '2026-06-28T22:39:57.385931+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Element
  ''CidadeTomadorDescricao'': This element is not expected.'
type: support-article
updated_at: '2025-07-08T19:50:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056872354-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Element-CidadeTomadorDescricao-This-element-is-not-expected
---

**Dúvida**Ao transmitir uma nota para prefeituras que usam provedor DSFNET, ocorre a falha de schema abaixo:Element 'CidadeTomadorDescricao': This element is not expected. Expected is (CidadeTomador).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Essa falha de schema ocorre porque a tag com o código do município desse tomador não foi gerada.  
Essa orientação também soluciona a falha de schema que ocorre quando a descrição da cidade do tomador não é gerada no XML.  
Se o município trabalha com o provedor DSFNET, é esperado o código do município de acordo com o SIAFI.  
Preencha corretamente o campo A1\_CODSIAF.  
  
![](https://totvssuporte.zendesk.com/attachments/token/AuYICaupx3FDsNgY8iJG8eWvr/?name=inline-367434432.png)​  
  
Caso não localize o código na consulta padrão do campo, acesse o cadastro de municípios e preencha o CC2\_CODSIAF:  
  
![](https://totvssuporte.zendesk.com/attachments/token/vEbakqs3wOtyySdtekiTJapHE/?name=inline1831607433.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/oblUYFLK9vtHrnJ6CRgRWhFyG/?name=inline1962734133.png)​  
  
Em seguida, volte no cadastro do cliente para preenchimento do A1\_CODSIAF.  
Retransmita e monitore a nota.
