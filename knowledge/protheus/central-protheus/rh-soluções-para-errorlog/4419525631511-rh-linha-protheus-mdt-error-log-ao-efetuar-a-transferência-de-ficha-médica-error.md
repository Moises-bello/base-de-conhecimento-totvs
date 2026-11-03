---
article_id: 4419525631511
category: RH - Soluções para error.log
content_hash: 7a00452c80c1a7947e42974c5857a90908d57f3b7fff13eee13280af7385b835
fetched_at: '2026-06-28T22:44:10.004800+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - MDT - Error log ao efetuar a transferência de ficha
  médica - Error : 156 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL
  Server]Sintaxe incorreta próxima à palavra-chave ''WHERE''.'
type: support-article
updated_at: '2022-01-18T20:51:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419525631511-RH-Linha-Protheus-MDT-Error-log-ao-efetuar-a-transfer%C3%AAncia-de-ficha-m%C3%A9dica-Error-156-37000-RC-1-Microsoft-SQL-Server-Native-Client-11-0-SQL-Server-Sintaxe-incorreta-pr%C3%B3xima-%C3%A0-palavra-chave-WHERE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar efetuar a **transferência de ficha médica**, através da rotina **MDTA970**, gera error log: "***Error :* 156 (37000) (RC=-1) - *[Microsoft][*SQL *Server Native Client* 11.0][SQL *Server*]*Sintaxe* incorreta próxima à palavra-chave '*WHERE*'.**  
**( From tMSSQLConnection::GetQueryFile )**  
***Thread ID* [8884] *User* [Administrador] IO [11958] *Tables* [61] *MaxTables* [62] *Comment* [MDTA970 - TCPIP - ThreadID(12928)] SP [ ] *Traced* [*No*] SQL*Replay* [*No*] *In*Tran [*No*] DBEnv [MSSQL/P1227] DB*Thread* [(SPID 52,59,54)] *Started* [03/12/2021 11:27:33] IP [127.0.0.1:2590] IDLE [ ] *InTransact* [ ] *Memory* [0] *Running* [ROP\_*QUERY* *for* 0 s.] RCV [170854] SND [1126095] TCBuild [20210202-20210930] TC*Version* [21.1.1.0] ARCH [64] OS *[WINDOWS] BUILD [RELEASE]***  
***SELECT* X2\_PATH *FROM**WHERE* X2\_CHAVE = 'TM0' on \_\_EXECSQL(APLIB300.PRW)**"**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**O erro ocorre em ambientes com o fonte **MDTA970** com data igual ou anterior a **26/11/2021**   
  
**Solução**Para correção do erro, é necessário aplicação do pacote abaixo:  
12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=1058225> ; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1058226> ; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1058227> ;  
  
**Obs.:**Devido ao Ciclo de Vida de Software TOTVS estipulado e a data da expedição desta correção (06/01/2022), esta correção **não estará disponível para a versão 12.1.25**:  
<https://tdn.totvs.com/display/public/PROT/Ciclo+de+Vida+de+Software+-+TOTVS+Linha+Protheus>   
  
**Informações complementares**Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
Pacote de Expedição Contínua do eSocial:[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>
