---
article_id: 360007428151
category: Gestão de Transportes (TMS)
content_hash: 8106704a7d4de274b03406019171fad5a534286ddc7a9eb3ac11d49e3bcf429e
fetched_at: '2026-06-28T22:45:32.400867+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TME75QRY Validar Registro
  na rotina Edi Automático
type: support-article
updated_at: '2022-06-17T18:42:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007428151-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TME75QRY-Validar-Registro-na-rotina-Edi-Autom%C3%A1tico
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:00:50 min**

**Dúvida**Como implementar o ponto de entrada **TME75QRY** Validar Registro na rotina Edi Automático?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TME75QRY** está localizado na rotina **EDI** **Automático** (**TMSAE75**) e consiste em validar o registro retornado pela *Query*. Também é possível verificar se o registro será apresentado ou não pela **Mark** **browser**.  
  
**Programa Fonte**: **TMSAE75.PRW**  
  
**Parâmetros**:  
PARAMIXB[1] CGC do Remetente   
PARAMIXB[2] Número do Documento   
PARAMIXB[3] Serie do Documento   
PARAMIXB[4] Código do Produto   
PARAMIXB[5] Recno  
PARAMIXB[6]  Alias da query  
  
**Retorno**:  
Booleano(lRET)

* .T. = O registro selecionado pela *query* será incluso no vetor que será apresentado na tela!
* .F. = O registro selecionado pela *query* não será incluso no vetor que será apresentado na tela!

**Exemplos**:  
User Function **TME75Qry()**  
  
Local \_cCGCREM := PARAMIXB[1] //--CGC do Remetente   
Local \_cDOC         := PARAMIXB[2] //--Numero do Documento   
Local \_cSERIE       := PARAMIXB[3] //--Serie do Documento   
Local \_cCODPRO  := PARAMIXB[4] //--Código do Produto   
Local \_cRECNO     := PARAMIXB[5] //--Recno  
Local \_cAlias := PARAMIXB[6] //-- Alias da *query*.  
Local lPEQRY := .T.  
  
If Empty(\_cCODPRO) .Or. Empty(\_cDOC)   
    lPEQRY := .F.   
    MsgAlert("Executando o P.E. **TME75Qry**, O registro selecionado pela *query* não será incluso no vetor aItensEDI!")   
Else   
    lPEQRY := .T.   
    MsgAlert("Executando o P.E. **TME75Qry**, O registro selecionado pela *query* será incluso no vetor aItensEDI!")   
EndIf   
  
Return(lPEQRY)
