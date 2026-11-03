---
article_id: 38643873314967
category: SIGAEST - CUSTOS
content_hash: 41343e7b7c604aab097a1b66bf7519c128c01f77c79a38735760a679afed5cb9
fetched_at: '2026-06-28T22:39:00.603932+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - argument error in
  function Len() on UPDPROMOD(MATA330MOD.PRX)
type: support-article
updated_at: '2026-02-25T21:29:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38643873314967-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-argument-error-in-function-Len-on-UPDPROMOD-MATA330MOD-PRX
---

O artigo aborda um erro no TOTVS Protheus durante o processamento de custeio de produtos MOD com integração contábil, causado por incompatibilidade na procedure CTB250. A solução recomendada é reinstalar a procedure contábil 26 e realizar novo processamento.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38643886935575) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Durante o processamento de custeio, marcando o calculo de produto MOD para serem custeados com integração contabil, ocorre o erro:

argument error in function Len() on UPDPROMOD(MATA330MOD.PRX) 01/12/2023 16:34:43 line : 809  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**

Esse erro pode ser ocasionado por alguma incompatilibilidade na procedure contabil CTB250.   
  
**Solução**  
Reinstale a procedure contabil 26 e realize um novo processamento.

Exemplo do erro gerado em produtividade:

```
THREAD ERROR ([3255078], User, TESTE)   25/02/2026 11:10:36
argument error in function Len() on UPDPROMOD(MATA330MOD.PRX) 01/12/2023 16:34:43 line : 809

[TOTVS build: 7.00.240223P-20251030]
Called from A330MODB(MATA330MOD.PRX) 01/12/2023 16:34:43 line : 155
Called from A330CALCMOD(MATA330MOD.PRX) 01/12/2023 16:34:43 line : 78
Called from MA330PROCESS(MATA330.PRX) 29/01/2026 09:18:48 line : 898
Called from {|LEND|MA330PROCESS(ALISTAFIL,LBAT,@LEND,NRATEIOFROTA,NRATEIOVEICULO,NRATEIOVIAGEM,LEXISTPROC,L331X330)}(MATA330.PRX) 29/01/2026 09:18:48 line : 443
Called from {|| FWSETSHOWKEYS( .F. ), EVAL( BACTION, @LEND ),LEND := .T. , FWSETSHOWKEYS( .T. ), ODLGMODAL:DEACTIVATE() }(MSPROCES.PRW) 03/12/2025 18:11:27 line : 123
Called from {|SELF|(EVAL(OSELF:BINIT))}(FWDIALOGMODAL.PRW) 03/12/2025 18:11:22 line : 468
Called from ::MSDIALOG:ACTIVATE
Called from FWDIALOGMODAL:ACTIVATE(FWDIALOGMODAL.PRW) 03/12/2025 18:11:22 line : 468
Called from PROCESSA(MSPROCES.PRW) 03/12/2025 18:11:27 line : 124
Called from {||  IF(MTA330TOK(),(PROCESSA({|LEND|MA330PROCESS(ALISTAFIL,LBAT,@LEND,NRATEIOFROTA,NRATEIOVEICULO,NRATEIOVIAGEM,LEXISTPROC,L331X330)},OEMTOANSI(FWI18NLANG(
"MATA330","STR0007",7)),OEMTOANSI(FWI18NLANG("MATA330","STR0011",11)), .F. ),ODLG:END()),)}(MATA330.PRX) 29/01/2026 09:18:48 line : 443
Called from ::MSDIALOG:ACTIVATE
Called from MATA330(MATA330.PRX) 29/01/2026 09:18:48 line : 445
Called from __EXECUTE(APLIB090.PRW) 03/12/2025 18:11:24 line : 735
Called from MDIEXECUTE(APLIB260.PRW) 03/12/2025 18:11:24 line : 921
```

O Erro ocorre porque a função **LEN**, tentou preencher a variavel aSaldos durante o processamento dos produtos MOD e GGF, e ocorre que essa variavel acabou passando um valor Nulo ou diferente do esperado.

Pode notar-se uma avaliação no arquivo **DBCONSOLE.LOG** do ambiente onde foi gerado o erro, pois ali vai existir a chamada da procedure, com a indicação do erro:

```
Error : 6502 - ORA-06502: PL/SQL: numeric or value error: character string buffer too small
ORA-06512: at "AMBIENTE_XTPO.CTB250_26_01", line 94
ORA-06512: at line 1
 ( From tOracleStmt::SPExec )
Thread ID [2710828]	User [Administrador]	IO [3219]	Tables [80]	MaxTables [80]	Comment [MATA330 - TCPIP - ThreadID(2712232)]	SP [CTB250_26_01]	Traced [No]	SQLReplay [No]	InTran [No]	DBEnv [ORACLE/C0Q6YO_196915_P]	DBThread [(SID 3104,6904,1)]	Started [25/02/2026 14:06:36]	IP [10.0.2.3:6000]	IDLE [ ]	InTransact [ ]	Memory [0]	Running [ROP_SPEXEC for 2 s.]	RCV [1569638]	SND [2407475]	TCBuild [20240224-20250929]	TCVersion [24.1.1.0]	ARCH [64]	OS [LINUX]	BUILD [RELEASE]	
CTB250_26_01
[ENDLOG]
[20260225 14:07:18.173][Thread 2710828][BEGINLOG]
-- CALL CTB250_26_01 ('01001','59999               ','20260101','20260131','1','00000001','               ','               ','1') FAILED.
```

Nesse caso, a reinstalação da procedure 26, ou de todas como um todo, pode reajustar as procedures para calculo.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
