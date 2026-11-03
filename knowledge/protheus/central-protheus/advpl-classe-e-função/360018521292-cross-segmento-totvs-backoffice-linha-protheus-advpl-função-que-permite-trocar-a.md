---
article_id: 360018521292
category: ADVPL - Classe e Função
content_hash: 7ddf89fa47e1782666c4946d4a447055f36fa24a6a34708a3c014191d33ee884
fetched_at: '2026-06-28T22:40:14.306584+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Função que permite
  trocar a empresa em tempo de execução
type: support-article
updated_at: '2025-08-25T17:29:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018521292-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-que-permite-trocar-a-empresa-em-tempo-de-execu%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33539617263383)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Existe alguma função que permite trocar a empresa em tempo de execução?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Não existe uma função específica que permita consultas ou manipulação em uma empresa 'B' enquanto estiver conectado em ambiente da empresa 'A'. Para possibilitar uma ação desse tipo é necessário que outra Thread seja iniciada para uma execução independente, e nela preparado um ambiente para tal. O recurso para essa necessidade seria a função [StartJob](http://tdn.totvs.com/display/tec/StartJob).   
A seguir um exemplo de rotina automática, para a inclusão de um produto, em duas empresas diferentes simultaneamente:

**Threads Sem interface:**

```
#Include 'Protheus.ch'  
#Include 'TBICONN.ch'  
  
User Function tStJb010()  
Local aVetor := {}  
  
PRIVATE lMsErroAuto := .F.  
Private INCLUI := .T.  
  
PREPARE ENVIRONMENT EMPRESA "01" FILIAL '0101'USER "Usuario" PASSWORD "****" MODULO "EST"  
  
aVetor:= {{"B1_COD" ,'PA01           ' ,NIL},;   
 {"B1_DESC" ,"TESTE EXECAUT " ,NIL},;   
 {"B1_TIPO" ,"PA" ,Nil},;   
 {"B1_UM" ,"UN" ,Nil},;   
 {"B1_PESO" ,10 ,Nil},;   
 {"B1_LOCPAD" ,"01" ,Nil},;  
 {"B1_RASTRO" ,"N" ,Nil},;  
 {"B1_LOCALIZ" ,"N" ,Nil}}  
   
//Inclui o produto na empresa corrente ('99')   
MSExecAuto({|x,y| Mata010(x,y)},aVetor,3)  
  
If !lMsErroAuto   
 ConOut("Produto incluído na empresa 99")   
Else   
 ConOut("Erro na inclusao!")   
 MostraErro()  
EndIf  
  
//Inclui o mesmo produto na empresa '02'  
STARTJOB("U_T010Auto",getenvserver(),.t.,aVetor)  
  
RESET ENVIRONMENT  
   
Return  
  
User Function T010Auto(aVetor)  
PRIVATE lMsErroAuto := .F.  
Private INCLUI := .T.  
  
PREPARE ENVIRONMENT EMPRESA "02" FILIAL '0201'USER "Usuario" PASSWORD "****" MODULO "EST"  
  
MSExecAuto({|x,y| Mata010(x,y)},aVetor,3)  
  
If !lMsErroAuto   
 ConOut("Produto incluído na empresa 02 ")   
Else   
 ConOut("Erro na inclusao!")   
 MostraErro()  
EndIf  
  
RESET ENVIRONMENT  
  
Return
```
