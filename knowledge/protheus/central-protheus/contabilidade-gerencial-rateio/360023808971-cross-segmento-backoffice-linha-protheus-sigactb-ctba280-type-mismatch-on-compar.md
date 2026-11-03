---
article_id: 360023808971
category: Contabilidade Gerencial - Rateio
content_hash: ce2a088c773371abb52ed6e0b4f2c5d0c4f529fe10e9513584b210645cb62f05
fetched_at: '2026-06-28T22:40:35.548204+00:00'
product: protheus
section_id: 1500001548962
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA280  "type mismatch
  on compare  on CTB280PROC"
type: support-article
updated_at: '2022-07-18T18:23:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023808971-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA280-type-mismatch-on-compare-on-CTB280PROC
---

**Ocorrência**Ao processar a rotina de rateio CTBA280 é gerado o error log:

THREAD ERROR ([9936], magali.morais, MC2NB0139)  13/02/2019 10:47:13  
type mismatch on compare  on CTB280PROC(CTBA280.PRW) 14/12/2018 18:31:39 line : 744

[TOTVS build: 7.00.131227A-20180425 NG]  
Called from CTB280PROC(CTBA280.PRW) 14/12/2018 18:31:39 line : 744  
Called from {|lEnd| Ctb280Proc()}(CTBA280.PRW) 14/12/2018 18:31:39 line : 744  
Called from { || FWSetShowKeys( .F. ), Eval( bAction, @lEnd ),lEnd := .t. , FWSetShowKeys( .T. ), oDlgModal:Deactivate() }(MSPROCES.PRW) 15/05/2018 17:39:50 line : 744  
Called from {|Self|(Eval(oSelf:bInit))}(FWDIALOGMODAL.PRW) 15/05/2018 17:39:45 line : 744  
Called from ::MSDIALOG:ACTIVATE line : 744  
Called from FWDIALOGMODAL:ACTIVATE(FWDIALOGMODAL.PRW) 15/05/2018 17:39:45 line : 461  
Called from PROCESSA(MSPROCES.PRW) 15/05/2018 17:39:50 line : 95  
Called from CTBA280(CTBA280.PRW) 14/12/2018 18:31:39 line : 153  
Called from \_\_EXECUTE(APLIB090.PRW) 15/05/2018 17:39:45 line : 600  
Called from FWPREEXECUTE(FWPREEXECUTE.PRW) 15/05/2018 17:39:51 line : 82  
Called from {|| FWPreExecute('Rateio Off-line', 'CTBA280()', 1, '34', 'xxxxxxxxxx') }(FWUIMENUL.PRW) 15/05/2018 17:39:50 line : 82  
Called from ::TWINDOW:ACTIVATE line : 82  
Called from MSAPP:ACTIVATE(FWAPP.PRW) 15/05/2018 17:39:50 line : 696  
Called from SIGAADV(APLIB000.PRW) 15/05/2018 17:39:45 line : 48  
Called from STATICCALL(APLIB000.PRW) 15/05/2018 17:39:45 line : 48

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus  – Contabilidade Gerencial – A partir da versão 11.80. **Causa** O error log é reproduzido pois falta a pergunta 14 na SX1 do grupo CTB280.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021264931/mceclip0.png)  
  
**Solução**

Necessário atualizar o grupo de perguntas para que pergunta  "Atualiza Saldo?" seja apresentada na SX1, GRUPO CTB280

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021265071/mceclip1.png)
