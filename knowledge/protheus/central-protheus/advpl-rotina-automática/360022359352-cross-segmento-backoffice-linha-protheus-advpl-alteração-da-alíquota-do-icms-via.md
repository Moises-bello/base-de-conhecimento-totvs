---
article_id: 360022359352
category: ADVPL - Rotina Automática
content_hash: 8668639e2dc3bf8fa3f1cfa0cbbe287591f508e832e2c0fa18fb86488f72f920
fetched_at: '2026-06-28T22:40:23.915001+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Alteração da alíquota
  do ICMS via execauto (MATA116)
type: support-article
updated_at: '2021-12-29T13:24:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022359352-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Altera%C3%A7%C3%A3o-da-al%C3%ADquota-do-ICMS-via-execauto-MATA116
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Nós criamos uma rotina automática da "**MATA116**", e está já encontra-se normalmente funcional atualmente. Nós queremos saber como passar a alíquota (**D1\_PICM**) como parâmetro para a função ?

**Ambiente**Protheus – ADVPL – A partir da versão 11.8  
  
**Solução**Para a alteração da alíquota do ICMS via execauto basta adicionar os campos abaixo:

```
aadd(acabec,{"NF_VALICM",40})  
aadd(acabec,{"IT_ALIQICM",4})
```

**Saiba Mais:  
[MATA116 - Programa de digitação de Nota Fiscal de conhecimento de Frete](http://tdn.totvs.com/pages/releaseview.action?pageId=6085187)**
