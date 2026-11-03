---
article_id: 360007724771
category: Gestão de Transportes (TMS)
content_hash: 088a2303ed044bb5007a31d82c57f14f5d63b6632854ad116e4b6f0612b6a64d
fetched_at: '2026-06-28T22:45:32.351597+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM310ODE Odometro do Veículo
  - Entrada
type: support-article
updated_at: '2023-02-28T14:22:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007724771-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM310ODE-Odometro-do-Ve%C3%ADculo-Entrada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **TM310ODE** **- Odometro do Veículo - Entrada**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM310ODE** serve para obter o **Odometro do Veículo - Entrada.**  
  
**Programa** **Fonte**: TMSA310.PRW  
  
**Sintaxe**: TM310ODE - Odometro do Veículo - Entrada ( [ Filial de Origem ], [ Viagem ], [ Veiculo ] ) --> nRetPE  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | Filial de Origem |  |  | Caracter |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Viagem |  |  | Caracter |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Veiculo |  |  | Caracter |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Retorno**:  
  

**nRetPE**

(numerico)* onde nRetPE = quilometragem do veículo

**Exemplos**:  
  
*User function* **TM310ODE**()

Local cFilOri := ParamIXB[1]

Local cViagem := ParamIXB[2]

Local cCodVei := ParamIXB[3]

Local NKM :=10

*MsgAlert*("Ponto de entrada TM310ODE"+" "+cFilOri+" "+cViagem+" " +cCodVei)

*Return* NKM
