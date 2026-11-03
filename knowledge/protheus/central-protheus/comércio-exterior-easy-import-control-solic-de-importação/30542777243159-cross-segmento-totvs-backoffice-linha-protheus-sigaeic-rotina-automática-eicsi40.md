---
article_id: 30542777243159
category: Comércio Exterior - Easy Import Control - Solic. de Importação
content_hash: 7a973ca52b422f311698dde200a25513933787721d6b4f829b3e72997ffed8fe
fetched_at: '2026-06-28T22:39:46.731885+00:00'
product: protheus
section_id: 1500001538401
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Rotina Automática
  EICSI400 - Solicitação de Importação
type: support-article
updated_at: '2025-03-10T20:36:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30542777243159-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Rotina-Autom%C3%A1tica-EICSI400-Solicita%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30542777229975) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Exemplo de ExecAuto na rotina de Solicitação de Importação (EICSI400).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – Todas versões.  
  
**Solução**Exemplo de ExecAuto:

```
#include "totvs.ch"  
#include "tbiconn.ch"  
  
User Function Inc_EICSI()  
Local aItens := {}  
Local aDadosAuto := {}   
Local aCab:={}  
Private lMsHelpAuto := .f. // Determina se as mensagens de help devem ser direcionadas para o arq. de log  
Private lMsErroAuto := .f. // Determina se houve alguma inconsistência na execução da rotina  
  
rpcsetenv("99","01","admin","","EIC")  
aCab := { {'W0__CC' ,'01' ,NIL},;  
{'W0_CCDESC' ,"PRODUTOS" ,NIL},;  
{'W0__NUM' ,"301" ,NIL},;  
{'W0_DT' ,dDataBase ,NIL},;  
{'W0_COMPRA' ,'01' ,NIL},;  
{'W0_MOEDA' ,'US$' ,NIL},;  
{'W0_POLE' ,'01' ,NIL},;  
{'W0_POLEDE' ,"CENTRO" ,NIL};  
}  
  
aAdd(aItens,{ {'W1_COD_I' ,'01' , NIL},;  
{'W1_POSICAO' , "0001" , NIL},;  
{'W1_POSIT' , "0001" , NIL},;  
{'W1_FABR' ,'01' , NIL},;  
{'W1_FABLOJ' ,'01' , NIL},;  
{'W1_FORN' ,'01' , NIL},;  
{'W1_FORLOJ' ,'01' , NIL},;  
{'W1_QTDE' , 10 , NIL},;  
{'W1_PRECO' , 10 , NIL};  
})  
aAdd(aItens,{ {'W1_COD_I' ,'01' , NIL},;  
{'W1_POSICAO' , "0002" , NIL},;  
{'W1_POSIT' , "0002" , NIL},;  
{'W1_FABR' ,'01' , NIL},;  
{'W1_FABLOJ' ,'01' , NIL},;  
{'W1_FORN' ,'01' , NIL},;  
{'W1_FORLOJ' ,'01' , NIL},;  
{'W1_QTDE' , 20 , NIL},;  
{'W1_PRECO' , 20 , NIL};  
})  
  
MSExecAuto( {|X,Y,Z| EICSI400(X,Y,Z)} ,aCab ,aItens, 3)  
If lMsErroAuto  
lRetorno := .F.  
MostraErro()  
Else  
lRetorno:=.T.  
EndIf  
Return
```

**Saiba mais:**  
[**Rotina Automática EICSI400 - Atualização da Solicitação de Importação**](https://tdn.totvs.com/pages/releaseview.action?pageId=73084026)  
[**Solicitação de Importação (EICSI400 - SIGAEIC)**](https://tdn.totvs.com/pages/viewpage.action?pageId=306858805)
