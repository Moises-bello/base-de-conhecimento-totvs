---
article_id: 360052783994
category: Escrita Fiscal - Error.log
content_hash: 42a6cc0ef7ea9ef1b4f3034748bc4e4c4ebcfc8906ad71b1e3010e2742335b18
fetched_at: '2026-06-28T22:39:32.915168+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: 'MP - FIS - DB error (Update): -29 File: SFT010 - Error : 1 - ORA-00001: unique
  constraint (PROTHEUS.SFT010_UNQ) violated'
type: support-article
updated_at: '2021-04-28T20:44:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052783994-MP-FIS-DB-error-Update-29-File-SFT010-Error-1-ORA-00001-unique-constraint-PROTHEUS-SFT010-UNQ-violated
---

**Dúvida**  
THREAD ERROR ([29800], XXXXX, ADMDEV01) 20/08/2020 08:58:55  
SFT010: DB error (Update): -29 File: SFT010 - Error : 1 - ORA-00001: unique constraint (PROTHEUS.SFT010\_UNQ) violated  
 ( From tISAMFile::Update )  
Thread ID [194380] User [XXXX] IO [21313] Tables [137] MaxTables [138] Comment [MATA103 - TCPIP - ThreadID(29800)] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [ORACLE] DBThread [(SID 21,14615,1)] Started [21/08/2020 08:43:46] IP [11.2.4.31:2459] IDLE [ ] InTransact [6 s.] Memory [0] Running [ROP\_UPDATE for 0 s.] RCV [1083571] SND [8463900] TCBuild [20191119-20200706] TCVersion [19.2.1.1] ARCH [64] OS [WINDOWS] BUILD [RELEASE]   
UPDATE SFT010 SET D\_E\_L\_E\_T\_ = :1,R\_E\_C\_D\_E\_L\_ = :2 WHERE R\_E\_C\_N\_O\_ = :3  
-- Binded Parameters List --  
#1 [C] [ ]  
#2 [R] [0]  
#3 [N] [31868430.000000]  
 on RECLOCKED(APLIB060.PRW) 05/03/2020 22:36:09 line : 599  
   
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para identificar a causa do error.log, será necessário verificar se esta sendo utilizado algum ponto de entrada no processo utilizado pelo cliente.

No exemplo acima, foi identificado o ponto de entrada "MT103DRF", abaixo trecho do erro mencionando o ponto de entrada:   
  
d:\totvs\protheus\protheus\_data\system\xx7010.dtc; Rdd:DBFCDX; Alias:XX7; Filter :; Recno:592; Total Recs:2130; Order:2  
    Index (0) :I\_RECNO   
    Index (1) :\*\*XX70101  XX7\_CODFUN+XX7\_TYPE+XX7\_FILIAL  
    Index (2) :XX70102  XX7\_TYPE+XX7\_CODFUN+XX7\_FILIAL  
    Field 1: D\_E\_L\_E\_T\_E\_D(C) :  
    Field 2: R\_E\_C\_N\_O(N) :592  
**Field 3: XX7\_CODFUN(C) :MT103DRF**  
    Field 4: XX7\_TYPE(C) :1  
    Field 5: XX7\_FILIAL(C) :   
    Field 6: XX7\_STATUS(C) :1  
    Field 7: XX7\_DEFRET(C)  
  
Para certificar se o ponto de entrada está impactando no processo, será necessário desabilitar os pontos de entrada através da chave IXBLOG=NORUN.
