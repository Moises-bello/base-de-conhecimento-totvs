---
article_id: 35648004256279
category: Financeiro - Viagens
content_hash: ba34874a5a1c3da0cfefc55c380df3fe5f77847e3539c4a98e6a324a24d9cf07
fetched_at: '2026-06-28T22:38:21.261913+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA666 - Exemplo de
  execauto para solicitação de viagem
type: support-article
updated_at: '2025-10-15T14:11:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35648004256279-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA666-Exemplo-de-execauto-para-solicita%C3%A7%C3%A3o-de-viagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35647980458903) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Exemplo de execução automática para rotina de solicitação de viagem.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
  
**Solução**  
Para execução da rotina automática, ilustramos algumas funcionalidades como **Inclusão (MyFA666Inc), Alteração (MyFA666Alt) e Exclusão (MyFA666Del),** nos seguintes exemplos:

```
#INCLUDE "PROTHEUS.CH"
#INCLUDE "FWMVCDEF.CH"

//---------- Inclusao da solicitacao de viagem ----------//
User Function MyFA666Inc()

Local oModel := Nil
Local oModelFW3 := Nil
Local oModelFW4 := Nil
Local oModelFW5 := Nil
Local oModelFW6 := Nil
Local cFilAtu := ""

RpcSetEnv("T1","D MG 01 ","claudio.ribeiro","1") // Inicializa ambiente com usuario solicitante

oModel := FWLoadModel("FINA666")
oModelFW3 := oModel:GetModel("FW3MASTER") // Cabecalho da viagem
oModelFW4 := oModel:GetModel("FW4DETAIL") // Servicos
oModelFW5 := oModel:GetModel("FW5DETAIL") // Participantes
oModelFW6 := oModel:GetModel("FW6DETAIL") // Centro de custo
cFilAtu := xFilial("FW3")

oModel:SetOperation(MODEL_OPERATION_INSERT)
oModel:Activate()
// Preenche cabecalho da solicitacao de viagem
oModelFW3:SetValue("FW3_FILIAL",cFilAtu)
oModelFW3:SetValue("FW3_NACION","1")
oModelFW3:SetValue("FW3_CODORI","SP")
oModelFW3:SetValue("FW3_CODDES","RJ")
oModelFW3:SetValue("FW3_DTINI",StoD("20190702"))
oModelFW3:SetValue("FW3_DTFIM",StoD("20190705"))
oModelFW3:SetValue("FW3_CLIENT","001 ")
oModelFW3:SetValue("FW3_LOJA","01")
oModelFW3:SetValue("FW3_STATUS","0") // Em Aberto, status inicial
// Preenche grid do servico incluso na solicitacao da viagem
oModelFW4:SetValue("FW4_ITEM",StrZero(1,TamSX3("FW4_ITEM")[1]))
oModelFW4:SetValue("FW4_TIPO","1") // Aereo
oModelFW4:SetValue("FW4_OBS", "Visita ao cliente")
// Preenche grid dos participantes viajantes
oModelFW5:SetValue("FW5_ITEM",StrZero(1,TamSX3("FW4_ITEM")[1]))
oModelFW5:SetValue("FW5_PARTIC","000001")
oModelFW5:SetValue("FW5_ADIANT",.T.) // Adiciona adiantamento ao participante
oModelFW5:AddLine() // Adiciona linha para um segundo viajante
oModelFW5:SetValue("FW5_ITEM",StrZero(2,TamSX3("FW4_ITEM")[1]))
oModelFW5:SetValue("FW5_PARTIC","000002")
oModelFW5:SetValue("FW5_ADIANT",.T.) // Adiciona adiantamento ao participante
// Preenche grid do centro de custo
oModelFW6:SetValue("FW6_ITEM",StrZero(1,TamSX3("FW4_ITEM")[1]))
oModelFW6:SetValue("FW6_CC","002 ")
oModelFW6:SetValue("FW6_PORCEN",100)
oModelFW5:GoLine(1)
// Validacao e gravacao dos dados se consistentes
If oModel:VldData()
    oModel:CommitData()
    Conout("Inclusao da solicitacao de viagem concluida com sucesso.")
Else
    VarInfo("",oModel:GetErrorMessage())
    Conout("Erro na validacao, solicitacao de viagem nao foi incluida.")
EndIf

oModel:DeActivate()
oModel:Destroy()
RpcClearEnv()

Return


//---------- Alteracao da solicitacao de viagem ----------//
User Function MyFA666Alt()

Local aKeyFW4 := {}
Local oModel := Nil
Local oModelFW5 := Nil
Local oModelFW6 := Nil
Local cSolic := "0000000010"

RpcSetEnv("T1","D MG 01 ","richard.santos","1") // Inicializa ambiente com usuario solicitante

dbSelectArea("FW3")
dbSetOrder(1)
dbSeek(xFilial("FW3")+cSolic)
// Carrega modelo de dados com a solicitacao de viagem posicionada
oModel := FWLoadModel("FINA666")
oModelFW5 := oModel:GetModel("FW5DETAIL") // Participantes
oModelFW6 := oModel:GetModel("FW6DETAIL") // Centro de custo
// Chave de busca do participante dentro da sol. da viagem
aKeyFW4 := { {"FW5_FILIAL",xFilial("FW5")},{"FW5_SOLICI",cSolic},{"FW5_ITEM","01"},{"FW5_PARTIC","000002"} }

oModel:SetOperation(MODEL_OPERATION_UPDATE)
oModel:Activate()
// Remove um dos viajantes, no caso o participante 000002
If oModelFW5:SeekLine(aKeyFLE)
    oModelFW5:DeleteLine()
Else
    Conout("Viajante nao encontrado nesta solicitacao de viagem.")
EndIf
// Altera o centro de custo (posicionado automaticamente no primeiro grid)
oModelFW6:SetValue("FW6_CC","003 ")

// Validacao e gravacao dos dados se consistentes
If oModel:VldData()
    oModel:CommitData()
    Conout("Alteracao da solicitacao de viagem efetuada com sucesso.")
Else
    VarInfo("",oModel:GetErrorMessage())
    Conout("Erro na validacao, solicitacao de viagem nao foi alterada.")
EndIf

oModel:DeActivate()
oModel:Destroy()
RpcClearEnv()

Return


//---------- Exclusao da solicitacao de viagem ----------//
User Function MyFA666Del()

Local oModel := Nil
Local cSolic := "0000000010"

RpcSetEnv("T1","D MG 01 ","claudio.ribeiro","1") // Inicializa ambiente com usuario solicitante

dbSelectArea("FW3")
dbSetOrder(1)
dbSeek(xFilial("FW3")+cSolic)
// Carrega modelo de dados com a solicitacao de viagem posicionada
oModel:= FWLoadModel("FINA666")
oModel:SetOperation(MODEL_OPERATION_DELETE)
oModel:Activate()

// Validacao e gravacao da exclusao
If oModel:VldData()
    oModel:CommitData()
    Conout("Solicitacao de viagem excluida com sucesso.")
Else
    VarInfo("",oModel:GetErrorMessage())
    Conout("Erro na validacao, solicitacao de viagem nao foi excluida.")
EndIf

oModel:DeActivate()
oModel:Destroy()
RpcClearEnv()

Return
```

**Saiba mais:** [**Solicitação de Viagem - Financeiro - P12**](https://tdn.totvs.com/pages/releaseview.action?pageId=500279288#Solicita%C3%A7%C3%A3odeViagemFinanceiroP12-03.ROTINAAUTOM%C3%81TICA)
