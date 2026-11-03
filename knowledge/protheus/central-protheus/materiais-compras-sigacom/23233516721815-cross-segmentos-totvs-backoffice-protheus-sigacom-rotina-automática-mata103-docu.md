---
article_id: 23233516721815
category: Materiais - Compras (SIGACOM)
content_hash: 56f20faa9e8f1b8ab3f97faa8fcb91ff0c09d1efb81af9381be94a63074f7227
fetched_at: '2026-06-28T22:41:25.239846+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Automática MATA103
  - Documento Devolução Terceiros.
type: support-article
updated_at: '2024-05-03T13:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23233516721815-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Autom%C3%A1tica-MATA103-Documento-Devolu%C3%A7%C3%A3o-Terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23233493699223) Tempo aproximado para leitura: **00:10:00min** **Dúvida**Como posso criar Rotina Automática MATA103 para Documento de Devolução Terceiros?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras- Versão 12  
  
**Solução**Siga o exemplo abaixo:

**//DOCUMENTO DEVOLUÇÃO - Terceiros**

**[ADV0050\_EXECAUTO MATA103 DEVOLUÇÂO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=322147442)**

#Include "[Protheus.ch](http://protheus.ch/)"  
#Include "[RwMake.ch](http://rwmake.ch/)"  
#Include "[TbiConn.ch](http://tbiconn.ch/)"

User Function EXEC103()

Local aCabec := {}  
Local aItens := {}  
Local aLinha := {}  
Local cDoc := ""  
PRIVATE lMsErroAuto := .F.

ConOut(PadC(OemToAnsi("Teste de Inclusao de NFE DEVOLUCAO COM NOTA DE ORIGEM NFS"),80))

PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "COM" FUNNAME "MATA103"

cDoc := "DEV000002"  
aCabec := {}  
aItens := {}

aadd(aCabec,{"F1\_TIPO" ,"D" })  
aadd(aCabec,{"F1\_FORMUL" ,"N" })  
aadd(aCabec,{"F1\_DOC" ,cDoc })  
aadd(aCabec,{"F1\_SERIE" ,"000" })  
aadd(aCabec,{"F1\_EMISSAO" ,dDataBase })  
aadd(aCabec,{"F1\_FORNECE" ,"2 " })  
aadd(aCabec,{"F1\_LOJA" ,"1 " })  
aadd(aCabec,{"F1\_ESPECIE" ,"NFE" })

aLinha := {}  
aadd(aLinha,{"D1\_ITEM" ,"001" ,Nil})  
aadd(aLinha,{"D1\_COD" ,"2 " ,Nil})  
aadd(aLinha,{"D1\_QUANT" ,1 ,Nil})  
aadd(aLinha,{"D1\_VUNIT" ,10 ,Nil})  
aadd(aLinha,{"D1\_TOTAL" ,10 ,Nil})  
**aadd(aLinha,{"D1\_TES" ,"101" ,Nil})//TES DEVOLUÇÃO**  
aAdd(aLinha,{"D1\_CF" ,"000 " ,Nil})  
aAdd(aLinha,{"D1\_DOC" ,cDoc ,Nil}) // \*  
aAdd(aLinha,{"D1\_SERIE" ,"000" ,Nil}) // \*  
aAdd(aLinha,{"D1\_EMISSAO",dDataBase ,Nil}) // ADICIONEI  
**aadd(aLinha,{"D1\_NFORI" ,"000005 " ,Nil}) // nota de origem**  
**aadd(aLinha,{"D1\_SERIORI","1 " ,Nil})**  
**aadd(aLinha,{"D1\_ITEMORI","01" ,Nil})**  
**AAdd(aLinha,{"D1\_IDENTB6","000334" ,Nil}) // d2\_nunseq**  
aadd(aLinha,{"AUTDELETA" ,"N" ,Nil})  
aadd(aItens,aLinha)

MSExecAuto({|x,y,z| mata103(x,y,z)},aCabec,aItens,3)

If !lMsErroAuto  
ConOut("Incluido com sucesso! "+cDoc)  
Else  
ConOut("Erro na inclusao!")  
mostraerro()  
EndIf

ConOut(OemToAnsi("Fim : ")+Time())

RESET ENVIRONMENT

Return(.T.)

**Saiba Mais:**

* [PCOM12003 - Documento de Entrada (Rotina Automática MATA103 - EXECAUTO)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=235592777)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
