---
article_id: 360007711271
category: Gestão de Transportes (TMS)
content_hash: bb031dfbc98620e12f0197ce9d9ee7edc56fe084aa682b0aae58be61ecd29adc
fetched_at: '2026-06-28T22:45:32.263692+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250SLD Informações sobre
  saldo do Contrato de Carreteiro
type: support-article
updated_at: '2023-03-01T19:27:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007711271-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250SLD-Informa%C3%A7%C3%B5es-sobre-saldo-do-Contrato-de-Carreteiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:55 min  
  
Dúvida**Como implementar o ponto de entrada **TM250SLD** - Informações sobre saldo do Contrato de Carreteiro?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250SLD** está localizado no programa **TMSA250** (**Contrato** **de** **Carreteiro**). O mesmo tem como objetivo apresentar informação sobre o saldo do contrato de carreteiro.  
  
  
**Programa Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250SLD - Informações sobre saldo do Contrato de Carreteiro ( [ DTY->DTY\_FILIAL ], [ DTY->DTY\_VIAGEM ], [ cNrContr ], [ ] )  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | DTY->DTY\_FILIAL |  |  | Caracter |  |  | Filial |  |  |  |  |  |  |  |  |  |  |
|  | DTY->DTY\_VIAGEM |  |  | Array of Record |  |  | Numero da Viagem |  |  |  |  |  |  |  |  |  |  |
|  | cNrContr |  |  | Array of Record |  |  | Numero do contrato de carreteiro |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Array of Record |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Retorno:**

()

**Exemplos:**

#Include 'Protheus.ch'

User Function TM250SLD()

Local cFilial := ParamIXB[1]

Local cViagem := ParamIXB[2]

Local cNrContr := ParamIXB[3]

MsgInfo("Filial: " +cFilial+ " Viagem: " +cViagem+ " Numero do Contrato: " +cNrContr)

Return ()

**Variáveis:**

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Escopo |  |  | Pode Alterar |  |  | descrição |  |
|  |  |  |  | Array of Record |  |  | Global |  |  | Não |  |  |  |  |
