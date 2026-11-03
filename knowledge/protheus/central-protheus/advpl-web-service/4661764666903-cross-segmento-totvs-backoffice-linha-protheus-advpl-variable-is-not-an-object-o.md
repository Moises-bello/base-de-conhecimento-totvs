---
article_id: 4661764666903
category: ADVPL - Web Service
content_hash: 0cb44e058fdefd78e9990b3542744f157bc1f53de7f71c5528a34256a9e6d48d
fetched_at: '2026-06-28T22:40:10.322757+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Variable is not
  an object  on RESTCALLWS(FWRESTHANDLER.PRW) '
type: support-article
updated_at: '2022-03-09T20:30:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4661764666903-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Variable-is-not-an-object-on-RESTCALLWS-FWRESTHANDLER-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Erro ao efetuar requisições Rest no release 12.1.33 Rest2.0:

```
variable is not an object  on RESTCALLWS(FWRESTHANDLER.PRW)
```

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12.1.27  
  
**Causa**O erro é causado quando se utiliza o objeto publico **oRest** em customizações e este é destruído ou alterado, desta forma as execuções e métodos deixam de ser executado no **Rest2.0.**Tal objeto não precisa ser construído, pois ele é declarado com escopo público e construído na inicialização de cada Thread e a ele é dado o nome de **oRest**.

Portanto, para cada Thread de atendimento haverá um objeto **oRest** para uso.  
  
**Solução**Renomear nos fontes customizado o objeto **oRest****Saiba mais**[oRest](https://tdn.totvs.com/pages/viewpage.action?pageId=553336167) 

[Rest2.0](https://tdn.totvs.com/display/framework/Entendendo+as+novidades+do+REST)
