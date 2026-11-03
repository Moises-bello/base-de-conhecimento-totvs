---
article_id: 360018341551
category: ADVPL - Classe e Função
content_hash: f315425490ba017c900a65bc537365df65aa19d4b9a8aeae8976a7daa33e3db7
fetched_at: '2026-06-28T22:40:20.470922+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - InterFunctionCall:
  cannot find function MTC010SX1'
type: support-article
updated_at: '2022-01-11T22:03:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018341551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-InterFunctionCall-cannot-find-function-MTC010SX1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Após a migração para a versão 12, está apresentando erro *InterFunctionCall: cannot find function **MTC010SX1.***  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**A mensagem de erro informa que a função **MTC010SX1()** não está disponível no rpo.  
Verifique se o fonte **A420ATPLAN** está compilado.  
Verifique se está utilizando a função **PutSX1**. A função **PutSX1** não está disponível no Protheus 12. Todas as alterações de dicionários devem ser feitas via Configurador ou através do Release Incremental.  
  
**Saiba mais**[PutSX1 - Criação de pergunta](http://tdn.totvs.com/pages/releaseview.action;jsessionid=B53926AEF5304F339ECD16467CB67C8F?pageId=244740739)
