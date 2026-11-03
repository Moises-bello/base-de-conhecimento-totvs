---
article_id: 360007322372
category: Gestão de Transportes (TMS)
content_hash: fb4bc0145fbda1cc63a9c5f1a2155869ea1093384a789c59cf98764e1dbfb394
fetched_at: '2026-06-28T22:45:32.195681+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250CNT Contrato Complementar
type: support-article
updated_at: '2022-11-29T19:24:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007322372-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250CNT-Contrato-Complementar
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **TM250CNT - Contrato Complementar**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250CNT**está localizado no fonte **TMSA250** - **Geração Complemento do Contrato de Carreteiro,** e é executado na rotina do contrato complementar.  
  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Sintaxe**: TM250CNT - Contrato Complementar ( [ @cFilOri ] ) --> lRet  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | cFilOri |  |  | Caracter |  |  | Filial de Origem do Contrato |  |  |  |  |  |  |  |  | X |  |

**Retorno**:  
  

**lRet**

(logico)* Variavel de retorno para geração do contrato complementar

**Exemplos**:  
  
User Function TM250CNT()

Local lRet :=.T.

Local cFilial := AllTrim(ParamIXB[1])

Aviso('Ponto TM250CNT','Filial: '+cFilial,{'OK'})

Return lRet
