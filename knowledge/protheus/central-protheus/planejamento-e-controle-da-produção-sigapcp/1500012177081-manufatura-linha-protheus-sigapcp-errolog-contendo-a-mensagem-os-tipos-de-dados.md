---
article_id: 1500012177081
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4ba9d1425d14f88dd40194362ae497040ab7b651ca6a7b7374949d024561ed11
fetched_at: '2026-06-28T22:42:42.301130+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Errolog contendo a mensagem Os tipos
  de dados image e image são incompatíveis no operador equal to ao atualizar a demanda
  ou em inglês The data types image and image are incompatible in the equal to operator
type: support-article
updated_at: '2022-11-17T14:19:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012177081-Manufatura-Linha-Protheus-SIGAPCP-Errolog-contendo-a-mensagem-Os-tipos-de-dados-image-e-image-s%C3%A3o-incompat%C3%ADveis-no-operador-equal-to-ao-atualizar-a-demanda-ou-em-ingl%C3%AAs-The-data-types-image-and-image-are-incompatible-in-the-equal-to-operator
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:30 min**  
**Ocorrência**Ao atualizar as demandas através do **PCPA136 - Demandas do MRP** ocorre a mensagem **Os tipos de dados image e image são incompatíveis no operador equal to** ou a mensagem em inglês **The data types image and image are incompatible in the equal to operator**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem ocorre quando os campos **memo** das tabelas relacionadas na expressão **SQL - Standard Query Language** possuem tipos diferentes no banco de dados  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Observe a expressão **SQL** listada logo abaixo da mensagem;  
2. Nesta expressão **SQL**, verifique quais são as tabelas que possuem campos **\_MOPC - Memo** listados;  
3. Faça um *backup* dessas tabelas;  
4. Delete do banco de dados;  
5. No **dbaccess.ini** inclua a chave **MemoAsBlob=1**;  
6. Reinicie o **dbaccess** e o **appserver**;  
6. Acesse as rotinas que criam essas tabelas para que as tabelas sejam recriadas;  
7. Restaure o *backup*.  
  
**Exemplo:**Considerando a mensagem de erro:  
**: Error : 402 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Os tipos de dados image e image são incompatíveis no operador equal to.**  
**( From tMSSQLConnection::GetQueryFile )**  
**Thread ID [10516] User [newbridge] IO [651] Tables [29] MaxTables [30] Comment [PCPA136 - TCPIP - ThreadID(16648)] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [MSSQL/DADOSP12] DBThread [(SPID 61,63)] Started [10/05/2021 21:28:30] IP [10.1.2.62:1413] IDLE [ ] InTransact [1 s.] Memory [0] Running [ROP\_QUERY for 0 s.] RCV [25381] SND [25097] TCBuild [20200606-20201012] TCVersion [20.1.1.0] ARCH [64] OS [WINDOWS] BUILD [RELEASE]**   
**SELECT TMP.RECPRV RECPREVISAO, SVR.R\_E\_C\_N\_O\_ RECDEMANDA FROM SVR010 SVR, dbo.##TMPSC00\_61 TMP, SC4010 SC4 WHERE SVR.VR\_FILIAL = '01' AND SVR.VR\_CODIGO = 'TST202105 ' AND SVR.VR\_TIPO = '2' AND SVR.VR\_REGORI = TMP.RECPRV AND SVR.D\_E\_L\_E\_T\_ = ' ' AND SC4.R\_E\_C\_N\_O\_ = SVR.VR\_REGORI AND EXISTS( SELECT 1 FROM SC6010 SC6, SF4010 SF4 WHERE SC6.C6\_FILIAL = '01' AND SC6.C6\_PRODUTO = SC4.C4\_PRODUTO AND (SC6.C6\_BLQ = ' ' OR SC6.C6\_BLQ = 'N ') AND SC6.C6\_QTDENT < SC6.C6\_QTDVEN AND SC6.D\_E\_L\_E\_T\_ = ' ' AND SF4.F4\_FILIAL = '01' AND SF4.F4\_CODIGO = SC6.C6\_TES AND SF4.F4\_ESTOQUE = 'S' AND SF4.D\_E\_L\_E\_T\_ = ' ' AND ((SC6.C6\_MOPC IS NULL AND SC4.C4\_MOPC IS NULL) OR (SC6.C6\_OPC = SC4.C4\_OPC) OR (SC6.C6\_MOPC = SC4.C4\_MOPC) ) AND SC6.C6\_OP <> '02' AND SC6.C6\_ENTREG >= SC4.C4\_DATA AND YEAR( CAST(SC4.C4\_DATA AS DATE)) = YEAR( CAST(SC6.C6\_ENTREG AS DATE)) AND MONTH(CAST(SC4.C4\_DATA AS DATE)) = MONTH(CAST(SC6.C6\_ENTREG AS DATE)) AND ((DAY(CAST(SC4.C4\_DATA AS DATE)) BETWEEN 1 AND 15 AND DAY(CAST(SC6.C6\_ENTREG AS DATE)) BETWEEN 1 AND 15) OR (DAY(CAST(SC4.C4\_DATA AS DATE)) BETWEEN 16 AND 31 AND DAY(CAST(SC6.C6\_ENTREG AS DATE)) BETWEEN 16 AND 31)) ) ORDER BY SVR.VR\_FILIAL, SVR.VR\_CODIGO, SVR.VR\_DATA, SVR.VR\_PROD on PRCQTDPREV(PCPA136IMP.PRW) 08/04/2021 23:03:32 line : 1600**  
Observe que as os campos **\_MOPC** relacionados são **C6\_MOPC - Memo** e **C4\_MOPC - Memo**. Neste caso, execute os passos abaixo:  
  
1. Faça um *backup* das tabelas **SC6 - Pedido de Venda** e **SC4 - Previsão de Venda;**  
2. Delete do banco de dados essas duas tabelas;  
3. No **Dbaccess** inclua a chave **MemoAsBlob=1**;4. Reinicie o **dbaccess** e o **appserver**;5. Acesse as rotinas **MATA410 - Pedido de Venda** e **MATA700 -  Previsão de Vendas** para que as tabelas sejam recriadas;  
6. Restaure o *backup*.
