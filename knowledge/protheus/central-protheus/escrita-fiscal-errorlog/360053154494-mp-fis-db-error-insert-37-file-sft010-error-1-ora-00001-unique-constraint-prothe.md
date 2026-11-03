---
article_id: 360053154494
category: Escrita Fiscal - Error.log
content_hash: e3d0a05d2f101fbe36b4a9bbc52d116238d5e18d90818d8c9c96ecd883bb21ac
fetched_at: '2026-06-28T22:39:32.912166+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: 'MP - FIS - DB error (Insert): -37 File: SFT010 - Error : 1 - ORA-00001: unique
  constraint (PROTHEUS.SFT010_UNQ) violated'
type: support-article
updated_at: '2021-04-28T19:11:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053154494-MP-FIS-DB-error-Insert-37-File-SFT010-Error-1-ORA-00001-unique-constraint-PROTHEUS-SFT010-UNQ-violated
---

**Dúvida**THREAD ERROR ([112156], XXXXX) 20/08/2020 10:44:59  
SFT010: DB error (Insert): -37 File: SFT010 - Error : 1 - ORA-00001: unique constraint (PROTHEUS.SFT010\_UNQ) violated  
 ( From tISAMFile::Write )  
Thread ID [51632] User [Adrian] IO [8291] Tables [163] MaxTables [164] Comment [MATA103 - TCPIP - ThreadID(112156)] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [ORACLE/COOPEAVI] DBThread [(SID 6798,60174,1)] Started [20/08/2020 10:11:34] IP [10.1.1.31:1409] IDLE [ ] InTransact [4 s.] Memory [0] Running [ROP\_WRITE for 0 s.] RCV [661170] SND [4464374] TCBuild [20191119-20200706] TCVersion [19.2.1.1] ARCH [64] OS [WINDOWS] BUILD [RELEASE]   
INSERT INTO SFT010(FT\_FILIAL,FT\_ENTRADA,FT\_EMISSAO,FT\_NFISCAL,FT\_SERIE,FT\_CLIEFOR,FT\_LOJA,FT\_ESTADO,FT\_CFOP,FT\_ALIQICM,FT\_VALCONT,FT\_BASEICM,FT\_VALICM,FT\_ISENICM,FT\_OBSERV,FT\_TIPO,FT\_PDV,FT\_ESPECIE,FT\_CREDST,FT\_PRODUTO,FT\_TIPOMOV,FT\_ITEM,FT\_CLASFIS,FT\_CTIPI,FT\_POSIPI,FT\_IDENTF3,FT\_ESTOQUE,FT\_DESPIPI,FT\_QUANT,FT\_PRCUNIT,FT\_TOTAL,FT\_SERORI,FT\_ITEMORI,FT\_RECISS,FT\_CHVNFE,FT\_CSTPIS,FT\_CSTCOF,FT\_CODBCC,FT\_TPPRODE,FT\_TNATREC,FT\_CNATREC,FT\_AGREG,FT\_CODISS,FT\_IDSFB,FT\_IDSFC,FT\_IDSB5,FT\_IDSED,FT\_IDSF7,FT\_IDSA2,FT\_IDSBZ,FT\_IDCFC,FT\_CV139,FT\_SERSAT,FT\_CEST,FT\_ATIVCPB,FT\_CLIDEST,FT\_LOJDEST,FT\_BSICMOR,FT\_TAFKEY,FT\_TES,FT\_SDOC,FT\_SDOCORI,FT\_LOJDVMC,FT\_CLIDVMC,FT\_COLVDIF,R\_E\_C\_N\_O\_) VALUES ( :1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37,:38,:39,:40,:41,:42,:43,:44,:45,:46,:47,:48,:49,:50,:51,:52,:53,:54,:55,:56,:57,:58,:59,:60,:61,:62,:63,:64,:65,:66)  
-- Binded Parameters List --  
#1 [C] [47]  
#2 [D] [20200731]  
#3 [D] [20200729]  
#4 [C] [000004259]  
#5 [C] [1 ]  
#6 [C] [139803]  
#7 [C] [01]  
#8 [C] [ES]  
#9 [C] [1201 ]  
#10 [N] [17.000000]  
#11 [N] [1.000000]  
#12 [N] [0.180000]  
#13 [N] [0.030000]  
#14 [N] [0.820000]  
#15 [C] [ ]  
#16 [C] [D]  
#17 [C] [ ]  
#18 [C] [SPED ]  
#19 [C] [ ]  
#20 [C] [029610 ]  
#21 [C] [E]  
#22 [C] [0001]  
#23 [C] [020]  
#24 [C] [49]  
#25 [C] [04051000 ]  
#26 [C] [000001]  
#27 [C] [S]  
#28 [C] [S]  
#29 [N] [1.000000]  
#30 [N] [1.000000]  
#31 [N] [1.00 - Integrity failure. on ENDTRAN(APLIB060.PRW) 05/03/2020 22:36:09 line : 220  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para identificar a causa do error.log, será necessário verificar se esta sendo utilizado algum ponto de entrada no processo utilizado pelo cliente.

No exemplo acima, foi identificado o ponto de entrada "MA030ROT e SD1100I ", abaixo trecho do erro mencionando os pontos de entradas impactando no processo:   
  
d:\totvs\protheus\protheus\_data\system\xx6010.dtc; Rdd:DBFCDX; Alias:XX6; Filter :; Recno:1; Total Recs:2130; Order:2  
 Index (0) :I\_RECNO   
 Index (1) :\*\*XX60101 XX6\_CODFUN+XX6\_TYPE  
 Index (2) :XX60102 XX6\_DESC+XX6\_CODFUN  
 Field 1: D\_E\_L\_E\_T\_E\_D(C) :   
 Field 2: R\_E\_C\_N\_O(N) :1  
 **Field 3: XX6\_CODFUN(C) :MA030ROT**  
 Field 4: XX6\_TYPE(C) :2  
 Field 5: XX6\_DESC(C) :Incluído automaticamente pelo sistema-03/07/10   
 d:\totvs\protheus\protheus\_data\system\xx7010.dtc; Rdd:DBFCDX; Alias:XX7; Filter :; Recno:129; Total Recs:2130; Order:2  
 Index (0) :I\_RECNO   
 Index (1) :\*\*XX70101 XX7\_CODFUN+XX7\_TYPE+XX7\_FILIAL  
 Index (2) :XX70102 XX7\_TYPE+XX7\_CODFUN+XX7\_FILIAL  
 Field 1: D\_E\_L\_E\_T\_E\_D(C) :   
 Field 2: R\_E\_C\_N\_O(N) :129  
 F**ield 3: XX7\_CODFUN(C) :SD1100I**   
 Field 4: XX7\_TYPE(C) :1  
 Field 5: XX7\_FILIAL(C) :   
 Field 6: XX7\_STATUS(C) :1  
 Field 7: XX7\_DEFRET(C)   
  
Para certificar se o ponto de entrada está impactando no processo, será necessário desabilitar os pontos de entrada através da chave IXBLOG=NORUN.
