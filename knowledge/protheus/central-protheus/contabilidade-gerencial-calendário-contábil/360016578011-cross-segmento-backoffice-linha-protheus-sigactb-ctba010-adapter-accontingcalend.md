---
article_id: 360016578011
category: Contabilidade Gerencial - Calendário Contábil
content_hash: f25bc7a9523c21c2a53fc877094d37a47eabaa7b21315a440eb78b2be2d1f990
fetched_at: '2026-06-28T22:41:03.335403+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus  - SIGACTB - CTBA010 ADAPTER  (ACCONTINGCALENDAR) '
type: support-article
updated_at: '2022-06-03T21:41:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016578011-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA010-ADAPTER-ACCONTINGCALENDAR
---

**Ocorrência**Adapter CTBA010 - (ACCONTINGCALENDAR) cadastrado, porem na execução da rotina de sincronização (carga inicial) retorna mensagem "este adapter não esta pronto para iniciar a sincronização".

**Ambiente**Protheus  – Sigactb – A partir da versão 11.80  
   
 **Causa**

Não foi informado no adapter o alias referente a rotina.  
Que é  uma das três validações que são verificadas  na integração.

**Solução**

A rotina faz três validações

1. Se existe model.
2. Se existe cadastro no SYSOBJ.
3. E por fim se nenhum dos anteriores existir, verifica  se o ALIAS está informado.

O processo foi corretamente processado após informar o ALIAS no cadastro do EAI.
