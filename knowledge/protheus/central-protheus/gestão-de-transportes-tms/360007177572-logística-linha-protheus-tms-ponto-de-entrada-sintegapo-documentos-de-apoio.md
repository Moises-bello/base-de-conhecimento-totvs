---
article_id: 360007177572
category: Gestão de Transportes (TMS)
content_hash: 22d757718288fbe217ece56cbd89114745d1016ba36ffc2d04f400f4d50183e8
fetched_at: '2026-06-28T22:45:29.582744+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada SINTEGAPO Documentos de
  Apoio
type: support-article
updated_at: '2022-06-20T19:01:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007177572-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-SINTEGAPO-Documentos-de-Apoio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)  Tempo aproximado para leitura: 00:00:20 min  
  
Dúvida**Como implementar o ponto de entrada **SINTEGAPO** Documentos de Apoio?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **SINTEGAPO** verifica se a *Query* na **DT6** retornará todos os documentos de apoio.  
  
**Programa** **Fonte**: **TMSXFUNC.PRW**  
  
**Sintaxe**: SINTEGAPO - Documentos de Apoio ( [ cQuery ] ) --> cRet

**Parâmetros**:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Nome | Tipo | Descrição | Default | Obrigatório | Referência |
| cQuery | Caracter | Query para selecionar os documentos de apoio. |  |  |  |

**Retorno**:  
cRet

     (caracter)  
     *Query* para selecionar os documentos de apoio.  
  
O retorno deste ponto de entrada deve conter somente os tipo de documento de **APOIO**.  
  
**Exemplos**:   
  
#Include "Protheus.ch"   
  
User Function SINTEGAPO()   
  
Local ret1 := PARAMIXB[1]   
  
MSGALERT("Passou pelo Ponto de entrada SINTEGAPO")  
  
Return (ret1)  
  
**Variáveis**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Tipo | Escopo | Pode Alterar | Descrição |
|  | Array of Record | Global | Não |  |
