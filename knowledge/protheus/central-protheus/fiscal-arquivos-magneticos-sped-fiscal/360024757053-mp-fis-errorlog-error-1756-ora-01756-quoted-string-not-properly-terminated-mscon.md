---
article_id: 360024757053
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 227389ad239df601df440b0f7aaf9dd9b5914f3f4b339c6a4119f08b1a69693f
fetched_at: '2026-06-28T22:42:03.779986+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'MP - FIS - Error.log - Error : 1756 - ORA-01756: quoted string not properly
  terminated - MSCONHIST(MATXFUNC.PRX)'
type: support-article
updated_at: '2021-04-28T14:25:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024757053-MP-FIS-Error-log-Error-1756-ORA-01756-quoted-string-not-properly-terminated-MSCONHIST-MATXFUNC-PRX
---

**Dúvida**Ao gerar o SPED FISCAL esta sendo apresentado o error.log abaixo:

THREAD ERROR ([3984], Sistem, MTZ-TREI001) 12/06/2019 12:14:30  
: Error : 1756 - ORA-01756: quoted string not properly terminated  
 ( From tOracleConnection::GetQueryFile )  
Thread ID [4896] User [Marcela.Santos] IO [747413] Tables [106] MaxTables [107] Comment [SPEDFISCAL - TCPIP - ThreadID(3984)] SP [ ] Traced [No] SQLReplay [No] InTran [No] DBEnv [ORACLE/ORAINST] DBThread [(SID 2958,35417,2)] Started [12/06/2019 10:42:59] IP [172.16.10.42:12004] IDLE [ ] InTransact [ ] Memory [-141233152] Running [ROP\_QUERY] RCV [222069027] SND [414292379] TCBuild [20181212-20190211] TCVersion [18.2.1.0] ARCH [64] OS [WINDOWS] BUILD [RELEASE]   
SELECT \* FROM AIF010 AIF WHERE AIF.AIF\_FILIAL='01001001' AND AIF.AIF\_FILTAB='01 ' AND AIF.AIF\_TABELA='SA4' AND AIF.AIF\_TRANSP='00000'' AND AIF.AIF\_DATA>='20190501' AND AIF.AIF\_DATA<='20491231' AND AIF.D\_E\_L\_E\_T\_=' ' ORDER BY AIF\_FILIAL,AIF\_FILTAB,AIF\_TABELA,AIF\_TRANSP,AIF\_DATA on MSCONHIST(MATXFUNC.PRX) 11/06/2018 10:26:23 line : 8928

[TOTVS build: 7.00.131227A-20181218 NG]  
Called from MSCONHIST(MATXFUNC.PRX) 11/06/2018 10:26:23 line : 8928  
Called from PRSPED(SPEDFISCAL.PRW) 12/12/2018 11:06:57 line : 995  
Called from {|oSay|PrSped(@lEnd,@cFileDest,cPerfil,oSay,lTabComp,lTabCDT,lTabCD0,lTabCE5,lIntTMS,aWizScreen,lTabCD1)}(SPEDFISCAL.PRW) 12/12/2018 11:06:57 line : 995  
Called from {|| Eval(bAction, oSay), oDlgSVG:End() }(FWMSGRUN.PRW) 23/10/2018 18:06:47 line : 995  
Called from ::FWSTYLEDDIALOG:ACTIVATE line : 995  
Called from FWMSGRUN(FWMSGRUN.PRW) 23/10/2018 18:06:47 line : 100  
Called from SPEDFISCAL(SPEDFISCAL.PRW) 12/12/2018 11:06:57 line : 77  
Called from \_\_EXECUTE(APLIB090.PRW) 23/10/2018 18:06:47 line : 636  
Called from MDIEXECUTE(APLIB260.PRW) 23/10/2018 18:06:47 line : 836  
Called from STATICCALL(APLIB260.PRW) 23/10/2018 18:06:47 line : 836

**Ambiente**  
Protheus – Livos Fiscais – A partir da versão 11.80  
  
**Solução**O problema está no campo F2\_TRANSP, onde o mesmo está preenchido com uma aspa no final do preenchimento do campo.  
  
Retire a mesma do campo da SF2 para a solução do problema, verifique se no cadastro da transportadora o mesmo está preenchido com a aspa.  
  
 Field 177: F2\_TRANSP(C) :00000'  
  
Apos a correção do campo F2\_TRANSP na SF2 o erro será solucionado.
