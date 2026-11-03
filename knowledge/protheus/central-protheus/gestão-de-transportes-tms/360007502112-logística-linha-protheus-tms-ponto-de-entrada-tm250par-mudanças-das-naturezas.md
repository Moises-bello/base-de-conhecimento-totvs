---
article_id: 360007502112
category: Gestão de Transportes (TMS)
content_hash: a26b426423642bea8b44129637d2030940e152bc7ed40fdb6b2e9ce3ab5c0aa8
fetched_at: '2026-06-28T22:45:32.243815+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250PAR Mudanças das Naturezas
type: support-article
updated_at: '2023-02-28T17:12:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007502112-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250PAR-Mudan%C3%A7as-das-Naturezas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **TM250PAR** - **Mudanças das Naturezas**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250PAR** está localizado na rotina de geração de Contrato de Carreteiro.  
  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: **TM250PAR** - Mudanças das Naturezas ( < nTpNat> ) --> cNewNat  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | nTpNat |  |  | Array of Record |  |  |  |  |  |  |  |  | X |  |  |  |  |

**Retorno**:  
  

***cNewNat***

(caracter)* Nova natureza para considerar na geração do contrato de carreteiro

**Observações**: Seu objetivo é possibilitar a mudança das naturezas envolvidas no processo: Natureza do título de Pedágio, Natureza do título de Débito e Natureza do título de Contrato de Carreteiro.  
  
**Exemplos**:  
  
*User Function* **TM250PAR**()

Local nOpc := PARAMIXB[1]

Local cNewNat := ''

If nOpc == 1 //-- Natureza ref. ao Contrato de Carreteiro

cNewNat := PadR('NAT-CTC',Len(SED->ED\_CODIGO)) //-- Nova Natureza

Else If

nOpc == 2 //-- Natureza ref. ao título de Pedágio

cNewNat := PadR('NAT-PDG',Len(SED->ED\_CODIGO)) //-- Nova Natureza

Else If

nOpc == 3 //-- Natureza Utilizada nos Titulos Gerados para a Filial de Debito

cNewNat := PadR('NAT-DEB',Len(SED->ED\_CODIGO)) //-- Novaatureza

End If

*Return*(cNewNat)
