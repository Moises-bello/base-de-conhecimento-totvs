---
article_id: 1500000824882
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 292448f138f702d8dd5a62ecf32a639ae5adbfaab487e6d8353c662239fa31ad
fetched_at: '2026-06-28T22:42:10.871275+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Error.log Ao
  Gerar DIEF PI Através da Rotina MATA950 - Instruções Normativas
type: support-article
updated_at: '2022-08-17T20:26:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000824882-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Error-log-Ao-Gerar-DIEF-PI-Atrav%C3%A9s-da-Rotina-MATA950-Instru%C3%A7%C3%B5es-Normativas
---

**Dúvida**  
Ao gerar o arquivo da DIEF PI através da rotina MATA950 - Instruções Normativas é apresentado o error.lg baixo:

THREAD ERROR ([27172], Teste, TI18)  23/12/2020 16:05:28  
type mismatch on compare  on {|X| &(X) }(MATA950.PRX) 29/10/2020 09:21:59 line : 980  
  
[TOTVS build: 7.00.191205P-20201012]  
Called from REGNORMA(MATA950.PRX) 29/10/2020 09:21:59  
Called from {|X| INCPROC(X[16]),"",AADD(ABUFFERFIM,REGNORMA(X,@NHANDLE,@CTRAB,CDIR,CMASKVLR,LXML,APROCFIL,@ATRAB,LTSF,LQUEBRALIN,LNFSE,LEN(ABUFFERFIM)==LEN(ANORMA)-1))}(MATA950.PRX) 29/10/2020 09:21:59 line : 626  
Called from PROCNORMA(MATA950.PRX) 29/10/2020 09:21:59  
Called from { ||PROCNORMA(CNORMA,CDEST,CDIRREC,APROCFIL,@ATRAB,,,,,LAUTOMATO)}(MATA950.PRX) 29/10/2020 09:21:59 line : 203  
Called from { || FWSETSHOWKEYS( .F. ), EVAL( BACTION, @LEND ),LEND := .T. , FWSETSHOWKEYS( .T. ), ODLGMODAL:DEACTIVATE() }(MSPROCES.PRW) 13/10/2020 16:57:59 line : 104  
Called from {|SELF|(EVAL(OSELF:BINIT))}(FWDIALOGMODAL.PRW) 13/10/2020 16:57:53 line : 462  
Called from ::MSDIALOG:ACTIVATE  
Called from FWDIALOGMODAL:ACTIVATE(FWDIALOGMODAL.PRW) 13/10/2020 16:57:53 line : 462  
Called from PROCESSA(MSPROCES.PRW) 13/10/2020 16:57:59 line : 105  
Called from MATA950(MATA950.PRX) 29/10/2020 09:21:59 line : 203  
Called from \_\_EXECUTE(APLIB090.PRW) 13/10/2020 16:57:54 line : 719  
Called from MDIEXECUTE(APLIB260.PRW) 13/10/2020 16:57:54 line : 896  
 **Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
O error.log mencionando acima ocorre por motivo de estar sendo gerado o arquivo da DIEF PI através da rotina Instruções Normativas (MATA950).  
  
A rotina correta para geração da DIEF PI é através da rotina Sintegra (MATA940).  
  
Mais informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=6076394> (mesma funcionalidade para P12).
