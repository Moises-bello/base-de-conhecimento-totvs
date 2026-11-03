---
article_id: 360007562871
category: Gestão de Transportes (TMS)
content_hash: e49248567149d21cd1b46ee72824c3587eab295d9807cdf51b68525320493cec
fetched_at: '2026-06-28T22:45:32.236009+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250NfOp Altera Documentos
  no Processo de Viagem
type: support-article
updated_at: '2023-03-01T19:29:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007562871-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250NfOp-Altera-Documentos-no-Processo-de-Viagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como implementar o ponto de entrada **TM250NfOp** - Altera Documentos no Processo de Viagem?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250NfOp** está localizado na função responsável pela geração dos dados para **Operadora de Frotas/Vale-Pedágio**.  
  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250NfOp - Altera Documentos no Processo de Viagem. ( < cFilDoc> , < cDoc> , < cSerie> ) --> aNFs  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cFilDoc |  |  | Array of Record |  |  | PARAMIXB[1] - Filial do Documento. |  |  |  |  |  | X |  |  |  |  |
|  | cDoc |  |  | Array of Record |  |  | PARAMIXB[2] - Documento. |  |  |  |  |  | X |  |  |  |  |
|  | cSerie |  |  | Array of Record |  |  |  |  |  |  |  |  | X |  |  |  |  |

**Retorno**:  
  
**aNFs**

(vetor)* Vetor com os novos documentos que farão parte do XML de envio para Operadora de Frotas/Vale-Pedágio, sendo:  
  aNFs[x,1] - Numero do Documento  
  aNFs[x,2] - Série do Documento  
  aNFs[x,3] - Código do Cliente Remetente  
  aNFs[x,4] - Loja do Cliente Remetente  
  aNFs[x,5] - Código do Cliente Destinatário  
  aNFs[x,6] - Loja do Cliente Destinatário  
  aNFs[x,7] - Peso  
  aNFs[x,8] - Valor da Mercadoria

**Observações**: Seu objetivo é possibilitar a alteração dos documentos envolvidos no processo. Este ponto de entrada será chamado para cada documento do viagem, ou seja, se a viagem possuir três documentos, este ponto de entrada será acionado três vezes.  
  
**Exemplos**:  
  
#INCLUDE 'Protheus.CH'

User Function TM250NfOp()

Local cFilDoc := ''

Local cDoc := ''

Local cSerie := ''

Local aRet := {}//-- Parametros recebidos do Pontos de entradac

FilDoc := PARAMIXB[1]

cDoc := PARAMIXB[2]

cSerie := PARAMIXB[3]//-- Formato do Array de Retorno:

//-- aRet[1] - Numero do Documento

//-- aRet[2] - Serie do Documento

//-- aRet[3] - Codigo do Cliente Remetente

//-- aRet[4] - Loja do Cliente Remetente

//-- aRet[5] - Codigo do Cliente Destinatario

//-- aRet[6] - Loja do Cliente Destinatario

//-- aRet[7] - Peso

//-- aRet[8] - Valor da Mercadoria

AAdd( aRet, { '000001',; 'UNI',; 'SP0002',; '01',; 'RJ0001',; '01',; 1000,; 1500.79 } )

AAdd( aRet, { '000002',; 'UNI',; 'SP0002',; '01',; 'RJ0001',; '01',; 156,; 180.05 } )

Return( aRet )
