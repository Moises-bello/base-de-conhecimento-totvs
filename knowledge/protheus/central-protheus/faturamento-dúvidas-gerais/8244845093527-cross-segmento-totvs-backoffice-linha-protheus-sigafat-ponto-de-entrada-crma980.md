---
article_id: 8244845093527
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e0b85b840df51f7071d2c01de250e91cbe4d6c16ce6c0b09fc9c28eb062df94c
fetched_at: '2026-06-28T22:38:32.814246+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  CRMA980 - FORMPOS
type: support-article
updated_at: '2022-09-09T13:13:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8244845093527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-CRMA980-FORMPOS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **CRMA980 - FORMPOS**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**O retorno do Ponto de Entrada **CRMA980** irá depender de qual **ID** estará sendo executado no momento, nesse exemplo iremos utilizar o **ID FORMPOS** que é chamado nas operações de **inclusão e** **alteração.**  
  
**Obs.:** O nome do arquivo não poderá ser **CRMA980.PRW**, utilize por exemplo **MYCRMA980.PRW**.  
  
**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "FWMVCDEF.CH"  
  
Static __LogTela    := NIL  
  
User Function CRMA980() ///cXXX1,cXXX2,cXXX3,cXXX4,cXXX5,cXXX6  
  
    Local aParam        := PARAMIXB  
    Local xRet          := .T.  
    Local lIsGrid       := .F.  
    Local cIDPonto      := ''  
    Local cIDModel      := ''  
    Local cIDForm       := ''  
    Local oObj          := NIL  
  
    If __LogTela == NIL  
        __LogTela   := ApMsgYesNo("A geracao do 'LOG de processamento' dos PE 'CRMA980' (MVC) sera exibido em TELA?" + CRLF + CRLF +;  
            'SIM = TELA' + CRLF +;  
            'NAO = CONSOLE do AppServer')  
    EndIf  
  
    If aParam <> NIL  
        oObj        := aParam[1]  
        cIDPonto    := aParam[2]  
        cIDModel    := aParam[3]  
        lIsGrid     := (Len(aParam) > 3)  
        nOperation := oObj:GetOperation()  
  
        If cIDPonto == 'FORMPOS'  
            cIDForm     := oObj:GetID()  
            MsgAlert("Entrou no PE - FORMPOS", "PE CRMA980")  
        EndIf  
  
    EndIf  
  
Return xRet
```

**Saiba Mais:**

**[PE CRMA980 - Pontos de Entrada do Cadastro de Clientes (MVC)](https://tdn.totvs.com/x/-rO6J)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Ponto de entrada MVC id modelpos: Executa duas vezes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056429414-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MVC-id-modelpos-Executa-duas-vezes#:~:text=Por%20qual%20motivo%20o%20ID,MVC%20%C3%A9%20chamado%20duas%20vezes%3F&text=Esse%20comportamento%20%C3%A9%20padr%C3%A3o%20dos,execu%C3%A7%C3%A3o%20do%20evento%20do%20modelo.)**
