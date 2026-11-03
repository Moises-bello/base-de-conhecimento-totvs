---
article_id: 360006975951
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 8f4d57059d15019f9ec51e43724288c9f75621afe38ff70bb91e76712e894361
fetched_at: '2026-06-28T22:40:47.590040+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: MP - SIGACTB - ECF -dbo.CH8010' with unique index 'CH8010_UNQ
type: support-article
updated_at: '2023-08-16T19:41:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006975951-MP-SIGACTB-ECF-dbo-CH8010-with-unique-index-CH8010-UNQ
---

**Ocorrência**

TAF : Erro apresentado ao realizar a Integração com o TAF.

01/07/2018 15:25:35 : Error : 2601 (23000) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]Cannot insert duplicate key row in object 'dbo.CH8010' with unique index 'CH8010\_UNQ'. ( From tISAMFile::Update )   
Thread ID [7056] User [USUARIO] IO [11555] Tables [20] MaxTables [20] Comment [TAF - Thread( 01 ) - Processamento autocontidas Empresa/Filial: 01/01] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [MSSQL/P12\_HOMOLOGACAO] DBThread [(SPID 56)] Started [01/07/2018 14:45:03] IP [10.1.0.3:1241] IDLE [ ] InTransact [4 s.] Memory [936672] Running [ROP\_UPDATE] RCV [16650196] SND [19090243] TCBuild [20171117-20180412]  
UPDATE dbo.CH8010 SET CH8\_CODIGO = ?,CH8\_DESCRI = ? WHERE R\_E\_C\_N\_O\_ = ?   
   
 **Ambiente**  
Protheus – TAF – Versão P12.1.17  
   
  
 **Solução**

* **Em base teste :**
* **Realize uma copia da tabela CH8**
* **Dropar a tabela**
* **Limpar o conteúdo do parâmetro  MV\_VAUTCON**
* **Executar Autocontida**
