---
article_id: 28956524855831
category: Suricato
content_hash: 109fce44a3ca7a33f5ed941642b3f7319eed32c16196c33d96cc640d8203af90
fetched_at: '2026-06-28T22:46:26.324554+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Erro na integração RM e Suricato - Cannot obtain Oracle Client
type: support-article
updated_at: '2025-09-05T20:06:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28956524855831-RH-RM-PTO-Erro-na-integra%C3%A7%C3%A3o-RM-e-Suricato-Cannot-obtain-Oracle-Client
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28956555107991) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como corrigir o erro a seguir ao editar um funcionário, realizar a carga inicial para Suricato ou algum outro processo que acione a integração com Suricato?

Erro no Agente de Envio (mensagem assíncrona). System.Web.Services.Protocols.SoapException:   
O servidor não pôde processar a solicitação. ---> System.InvalidOperationException: Cannot obtain Oracle Client information from registry. Make sure that Oracle Client Software is installed, or use the Direct mode when connecting to server.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28956524832791)  
  
**Ambiente**TOTVS RH - TOTVS RH(Linha RM) - Automação de Ponto - A partir da versão 12.1  
  
**Solução**

Esse erro pode ocorrer quando não se tem instalado o Oracle Client na máquina que está sendo executado o processo da carga inicial ou algum outro processo que acione a integração com Suricato

Ou não está instalado no servidor onde está configurado o Webservice RM.

Para solucionar o Oracle Client deve ser instalado na máquina do usuário e no servidor onde está configurado o Webservice RM.

A arquitetura do Oracle Client precisa ser igual ao do servidor onde está o Webservice RM (32bits ou 64bits)
