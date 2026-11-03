---
article_id: 360028990552
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 5ec7eaf81cb36a172d0efdc8eb662c525e7b6af42f7e37d356779a0d8507f7c9
fetched_at: '2026-06-28T22:38:31.194776+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Erro no Oracle ao faturar - Quoted string not properly terminated
type: support-article
updated_at: '2021-04-28T15:54:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028990552-MP-FAT-Erro-no-Oracle-ao-faturar-Quoted-string-not-properly-terminated
---

**Ocorrência**Ao faturar a nota de saída (**MATA461**), gera o erro:

**: Error : 1756 - ORA-01756: quoted string not properly terminated**  
 **( From tOracleConnection::GetQueryFile )**  
**Thread ID [9840] User [VANESSA NATHALIA] IO [5468] Tables [154] MaxTables [154] Comment [VDAGL001 - TCPIP - ThreadID(41302)] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [ORACLE/PROTHEUSPRD12] DBThread [(SID 1971,55353,1)] Started [07/06/2019 12:35:15] IP [192.168.7.102:11239] IDLE [ ] InTransact [13 s.] Memory [4113992] Running [ROP\_QUERY] RCV [1726679] SND [4288196] TCBuild [20171117-20180412]**   
**SELECT CE1\_LOJISS,CE1\_FORISS FROM CE1010 WHERE CE1\_FILIAL = '27' AND CE1\_ESTISS = 'MG' AND CE1\_CMUISS = '54457'' AND CE1\_PROISS = '00010201 ' on A040DUPREC(FINXFIN.PRX) 12/04/2019 11:46:05 line : 9768**  
  
 **Ambiente**

Microsiga Protheus - todas as versões.  
   
 **Causa**

O erro : Error : 1756 - ORA-01756: quoted string not properly terminated, ocorre por o código do município passado para o campo está sendo enviado para a gravação do Oracle está com apostrofo, veja o trecho do erro:  
  
SELECT CE1\_LOJISS,CE1\_FORISS FROM CE1010 WHERE  CE1\_FILIAL = '27' AND CE1\_ESTISS = 'MG' AND **CE1\_CMUISS = '54457''** AND CE1\_PROISS = '00010201 ' on A040DUPREC(FINXFIN.PRX)  
  
**Local 121: CMUN(C) :54457'**  
 Local 122: CUF(C) :MG  
 Local 123: CCONSULTA(C) :SELECT CE1\_LOJISS,CE1\_FORISS FROM CE1010 WHERE  CE1\_FILIAL = '27' AND CE1\_ESTISS = 'MG' AND CE1\_CMUISS = '54457''  AND CE1\_PROISS = '00010201 '  
  
**Field 14: A1\_COD\_MUN(C) :54457' ---> código de  município com carácter especial**  
  
**Solução**

Altere o campo **A1\_COD\_MUN (MATA030),** deixando o código do município sem o uso do apostrofo para que o erro deixe de ocorrer.
