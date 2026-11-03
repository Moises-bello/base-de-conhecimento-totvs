---
article_id: 360022923151
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 93e6a98e65d7d931fc577c937b83eea83c19b28f6c7366f1398b8ad5611c55f4
fetched_at: '2026-06-28T22:40:32.413172+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Ao Gerar contabilização
  apresenta mensagem HELP FALTAVALOR
type: support-article
updated_at: '2022-04-01T16:31:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022923151-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Ao-Gerar-contabiliza%C3%A7%C3%A3o-apresenta-mensagem-HELP-FALTAVALOR
---

**Ocorrência**

Ao Gerar contabilização apresenta mensagem **HELP FALTAVALOR**

**![](https://totvssuporte.zendesk.com/hc/article_attachments/360020401212/mceclip0.png)**

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**

Deve ser avaliado o cadastro do Lançamento Padrão (Rotina **CTBA080**) da operação responsável por esta contabilização,Ou seja deve avaliar o cadastro e a referencia sobre o valor na moeda 1, desta forma o valor do lançamento será diferente de 0, no lançamento contábil.

 Ex:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020401792/mceclip2.png)

Saiba mais :

* [CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)
