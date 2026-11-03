---
article_id: 360048041013
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 6dfa1cc046e0ae80e19fc89b48442356bb197cf52fd7fad9f408cf761754f715
fetched_at: '2026-06-28T22:39:58.596659+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: TAG
  <IssRetido> (Linhares/ES)'
type: support-article
updated_at: '2021-10-06T19:11:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048041013-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-TAG-IssRetido-Linhares-ES
---

**Dúvida**Porque o TSS está invertendo o conteúdo da tag <IssRetido>?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**A prefeitura de Linhares/ES possui uma particularidade, onde no caso o conteúdo da tag <IssRetido> é ao contrário da maioria das prefeituras.  
  
Abaixo o padrão de Linhares:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069292814/mceclip1.png)  
  
Portanto, caso verifique que o XML exportado ou o campo XML\_ERP (convertido pelo TSS) da SPED051 estejam com o conteúdo contrário ao informado no Protheus (A1\_RECISS e C5\_RECISS), fique ciente que é justamente para se enquadrar nessa particularidade e alinhar o que foi informado no Protheus com o que será apresentado na nota impressa.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070357493/mceclip2.png)  
  
Para detalhes do Manual de Integração da Prefeitura [clique aqui.](http://notafiscal.linhares.es.gov.br/el-nfse/paginas/sistema/login.jsf)
