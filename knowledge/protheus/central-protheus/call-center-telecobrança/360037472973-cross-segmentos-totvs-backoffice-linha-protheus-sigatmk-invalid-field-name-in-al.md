---
article_id: 360037472973
category: Call Center - Telecobrança
content_hash: 194a53fb218f86024312d240d2fa9db432b2327a0647d62cb87a54d6f72b5150
fetched_at: '2026-06-28T22:41:28.657472+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- invalid field name
  in Alias ACG->ACG_DECRESC on TK274GRVTLC(TMKA274.PRW)
type: support-article
updated_at: '2022-06-22T17:20:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037472973-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-invalid-field-name-in-Alias-ACG-ACG-DECRESC-on-TK274GRVTLC-TMKA274-PRW
---

**Ocorrência**

Como solucionar o error.log apresentado no telecobrança Call Center:  
***invalid field name in Alias ACG->ACG\_DECRESC on TK274GRVTLC(TMKA274.PRW)***

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-A partir da versão 11.80.

**Causa**

O erro somente ocorre se o campo **ACG\_DECRESC**estiver com o uso desmarcado.

**Solução**

Avalie se o campo **ACG\_DECRESC**está como usado no dicionário de dados, via configurador.

Para ajustar:

1-Edite a tabela **ACG**;  
2-Edite o campo **ACG\_DECRESC**;  
3-Marque-o como usado;  
4-Salve a tabela;  
5-Atualize o dicionário de dados;  
6-Reinicie o smartclient e refaça o processo,  o erro deixará de ocorrer.
