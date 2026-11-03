---
article_id: 360007132252
category: Gestão de Transportes (TMS)
content_hash: f23a777a246a13eda4f47b720a92bdee629e35c4fc2d6c10461daf462875d8ba
fetched_at: '2026-06-28T22:45:32.396150+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TME75MRK Marque/Desmarque
  do Checkbox do EDI Automático
type: support-article
updated_at: '2022-06-17T18:44:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132252-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TME75MRK-Marque-Desmarque-do-Checkbox-do-EDI-Autom%C3%A1tico
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:00:50 min**

**Dúvida**Como implementar o ponto de entrada **TME75MRK** Marque/Desmarque do *Checkbox* do EDI Automático?

**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TME75MRK**está localizado na rotina **EDI** **Automático** **TMSAE75** e permite ao usuário validar cada item selecionado pelo ***Checkbox*** - Marca/Desmarca. É possível **Marcar** ou **Desmarcar** todos os documentos ou selecioná-los um a um.  
  
Programa Fonte:**TMSAE75.PRW**  
  
**Parâmetros**:  
1º CGC do Remetente   
2º Número da Nota fiscal   
3º Serie da Nota Fiscal   
4º Posição   
5º Checkbox lTodosMark   
6º Vetor com itens da Nota fiscal  
  
**Retorno**: Booleano  
  
**Exemplos**:  
  
User Function TME75MRK()  
  
Local \_cCGCREM := PARAMIXB[1] //--CGC do Remetente  
Local \_cNUMNFC := PARAMIXB[2] //--Numero da Nota fiscal  
Local \_cSERNFC := PARAMIXB[3] //--Serie da Nota Fiscal  
Local \_cPOSIC := PARAMIXB[4] //--Posição  
Local \_cTodosM := PARAMIXB[5] //--Checkbox lTodosMark  
Local \_ItensED := PARAMIXB[6] //--Vetor com itens da Nota Fiscal  
Local lPEMRK := .T.　  
  
If \_cTodosM  
     lPEMRK := .T.  
     MsgAlert("Executando o P.E. **TME75MRK**, Marcar todos!")  
Else  
     lPEMRK := .F.  
EndIf  
  
Return (lPEMRK)
