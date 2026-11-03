---
article_id: 360018272612
category: Contabilidade Gerencial - Relatórios Comparativos
content_hash: 62d9c9ced10c637923b92470faee68bbfed781d96171c14a06599f2d001844c4
fetched_at: '2026-06-28T22:40:37.158002+00:00'
product: protheus
section_id: 1500001548922
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR670 cannot find
  function CONR420 in AppMap
type: support-article
updated_at: '2022-07-18T18:08:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018272612-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR670-cannot-find-function-CONR420-in-AppMap
---

**Ocorrência**A rotina **lotes com diferença(CONR420)** está apresentando o seguinte error.log:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013858252/mceclip0.png)

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – a partir 12.1.17

**Solução**

A rotina **CONR420**, pertence ao módulo **SIGACON** que foi descontinuado. No módulo **SIGACTB**, a rotina responsável pelo relatório de **lançamentos com diferenças é a CTBR670**, porém o mesmo não verifica o lote inteiro e sim os lançamentos com diferenças, no momento não há um relatório que traga as diferenças por lote.

Verifique se rotina esta disponível em seu menu do módulo **SIGACTB**, caso não esteja, realize a troca do menu.

Para maiores informações sobre as alterações no menu, **acesse:** <http://tdn.totvs.com/pages/viewpage.action?pageId=271164329>
