---
article_id: 8401082625559
category: Faturamento - Cenários de Venda
content_hash: 783ef103c684f57163e3741f5ef180d7bb0c2c4607195b4d572a4916bc823af3
fetched_at: '2026-06-28T22:38:34.114941+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  FORMPRE validar alteração de campos
type: support-article
updated_at: '2022-08-24T19:05:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8401082625559-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-FORMPRE-validar-altera%C3%A7%C3%A3o-de-campos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como utilizar o Ponto de Entrada FORMPRE (MVC) para validar a alteração em um campo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**Em fontes que possuem a escrita em MVC, para validar a alteração de campos, é possível utilizar o  "**FORMPRE**", com ele é possível validar qualquer alteração nos campos do formulário, ou de um campo específico (de acordo com a regra estabelecida).

**Obs.:** O nome do arquivo não poderá ser **o mesmo do fonte que esta customizando**, ou seja caso customize o fonte FATA300.prw utilize, por exemplo, o nome do arquivo como  **MYFATA300.PRW**.

**Exemplo**:

```
Static Function GetFldAtMoment(aParam)  
  
Local cFldAtMnt := NIL  
  
If (aParam[2] == "FORMPRE")  
If (aParam[4] == "SETVALUE")  
cFldAtMnt := PARAMIXB[5]  
EndIf  
EndIf  
  
Return (cFldAtMnt)  
  
User Function FATA300()  
  
Local aParam := PARAMIXB  
Local xRet := .T.  
Local oObj := ""  
Local cIdPonto := ""  
Local cIdModel := ""  
Local cField := NIL  
  
If (aParam != NIL)  
oObj := aParam[1]  
cIdPonto := aParam[2]  
cIdModel := aParam[3]  
  
cField := GetFldAtMoment(aParam) // FUNÇÃO AQUI  
  
If (cField != NIL)  
MsgInfo("Campo alterado: " + cField, "PE FATA300 - FORMPRE")  
cField := NIL  
EndIf  
EndIf  
  
Return (xRet)
```

**Saiba mais**: [Pontos de Entrada do Cadastro de Clientes (MVC)](https://tdn.totvs.com/x/-rO6J)
