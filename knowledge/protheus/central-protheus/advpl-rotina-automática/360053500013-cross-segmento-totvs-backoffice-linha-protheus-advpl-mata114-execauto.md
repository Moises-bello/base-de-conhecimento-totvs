---
article_id: 360053500013
category: ADVPL - Rotina Automática
content_hash: 25e76e440e11986c1994e6583717a459eea48d714acaba1a26ac0d93b09c7524
fetched_at: '2026-06-28T22:40:25.105552+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus- ADVPL - MATA114 - ExecAuto
type: support-article
updated_at: '2021-05-21T17:55:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053500013-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-MATA114-ExecAuto
---

**Dúvida**Existe alguma forma de executar a rotina MATA114 automática?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL- A partir da versão 12.  
  
**Solução**Conforme a documentação a rotina está em MVC, sendo assim podemos executar conforme o modelo padrão MVC .  
Segue abaixo um modelo de exemplo:

```
#include 'TOTVS.ch'  
#include 'FWMVCDef.ch'  
//-------------------------------------------------------------------  
/*/{Protheus.doc} ExMata114                                                                                
@author Eduardo Paro de Simoni  
@version P12  
//-------------------------------------------------------------------  
function U_Incluir1()  
    local oModel    := nil  
      
    //Preparação do Ambiente  
    RpcSetEnv("99","01","Administrador","","COM","MATA114",{"SAL","DBL",""})  
      
    oModel := FwLoadModel("MATA114")  
    oModel:SetOperation(MODEL_OPERATION_INSERT)  
    oModel:Activate()  
      
    //MASTER ModelSAL  
    oModel:SetValue("ModelSAL" ,"AL_COD"       ,"000002")  
    oModel:SetValue("ModelSAL" ,"AL_DESC"      ,"TESTE02             ")  
      
    //DETAIL DetailSAL  
    oModel:SetValue("DetailSAL","AL_ITEM"     ,"01")  
    oModel:SetValue("DetailSAL","AL_APROV"     ,"000001")  
    oModel:SetValue("DetailSAL" ,"AL_PERFIL"    ,"PERFIL")  
    oModel:SetValue("DetailSAL" ,"AL_USER"      ,"000000")  
    oModel:SetValue("DetailSAL" ,"AL_NIVEL"     ,"1 ")  
      
    //DETAIL DetailDBL  
    oModel:SetValue("DetailDBL" , "DBL_GRUPO"    , "000001")  
    oModel:SetValue("DetailDBL" , "DBL_ITEM"     , "01")  
    oModel:SetValue("DetailDBL" , "DBL_CC"       , "CENTR0001")  
      
    //DETAIL DetailDHM  
    oModel:SetValue("DetailDHM" , "DHM_GRUPO"   , "")  
    oModel:SetValue("DetailDHM" , "DHM_APROV"   , "")  
    oModel:SetValue("DetailDHM" , "DHM_TIPCOM"  , "")  
  
    If oModel:VldData()  
        oModel:CommitData()  
        conout("Registro INCLUIDO!")  
    Else  
        VarInfo("Erro ao incluir",oModel:GetErrorMessage())  
    EndIf  
    oModel:DeActivate()  
    oModel:Destroy()  
    oModel := nil  
    
return 
```

**Saiba Mais**  
[Fontes](https://tdn.totvs.com/display/public/PROT/Fontes+em+MVC#Modulos-COM) [em MVC](https://tdn.totvs.com/display/public/PROT/Fontes+em+MVC#Modulos-COM)
