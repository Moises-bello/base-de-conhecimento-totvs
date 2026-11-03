---
article_id: 360007713011
category: Gestão de Transportes (TMS)
content_hash: e3d6e273b7e9ae35b29af4cc8ad513ba1f697b14b50bbeb3f8a9a28c4f0f5832
fetched_at: '2026-06-28T22:45:32.297145+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM251CAN Estorno da Liberação
  do Contrato de Carreteiro
type: support-article
updated_at: '2023-03-01T19:25:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007713011-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM251CAN-Estorno-da-Libera%C3%A7%C3%A3o-do-Contrato-de-Carreteiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:05 min  
  
Dúvida**Como implementar o ponto de entrada TM251CAN - Estorno da Liberação do Contrato de Carreteiro?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM251CAN** está localizado no início do estorno da liberação do contrato de carreteiro. Utilizado para efetuar validações que permita ou não, efetuar o estorno da liberação.

**Programa** **Fonte**: TMSA251  
  
**Sintaxe**: TM251CAN - Estorno da Liberação do Contrato de Carreteiro ( [ cFilOri ], [ cViagem ], [ cNumCTC ] ) --> lRet  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cFilOri |  |  | Caracter |  |  | Filial de origem do contrato de carreteiro. |  |  |  |  |  |  |  |  |  |  |
|  | cViagem |  |  | Array of Record |  |  | Número da viagem do contrato de carreteiro. |  |  |  |  |  |  |  |  |  |  |
|  | cNumCTC |  |  | Array of Record |  |  | Número do contrato de carreteiro. |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
  

**lRet**

()* .F. - Bloqueia estorno da liberação de contrato..T. - Permite estornar liberação do contrato.

**Exemplos**:

#Include 'Protheus.ch'

User Function TM251Can()

Local lRet := .T.

Local cFilOri := ParamIxB[1]

Local cViagem := ParamIxB[2]

Local cNumCTC := ParamIxB[3]

If MsgYesNo("Bloqueia Estorno de Liberação?")

lRet := .F.

EndIf

Return (lRet)  
  
**Variáveis**:  
​

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |
