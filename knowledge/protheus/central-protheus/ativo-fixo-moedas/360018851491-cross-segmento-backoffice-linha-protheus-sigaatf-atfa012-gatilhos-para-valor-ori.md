---
article_id: 360018851491
category: Ativo Fixo - Moedas
content_hash: 1dc8096a61f119ff67a5f2f2ae2f5697c075bffe458364532cec3a31215342b2
fetched_at: '2026-06-28T22:41:37.775931+00:00'
product: protheus
section_id: 1500001536641
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - Gatilhos para
  valor original do bem em outras moedas
type: support-article
updated_at: '2023-07-25T18:46:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018851491-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Gatilhos-para-valor-original-do-bem-em-outras-moedas
---

**Ocorrência**

Ao informar o **valor original do bem (N3\_VORIG1)** o sistema deveria calcular o valor original na **moeda 03**, pois o paramento **MV\_ATFMOED** está configurado para **3** e a data de inicio da depreciação contém a taxa da moeda preenchida.

**Ambiente**Protheus – Contabilidade Gerencial – 12.1.17

**Causa**

Isto ocorre, pois por padrão o sistema não verifica a **taxa da data de inicio da depreciação(N3\_DINDEPR)** e sim a **taxa do dia da aquisição do bem(N1\_AQUISIC)**, sendo que os campos referentes ao **valor original do bem(N3\_VORIG1, N3\_VORIG2 e etc...)** tem por conceito, conter o valor inicial do bem, ou seja, a **quantia da aquisição do mesmo**.

**Solução**

Para que o gatilho funcione corretamente, os campos de taxa para as moedas na **SM2** devem estar preenchidos para o dia correspondente ao da **aquisição do bem(N1\_AQUISIC**):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014356031)

Deve ser verificado também se o parâmetro MV\_ATFMOED está configurado para a moeda desejada.
