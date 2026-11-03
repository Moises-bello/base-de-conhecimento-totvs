---
article_id: 12044301643287
category: BI - Business- Intelligence - Workflow
content_hash: c28dceaa40f9ae5308f257461797cf77c389ba16aacb9bd73993c6156cd7976d
fetched_at: '2026-06-28T22:37:03.124781+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Invalid function call
  : WFLAUNCHER'
type: support-article
updated_at: '2023-01-30T18:30:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12044301643287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Invalid-function-call-WFLAUNCHER
---

**Dúvida**Como resolver o erro *Invalid function call : WFLAUNCHER ?*  
  
**Ambiente**Protheus – Workflow – A partir da versão 12  
  
**Solução**

A mensagem "*Invalid function call : WFLAUNCHER*" ocorre principalmente pela falta de configuração correta no appserver.ini, em especifico nos parâmetros do "*Schedulerwf*" conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044043927831)

gerando o erro abaixo ao subir o serviço:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044084386327)

Para resolver este erro, basta adicionar a informação completa dos parâmetros na *SchedulerWf*:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044165635607)

**Saiba mais**

[Configuração Workflow appserver.ini](https://tdn.totvs.com/pages/releaseview.action?pageId=225268728)
