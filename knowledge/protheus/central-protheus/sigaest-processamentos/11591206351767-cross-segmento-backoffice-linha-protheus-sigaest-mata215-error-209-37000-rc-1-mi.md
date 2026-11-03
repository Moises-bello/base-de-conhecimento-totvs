---
article_id: 11591206351767
category: SIGAEST - PROCESSAMENTOS
content_hash: 20a9a6789d3d5d8617323462a755ce818e54359769a438b3a31eee2f0679ee28
fetched_at: '2026-06-28T22:39:04.922471+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA215 - Error :
  209 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Ambiguous
  column name ''C6_NUM'
type: support-article
updated_at: '2023-01-11T18:02:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11591206351767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA215-Error-209-37000-RC-1-Microsoft-SQL-Server-Native-Client-11-0-SQL-Server-Ambiguous-column-name-C6-NUM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao processar a rotina REFAZ EMPENHOS (MATA215) apresenta o error.log abaixo

THREAD ERROR ([17640], \*\*\*\*\*\*\*, )  02/02/2022

: Error : 209 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]***Ambiguous column name 'C6\_NUM'.***  
Error : 209 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]***Ambiguous column name 'C6\_ITEM'.***  
Error : 209 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]***Ambiguous column name 'C6\_PRODUTO'.***  
 ( From tMSSQLConnection::GetQueryFile )  
Thread ID [15700]    User [HELTON.SILVA]    IO [328681]    Tables [79]    MaxTables [79]    Comment [MATA215 - TCPIP - ThreadID(17640)]    SP [ ]    Traced [No]    SQLReplay [No]    InTran [No]    DBEnv [MSSQL/P12]    DBThread [(SPID 56,57,60)]    Started [02/02/2022 22:38:40]    IP [192.168.0.238:2351]    IDLE [ ]    InTransact [ ]    Memory [0]    Running [ROP\_QUERY for 0 s.]    RCV [5235481]    SND [47454137]    TCBuild [20210202-20210930]    TCVersion [21.1.1.0]    ARCH [64]    OS [WINDOWS]    BUILD [RELEASE]     
SELECT SC6.C6\_FILIAL,SC6.C6\_NUM,SC6.C6\_ITEM,SC6.C6\_PRODUTO,SC6.C6\_BLQ,SC6.C6\_NUMOS,SC6.C6\_QTDEMP,SC6.C6\_NUMOSFA,SC6.C6\_QTDENT,SC6.C6\_RESERVA,SC6.C6\_TES,SC6.C6\_NUMLOTE,SC6.C6\_CLI,SC6.C6\_LOCAL,SC6.C6\_LOTECTL,SC6.C6\_LOJA,SC6.C6\_QTDVEN,SC6.C6\_OP,SC6.C6\_NUMSERI,SC6.C6\_LOCALIZ,SC6.C6\_QTDRESE,SC6.C6\_DTVALID,SC6.C6\_QTDLIB,SC6.C6\_PRCVEN,SC6.C6\_PRUNIT,SC6.C6\_VALDESC,SC6.C6\_VALOR,SC6.C6\_UNSVEN,SC6.C6\_ENTREG,SC6.C6\_DATFAT,SC6.C6\_DESCONT,SC6.C6\_QTDLIB2,SC6.R\_E\_C\_N\_O\_ SC6RECNO,SC6TMP.RECNOSB1 SB1RECNO,SC6.C6\_QTDEMP2,SC6.C6\_QTDENT2 FROM SC6SB0 SC6 INNER JOIN DBO.##TMPSC00\_56 SC6TMP ON SC6.C6\_NUM = SC6TMP.C6\_NUM AND SC6.C6\_ITEM = SC6TMP.C6\_ITEM AND SC6.C6\_PRODUTO = SC6TMP.C6\_PRODUTO AND SC6.R\_E\_C\_N\_O\_ = SC6TMP.RECNOSC6 AND SC6TMP.EXISTSB1 ='1' WHERE  SC6.C6\_FILIAL='01' AND SC6.D\_E\_L\_E\_T\_=' '  ORDER BY  C6\_FILIAL,C6\_NUM,C6\_ITEM,C6\_PRODUTO  on A215ATUSC6(MATA215.PRX) 25/08/2021 18:07:44 line : 2752  
  
[TOTVS build: 7.00.210324P-20211006]  
Called from MA215PROC(MATA215.PRX) 25/08/2021 18:07:44 line : 1253  
Called from {|LEND| MA215PROC(LBAT,OOBJ,LNEWPROC)}(MATA215.PRX) 25/08/2021 18:07:44 line : 115  
Called from {|| EVAL(SELF:BACTION,@SELF:LEND,@SELF),SELF:LEND := .T. ,SELF:ODLG:END()}(MSNEWPROC.PRW) 12/11/2021 14:43:28 line : 66  
Called from ::MSDIALOG:ACTIVATE  
Called from MSNEWPROCESS:ACTIVATE(MSNEWPROC.PRW) 12/11/2021 14:43:28 line : 68  
Called from MA215DO(MATA215.PRX) 25/08/2021 18:07:44 line : 116  
Called from {|| IF(MA215DO(LBAT),FECHABATCH(), .F. ) }(MATA215.PRX) 25/08/2021 18:07:44 line : 66  
Called from ::MSDIALOG:ACTIVATE  
Called from FORMBATCH(MATXFUNB.PRX) 09/09/2021 22:15:11 line : 2891  
Called from MATA215(MATA215.PRX) 25/08/2021 18:07:44 line : 77  
Called from \_\_EXECUTE(APLIB090.PRW) 12/11/2021 14:43:23 line : 721  
Called from MDIEXECUTE(APLIB260.PRW) 12/11/2021 14:43:23 line : 924

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Esse incidente ocorre, no SQL 2008. Esse banco não tem mais suporte pela Microsoft e confirme link abaixo e não esta mais homologado pela TOTVS  
  
  
**Solução**

Efetuar testes com SQL atualizado e versão homologada pela TOTVS.​ Recomendamos que faça atualização do SQL em uma base de homologação, realizar o backup das informações.  
  
***Documentação sobre os bancos homologados pela TOTVS.  
<https://tdn.totvs.com/display/tec/DBAccess+-+Banco+de+dados>  
  
Documentação sobre a versão de SQL 2008.  
<https://tdn.totvs.com/pages/releaseview.action?pageId=384578531>***

***Dica:***Para os casos em que não pode migrar para uma versão mais atualizada do SQL:

O recomendado ao cliente utilizar algum banco de dados homologado, ou em caso ele esteja com problema financeiro por exemplo para atualizar o SGBD, poderia esta utilizar o PostgreSQL como seu principal SGBD, este banco de dados é gratuito e não teria mais problema desse tipo.  
  
Hoje o banco de dados postgreSQL esta muito bem documentado pela engenharia da TOTVS.  
  
***Instalado o PostgreSQL e subindo para o Protheus.***  
***<https://tdn.totvs.com/display/public/PROT/Protheus+com+PostgreSQL+-+Linux>***  
  
***Dicas de como Migrar o SQL Server para PostgreSQL (Passo a Passo)***  
***<https://tdn.totvs.com/pages/releaseview.action?pageId=642410484>***

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*
