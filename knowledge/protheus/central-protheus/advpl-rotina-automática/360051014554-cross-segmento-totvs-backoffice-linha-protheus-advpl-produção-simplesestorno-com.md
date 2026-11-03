---
article_id: 360051014554
category: ADVPL - Rotina Automática
content_hash: f10bf29239dd803e595bf4fa74a39480e980c6ae4d1f9c66994aacc66f38c5e7
fetched_at: '2026-06-28T22:40:25.016093+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Produção Simples:Estorno
  com ExecAuto MATA250
type: support-article
updated_at: '2021-08-02T20:27:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051014554-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Produ%C3%A7%C3%A3o-Simples-Estorno-com-ExecAuto-MATA250
---

**Dúvida**Como executar estorno de produção simples MATA250 através de rotina automática?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12  
  
**Solução**

```
#include'totvs.ch'  
  
User Function REMAT250()   
  
Local aVetor    := {}   
Local nOpc      := 5 //-Opção de execução da rotina, informado nos parâmetros quais as opções possiveis   
Local cOp       := "R1340101001   "   
Local cCod      := "01PROD061                     "   
Local cLocal    := "01"   
Local cChave    := ""   
lMsErroAuto     := .F.    
  
RpcSetEnv( "99","01",,,,,,,,,)   
    cChave:= xFilial("SD3") + cOp + cCod + cLocal   
    SD3->(DbSetOrder(1))   
    If SD3->(DbSeek(cChave))  
        While !(SD3->(Eof())) .And. SD3->(D3_FILIAL + D3_OP + D3_COD + D3_LOCAL) == cChave      
            If SD3->D3_ESTORNO == " "    
            aVetor := { {"D3_FILIAL"        ,XFILIAL("SD3") ,NIL},;  
                        {"D3_TM"            ,"010"          ,NIL},;  
                        {"D3_OP"            ,cOp            ,NIL},;  
                        {"D3_COD"           ,cCod           ,NIL},;  
                        {"D3_QUANT"         ,1              ,NIL},;  
                        {"D3_LOCAL"         ,"01"           ,NIL},;  
                        {"D3_EMISSAO"       ,dDatabase      ,NIL},;  
                        {"ATUEMP"           , "T"           ,NIL}}     
  
                MSExecAuto({|x, y| mata250(x, y)},aVetor, nOpc )       
  
                If lMsErroAuto  
                    Mostraerro()    
                Else     
                    Alert("Ok")    
                Endif    
                Exit    
            EndIf    
            SD3->(DbSkip())    
        EndDo   
    EndIf   
Return
```

**Saiba Mais**  
**[MATA250 - Produção](https://tdn.totvs.com/pages/releaseview.action?pageId=6087461)**
