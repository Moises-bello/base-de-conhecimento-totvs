---
article_id: 360027217332
category: Materiais - Compras (SIGACOM)
content_hash: 47fd0676dd5a6596a372ea78af1d46bd0cde1e22ed962ea103ecff73d07a6bf2
fetched_at: '2026-06-28T22:41:10.459760+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Totvs Colaboração -
  Consulta do CTe importado não é encontrada se realizada por número do documento
type: support-article
updated_at: '2022-05-16T20:59:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027217332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Totvs-Colabora%C3%A7%C3%A3o-Consulta-do-CTe-importado-n%C3%A3o-%C3%A9-encontrada-se-realizada-por-n%C3%BAmero-do-documento
---

**Dúvida**Totvs Colaboração - Consulta do CTe importado não é encontrada se realizada por número do documento  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**Na importação de um documento CTE, quando a busca pelo documento de origem for realizada pelo numero do documento, o numero do documento deve estar incluído com zeros a esquerda.

**Exemplo:**

No XML, o número está: **359559**

No Sistema, o número deve estar: **000359559**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027010651/mceclip0.png)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027038331/mceclip1.png)
