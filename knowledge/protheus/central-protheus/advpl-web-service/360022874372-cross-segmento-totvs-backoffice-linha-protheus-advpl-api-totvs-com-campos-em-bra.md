---
article_id: 360022874372
category: ADVPL - Web Service
content_hash: f04133a63be38f063aaa13463a4ebc0ce009dadb60cfb6ff17eebfdb4a857f1d
fetched_at: '2026-06-28T22:40:10.167539+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - API totvs com
  campos em branco
type: support-article
updated_at: '2021-05-06T17:05:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022874372-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-API-totvs-com-campos-em-branco
---

**Dúvida**Ao fazer uma requisição notamos que vários campos retornados no JSON vieram em branco, assim sendo surgiu a seguinte dúvida, eu posso preencher todos os campos do JSON? ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020849092/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Solução**As APIs TOTVS não são exclusivas para apenas uma linha de produto (mesmo que algumas atualmente só estejam disponíveis para apenas uma linha), assim sendo, as APIs já são criadas segundo o conceito do comitê interno TOTVS para futuramente comportar os dados dos demais produtos.

Desta forma, recomendamos que apenas os campos relacionados com a sua linha de produto sejam utilizados.  
  
**Observação**  
Nem todos os campos estão listados nas APIs TOTVS, assim sendo, cadastros mais complexos deverão ser realizados por meio de rotinas automáticas ou pela criação do próprio serviço REST (ambas por meio de customização desenvolvidas por parte do cliente).  
  
**SAIBA MAIS**  
[API REFERENCE - TOTVS DEVELOPERS](https://api.totvs.com.br/)
