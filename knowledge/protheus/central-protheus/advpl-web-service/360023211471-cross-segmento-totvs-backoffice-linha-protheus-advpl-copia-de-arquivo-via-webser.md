---
article_id: 360023211471
category: ADVPL - Web Service
content_hash: bef780234c9283f44396a7be0bc8c87b94519b0026d856e575f1590903f224d0
fetched_at: '2026-06-28T22:40:10.416567+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Copia de arquivo
  via WebService
type: support-article
updated_at: '2025-08-28T20:27:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023211471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Copia-de-arquivo-via-WebService
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34525521241879)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Desenvolvi um web service que grava um arquivo texto (json) e preciso gerar uma copia desse arquivo via Web Service em outra pasta, as funções GETTEMPPATH e CPYS2T não funcionam em job/ws.

Existe alguma maneira de fazer isso?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**De fato as funções [GETTEMPPATH](https://tdn.totvs.com.br/display/tec/GetTempPath) e [CPYS2T](http://tdn.totvs.com/display/tec/CpyS2T) não executam via *Job*.

No seu caso send um arquivo texto pode utilizar a função [FWrite](http://tdn.totvs.com/display/tec/FWrite) para gerar o arquivo na própria pasta desejada ou utilizar a [MemoWrite](http://tdn.totvs.com/display/tec/MemoWrite)
