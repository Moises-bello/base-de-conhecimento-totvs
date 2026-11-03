---
article_id: 360049423694
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 92b809b4b761df7dcfcd93ad676a9812eb51c9b4d32980bc1f7ea95e6b1bc202
fetched_at: '2026-06-28T22:39:56.411627+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - CST FLORIANOPOLIS
type: support-article
updated_at: '2025-07-18T14:48:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049423694-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-CST-FLORIANOPOLIS
---

**Dúvida**Como gerar a tag CST no XML da nota de Florianópolis?   
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**

O campo F4\_CSTISS (Sit. Trib. ISS) deve ser preenchido com um CST válido conforme Figura 4, disponível no manual de integração webservice:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075236893/mceclip0.png)

[Manual Webservice Florianopolis](http://www.pmf.sc.gov.br/arquivos/arquivos/pdf/22_01_2014_14.55.12.318070b51e70a646d8f186b636899251.pdf)

O CST deve ser cadastrado previamente na S9 (SX5), para ficar disponível na consulta padrão do  F4\_CSTISS.  
Se o campo F4\_CSTISS estiver vazio, será considerado o conteúdo do campo B1\_ORIGEM.
