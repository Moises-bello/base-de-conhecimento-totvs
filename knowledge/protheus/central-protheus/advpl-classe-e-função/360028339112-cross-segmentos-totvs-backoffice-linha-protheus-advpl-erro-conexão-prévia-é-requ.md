---
article_id: 360028339112
category: ADVPL - Classe e Função
content_hash: a76a07ad4e829d5ddd3f4993b1bfd3c710cc22233edb40afce9ace28e3c5f728
fetched_at: '2026-06-28T22:40:18.332312+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro conexão
  prévia é requerida para este procedimento ao compilar fonte TDS 11.3
type: support-article
updated_at: '2022-01-06T20:27:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028339112-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-conex%C3%A3o-pr%C3%A9via-%C3%A9-requerida-para-este-procedimento-ao-compilar-fonte-TDS-11-3
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min****Dúvida**

Ao compilar fonte no TDS 11.3 ocorre o erro abaixo

```
Conexão prévia é requerida para este procedimento   
br.com.totvs.tds.startup.exception.TdsException: Conexão prévia é requerida para este procedimento   
br.com.totvs.tds.sdk.jobs.compile.CompileJob.endBuild(CompileJob.java:444)   
br.com.totvs.tds.sdk.jobs.compile.CompileJob.doProcess(CompileJob.java:356)   
br.com.totvs.tds.sdk.jobs.compile.CompileJob.run(CompileJob.java:273)   
org.eclipse.core.internal.jobs.Worker.run(Worker.java:54)   
Conexão prévia é requerida para este procedimento   
br.com.totvs.tds.server.exception.ServerException: Conexão prévia é requerida para este procedimento   
br.com.totvs.tds.server.connector.ServerConnectorHandler.invoke(ServerConnectorHandler.java:55)   
com.sun.proxy.$Proxy17.endBuild(Unknown Source)   
br.com.totvs.tds.sdk.jobs.compile.CompileJob.endBuild(CompileJob.java:442)   
br.com.totvs.tds.sdk.jobs.compile.CompileJob.doProcess(CompileJob.java:356)   
br.com.totvs.tds.sdk.jobs.compile.CompileJob.run(CompileJob.java:273)   
org.eclipse.core.internal.jobs.Worker.run(Worker.java:54)   
[13:54:58.416] Compilação finalizada (11,579 segs.) 
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Faça a atualização do TDS

- Opção -> Ajuda -> Verificar Atualizações

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028996931/mceclip0.png)

**Saiba Mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Atualização do TDS 11.3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028128591)  
[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro na atualização automática do TDS 11.3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024991672)   
[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro Atualização TDS no momento de instalação plugin](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028193951)  
[Perguntas e Respostas TDS 11.3](http://tdn.totvs.com/display/tec/Perguntas+e+Respostas+TDS+11.3)
