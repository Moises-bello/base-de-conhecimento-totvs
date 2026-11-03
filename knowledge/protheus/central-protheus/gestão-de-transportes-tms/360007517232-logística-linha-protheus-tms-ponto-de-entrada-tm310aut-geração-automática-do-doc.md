---
article_id: 360007517232
category: Gestão de Transportes (TMS)
content_hash: 9391702312bd842d28e5064b31664156801c3dd91d344073c997dad141e62496
fetched_at: '2026-06-28T22:45:32.334594+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM310AUT - Geração Automática
  do Documento de Reentrega
type: support-article
updated_at: '2023-03-01T19:34:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007517232-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM310AUT-Gera%C3%A7%C3%A3o-Autom%C3%A1tica-do-Documento-de-Reentrega
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min  
  
Dúvida**Qual o ponto de entrada TM310AUT - Geração Automática do Documento de Reentrega?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM310AUT** está localizado na rotina de gravação do fechamento da viagem **TMSA310GRV** e tem o objetivo de permitir a geração automática do documento de reentrega.  
  
  
**Programa** **Fonte**: TMSA310.PRW  
  
**Sintaxe**: TM310AUT - Geração Automática do Documento de Reentrega ( [ cFilOri ], [ cViagem ] ) --> lAutRee  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cFilOri |  |  | Caracter |  |  | Filial de Origem da Viagem |  |  |  |  |  |  |  |  |  |  |
|  | cViagem |  |  | Array of Record |  |  | Número da Viagem |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
  

**lAutRee**

logico* .T. - permite a geração automática do documento de reentrega.F. - não permite a geração automática do documento de reentrega

**Variáveis**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |
