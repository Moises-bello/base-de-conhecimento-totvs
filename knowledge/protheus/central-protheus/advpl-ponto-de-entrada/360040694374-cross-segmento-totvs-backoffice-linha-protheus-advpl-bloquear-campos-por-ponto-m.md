---
article_id: 360040694374
category: ADVPL - Ponto de Entrada
content_hash: f22eb070d3358458cb0b4092bac41b5eedcd17f71dfc1c424be20925e8ac94c6
fetched_at: '2026-06-28T22:40:11.659187+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Bloquear campos
  por ponto MVC
type: support-article
updated_at: '2024-02-19T21:33:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040694374-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Bloquear-campos-por-ponto-MVC
---

**Dúvida**Como bloquear campos (`X3_WHEN == .F.`) por meio de um ponto de entrada MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**Utilizar o id de ponto `MODELVLDACTIVE` e por meio dos métodos `GetModel()` + `GetStruct()` + `SetProperty()` alterar o X3\_WHEN utilizando a constante `MODEL_FIELD_WHEN` para atribuir o valor retornado pela função `FwBuildFeature()` + `STRUCT_FEATURE_WHEN`.  
  
**Fonte**

```
// BIBLIOTECAS UTILIZADAS  
#Include "TOTVS.ch"  
#Include "FWMVCDEF.ch"  
  
// EXEMPLO COM O PE MVC DA MATA010  
User Function ITEM()  
    Local aParam   := PARAMIXB // PARÂMETROS PASSADOS PARA O PONTO  
    Local xRet     := .T.      // RETORNO LÓGICO PARA PROSSEGUIMENTO DA ROTINA  
    Local oObj     := NIL      // OBJETO QUE ARMAZENARÁ O MODELO TOTAL  
    Local cIdPonto := Space(0) // ID DO MOMENTO DA CHAMADA DO PONTO  
  
    // CERTIFICA-SE QUE EXISTEM PARÂMETROS PARA O MOMENTO  
    If (!aParam == NIL)  
        oObj     := aParam[1]  
        cIdPonto := aParam[2]  
        cIdModel := aParam[3]  
  
        // VALIDAÇÃO ANTES DA ATIVAÇÃO DO MODELO  
        If (cIdPonto == "MODELVLDACTIVE")  
            // MODELO -> SUBMODELO -> ESTRUTURA -> PROPRIEDADE -> BLOCO DE CÓDIGO -> X3_WHEN := .F.  
            oObj:GetModel("SB1MASTER"):GetStruct():SetProperty("B1_COD", MODEL_FIELD_WHEN, FwBuildFeature(STRUCT_FEATURE_WHEN , ".F."))  
            oObj:GetModel("SB1MASTER"):GetStruct():SetProperty("B1_DESC", MODEL_FIELD_WHEN, FwBuildFeature(STRUCT_FEATURE_WHEN , ".F."))  
            oObj:GetModel("SB1MASTER"):GetStruct():SetProperty("B1_TIPO", MODEL_FIELD_WHEN, FwBuildFeature(STRUCT_FEATURE_WHEN , ".F."))  
        EndIf  
    EndIf  
Return (xRet) // RETORNO LÓGICO PARA PROSSEGUIMENTO
```

  
**Saiba mais**

[Apostila: ADVPL utilizando MVC](https://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC)  
[MPFormModel](https://tdn.totvs.com/display/framework/MPFormModel)

[FWFormModel](https://tdn.totvs.com/display/public/PROT/FWFormModel)

[Ponto de Entrada Padrão do MVC](https://tdn.totvs.com/pages/releaseview.action?pageId=208345968)

[FWFormModelStruct](https://tdn.totvs.com/display/framework/FWFormModelStruct)

[FWBuildFeature](https://tdn.totvs.com/display/framework/FWBuildFeature)
