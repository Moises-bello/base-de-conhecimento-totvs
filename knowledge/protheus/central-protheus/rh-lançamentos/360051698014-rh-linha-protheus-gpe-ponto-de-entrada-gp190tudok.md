---
article_id: 360051698014
category: RH - Lançamentos
content_hash: 219e838f6c89c9a4eb14d7e528b8fd8cc38cbf1d45c90928abf346c3fcb93ca9
fetched_at: '2026-06-28T22:43:31.397457+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de entrada GP190TudOk()
type: support-article
updated_at: '2025-07-24T17:04:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051698014-RH-Linha-Protheus-GPE-Ponto-de-entrada-GP190TudOk
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26164859796119) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Detalhamento sobre o ponto de entrada GP190TudOk().  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Este ponto de entrada tem como objetivo permitir **criar validações ao confirmar a inclusão de uma tarefa**.

O ponto de entrada é executado ao final das validações padrões da função **GP190TudOk().**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082028894)

**Exemplo**:

#INCLUDE 'PROTHEUS.CH'  
#INCLUDE 'PARMTYPE.CH'

User Function GP190TOK()

Local lRet := .T.  
  
If Empty(GdFieldGet("RO\_ITEM"))  
Help(,, "HELP",, + CRLF + "Item não foi informado,", 1, 0)  
lRet := .F.  
EndIf  
  
Return lRet

**Saiba mais:**

[RH - Lançamentos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781734-RH-Lan%C3%A7amentos)
