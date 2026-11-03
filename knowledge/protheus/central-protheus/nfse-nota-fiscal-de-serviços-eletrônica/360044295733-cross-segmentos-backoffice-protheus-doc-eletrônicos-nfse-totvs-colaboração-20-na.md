---
article_id: 360044295733
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 44c137d4f0d3a32ac6af84bbf8f0376204f3399f124d0e3461fc29242cb7cc37
fetched_at: '2026-06-28T22:39:58.541376+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - TOTVS COLABORAÇÃO
  2.0 NAO LICENCIADO
type: support-article
updated_at: '2025-06-10T18:35:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044295733-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-TOTVS-COLABORA%C3%87%C3%83O-2-0-NAO-LICENCIADO
---

**Dúvida**Ao acessar a rotina FISA022, as telas abaixo são apresentadas:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059035894/mceclip0.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059032534/mceclip1.png)  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**Esse erro normalmente ocorre quando as tabelas CKQ, CKO E CKP não existem no banco de dados do Protheus.  
Nesse caso, para criação das tabelas é necessário execução do [UPDDISTR](https://tdn.totvs.com/pages/viewpage.action?pageId=181965468).
