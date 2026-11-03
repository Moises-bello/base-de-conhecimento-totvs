---
article_id: 360027664932
category: BI - Business- Intelligence - Workflow
content_hash: f31ebb6c525d58b80f249923dd968795a1aa8d66d86acd7006090cad6252dec5
fetched_at: '2026-06-28T22:37:03.039849+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Erro: Messenger -
  Workflow - Abertura da tela'
type: support-article
updated_at: '2022-07-27T18:26:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027664932-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Erro-Messenger-Workflow-Abertura-da-tela
---

**Dúvida**Ao abrir a rotina do Messenger, é apresentando o erro de Conexão com o Ambiente.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Workflow – A partir da versão 12  
  
**Solução****Configurar Driver de comunicação utilizado no messenger do Workflow:**O **Messenger**é um recurso disponível no **Microsiga Protheus**que serve para avisar aos usuários de algum processo ou mensagem de workflow que esteja aguardando alguma ação à ser tomada. Ao acessar o messenger, uma *thread* é aberta para trabalho, utilizando como base de comunicação com o *AppServer* a diretiva *active* que está disponível na seção *drivers*do SmartClient.INI.

Essa diretiva é utilizada apenas quando houver um valor, ao possuir mais de um valor, o messenger não faz distinção da comunicação utilizada, gerando e assim, erro de comunicação com o servidor. Caso utilize mais de um valor, será necessário criar uma nova diretiva, a **WFMSG**nesta mesma seção. Essa nova diretiva deverá informar um único valor, que será a comunicação com o servidor que deseja executar o **Messenger**.   
  
**Exemplo:****[Drivers]**  
Active=TCP,SERVERHOMOLOG,SERVERPROD  
WFMSG=SERVERHOMOLOG
