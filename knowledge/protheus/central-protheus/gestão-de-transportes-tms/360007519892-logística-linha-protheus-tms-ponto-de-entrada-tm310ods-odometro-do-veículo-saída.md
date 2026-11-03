---
article_id: 360007519892
category: Gestão de Transportes (TMS)
content_hash: 9addb3e8ca212ed0cbe162733ff6a79bda9b24ea18676c7a7d0e74eb939dff86
fetched_at: '2026-06-28T22:45:32.361610+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM310ODS Odometro do Veículo
  - Saída
type: support-article
updated_at: '2023-10-26T21:26:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007519892-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM310ODS-Odometro-do-Ve%C3%ADculo-Sa%C3%ADda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18591873919511)** Tempo aproximado para leitura: **00:00:25 min  
  
Dúvida**Como implementar o ponto de entrada **TM310ODS - Odometro do Veículo - Saída**?

**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM310ODS** serve para obter o **Odometro** **do Veículo - Saída**.

**Programa** **Fonte**: TMSA310.PRW

**Sintaxe**: **TM310ODS** - Odometro do Veículo - Saída ( [ Filial de Origem ], [ Viagem ], [ Veiculo ] ) --> nRetPE  
  
**Parâmetros**:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Nome |  |  | Tipo |  |  | Descrição |  |  | Default |  |  | Obrigatório |  |  | Referência |  |
|  | Filial de Origem |  |  | Caracter |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Viagem |  |  | Caracter |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Veiculo |  |  | Caracter |  |  |  |  |  |  |  |  |  |  |  |  |  |

 **Retorno**:

nRetPE

(numéri* onde nRetPE = quilometragem do veiculo

**Exemplos**:

*User function* **TM310ODS**()

Local cFilOri := ParamIXB[1]

Local cViagem := ParamIXB[2]

Local cCodVei := ParamIXB[3]

Local NKM :=15MsgAlert("Ponto de entrada TM310ODS"+" "+cFilOri+" "+cViagem+" " +cCodVei)

*Return* NKM
