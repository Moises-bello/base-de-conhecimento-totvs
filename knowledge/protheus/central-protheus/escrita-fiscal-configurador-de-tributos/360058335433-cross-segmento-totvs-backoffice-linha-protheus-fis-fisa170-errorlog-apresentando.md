---
article_id: 360058335433
category: Escrita Fiscal - Configurador de Tributos
content_hash: 366537ef714d732ce61095d18cdc813a58141bb0f8c3e6149b92efc9ab66acdf
fetched_at: '2026-06-28T22:39:17.273858+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 -  ERROR.LOG
  apresentando ao acessar a rotina?
type: support-article
updated_at: '2024-11-18T11:58:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058335433-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-ERROR-LOG-apresentando-ao-acessar-a-rotina
---

**Dúvida**

Erro.log ao solicitar a abertura da rotina Configurador de Tributos - Regras Financeiras (FISA170)

THREAD ERROR ([31979], pablot, BHZ025367) 27/10/2020 10:14:22  
F21010: DB error (Insert): -37 File: F21010 - Error : 1 - ORA-00001: unique constraint (SIGA.F21010\_UNQ) violated  
( From tISAMFile::Write )  
Thread ID [27255] User [bh35644] IO [974] Tables [53] MaxTables [53] Comment [FISA170 - TCPIP - ThreadID(31979)] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [ORACLE/ERPH1.DTC.JAMEF] DBThread [(SID 803,55218,2)] Started [27/10/2020 10:14:07] IP [172.17.8.131:1237] IDLE [ ] InTransact [0 s.] Memory [0] Running [ROP\_WRITE for 0 s.] RCV [13943] SND [73533] TCBuild [20191119-20200706] TCVersion [19.2.1.1] ARCH [64] OS [LINUX] BUILD [DEBUG]   
INSERT INTO F21010(F21\_CODIGO,F21\_UFORI,F21\_UFDEST,R\_E\_C\_N\_O\_) VALUES ( :1,:2,:3,:4)

**Ambiente**

Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
O erro ocorre por haver um registro duplicado na Tabela 12 da SX5, e no momento da carga no configurador de tributos, ocorre o erro de chave duplicada.  
  
Após identificar o registro duplicado na tabela 12 da SX5, Basta logar novamente na rotina que não haverá mais o erro.
