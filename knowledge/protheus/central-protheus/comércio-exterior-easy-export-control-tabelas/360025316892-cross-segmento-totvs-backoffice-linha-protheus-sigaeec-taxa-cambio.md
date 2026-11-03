---
article_id: 360025316892
category: Comércio Exterior - Easy Export Control - Tabelas
content_hash: fb29445fff1996929c1ef6c3934ebf036cc495afa8b01c6c102bfb41780c1e7c
fetched_at: '2026-06-28T22:37:01.451378+00:00'
product: protheus
section_id: 1500001549222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAEEC - Taxa Cambio
type: support-article
updated_at: '2023-06-05T14:15:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025316892-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Taxa-Cambio
---

**Dúvida**Onde o sistema busca o conteúdo para o campo EEQ\_TX?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.   
  
**Solução**  
O campo **taxa câmbio (EEQ\_TX)** e preenchido automaticamente com o conteúdo informado em **SIGAEEC / Tabelas / Cotacao moedas (EICA140)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024351511/mceclip2.png)

**Observação:** A rotina de **Câmbio (EECAF200)** irá verificar o parâmetro **MV\_EXP\_TX** para preencher a taxa de compra ou venda no campo **taxa câmbio (EEQ\_TX)**. Caso a taxa não esteja cadastrada para a data informada de liquidação, o campo **taxa câmbio (EEQ\_TX)** será preenchido com a última taxa cadastrada na rotina **Cotacao moedas (EICA140)**.
