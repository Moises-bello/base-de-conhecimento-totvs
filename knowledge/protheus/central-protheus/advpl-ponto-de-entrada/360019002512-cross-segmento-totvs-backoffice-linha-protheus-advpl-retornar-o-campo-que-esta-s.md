---
article_id: 360019002512
category: ADVPL - Ponto de Entrada
content_hash: efe975c95bebee5ea4320a42bc9a96e594195a5d4c4891faf4f265471f5ec074
fetched_at: '2026-06-28T22:40:12.867258+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Retornar o campo
  que esta sendo alterado em rotina MVC
type: support-article
updated_at: '2021-12-30T17:51:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019002512-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Retornar-o-campo-que-esta-sendo-alterado-em-rotina-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como saber o campo que está sendo alterado no momento por meio de um ponto de entrada MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Crie uma função estática para ser utilizada em conjunto com os pontos de entrada MVC:

```
Static Function GetFldAtMoment(aParam)  
    Local cFldAtMnt := NIL  
  
    If (aParam[2] == "FORMPRE")  
        If (aParam[4] == "SETVALUE")  
            cFldAtMnt := PARAMIXB[5]  
        EndIf  
    EndIf  
Return (cFldAtMnt)
```

**Exemplo**

```
#Include "TOTVS.ch"  
  
// PONTO DE ENTRADA DA MATA020 UTILIZADO COMO EXEMPLO  
User Function CUSTOMERVENDOR()  
    Local aParam   := PARAMIXB  
    Local xRet     := .T.  
    Local oObj     := ""  
    Local cIdPonto := ""  
    Local cIdModel := ""  
    Local cField   := NIL  
   
    If (aParam != NIL)  
        oObj     := aParam[1]  
        cIdPonto := aParam[2]  
        cIdModel := aParam[3]  
   
        cField := GetFldAtMoment(aParam) // FUNÇÃO AQUI  
   
        If (cField != NIL)  
            MsgInfo("Field at Moment: " + cField, "MVC entry point")  
 cField := NIL  
        EndIf  
    EndIf  
Return (xRet)
```

**Importante**  
Quando o campo conter gatilhos, somente a primeira chamada da função retornará o campo que disparou a ação, as demais chamadas serão referentes aos campos alimentados pelo gatilho.
