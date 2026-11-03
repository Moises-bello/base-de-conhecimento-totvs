---
article_id: 360050491033
category: ADVPL - Relatório
content_hash: 0b55190a98e05794466a4b5f28a6b52965ff7733c42e575fe3a8d702a22ed2d6
fetched_at: '2026-06-28T22:40:22.923776+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TReport - Alterar
  titulo e-mail
type: support-article
updated_at: '2021-12-30T19:05:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050491033-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TReport-Alterar-titulo-e-mail
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como posso setar o título do e-mail?

**Ambiente**Protheus - A partir da versão 12.1.17  
  
**Solução**O título do e-mail é proveniente do título dado ao TReport, valor passado no método construtor, sendo parâmetro (*cTitle*):

```
TReport():New( <cReport> , <cTitle> , <uParam> , <bAction> , <cDescription> , <lLandscape> , <uTotalText> , <lTotalInLine> , <cPageTText> , <lPageTInLine> , <lTPageBreak> , <nColSpace> )
```

O mesmo recebe mais informações, e não pode ser alterado.  
  
**Saiba mais**  
[Treport](https://tdn.totvs.com/display/public/PROT/TReport)
