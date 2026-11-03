---
article_id: 8058455139479
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 033c0859a92648016f6a67d1cac0100d439e8e9990b60f960d630656b4f93550
fetched_at: '2026-06-28T22:38:29.930584+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento(SIGAFAT)
  - Execauto cadastro de Transportadoras - MATA050
type: support-article
updated_at: '2025-01-10T20:22:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8058455139479-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Execauto-cadastro-de-Transportadoras-MATA050
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Preciso de um exemplo da rotina automática de cadastro de Transportadora.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Faturamento – A partir da versão 12.1.17  
  
**Solução**Segue abaixo modelo de rotina automática, neste exemplo foi incluído novos campos obrigatórios.

Exemplo

```
#Include "Protheus.ch"  
#include "TBICONN.CH"  
//-------------------------------------------------------------------  
/*/{Protheus.doc} MyMata050  
Função de exemplo para utilização da rotina automática de Transportadora.  
/*/  
//-------------------------------------------------------------------  
  
User Function MyMata050()  
  
Local aDados := {}  
Local nOpcAuto := 3//MODEL_OPERATION_INSERT  
Local lRet := .T.  
  
Private lMsErroAuto := .F.  
  
lRet := RpcSetEnv("99","01")  
  
If lRet  
  
//----------------------------------  
// Dados do Transportadora  
//----------------------------------  
  
aAdd(aDados, {"A4_FILIAL",  xFilial("SA4")       , nil})  
aAdd(aDados, {"A4_COD"   ,  "000002"             , nil})  
aAdd(aDados, {"A4_NOME"  ,  "TRANSPORTADORA MSI" , nil})   
  
//------------------------------------  
// Chamada para cadastrar o cliente.  
//------------------------------------  
MSExecAuto({|x,y|mata050(x,y)},aDados,nOpcAuto)  
  
If lMsErroAuto   
lRet := lMsErroAuto  
MostraErro()// não usar via JOB  
Else  
Conout("Transportadora incluída com sucesso!")  
EndIf  
  
EndIf  
  
RpcClearEnv()  
  
Return lRet
```
