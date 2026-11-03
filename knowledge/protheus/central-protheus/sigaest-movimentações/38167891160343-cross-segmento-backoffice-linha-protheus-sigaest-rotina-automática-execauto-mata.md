---
article_id: 38167891160343
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ca911de691e3a17546806f12702e5539099a5b08bd0c94ed24c52990dabc3ac4
fetched_at: '2026-06-28T22:38:54.140819+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rotina Automática
  ExecAuto MATA390 - Manutenção de Lotes
type: support-article
updated_at: '2026-02-04T19:07:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38167891160343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-Autom%C3%A1tica-ExecAuto-MATA390-Manuten%C3%A7%C3%A3o-de-Lotes
---

Execauto rotina MATA390 - Manutenção de Lotes - Rotina automática  
  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38167853197079) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Qual o exemplo de Execauto utilizado para executar automaticamente a rotina de Manutenção de Lotes - MATA390?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Abaixo segue um exemplo de inclusão de manutenção de lotes através da rotina automática:

```
////////////////////////Inclusão/////////////////////////////
 
#Include 'Protheus.ch'
 
User Function AUT390INC()
 
Local cProd := ""
Local cLocal := ""
Local cLoteCtl := ""
Local dData := CtoD("//")
Local dDataVld := CtoD("//")
Local aVetor := {}
Local aTamCOD := {}
Local aTamLOC := {}
Local aTamLOT := {}
Local nQtd := 0
Local nOpc := 3
 
Private lMsErroAuto := .F.
 
PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "D MG 01" MODULO "EST" TABLES "SD5"
 
aTamCOD := TamSx3("D5_PRODUTO")
aTamLOC := TamSx3("D5_LOCAL")
aTamLOT := TamSx3("D5_LOTECTL")
 
DbSelectArea("SD5")
 
cProd := PadR("0005",aTamCOD[1])
cLocal := PadR("01",aTamLOC[1])
dData := dDataBase
nQtd := 12000
cLoteCtl := PadR("11223344",aTamLOT[1])
dDataVld := dDataBase+30
 
aadd(aVetor,{"D5_PRODUTO" ,cProd ,NIL})
aadd(aVetor,{"D5_LOCAL" ,cLocal ,NIL})
aadd(aVetor,{"D5_LOTECTL" ,cLoteCtl ,NIL})
aadd(aVetor,{"D5_DATA" ,dData ,NIL})
aadd(aVetor,{"D5_QUANT" ,nQtd ,NIL})
aadd(aVetor,{"D5_DTVALID" ,dDataVld ,NIL})
 
MSExecAuto({|x,y| Mata390(x,y)},aVetor,nOpc)
 
If !lMsErroAuto
ConOut("Incluido com sucesso! " + cProd)
Else
MostraErro()
ConOut("Erro na inclusao!")
EndIf
 
RESET ENVIRONMENT
 
Return



//////////////////////////Alteração de Data/////////////////////////////////
//Observação: Não esquecer de informar o número de lote (D5_NUMLOTE) e número sequência (D5_NUMSEQ), conforme números gerados após a inclusão.
 
#Include 'Protheus.ch'
 
User Function AUT390DAT()
 
Local cProd := ""
Local cLocal := ""
Local cLoteCtl := ""
Local cNumLote := ""
Local cNumSeq := ""
Local dDataVld := CtoD("//")
Local aVetor := {}
Local aTamCOD := {}
Local aTamLOC := {}
Local aTamLOT := {}
Local aTamNLOT := {}
Local aTamSEQ := {}
Local nOpc := 4
 
Private lMsErroAuto := .F.
 
PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "D MG 01" MODULO "EST" TABLES "SD5"
 
aTamCOD := TamSx3("D5_PRODUTO")
aTamLOC := TamSx3("D5_LOCAL")
aTamLOT := TamSx3("D5_LOTECTL")
aTamNLOT := TamSx3("D5_NUMLOTE")
aTamSEQ := TamSx3("D5_NUMSEQ")
 
DbSelectArea("SD5")
 
cProd := PadR("0005",aTamCOD[1])
cLocal := PadR("01",aTamLOC[1])
cLoteCtl := PadR("11223344",aTamLOT[1])
cNumLote := PadR("",aTamNLOT[1])
cNumSeq := PadR("000014",aTamSEQ[1])
dDataVld := dDataBase+90
 
aadd(aVetor,{"D5_PRODUTO" ,cProd ,NIL})
aadd(aVetor,{"D5_LOCAL" ,cLocal ,NIL})
aadd(aVetor,{"D5_LOTECTL" ,cLoteCtl ,NIL})
aadd(aVetor,{"D5_NUMLOTE" ,cNumLote ,NIL})
aadd(aVetor,{"D5_NUMSEQ" ,cNumSeq ,NIL})
aadd(aVetor,{"B8_DTVALID" ,dDataVld ,NIL}) //Utiliza B8 mesmo
 
MSExecAuto({|x,y| Mata390(x,y)},aVetor,nOpc)
 
If !lMsErroAuto
ConOut("Alterado data de validade com sucesso! " + cProd)
Else
MostraErro()
ConOut("Erro na alteração da data!")
EndIf
 
RESET ENVIRONMENT
 
Return



/////////////////Exclusão//////////////////////////
//Observação: Não esquecer de informar o número de lote (D5_NUMLOTE) e número sequência (D5_NUMSEQ), conforme números gerados após a inclusão.
 
#Include 'Protheus.ch'
 
User Function AUT390EXC()
 
Local cProd := ""
Local cLocal := ""
Local cLoteCtl := ""
Local cNumLote := ""
Local cNumSeq := ""
Local aVetor := {}
Local aTamCOD := {}
Local aTamLOC := {}
Local aTamLOT := {}
Local aTamNLOT := {}
Local aTamSEQ := {}
Local nOpc := 5
 
Private lMsErroAuto := .F.
 
PREPARE ENVIRONMENT EMPRESA "T1" FILIAL "D MG 01" MODULO "EST" TABLES "SD5"
 
aTamCOD := TamSx3("D5_PRODUTO")
aTamLOC := TamSx3("D5_LOCAL")
aTamLOT := TamSx3("D5_LOTECTL")
aTamNLOT := TamSx3("D5_NUMLOTE")
aTamSEQ := TamSx3("D5_NUMSEQ")
 
DbSelectArea("SD5")
 
cProd := PadR("0005",aTamCOD[1])
cLocal := PadR("01",aTamLOC[1])
cLoteCtl := PadR("11223344",aTamLOT[1])
cNumLote := PadR("",aTamNLOT[1])
cNumSeq := PadR("000014",aTamSEQ[1])
 
aadd(aVetor,{"D5_PRODUTO" ,cProd ,NIL})
aadd(aVetor,{"D5_LOCAL" ,cLocal ,NIL})
aadd(aVetor,{"D5_LOTECTL" ,cLoteCtl ,NIL})
aadd(aVetor,{"D5_NUMLOTE" ,cNumLote ,NIL})
aadd(aVetor,{"D5_NUMSEQ" ,cNumSeq ,NIL})
 
MSExecAuto({|x,y| Mata390(x,y)},aVetor,nOpc)
 
If !lMsErroAuto
ConOut("Excluido com sucesso! " + cProd)
Else
MostraErro()
ConOut("Erro na exclusão!")
EndIf
 
RESET ENVIRONMENT
 
Return
```

 Para exemplos sobre alteração de preço e potência, consultar o TDN [MATA390 - Manutenções nas Movimentações de Lote SD5 (Rotina automática)](https://tdn.totvs.com/x/8XBZEg).

**Saiba mais:**

[Clique aqui e saiba mais sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Rotina MATA390 - Manutenção de Lotes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030246893-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Rotina-MATA390-Manuten%C3%A7%C3%A3o-de-Lotes)
