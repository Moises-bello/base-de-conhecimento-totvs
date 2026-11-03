---
article_id: 360049200134
category: ADVPL - Rotina Automática
content_hash: e368815e35d9b6544b9ca80a3cc838e992cb3e841ee5835b4002c740fd7f9867
fetched_at: '2026-06-28T22:40:25.087642+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -ADVPL - Campos obrigatórios
  na rotina automática MATA311
type: support-article
updated_at: '2024-07-10T12:49:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049200134-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Campos-obrigat%C3%B3rios-na-rotina-autom%C3%A1tica-MATA311
---

**Dúvida**  
Quais os campos obrigatórios na rotina automática do MATA311?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12  
  
**Solução**No exemplo documentado do tdn, consta todos os campos necessário/obrigatórios para a realização da rotina **automática** **MATA311**.

Exemplo de inclusão:

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "FWMVCDEF.CH"  
#INCLUDE "TBICONN.CH"  
  
/*  
Exemplo de inclusão de uma solicitação de transferência via rotina automática  
*/  
  
User Function M311Inc()  
Local oModel  
Local aLog  
Local cMensLog  
Local nX  
  
PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01' USER 'admin' PASSWORD '' MODULO "EST"  
  
oModel := FWLoadModel("MATA311") //Carrega o modelo  
oModel:SetOperation(MODEL_OPERATION_INSERT) // Seta operação de inclusão  
oModel:Activate() // Ativa o Modelo  
  
//Cabeçalho da solicitacao  
oModel:SetValue( 'NNSMASTER', 'NNS_CLASS', '1' )  
oModel:SetValue( 'NNSMASTER', 'NNS_ESPECI', ' ' )  
  
//Itens da solicitação  
// produto e local de origem  
oModel:SetValue( 'NNTDETAIL', 'NNT_FILORI', '01' )  
oModel:SetValue( 'NNTDETAIL', 'NNT_PROD', 'PRO001' )  
oModel:SetValue( 'NNTDETAIL', 'NNT_LOCAL', '0A' )  
oModel:SetValue( 'NNTDETAIL', 'NNT_QUANT', 1 )  
  
// produto e local de destino  
oModel:SetValue( 'NNTDETAIL', 'NNT_FILDES', '01' )  
oModel:SetValue( 'NNTDETAIL', 'NNT_PRODD', 'PRO001' )  
oModel:SetValue( 'NNTDETAIL', 'NNT_LOCLD', '0B' )  
  
If oModel:VldData() //Validação do modelo  
oModel:CommitData() // Gravação do Modelo  
Else  
  
aLog := oModel:GetErrorMessage() //Recupera o erro do model quando nao passou no VldData  
cMensLog := ''  
  
//laco para gravar em string cLog conteudo do array aLog  
For nX := 1 to Len(aLog)  
If !Empty(aLog[nX])  
cMensLog += Alltrim(aLog[nX]) + CHR(13)+CHR(10)  
EndIf  
  
Next nX  
  
lMsErroAuto := .T. //seta variavel private como erro  
AutoGRLog(cMensLog) //grava log para exibir com funcao mostraerro  
MostraErro()  
EndIf  
  
oModel:DeActivate() //desativa modelo  
  
Return NIL
```

**Saiba Mais  
[MATA311 - Rotina Automática de Solicitação de Transferências.](https://tdn.totvs.com/pages/releaseview.action?pageId=554642567)**
