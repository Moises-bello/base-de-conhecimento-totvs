---
article_id: 360050843714
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d9255d7fac02ecc0cd10343a4047b87bb4fc16e8ba7595c79d4ab03fe2518fc0
fetched_at: '2026-06-28T22:38:28.548384+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Erro 403 Forbidden
type: support-article
updated_at: '2023-01-30T18:03:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050843714-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-403-Forbidden
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao alterar o cadastro do cliente (**MATA030**) , está sendo mostrado a tela de erro abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078747574/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - a partir da release 12.1.25

**Causa**A mensagem ocorre por que o sistema não encontra os parâmetros de longitude da função Maplink  do módulo TMS, na sequência é gerado o erro:

***variable does not exist CLONTITUDE on { || TMSROT015(CFILENT,CENTIDA,CCODENT,CLATITUDE,CLONTITUDE) }(TMSAO48.PRW) 25/06/2019 08:59:45 line : 74***

Já encontra-se corrigido no fonte **TMSA048** de **05.09.2019.**

**Solução**

Para solucionar aplique o pacote contido no artigo:**[MP - TMS - variable does not exist CLONTITUDE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037748593-MP-TMS-variable-does-not-exist-CLONTITUDE-)**
