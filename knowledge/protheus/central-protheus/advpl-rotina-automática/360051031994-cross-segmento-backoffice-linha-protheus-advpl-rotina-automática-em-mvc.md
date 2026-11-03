---
article_id: 360051031994
category: ADVPL - Rotina Automática
content_hash: 00b8ed62e6e506ab968253b809839953475ef0e85497b5bf0971e996f28f6e5c
fetched_at: '2026-06-28T22:40:24.190116+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Rotina Automática em MVC
type: support-article
updated_at: '2022-09-08T20:14:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051031994-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Rotina-Autom%C3%A1tica-em-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como efetuar uma integração via rotina automática em rotina MVC?  
  
**Ambiente**Protheus– ADVPL – A partir da versão 11.80  
  
**Solução**Deve ser avaliada se a rotina pretendida esta preparada para execução automática, caso sim, o modelo de construção é o mesmo para todas a rotinas, exemplo a rotina **MATA180** (Complemento de Produto), desta forma basta seguir o exemplo documentado.

Exemplo:

```
/*------------------------------------------------------------------------  
EXEMPLO DE INCLUSÃO NA TABELA SB5 UTILIZANDO MVC  
------------------------------------------------------------------------*/  
Static Function Incluir1()  
Local oModel    := Nil  
Local cCodigo    := ""  
  
// informe o código do produto, a qual já deve estar registrado na tabela SB1  
cCodigo := "1234"  
  
//Para utilização da mesma, o modelo de dados chama-se MATA180M e nao MATA180  
oModel := FwLoadModel("MATA180")  
oModel:SetOperation(MODEL_OPERATION_INSERT)  
oModel:Activate()  
  
oModel:SetValue("SB5MASTER","B5_COD"    ,cCodigo)  
oModel:SetValue("SB5MASTER","B5_CEME"    ,"Nome científico")  
  
If oModel:VldData()  
    oModel:CommitData()  
    conout("Registro INCLUIDO!")  
Else  
    VarInfo("Erro ao incluir",oModel:GetErrorMessage())  
EndIf  
  
oModel:DeActivate()  
oModel:Destroy()  
oModel := NIL  
  
Return Nil
```

Abaixo documentação do exemplo utilizado:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=358453385>
