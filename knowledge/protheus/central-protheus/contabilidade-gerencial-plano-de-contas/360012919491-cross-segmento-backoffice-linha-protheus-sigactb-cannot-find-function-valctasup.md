---
article_id: 360012919491
category: Contabilidade Gerencial - Plano de Contas
content_hash: af3f6c6efeda681c674c1276d39d2abe1e0da1c11e0e7d5dcb11fcf06a294a43
fetched_at: '2026-06-28T22:40:33.292569+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - cannot find function
  VALCTASUP in AppMap
type: support-article
updated_at: '2022-06-10T23:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012919491-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-cannot-find-function-VALCTASUP-in-AppMap
---

**Ocorrência**

Ao incluir uma conta contábil ocorre o seguinte erro ***"cannot find function VALCTASUP"***.

**Ambiente**

Protheus – Contabilidade Gerencial – 12.1.17

**Causa**

Este erro ocorre devido a **validação** do campo **CT1\_CTASUP**, onde a mesma deve possuir a função **Ctb020CSup()**.

**Solução**

Para a correção deste problema, deve-se rodar o **UPDDISTR** conforme a seguinte documentação: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006655452-MP-SIGACTB-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ambiente-no-Microsiga-Protheus-12->

**Após a aplicação do mesmo o campo terá a validação da seguinte forma:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008868392/mceclip0.png)

 Veja mais :

[MP-SIGACTB-InterFunctionCall: cannot find function CTB020CSUP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007600152-MP-SIGACTB-InterFunctionCall-cannot-find-function-CTB020CSUP?source=search)
