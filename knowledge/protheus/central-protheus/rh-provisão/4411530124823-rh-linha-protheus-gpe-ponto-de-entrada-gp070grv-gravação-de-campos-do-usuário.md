---
article_id: 4411530124823
category: RH - Provisão
content_hash: f18a7accd19f3c49601b58c6f96f433c1a48ddba99efd9cfc1c219457d2bc3fe
fetched_at: '2026-06-28T22:43:55.998814+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada GP070GRV - Gravação de Campos
  do Usuário
type: support-article
updated_at: '2025-10-24T12:40:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411530124823-RH-Linha-Protheus-GPE-Ponto-de-Entrada-GP070GRV-Grava%C3%A7%C3%A3o-de-Campos-do-Usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998195331991) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Utilização do ponto de entrada GP070GRV.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**

### **01. VISÃO GERAL**

## Essa implementação tem o objetivo de permitir a gravação de campos criados pelo usuário.

**Programa Fonte**

GPEM070.PRX

**Sintaxe**

GP070GRV - Gravação de Campos do Usuário ( [ PARAMIXB[1] ], [ PARAMIXB[2] ], [ PARAMIXB[3] ] )

### **02. EXEMPLO DE UTILIZAÇÃO**

## #INCLUDE 'PROTHEUS.CH' User Function GP070GRV() Local aArea := GetArea() Local cFilial := PARAMIXB[1] Local cMat := PARAMIXB[2] Local nTpProv := PARAMIXB[3] //Alert( "Passou pelo PE GP070GRV" ) If nTpProv != 4 IF RecLock( "SRT" , .F. ) SRT->RT\_CAMPOX := SRA->RA\_CODFUNC SRT->RT\_CAMPOY := SRA->RA\_ADMISSA SRT->( MsUnlock() ) EndIF EndIf RestArea( aArea ) Return

### **03. Parâmetros**

**Outras Ações / Ações relacionadas**

| Nome | Tipo | Descrição |
| --- | --- | --- |
| Nome | Tipo | Descrição |
| --- | --- | --- |
| PARAMIXB[1] | Caracter | Filial do funcionário. |
| PARAMIXB[2] | Caracter | Matrícula do funcionário. |
| PARAMIXB[3] | Numérico | Tipo de provisão. |

### **04. Variáveis**

**Principais Campos e Parâmetros**

| Nome | Tipo | Escopo | Pode Alterar |
| --- | --- | --- | --- |
|  | Array of Record | Global | Não |

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

*<https://tdn.totvs.com/pages/viewpage.action?pageId=642638735>*
