---
article_id: 360015971771
category: ADVPL - Ponto de Entrada
content_hash: 9c005c8f8986c3bccb3dee75f20f0d140d47897e989d66591071648466ca0da2
fetched_at: '2026-06-28T22:40:11.777512+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Operação de cópia
  em ponto de entrada MVC (Lcopia)
type: support-article
updated_at: '2021-12-29T20:10:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015971771-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Opera%C3%A7%C3%A3o-de-c%C3%B3pia-em-ponto-de-entrada-MVC-Lcopia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como saber se estou em uma operação de cópia em um ponto de entrada MVC (*Model-View-Controller*)? **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80 **Solução**Para retornar se a operação é uma cópia ou não, utilize o método IsCopy() da classe FwFormModel().  
  
**Exemplo**

```
User Function ITEM()  
Local aParam := PARAMIXB   
Local xRet := .T.   
Local oObj := ""   
Local cIdPonto := ""   
Local cIdModel := ""   
Local lIsGrid := .F.   
Local oModelX := nil  
  
If aParam <> NIL  
   
 oObj := aParam[1]  
 cIdPonto := aParam[2]  
 cIdModel := aParam[3]  
 lIsGrid := ( Len( aParam ) > 3 )  
   
 If cIdPonto == 'FORMPRE'  
   
 oModelX := FwModelActive()// Instancia modelo ativo  
 oMedelB1 := oModelX:GetModel("SB1MASTER") //Instancia sub-modelo SB1  
   
 If oModelX:IsCopy() //Verifica se é uma operação de copia  
   
 // CUSTOMIZAÇÕES DO USUÁRIO (VALIDAÇÃO DE CAMPO, INSERÇÃO DE VALORES E ETC)  
   
 MsgInfo("FORMPRE - Operação de cópia")  
   
 xRet := .T.//Mantem o retorno para validação FORMPOS como .T., alterar se for necessário   
 EndIf  
   
 EndIf   
   
EndIf  
  
Return xRet
```

**Saiba mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada MVC para as rotinas MATA010, MATA020 e MATA030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016405952) [CLASSE FWFORMMODEL](http://tdn.totvs.com/display/PROT/FWFormModel)
