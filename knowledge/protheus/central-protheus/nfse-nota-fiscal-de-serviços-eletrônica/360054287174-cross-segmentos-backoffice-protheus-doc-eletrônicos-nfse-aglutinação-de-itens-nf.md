---
article_id: 360054287174
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f203395d5d106b074f104583c92c11f8032d505fb5f0ab0bb5e082d3ce198fa5
fetched_at: '2026-06-28T22:39:56.279058+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - AGLUTINAÇÃO
  DE ITENS NFSE
type: support-article
updated_at: '2025-07-14T21:40:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054287174-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-AGLUTINA%C3%87%C3%83O-DE-ITENS-NFSE
---

**Dúvida**Como realizar a aglutinação de itens para prefeituras que permitem apenas um único item por nota?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para realizar a aglutinação dos itens, todos eles devem possuir as mesmas características abaixo:- Todos os itens devem ter a mesma alíquota de ISS (B1\_ALIQISS ou BZ\_ALIQISS).  
- Todos os itens devem ter o mesmo código de ISS (B1\_CODISS ou BZ\_CODISS).  
- Todos os itens devem ter o mesmo código de Tributação municipal (B1\_TRIBMUN ou BZ\_TRIBMUN).  
  
*Obs.: Os campos 'BZ' são da tabela SBZ, apenas quando utilizado o [Indicador de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026420011-MP-NFSE-Indicador-de-Produto).*  
  
Além disso o parâmetro **MV\_ITEMAGL** deverá estar = **S  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091711494/mceclip0.png)**
