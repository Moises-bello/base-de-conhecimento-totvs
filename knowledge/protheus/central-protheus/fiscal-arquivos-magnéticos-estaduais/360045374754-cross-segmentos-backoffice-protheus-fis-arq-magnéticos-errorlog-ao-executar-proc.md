---
article_id: 360045374754
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: ab74a0ad2f692fa83d17a2f3dafaa8e9e313bf6d99f73a7472da9694859111ce
fetched_at: '2026-06-28T22:42:09.176732+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Error.log ao
  Executar Processamento do Arquivo TXT do Sintegra
type: support-article
updated_at: '2025-02-25T22:09:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045374754-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Error-log-ao-Executar-Processamento-do-Arquivo-TXT-do-Sintegra
---

**Dúvida**Error.log ao Executar Processamento do Arquivo TXT do Sintegra:

THREAD ERROR ([2956], pbtributario3, CONT-4W2R0Y1) 11/03/2020 10:37:08  
array out of bounds ( 0 of 1 ) on SINTEGRA(MATA940.PRX) 05/02/2020 15:28:02 line : 2814

[TOTVS build: 7.00.170117A-20200102]  
Called from {|X| &(X) }(MATA950.PRX) 06/02/2020 13:45:26 line : 977  
Called from REGNORMA(MATA950.PRX) 06/02/2020 13:45:26  
Called from {|X| INCPROC(X[16]),"",AADD(ABUFFERFIM,REGNORMA(X,@NHANDLE,@CTRAB,CDIR,CMASKVLR,LXML,APROCFIL,@ATRAB,LTSF,LQUEBRALIN,LNFSE,LEN(ABUFFERFIM)==LEN(ANORMA)-1))}(MATA950.PRX) 06/02/2020 13:45:26 line : 623  
Called from PROCNORMA(MATA950.PRX) 06/02/2020 13:45:26  
Called from { ||PROCNORMA(CNORMA,CDEST,CDIR,NIL,NIL,NIL,NIL,NIL,NIL,LJOB )}(MATA940.PRX) 05/02/2020 15:28:02 line : 109  
Called from { || FWSETSHOWKEYS( .F. ), EVAL( BACTION, @LEND ),LEND := .T. , FWSETSHOWKEYS( .T. ), ODLGMODAL:DEACTIVATE() }(MSPROCES.PRW) 06/12/2019 12:05:53 line : 104  
Called from {|SELF|(EVAL(OSELF:BINIT))}(FWDIALOGMODAL.PRW) 06/12/2019 12:05:51 line : 461  
Called from ::MSDIALOG:ACTIVATE  
Called from FWDIALOGMODAL:ACTIVATE(FWDIALOGMODAL.PRW) 06/12/2019 12:05:51 line : 461  
Called from PROCESSA(MSPROCES.PRW) 06/12/2019 12:05:53 line : 105  
Called from MATA940(MATA940.PRX) 05/02/2020 15:28:02 line : 109  
Called from \_\_EXECUTE(APLIB090.PRW) 06/12/2019 12:05:53 line : 680  
Called from FWPREEXECUTE(FWPREEXECUTE.PRW) 06/12/2019 12:05:55 line : 79  
Called from { ||FWPreExecute('Sintegra', 'MATA940()', 1, '09', 'xxxxxxxxxx') }(FWUIMENUF.PRW) 06/12/2019 12:05:55 line : 407  
Called from ::TWINDOW:ACTIVATE  
Called from MSAPP:ACTIVATE(FWAPP.PRW) 06/12/2019 12:05:53 line : 741  
Called from SIGAADV(APLIB000.PRW) 06/12/2019 12:05:53 line : 47

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Este erro ocorre quando há um problema na escrituração dos documentos.  
  
Referente o error.log mencionado acima, o sistema não está encontrando o documento fiscal apresentado no error.log na tabela SF3.   
  
Este documento existe na SD1/SD2, porém não foi encontrado ou está com dados divergentes na tabela SF3.  
   
Será necessário verificar se o documento fiscal foi escriturado na tabela SF3 e caso necessário, faça o reprocessamento do documento para verificar se a tabela SF3 foi criada.  
  
Outras possíveis causas:  
  
- O CFOP do documento fiscal apresentado no error.log OU do documento estão diferente nas tabelas SD1/SD2 e SF3.  
  
- A alíquota de ICMS (se o Livro fiscal ICMS = Tributado) está diferente nas tabelas SD1/SD2 e SF3 para os documentos.  
  
- Código do participante diferente nas tabelas SD1/SD2 e SF3 para os documentos. 

Anexo error.log completo para fins de consulta.
