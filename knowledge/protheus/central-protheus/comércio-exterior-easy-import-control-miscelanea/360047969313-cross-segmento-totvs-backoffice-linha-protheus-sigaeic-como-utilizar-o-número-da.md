---
article_id: 360047969313
category: Comércio Exterior - Easy Import Control - Miscelanea
content_hash: 42284ee3e590c65b1b8819e967d4aa3faed38288540d8c5a0f155708c4f840cb
fetched_at: '2026-06-28T22:39:41.966905+00:00'
product: protheus
section_id: 1500001549702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC - Como utilizar
  o número da Nota Fiscal do TXT Despachante
type: support-article
updated_at: '2022-04-05T17:33:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047969313-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-utilizar-o-n%C3%BAmero-da-Nota-Fiscal-do-TXT-Despachante
---

**Dúvida**Como utilizar o número da Nota Fiscal encaminhada no TXT enviado pelo Despachante, ao integrar o Layout Nota?   
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**A rotina Int. Despachante, ao integrar a nota irá verificar o parâmetro MV\_NFEDESP.  
Parâmetro **MV\_NFEDESP** igual a **T**, utiliza a numeração da nota fiscal e data emissão informada no txt: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070176933/mceclip0.png)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070177113/mceclip2.png)**Parâmetro**MV\_NFEDESP** igual a **F**, verifica a série da nota informada noparâmetro **MV\_SER\_NFE** e no TXT, para gravação automática da numeração sequencial da nota fiscal.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070177493/mceclip3.png)

**Saiba mais:** [Integração despachante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040571214)
