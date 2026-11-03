---
article_id: 28282044298263
category: Financeiro
content_hash: fb00ca68d48687b41bd2fa3ad4ebc09160c05943863ff503c66044e7018d63a8
fetched_at: '2026-06-28T22:38:03.119908+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Como criar
  um gatilho para o preenchimento do campo E-mail Bol para envio do boleto via API
type: support-article
updated_at: '2025-01-23T17:32:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28282044298263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Como-criar-um-gatilho-para-o-preenchimento-do-campo-E-mail-Bol-para-envio-do-boleto-via-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28282044275479) Tempo aproximado para leitura: **00:08 min****Dúvida**Como criar um gatilho para o preenchimento do campo **E-mail Bol. (A10\_EMABOL)?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**

Crie um gatilho com domínio **(X7\_CAMPO)** e contradomínio **(X7\_CDOMIN)** apontando para o campo que irá disparar a ação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28282059730071)

Insira a seguinte função no campo Regra e informe o campo ORIGEM e DESTINO:

**Regra**

```
 Eval({|cEmail| FwFldPut("AI0_EMABOL", cEmail)}, FwFldGet("A1_EMAIL"))
```

**Observação**

A função definida no campo Regra **(X7\_REGRA)** do gatilho deve ser do tamanho da regra.
