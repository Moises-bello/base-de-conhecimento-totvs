---
article_id: 360007373651
category: Gestão de Transportes (TMS)
content_hash: a518f8815f4d191216a2e122632461b2b736f02fa0b6526d75dd0b9793129a87
fetched_at: '2026-06-28T22:45:29.539354+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada EDIREG40 Revisão de campos
  gravados no fonte
type: support-article
updated_at: '2022-06-20T14:45:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007373651-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-EDIREG40-Revis%C3%A3o-de-campos-gravados-no-fonte
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** **Tempo aproximado para leitura:**00:00:40 min **Dúvida**Como implementar o ponto de entrada **EDIREG40** - Revisão de campos gravados no fonte?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **EDIREG40** é utilizado para verificação de campos que serão gravados no arquivo de trabalho **RT2** no fonte **EDIMT.****Programa** **Fonte**: EDIMT.PRW  
  
**Sintaxe**: EDIREG40 - Revisão de campos gravados no fonte ( [ ] )  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  |  |  |  | Array of Record |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
  
      ()  
  
**Observações**: Como este ponto de entrada foi incluído antes do MSUNLOCK na tabela RT2 é possível fazer verificações e alterar campos como os opcionais.  
  
**Exemplos**:  
  
#Include "Protheus.ch"   
  
User Function EDIREG40()//--Alterando valores do ICMS e FRETE sempre que passar pelo ponto.  
  
RT2->VALICMS := "10"  
RT2->VALFRET := "200"  
MSGALERT("Passou pelo Ponto de entrada EDIREG40")  
  
Return Nil  
  
**Variáveis**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |
