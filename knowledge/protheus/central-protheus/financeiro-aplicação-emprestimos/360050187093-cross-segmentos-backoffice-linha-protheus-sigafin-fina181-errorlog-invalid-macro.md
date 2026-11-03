---
article_id: 360050187093
category: Financeiro - Aplicação / Emprestimos
content_hash: e76187f231ce3dcfedf35e3c06f0273d3db8e5dd303435417f850a06e41890f1
fetched_at: '2026-06-28T22:37:59.475907+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA181 - Error.log
  -invalid macro source (SSYacc0105e: Error token failed, no valid token):(2.02.002)
  on A181RESGEMP(FINA181.PRX) '
type: support-article
updated_at: '2022-06-21T01:28:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050187093-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA181-Error-log-invalid-macro-source-SSYacc0105e-Error-token-failed-no-valid-token-2-02-002-on-A181RESGEMP-FINA181-PRX
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Ao tentar efetuar um resgate, apresenta o error. log

**THREAD ERROR ([5004], Administrator, CG-HV02) 09/06/2020 08:14:40**  
**invalid macro source (SSYacc0105e: Error token failed, no valid token):(2.02.002) on A181RESGEMP(FINA181.PRX) 24/04/2020 11:32:30 line : 2593**  
**Ambiente**Microsiga Protheus – Financeiro – FINA181 – A partir da versão 11.0  
  
**Causa  
MV\_NATREMP** - o parâmetro estava com conteúdo sem as aspas dupla.**Solução**O conteúdo deste parâmetro **MV\_NATREMP,** deve ser preenchido com aspas dupla, caso contrário corrigir no campo.  
Exemplo:

![](https://totvssuporte.zendesk.com/attachments/token/AJsrRIHlwrdHQAiQzfE6ZLTJs/?name=inline1622728483.png)

**Saiba mais:**<https://tdn.totvs.com/pages/releaseview.action?pageId=392500138>
