---
article_id: 360029074312
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: ff0fdabe3900bcda6fb21a791674d33e5564c54469ea082a68477f293e5660d9
fetched_at: '2026-06-28T22:38:28.480251+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Execauto
  Rotina Automática Cadastro de Clientes - CRMA980
type: support-article
updated_at: '2025-07-16T18:28:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029074312-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-Execauto-Rotina-Autom%C3%A1tica-Cadastro-de-Clientes-CRMA980
---

**Dúvida**Preciso de um exemplo da rotina automática de cliente mais atualizada.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Faturamento – A partir da versão 12.1.17  
  
**Solução**Segue abaixo modelo de rotina automática, neste exemplo foi incluído novos campos obrigatórios.

**{"A1\_INCISS" ,"N" ,Nil},;**  
 **{"A1\_GRPVEN" ,"000001" ,Nil}}**

Exemplo

```
#Include "Protheus.ch"  
#include "TBICONN.CH"  
//-------------------------------------------------------------------  
/*/{Protheus.doc} MyCRMA980  
Função de exemplo para utilização da rotina automática de Clientes.  
/*/  
//-------------------------------------------------------------------  
User Function MyCRMA980()  
   
Local aSA1Auto := {}  
Local aAI0Auto := {}  
Local nOpcAuto := 3//MODEL_OPERATION_INSERT  
Local lRet := .T.  
   
Private lMsErroAuto := .F.  
   
lRet := RpcSetEnv("T1","D MG 01","Admin")  
  
If lRet  
   
 //----------------------------------  
 // Dados do Cliente  
 //----------------------------------  
 aAdd(aSA1Auto,{"A1_COD" ,"XBX141" ,Nil})  
 aAdd(aSA1Auto,{"A1_LOJA" ,"01" ,Nil})  
 aAdd(aSA1Auto,{"A1_NOME" ,"ROTINA AUTOMATICA" ,Nil})  
 aAdd(aSA1Auto,{"A1_NREDUZ" ,"ROTAUTO" ,Nil})   
 aAdd(aSA1Auto,{"A1_TIPO" ,"F" ,Nil})  
 aAdd(aSA1Auto,{"A1_END" ,"BRAZ LEME" ,Nil})   
 aAdd(aSA1Auto,{"A1_BAIRRO" ,"CASA VERDE" ,Nil})   
 aAdd(aSA1Auto,{"A1_EST" ,"SP" ,Nil})  
 aAdd(aSA1Auto,{"A1_MUN" ,"SAO PAULO" ,Nil})  
 aAdd(aSA1Auto,{"A1_INCISS" ,"N" ,Nil})  
 aAdd(aSA1Auto,{"A1_GRPVEN" ,"000001" ,Nil})  
   
 //---------------------------------------------------------  
 // Dados do Complemento do Cliente  
 //---------------------------------------------------------  
 aAdd(aAI0Auto,{"AI0_SALDO" ,30 ,Nil})  
   
 //------------------------------------  
 // Chamada para cadastrar o cliente.  
 //------------------------------------  
 MSExecAuto({|a,b,c| CRMA980(a,b,c)}, aSA1Auto, nOpcAuto, aAI0Auto)  
   
 If lMsErroAuto   
 lRet := lMsErroAuto  
 MostraErro() // Não funciona na execução via JOB  
 Else  
 Conout("Cliente incluído com sucesso!")  
 EndIf  
   
EndIf  
   
RpcClearEnv()  
   
Return lRet
```

**Saiba Mais**

**[DT Novo Fonte de Cadastro de Clientes em MVC](http://tdn.totvs.com/display/public/PROT/DT+Novo+Fonte+de+Cadastro+de+Clientes+em+MVC)**

**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Rotina Cadastro de Cliente (MATA030) Descontinuada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403853592471-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Rotina-Cadastro-de-Cliente-MATA030-Descontinuada?source=search)**
