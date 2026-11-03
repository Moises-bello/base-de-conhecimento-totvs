---
article_id: 360020911512
category: BI - Business- Intelligence - Workflow
content_hash: bf78c1df6732d79a3e4e2e29bc18a76720a91ad8476be5eba142932ddbb74999
fetched_at: '2026-06-28T22:37:03.010972+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Configuração do ini
  WorKFlow
type: support-article
updated_at: '2023-07-06T12:26:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020911512-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Configura%C3%A7%C3%A3o-do-ini-WorKFlow
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15817421637655)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como devo configurar o ini do Workflow para envio de aprovação via Link?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) –BI – A partir da versão 11.80  
  
**Solução**A configuração do ini do WF deve seguir esta estrutura.

|  |  |
| --- | --- |
| **Passo a passo:** | Segue abaixo modelo para configurar o Serviço/JOB no AppServer.ini do Workflow via Link:   [<ip servidor:portaHTTP>/<diretório\_virtual>]  ENABLE=1  PORT=<portaHTTP>  PATH=<root\_path>  ENVIRONMENT=<ambiente>  RESPONSEJOB=JOB\_WF\_LINK    [JOB\_WF\_LINK]  TYPE=WEB  SIGAWEB=WF  ENVIRONMENT=<ambiente>  INSTANCES=<número mínimo,número máximo de instâncias>  INSTANCENAME=WF  ONSTART=STARTWEBEX  ONCONNECT=CONNECTWEBEX  ONEXIT=FINISHWEBEX    [schedulerwf] Main=WFONSTART Environment=<ambiente> nParms=4 parm1=<empresa>  parm2=<filial> parm3=<ambiente> parm4=<reativar processos? T ou F>    Exemplo:  [121.416.1.89:8080/wf]  ENABLE=1  PORT=8080  PATH=C:\p11\Protheus\_Data  ENVIRONMENT=P11  INSTANCENAME=WF  RESPONSEJOB=JOB\_WF\_LINK    [JOB\_WF\_LINK]  TYPE=WEB  ENVIRONMENT=P11  INSTANCES=1,10  SIGAWEB=WF  INSTANCENAME=WF  ONSTART=STARTWEBEX  ONCONNECT=CONNECTWEBEX  ONEXIT=FINISHWEBEX    [schedulerwf] Main=WFONSTART Environment=P11 nParms=4 parm1=99 parm2=01 parm3=P11 parm4=T |
| **Observação** | Necessário também possuir a seção HTTP:  Exemplo:  [HTTP]  ENABLE=1  PORT=8080  Maiores informações sobre a seção no link:  [Seção [HTTP]](http://tdn.totvs.com/pages/viewpage.action?pageId=6064817) |
