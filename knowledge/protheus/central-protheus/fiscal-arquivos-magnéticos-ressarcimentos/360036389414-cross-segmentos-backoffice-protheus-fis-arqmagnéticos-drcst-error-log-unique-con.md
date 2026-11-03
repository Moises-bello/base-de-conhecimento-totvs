---
article_id: 360036389414
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: f5be694b318f7f8f90c6f67dce00416741c06142173fe2d4c77ab3d3464f05df
fetched_at: '2026-06-28T22:42:12.693178+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DRCST - Error
  log: unique constraint (TOTVS_V12.F1M010_UNQ) violated.'
type: support-article
updated_at: '2022-08-18T17:55:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036389414-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DRCST-Error-log-unique-constraint-TOTVS-V12-F1M010-UNQ-violated
---

**Ocorrência**Ao realizar a apuração do ressarcimento do ICMS ST através da rotinda FISA230 é apresentado o error log a seguir:

THREAD ERROR ([77056], edy, SRVPRODESEN) 28/08/2019 13:36:15  
DB error (Insert): -37 File: F1M010 - Error : 1 - ORA-00001: unique constraint (TOTVS\_V12.F1M010\_UNQ) violated  
 ( From tISAMFile::Write )  
Thread ID [27620] User [edy] IO [69044] Tables [29] MaxTables [30] Comment [FISA230 - TCPIP - ThreadID(77056)] SP [ ] Traced [No] SQLReplay [No] InTran [Yes] DBEnv [ORACLE/HML] DBThread [(SID 1636,8087,1)] Started [28/08/2019 11:29:31] IP [172.17.1.129:7900] IDLE [ ] InTransact [7491 s.] Memory [1751456] Running [ROP\_WRITE] RCV [39161834] SND [24226467] TCBuild [20171117-20180412]   
INSERT INTO F1M010(F1M\_FILIAL,F1M\_IDAPUR,F1M\_ANOMES,F1M\_PRODUT,F1M\_ORDEM,F1M\_DTMOV,F1M\_TPMOV,F1M\_INDOP,F1M\_NFISCA,F1M\_SERIE,F1M\_ITEM,F1M\_CFOP,F1M\_ESPECI,F1M\_CHVDOC,F1M\_SERECF,F1M\_PARTIC,F1M\_LOJA,F1M\_CNPJ,F1M\_QTDMOV,F1M\_UNIDAD,F1M\_FATCON,F1M\_QTDCON,F1M\_VLRCON,F1M\_BASICM,F1M\_ALQICM,F1M\_VLRICM,F1M\_BASIST,F1M\_ALQIST,F1M\_VLRIST,F1M\_CODAJU,F1M\_CODDA,F1M\_NMDARE,F1M\_CODRES,F1M\_INDSAI,F1M\_NUMPDV,F1M\_COO,R\_E\_C\_N\_O\_) VALUES ( :1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29,:30,:31,:32,:33,:34,:35,:36,:37)  
-- Binded Parameters List --  
#1 [C] [05]  
#2 [C] [2e47ab94-b1fd-b134-1df1-e96b8fe9f20a]  
#3 [C] [201901]  
#4 [C] [1014010037 ]  
#5 [C] [000000001]  
#6 [D] [20160728]  
#7 [C] [S]  
#8 [C] [1]  
#9 [C] [004577 ]  
#10 [C] [4 ]  
#11 [C] [01 ]  
**#12 [C] [6411 ]**  
#13 [C] [SPED ]  
#14 [C] [42160786365350000681550040000045771003895550]  
#15 [C] [ ]  
#16 [C] [496722]  
#17 [C] [81]  
   
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
   
 **Causa**O error log aponta uma nota fiscal de Devolução de Compra de CFOP 6411. O erro ocorre porque o sistema não conseguiu localizar a nota fiscal original (Compra).  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
  
 1. Verifique se tanto o CFOP da devolução de compra quanto o CFOP da compra estão sendo considerados no **Cadastro de Regras para Movimentos**. Neste caso, o error log estava ocorrendo porque o CFOP 2403 (Nota fiscal de compra) havia sido excluído da Regra, então, o sistema leu a nota fiscal de devolução, porém, não encontrou a nota fiscal original.

2. Para solucionar este erro, foi necessário incluir novamente o CFOP 2403 no cadastro de Regras.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048450333/mceclip0.png)

Para mais informações sobre a rotina de apuração do Ressarcimento, Restituição e Complemento do ICMS, consulte a documentação abaixo:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=484701377>
