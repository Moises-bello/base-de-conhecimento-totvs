---
article_id: 360039943893
category: Manutenção de Ativos (SIGAMNT)
content_hash: 8f506718d355b3b4dddd9cb80f06c36d4af571ccfcdcd49f6425e44aa71fe502
fetched_at: '2026-06-28T22:42:33.045096+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Configuração do ambiente para recebimento
  de respostas para Pesquisa de Satisfação da Solicitações de Serviço
type: support-article
updated_at: '2025-02-04T17:42:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039943893-Manufatura-Linha-Protheus-MNT-Configura%C3%A7%C3%A3o-do-ambiente-para-recebimento-de-respostas-para-Pesquisa-de-Satisfa%C3%A7%C3%A3o-da-Solicita%C3%A7%C3%B5es-de-Servi%C3%A7o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22543556421143)*Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**Como configurar o ambiente para recebimento de respostas para pesquisa de satisfação da **Solicitações de Serviço - MNTA280**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Solução**Realizar as seguintes configurações abaixo no ambiente que se deseja permitir o processo de repostas para pesquisa de satisfação:  
  
1. Acessar o módulo **Configurador - SIGACFG** e informar no parâmetro **MV\_WFDIR - Diretório de trabalho do Workflow** o diretório onde serão gravados os arquivos da pesquisa de satisfação e no parâmetro **MV\_NGWFHT - Indica o IP e a Porta para a comunicação HTTP do workflow**o **IP** e **porta** para a comunicação **HTTP - HyperText Transfer Protocol**do *workflow*.    
  
2. Incluir as **tags** abaixo no arquivo **appserver.ini**, substituindo o conteúdo entre **<>** pelo valor correspondente;

```
[<ip servidor:portaHTTP>/<conteúdo do parâmetro MV_WFDIR>]  
ENABLE=1  
PORT=<portaHTTP>  
PATH=<root_path>  
ENVIRONMENT=<ambiente>  
RESPONSEJOB=JOB_WF_LINK  
  
[JOB_WF_LINK]  
TYPE=WEB  
SIGAWEB=WF  
ENVIRONMENT=<ambiente>  
INSTANCES=<número mínimo,número máximo de instâncias>  
INSTANCENAME=WF  
ONSTART=STARTWEBEX  
ONCONNECT=CONNECTWEBEX  
ONEXIT=FINISHWEBEX
```

3. Realizar a alteração das *tags*abaixo no arquivo **appserver.ini**, conforme o exemplo, substituindo o conteúdo entre **<>** pelo valor correspondente;

```
[ONSTART]  
JOBS=JOB_WF_LINK  
REFRESHRATE=120  
  
[HTTP]  
Enable=1  
PATH=<root_path>  
ENVIRONMENT=<ambiente>  
RESPONSEJOB=JOB_WF_LINK  
PORT=<portaHTTP>  
XFRAMEOPTIONS = ALLOW-FROM *
```
