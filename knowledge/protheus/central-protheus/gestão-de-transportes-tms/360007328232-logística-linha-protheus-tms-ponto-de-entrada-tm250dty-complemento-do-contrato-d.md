---
article_id: 360007328232
category: Gestão de Transportes (TMS)
content_hash: 8d53c709aea2556c12d3c685bdea1c79f704d14afce652fc886d867bfe6be445
fetched_at: '2026-06-28T22:45:32.212692+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada TM250DTY Complemento do
  Contrato de Carreteiro
type: support-article
updated_at: '2021-12-30T15:00:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007328232-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM250DTY-Complemento-do-Contrato-de-Carreteiro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min  
  
Dúvida**Como implementar o ponto de entrada **TM250DTY** **- Complemento do Contrato de Carreteiro**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - A partir da versão 11.80.  
  
**Solução**O ponto de entrada **TM250DTY** está localizado no fonte **TMSA250** - **Geração** **Complemento** **do** **Contrato** **de** **Carreteiro** e é executado após a gravação do complemento do contrato de carreteiro.  
  
Programa Fonte: **TMSA250.PRW**  
Sintaxe: **TM250DTY - Complemento do Contrato de Carreteiro**  
Retorno: **NIL**  
 **Exemplos**:

```
#INCLUDE "rwmake.ch"  
User Function TM250DTY()  
MsgAlert('PONTO TM250DTY - Contrato de complemento ' + DTY->DTY_NUMCTC + ' gerado com sucesso ')  
Return(Nil)
```
