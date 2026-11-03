---
article_id: 360019125131
category: Contabilidade Gerencial - Error log
content_hash: 01cb8ee115e690b6140e29e4e9dfbdfeef306f67f2a68554d71846439cd542ea
fetched_at: '2026-06-28T22:40:52.010125+00:00'
product: protheus
section_id: 1500001537581
source: central-protheus
title: 'MP - SIGACTB - Ao acessar alguma rotina é apresentado error: Super File Open
  - Open File - Ctree Error 14 - IO Error'
type: support-article
updated_at: '2021-04-28T14:47:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019125131-MP-SIGACTB-Ao-acessar-alguma-rotina-%C3%A9-apresentado-error-Super-File-Open-Open-File-Ctree-Error-14-IO-Error
---

**Ocorrência**

Ao acessar alguma rotina da **Contabilidade Gerencial** é apresentado o error: 

**"sigahle.hle: Super File Open - Open File - Ctree Error 14 - IO Error: 0 - File corrupt at open File: sigahle.hle on CHECKHLP(ENGXFUN.PRW) "**

**Ambiente**

Microsiga Protheus - Contabilidade Gerencial - A partir da versão 12.  
 **Causa**

Essa ocorrência é causada devido os arquivos de Help do sistema estarem corrompidos.  
 **Solução**  
Para solução segue os seguintes passos:  
  
Super File Open - Open File - Ctree Error 14 - IO Error:  
  
- Parar os serviços do **Protheus**, **Ctree** e **TOP**;  
  
- Retirar da pasta onde está instalado o **CtreeServer** os arquivos com extensão **\*.FCS** (ideal é criar uma pasta para guarda-los como backup e futura análise mas retirando da pasta original);   
  
- Apagar os arquivos de índices (\*.**CDX**, .**IDX** e \*.**IND**) do **Protheus** que estão na pasta **SYSTEM** ou equivalente;   
  
- Apagar o conteúdo da pasta **CTREEINT**, criada dentro da pasta **SYSTEM**;   
  
- Apagar os arquivos de índices (\*.**CDX**) do Protheus que estão na pasta **PROFILE** instanciada no **PROTHEUS\_DATA**;   
  
- Apagar o conteúdo da pasta **CTREEINT**, criada dentro da pasta **PROFILE**;   
  
- comentar a pasta Semáforo;  
  
- Limpar a pasta **%TEMP%** do SO  
  
- Apagar **sigahlp.hlp**, **sigahle.hle**, **sigahls.hls** da pasta **system**.  
  
- Baixar no Portal do Cliente -**bra-helps.rar**, descompactar no diretorio **systemload**.  
  
- Subir os serviços (**Ctree**, **Protheus** e **TOP**)  
  
- Acessar o sistema **exclusivo**;

 Veja mais :

[MP - SIGACTB - CTBA102: Erro no arquivo temporário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016501852-MP-SIGACTB-CTBA102-Erro-no-arquivo-tempor%C3%A1rio?source=search)
