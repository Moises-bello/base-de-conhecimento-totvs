---
article_id: 5568191867287
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 25620c4fb2fd46aca757c452cc2e100b90d1e836995d50bc183cd61483f0becf
fetched_at: '2026-06-28T22:39:50.111603+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem AVG0005351
  ao salvar o Desembaraço
type: support-article
updated_at: '2022-04-20T12:19:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5568191867287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-AVG0005351-ao-salvar-o-Desembara%C3%A7o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:00 min** **Dúvida**Ao tentar salvar o Dsembaraço (**EICDI501**) o sistema está exibindo esta mensagem impeditiva: AVG0005351 Problema: "No. da DI/DA não pode ser vazio(a) pois a Data Registo da DI foi informada."

Como fazemos para salvar o processo sem que exiba esta mensagem?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5568102752279/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**Para que a mensagem não seja apresentada, deve ser informado no campo **W6\_DI\_NUM** "DI/DA/DUIMP"**,** o número do registro da DI/DA.
