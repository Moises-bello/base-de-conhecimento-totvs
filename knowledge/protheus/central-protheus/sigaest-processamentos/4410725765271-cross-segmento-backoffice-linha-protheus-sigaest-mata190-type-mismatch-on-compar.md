---
article_id: 4410725765271
category: SIGAEST - PROCESSAMENTOS
content_hash: 4b549fba2a288a839316635a1d4d9a62ca9276eac40acb95954d081c64eb0645
fetched_at: '2026-06-28T22:39:04.900478+00:00'
product: protheus
section_id: 1500001538861
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA190 - type mismatch
  on compare  on A103RECC7(MATA103X.PRX)
type: support-article
updated_at: '2021-10-14T18:06:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410725765271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA190-type-mismatch-on-compare-on-A103RECC7-MATA103X-PRX
---

**Ocorrência**No módulo Estoque Custos ao processar a rotinas REFAZ CUSTO DE ENTRADA (MATA190) apresenta o error.log  "**type mismatch on compare on A103RECC7(MATA103X.PRX)**".

type mismatch on compare  on A103RECC7(MATA103X.PRX) 06/04/2021 15:06:01 line : 16947  
  
[TOTVS build: 7.00.191205P-20210522]  
Called from MONTAACOLS(MATA103.PRW) 01/04/2021 15:29:31 line : 17633  
Called from { || MONTAACOLS(BWHILESD1, .F. , .F. , .F. , .F. ,,,"SD1","SB1",@ARECSD1,{0,0,0},,,,,,,@AHEADER,@ACOLS, .F. ,,,LCONTINUA) }(MATA190.PRX) 05/05/2021 11:58:16 line : 1858  
Called from FILLGETDADOS(APLIB171.PRW) 06/07/2021 19:07:02 line : 187  
Called from GERACUSTO2(MATA190.PRX) 05/05/2021 11:58:16 line : 1858  
Called from RECALC(MATA190.PRX) 05/05/2021 11:58:16 line : 475  
Called from FA190PROCESSA(MATA190.PRX) 05/05/2021 11:58:16 line : 229  
Called from {|LEND| FA190PROCESSA(LBAT)}(MATA190.PRX) 05/05/2021 11:58:16 line : 166  
Called from { || FWSETSHOWKEYS( .F. ), EVAL( BACTION, @LEND ),LEND := .T. , FWSETSHOWKEYS( .T. ), ODLGMODAL:DEACTIVATE() }(MSPROCES.PRW) 06/07/2021 19:07:04 line : 104  
Called from {|SELF|(EVAL(OSELF:BINIT))}(FWDIALOGMODAL.PRW) 06/07/2021 19:07:01 line : 462  
Called from ::MSDIALOG:ACTIVATE  
Called from FWDIALOGMODAL:ACTIVATE(FWDIALOGMODAL.PRW) 06/07/2021 19:07:01 line : 462  
Called from PROCESSA(MSPROCES.PRW) 06/07/2021 19:07:04 line : 105  
Called from A190EXEC(MATA190.PRX) 05/05/2021 11:58:16 line : 166  
Called from MATA190(MATA190.PRX) 05/05/2021 11:58:16 line : 105  
Called from \_\_EXECUTE(APLIB090.PRW) 06/07/2021 19:07:02 line : 721  
Called from MDIEXECUTE(APLIB260.PRW) 06/07/2021 19:07:02 line : 912

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Causa**Esse erro ocorre, devido a ausência de alguma pergunta do grupo ***MTA140I.***  
  
**Solução**Para correção, abaixo um print demonstrando o grupo de perguntas completo e anexo o arquivo em .DTC caso desejar visualizar fisicamente.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410716291863/mceclip1.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410726040599/mceclip0.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Processamentos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538861-SIGAEST-PROCESSAMENTOS)*
