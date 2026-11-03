---
article_id: 360022495972
category: ADVPL - Rotina Automática
content_hash: 4d9c84bc739e0404f471e22df3dedd40af62d0324911c2c7af1b0a03b9129102
fetched_at: '2026-06-28T22:40:24.067814+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo da rotina automática
  FINA050
type: support-article
updated_at: '2023-02-20T20:37:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022495972-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-da-rotina-autom%C3%A1tica-FINA050
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Exemplo da rotina automática **FINA050**  
**Ambiente**Protheus – Financeiro – A partir da versão 11.8  
  
**Solução**Exemplo do funcionamento, da rotina automática

```
#Include "protheus.ch"  
#Include "parmtype.ch"  
#Include "tbiconn.ch"  
  
USER FUNCTION FIN050EXC()  
      
LOCAL aArray := {}  
PRIVATE lMsErroAuto := .F.  
  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  
  
aArray := {{ "E2_PREFIXO" , "" , NIL },;  
           { "E2_NUM" , "000000035" , NIL },;  
           { "E2_TIPO" , "BOL" , NIL },;  
           { "E2_NATUREZ" , "0000000001" , NIL },;  
           { "E2_FORNECE" , "FOR001" , NIL },;  
           { "E2_EMISSAO" , CtoD("30/01/2019"), NIL },;  
           { "E2_VENCTO" , CtoD("30/01/2019"), NIL },;  
           { "E2_VENCREA" , CtoD("30/01/2019"), NIL },;  
           { "E2_VALOR" , 250 , NIL },;  
           
MsExecAuto( { |x,y,z| FINA050(x,y,z)}, aArray,, 3) // 3 - Inclusao, 4 - Alteração, 5 - Exclusão  
  
If lMsErroAuto  
   MostraErro()  
     ConOut(Repl("-", 80))  
     ConOut(PadC("Teste FINA050 finalizado com erro!", 80))  
     ConOut(PadC("Fim: "+Time(), 80))  
     ConOut(Repl("-", 80))  
Else  
     ConOut(Repl("-", 80))  
     ConOut(PadC("Teste FINA050 finalizado com sucesso!", 80))  
     ConOut(PadC("Fim: "+Time(), 80))  
     ConOut(Repl("-", 80))  
EndIf  
  
RESET ENVIRONMENT  
  
Return
```

**Saiba Mais  
[FINA050 Contas a Pagar - Rotina Automática.](http://tdn.totvs.com/pages/releaseview.action?pageId=6070752)**
