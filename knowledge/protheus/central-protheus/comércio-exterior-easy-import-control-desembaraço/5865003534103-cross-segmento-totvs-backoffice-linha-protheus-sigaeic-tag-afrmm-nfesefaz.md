---
article_id: 5865003534103
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: abdb17c6546e4e063f16d9b19e9af1868fd39c594a6e5f8f0bbc844a440d8922
fetched_at: '2026-06-28T22:39:50.209402+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Tag AFRMM - NFESEFAZ
type: support-article
updated_at: '2022-06-02T13:06:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5865003534103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Tag-AFRMM-NFESEFAZ
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)T**empo aproximado para leitura:00:02:00 min **Dúvida**O módulo SIGAEIC é capaz de gerar a informação de **Valor do AFRMM** na **Tag do arquivo xml?****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Neste caso, é necessário verificar se o campo "**WN\_AFRMM**" está preenchido e o código da despesa referente a "**AFRMM".**

1. O parâmetro **MV\_CODAFRM**, deve estar com o código da despesa **AFRMM** que está no cadastro de despesas. Exemplo: 405.

2. A Taxa **AFRMM,** é uma despesa base de **ICMS** configurada como **Base de ICMS - Sim,Base de Custo - Sim** e **UF Estado do Importador** informado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5865951048343/mceclip0.png)

**Obs.** O critério de rateio do peso deve ser configurado conforme rateio feito pelo despachante aduaneiro.
