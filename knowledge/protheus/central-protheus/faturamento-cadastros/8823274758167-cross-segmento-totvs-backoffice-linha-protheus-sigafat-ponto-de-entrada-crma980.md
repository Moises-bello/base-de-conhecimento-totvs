---
article_id: 8823274758167
category: Faturamento - Cadastros
content_hash: bcf9a66b347913c4030b5990def5ab65fc48c5e7de551337a2d032e8e40662e1
fetched_at: '2026-06-28T22:38:36.613462+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  CRMA980 - MODELCOMMITNTTS
type: support-article
updated_at: '2022-09-12T19:51:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8823274758167-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-CRMA980-MODELCOMMITNTTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **CRMA980 - MODELCOMMITTTS**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**O retorno do Ponto de Entrada **CRMA980** irá depender de qual **ID** estará sendo executado no momento, nesse exemplo iremos utilizar o **ID MODELCOMMITTTS** que é chamado após a gravação total do modelo e fora da transação nas operações de **inclusão**, **alteração** e **exclusão**.  
  
**Obs.:** O nome do arquivo não poderá ser **CRMA980.PRW**, utilize por exemplo **MYCRMA980.PRW**.  
  
**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "FWMVCDEF.CH"  
  
Static __LogTela := NIL  
  
User Function CRMA980() ///cXXX1,cXXX2,cXXX3,cXXX4,cXXX5,cXXX6  
  
Local aParam := PARAMIXB  
Local xRet := .T.  
Local lIsGrid := .F.  
Local cIDPonto := ''  
Local cIDModel := ''  
Local oObj := NIL  
  
If __LogTela == NIL  
__LogTela := ApMsgYesNo("A geracao do 'LOG de processamento' dos PE 'CRMA980' (MVC) sera exibido em TELA?" + CRLF + CRLF +;  
'SIM = TELA' + CRLF +;  
'NAO = CONSOLE do AppServer')  
EndIf  
  
If aParam <> NIL  
  
oObj := aParam[1]  
cIDPonto := aParam[2]  
cIDModel := aParam[3]  
lIsGrid := (Len(aParam) > 3)  
nOperation := oObj:GetOperation()  
  
If cIDPonto == 'MODELCOMMITNTTS'  
  
// MOSTRA O TIPO DE OPERACAO  
//MsgAlert("Operacao " + CValToChar(nOperation), "Tipo de operacao MODELCOMMITNTTS")  
  
// INCLUSAO  
If nOperation == 3  
MsgAlert("Entrou no PE - Operacao de Inclusao", "Tipo de operacao 3")  
EndIf  
  
// ALTERACAO  
If nOperation == 4  
MsgAlert("Entrou no PE - Operacao de Alteracao", "Tipo de operacao 4")  
EndIf  
  
// EXCLUSAO  
If nOperation == 5  
MsgAlert("Entrou no PE - Operacao de Exclusao", "Tipo de operacao 5")  
EndIf  
  
EndIf  
  
EndIf  
  
Return xRet
```

**Saiba Mais**

**[PE CRMA980 - Pontos de Entrada do Cadastro de Clientes (MVC)](https://tdn.totvs.com/x/-rO6J)**
