---
article_id: 4408218843159
category: Comércio Exterior - Easy Import Control - Licença de Import
content_hash: d59bc9c8885c11949e98a696943023e601299c451565cafbf05984e6d0287e1c
fetched_at: '2026-06-28T22:39:42.688529+00:00'
product: protheus
section_id: 1500001549682
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como incluir o
  destaque para o produto suframa para PLI
type: support-article
updated_at: '2021-09-10T15:15:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408218843159-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-incluir-o-destaque-para-o-produto-suframa-para-PLI
---

**Dúvida**Como incluir o destaque para o produto Suframa para PLI?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

Para o destaque do produto seja preenchido na PLI, é necessário preencher o campo **No. Destaque** (YD\_DESTAQU).

1. No módulo SIGAEIC em Atualizações\ Tabelas \ N.c.m.;

2. Selecione a NCM e opção Alterar;

3. Preencha o campo **No. Destaque** (YD\_DESTAQU).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408218603031/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408218607255/mceclip1.png)

A NCM cadastrada pode ser vinculada ao cadastro do produto, ou ser alterada na inclusão da *Purchase Order* (EICPO400).

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408218690327/mceclip3.png)

Ao incluir a PLI a informação será gravada no campo **Destaque Imp** (WP\_DESTAQU).

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408224421527/mceclip2.png)
