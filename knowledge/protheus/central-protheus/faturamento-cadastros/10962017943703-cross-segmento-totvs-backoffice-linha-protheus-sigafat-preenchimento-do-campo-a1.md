---
article_id: 10962017943703
category: Faturamento - Cadastros
content_hash: 78f60a896eb849d4ba71b27a0ef65d971ba75a2e6ae642351cae4199b4da6baa
fetched_at: '2026-06-28T22:38:36.532674+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  Preenchimento
  do campo A1_COD_MUN
type: support-article
updated_at: '2022-12-14T20:17:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10962017943703-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-do-campo-A1-COD-MUN
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como preencher o campo **A1\_COD\_MUN** digitando o nome do Município   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**Será necessário criar um gatilho de um ponto de entrada. Segue abaixo os exemplos :  
  
Gatilho  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10961816121111)  
  
Ponto de Entrada

#Include "TOTVS.ch"

User Function T05GTMV()  
Local oModel := FwModelActive()  
Local cCodMun := IIf(!Empty(M->A1\_EST), Posicione("CC2", 2, XFilial("CC2") + Upper(NoAcento(FwFldGet("A1\_MUN"))), "CC2\_CODMUN"), "")

If (Empty(M->A1\_EST) == .T.)  
Help(NIL, NIL, "ERRO", NIL, "Ausência de Preenchimento",;  
1, 0, NIL, NIL, NIL, NIL, NIL, {"Preencha o campo Estado (A1\_EST)"})  
Else  
oModel:GetModel("SA1MASTER"):LoadValue("A1\_COD\_MUN", cCodMun)  
EndIf  
Return (NIL)  
  
O sistema vai preencher o código do município ao digitar o nome do Município quando o Estado estiver preenchido  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10961868923671)
