---
article_id: 115011884607
category: CRM - Dúvidas Gerais
content_hash: 1974055d6457b54eb734c3b39dce8dfe9253e43c85e6374ef7a2fc69241a5878
fetched_at: '2026-06-28T22:40:27.520573+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGACRM - Array out of
  bounds ( 1 of 0 ) on RUPCRMSEG
type: support-article
updated_at: '2021-12-21T16:59:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011884607-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGACRM-Array-out-of-bounds-1-of-0-on-RUPCRMSEG
---

**![time.png](https://totvssuporte.zendesk.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:00:02:00 min**

**Ocorrência**

Error.log: Array out of bounds ( 1 of 0 ) on RUPCRMSEG(RUP\_CRM.PRW)

**Causa**

A inconsistência ocorria no momento de migrar a versão 11.80 para 12, por falta do campo **AOV\_PAI**.

**Ambiente**

Cross SegmentosTOTVS -Backoffice (Linha Protheus)-SIGACRM- a partir da versão 12.

**Solução**

Baixe o dicionário de dado na pasta systemload, conforme o seu release:

<https://suporte.totvs.com/portal/p/10098/download#000006/P12117/P12117DD/>

<https://suporte.totvs.com/portal/p/10098/download#000006/P12123/P12123DD/>

<https://suporte.totvs.com/portal/p/10098/download#000006/P12125/P12125DD/>

<https://suporte.totvs.com/portal/p/10098/download#000006/P12127/P12127DD/>

<https://suporte.totvs.com/portal/p/10098/download#000006/P12133/P12133/>

Posteriormente, descompacte o dicionário de dados e rode o UPDDISTR para que os campos sejam criados conforme o dicionário.

**Estrutura do campo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416670559255/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416670566423/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416670569239/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416655610903/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416670583831/mceclip4.png)

**Obs. O processo de atualização de dicionário deve ser efetuado por uma analista com conhecimento de estrutura Protheus, na dúvida do processo de atualização por UPDDISTR, acione a equipe de FrameWork.**
