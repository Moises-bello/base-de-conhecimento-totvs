---
article_id: 360019238311
category: ADVPL - Rotina Automática
content_hash: 3092d2c5d6022e5f2ce75d3850b139782c75b80057684d5460c745b140af167e
fetched_at: '2026-06-28T22:40:24.060832+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - EXECUÇÃO DA ROTINA AUTOMATICA
  MATA650 VIA SCHEDULE
type: support-article
updated_at: '2025-11-26T19:57:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019238311-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-EXECU%C3%87%C3%83O-DA-ROTINA-AUTOMATICA-MATA650-VIA-SCHEDULE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**A rotina em questão **MATA650** deveria gerar os empenhos (preencher a tabela SD4) quando concluída a execução do **MATA650**.  
Se o cliente inclui a OP pela rotina padrão, via menu, ou se chama a rotina do fonte anexado via menu, o processo ocorre, porém se executa a rotina via Schedule, a geração dos empenhos (carga na tabela SD4) não ocorre.  
  
**Ambiente**Protheus - ADVPL – SIGAPCP - A partir da versão 11.80  
  
**Solução**Para que o sistema acate a inclusão de empenho da rotina MATA650 é necessário habilitar os parâmetros, MV\_EXPLOPU  = S ,MV\_A650GEF  = S , além de acrescentar o *array* ,({'AUTEXPLODE' ,"S" ,NIL}}) .

Exemplo:

```
#Include "Protheus.ch"  
#include "rwmake.ch"  
#include "TbiConn.ch"  
   
User Function Tmata650()  
Local aMATA650 := {} //-Array com os campos  
LOCAL DDATABASE := CTOD("08/11/2018")  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//³ 3 - Inclusao ³  
//³ 4 - Alteracao ³  
//³ 5 - Exclusao ³  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
Local nOpc := 3  
Private lMsErroAuto := .F.  
   
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  
   
aMATA650 := { {'C2_FILIAL' ,"01" ,NIL},;  
 {'C2_NUM' ,"000060" ,NIL},;   
 {'C2_ITEM' ,"01" ,NIL},;   
 {'C2_SEQUEN' ,"001" ,NIL},;  
 {'C2_PRODUTO' ,"P001 " ,NIL},;  
 {'C2_LOCAL' ,"01" ,NIL},;  
 {'C2_QUANT' ,5 ,NIL},;  
 {'C2_DATPRI' ,DDATABASE ,NIL},;  
 {'C2_DATPRF' ,CTOD("09/11/2018") ,NIL},;  
 {'AUTEXPLODE' ,"S" ,NIL}}  
   
  
ConOut("Inicio : "+Time())  
   
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//³ Se alteracao ou exclusao, deve-se posicionar no registro ³  
//³ da SC2 antes de executar a rotina automatica ³  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
If nOpc == 4 .Or. nOpc == 5  
 SC2->(DbSetOrder(1))//FILIAL + NUM + ITEM + SEQUEN + ITEMGRD  
 SC2->(DbSeek(xFilial("SC2")+"000056"+"01"+"001"))  
EndIf  
   
msExecAuto({|x,Y| Mata650(x,Y)},aMata650,nOpc)  
If !lMsErroAuto  
 ConOut("Sucesso! ")  
Else  
 ConOut("Erro!")  
 MostraErro()  
EndIf  
   
ConOut("Fim : "+Time())  
   
RESET ENVIRONMENT  
   
Return Nil
```
