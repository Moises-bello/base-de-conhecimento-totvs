---
article_id: 360007331772
category: Gestão de Transportes (TMS)
content_hash: d358d13e7b2c15ca0551bf179f4321f30bc3f535edeafa0a140e172ce3d79caf
fetched_at: '2026-06-28T22:45:32.221845+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250IND Filtro geração
  por período
type: support-article
updated_at: '2022-11-29T20:19:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007331772-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250IND-Filtro-gera%C3%A7%C3%A3o-por-per%C3%ADodo
---

**Dúvida**Como implementar o ponto de entrada **TM250IND** Filtro geração por período?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **TM250IND** permite alterar o filtro padrão, localizado na geração de contratos de carreteiros por período.  
  
**Programa** **Fonte**: TMSA250.PRW  
  
**Parâmetros**: Vetor (PARAMIXB) contendo um item, onde variável tipo caractere contendo filtro padrão.

**Retorno**: Variável tipo caractere contendo filtro usado no IndRegua.  
  
**Exemplo**:

```
User Function TM250IND()  
  
Local cRet := PARAMIXB[ 1 ]  
MsgInfo(cRet)  
  
Return cRet
```
