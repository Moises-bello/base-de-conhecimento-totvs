---
article_id: 22815908785431
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4214780c146ebba4d781708c22727616dd05ed9ee0f77b4d8be81fd9192c6f16
fetched_at: '2026-06-28T22:38:54.318984+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - array out of bounds
  ( 0 of 47 )  on A103DTVLD(MATA103X.PRX)
type: support-article
updated_at: '2024-04-15T16:39:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22815908785431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-array-out-of-bounds-0-of-47-on-A103DTVLD-MATA103X-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22815908755223) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**

Ao tentar Incluir ou Alterar Pré-nota de Entrada (MATA140) ou Documento de Entrada (MATA103) apresenta o error.log abaixo, como ajustar o ambiente para emissão dos documentos?

**array out of bounds ( 0 of 47 ) on A103DTVLD(MATA103X.PRX) 26/02/2024 18:39:19 line : 6232**

[TOTVS build: -]  
Called from {|| (A103DtVld(M->D1\_DTVALID)) .and. (.t.) .and. (A140FldOk())}(MSGETDAD.PRW) 29/02/2024 17:21:47 line : 1275  
Called from VALIDGET(MSMGETPR.PRW) 29/02/2024 17:21:47 line : 2069  
Called from {|SELF|(VALIDGET(\_\_\_ODLG,\_\_\_BVALID,\_\_\_OGET,,,@LCARGO) .AND. IIF(LNEWGETD .AND. OGLOGETDB:BFIELDOK<>NIL,VALIDGET(\_\_\_ODLG,OGLOGETDB:BFIELDOK,\_\_\_OGET,,,@LCARGO), .T. ))}(MSGETDAD.PRW) 29/02/2024 17:21:47 line : 1387  
Called from ::MSDIALOG:END  
Called from {|| \_\_\_ODLG:NLASTKEY := 13, \_\_\_ODLG:END(0)}(MSGETDAD.PRW) 29/02/2024 17:21:47 line : 1324  
Called from ::MSDIALOG:ACTIVATE  
Called from LEDITCOL(MSGETDAD.PRW) 29/02/2024 17:21:47 line : 1387  
Called from MSGETDADOS:EDITCELL(MSGETDAD.PRW) 29/02/2024 17:21:47 line : 501  
Called from { | NROW, NCOL | SELF:EDITCELL() }(MSGETDAD.PRW) 29/02/2024 17:21:47 line : 404  
Called from ::MSDIALOG:ACTIVATE  
Called from A140NFISCAL(MATA140.PRW) 23/02/2024 08:01:21 line : 1094  
Called from FWFORMBROWSE:EXECUTE(FWFORMBROWSE.PRW) 29/02/2024 17:21:49 line : 1149  
Called from {|| OSELF:EXECUTE("A140NFISCAL", 3, 0,"INCLUIR", 3,"","INCLUIR","", 3) }(FWFORMBROWSE.PRW) 29/02/2024 17:21:49 line : 579  
Called from ::MSDIALOG:ACTIVATE  
Called from FWMBROWSE:ACTIVATE(FWMBROWSE.PRW) 29/02/2024 17:21:47 line : 700  
Called from FWMBROWSE(MSLIB.PRW) 29/02/2024 17:21:47 line : 10499  
Called from MBROWSE(MSLIB.PRW) 29/02/2024 17:21:47 line : 170  
Called from MATA140(MATA140.PRW) 23/02/2024 08:01:21 line : 167  
Called from \_\_EXECUTE(APLIB090.PRW) 29/02/2024 17:21:47 line : 735  
Called from MDIEXECUTE(APLIB260.PRW) 29/02/2024 17:21:47 line : 924

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Causa**

Esse incidente ocorre por exemplo, no momento de informar a Data de Validade do Lote do produto.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

**- 1 -** Verificar na **tabela SD1** se os campos abaixo estão com as opções **"Usado"** e **"Browse"** selecionadas. É necessário que esses campos estejam marcados com essa opções.

**D1\_COD**

**D1\_LOCAL**

**D1\_NUMLOTE**

**D1\_LOTECTL**

**D1\_DTVALID**

**D1\_TIPO\_NF**

**D1\_LOTEFOR**

**- 2 -** Caso, mesmo assim persistir a ocorrência, também verificar na **tabela SB8** a ordem do **campo B8\_DFABRIC** deverá estar na **posição 031 ou 032** não poderá mudar a ordem (legenda vermelha). Veja exemplo abaixo de um ambiente padrão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22816372050455)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
