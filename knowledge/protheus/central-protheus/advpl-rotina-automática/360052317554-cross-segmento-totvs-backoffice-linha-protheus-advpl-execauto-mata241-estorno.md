---
article_id: 360052317554
category: ADVPL - Rotina Automática
content_hash: b035cb455f8a974744c9c0be141bc59e92a0e29fe6d390ec815378d79f97e5a4
fetched_at: '2026-06-28T22:40:24.270014+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Execauto MATA241
  estorno
type: support-article
updated_at: '2023-01-09T17:47:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052317554-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execauto-MATA241-estorno
---

**Dúvida**Qual o exemplo de ExecAuto utilizado para executar automaticamente a rotina MATA241 com a opção de estorno?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**

Segue abaixo um modelo de exemplo :

```
#INCLUDE "TOTVS.CH"  
#INCLUDE "TBICONN.CH"  
  
function U_TMATA241()  
    local _aCab1    := {}  
    local _aItem    := {}  
    local _atotitem :={}  
    local cLocal    :="01"  
    local cCodProd  :="000000000000002"  
    local cNumSeq   :="000038"  
    private lMsHelpAuto := .t. // se .t. direciona as mensagens de help  
    private lMsErroAuto := .f. //necessario a criacao  
    private _acod:={"1","MP1"}  
  
    RpcSetEnv("99","01","Administrador","","EST","MATA241",{"SD3"})  
  
    SD3->(DbgoTop())  
    SD3->(DbSetOrder(3))//D3_FILIAL, D3_COD, D3_LOCAL, D3_NUMSEQ,   
    IF!SD3->(DbSeek(xFilial("SD3");  
            + PadR(cCodProd ,TamSx3("D3_COD")[1]);  
            + PadR(cLocal   ,TamSx3("D3_LOCAL")[1]);  
            + PadR(cNumSeq  ,TamSx3("D3_NUMSEQ")[1])))  
        fwAlertInfo("Registro não encontrado")  
        return .F.  
    EndIf  
  
    _aCab1 := { {"D3_TM"        ,SD3->D3_TM     , nil},;  
                {"D3_EMISSAO"   ,SD3->D3_EMISSAO, nil}}  
  
    _aItem:={ {"D3_COD"     ,SD3->D3_COD        ,nil},;  
              {"D3_UM"      ,SD3->D3_UM         ,nil},;  
              {"D3_QUANT"   ,SD3->D3_QUANT      ,nil},;  
              {"D3_LOCAL"   ,SD3->D3_LOCAL      ,nil},;  
              {"D3_LOTECTL" ,SD3->D3_LOTECTL    ,nil}}  
            
    aadd(_atotitem,_aitem)  
  
    MSExecAuto({|x,y,z| MATA241(x,y,z)},_aCab1,_atotitem,6)  
  
    If lMsErroAuto  
        mostraErro()  
        return .F.  
    else  
        fwAlertSuccess("Sucesso!")  
    endIf  
  
  RpcClearEnv()  
  
return .T.
```

**Saiba mais**[MP - SIGAEST - Rotina Automática da rotina MATA241(MOVIMENTOS INTERNOS MÚLTIPLOS)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022031372)  
[Movimentos Internos Modelo 2 - MATA241 - Estoque - P12](https://tdn.totvs.com.br/display/public/PROT/Movimentos+Internos+Modelo+2+-+MATA241+-+Estoque+-+P12)
