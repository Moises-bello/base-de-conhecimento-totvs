---
article_id: 21712260990999
category: ADVPL - Classe e Função
content_hash: 8b0f3de7de94905f3650f9cd0f0d3121adc78be660570e3cfcf3a9df23d89588
fetched_at: '2026-06-28T22:40:18.271824+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- Função de calculo
  de data
type: support-article
updated_at: '2024-03-01T17:46:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21712260990999-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-de-calculo-de-data
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21712260972183) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Existe função AdvPL para efetuar o cálculo de datas?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

O AdvPL não possui função específica para se fazer o cálculo entre duas datas, todavia caso a variável esteja no formato data, basta utilizar o operador de subtração ou então converter o dado para data e efetuar o cálculo.

**Exemplo**

```
#Include "totvs.ch"  
#Include "parmtype.ch"  
  
  
User Function CalcDT()  
    Local dDateA := SToD("20240201")  
    Local dDateB := SToD("20240220")  
    Local nDias  := 0  
  
  
    nDias := dDateB - dDateA  
  
  
    MsgInfo("A diferença entre as duas datas informadas é de: " + CValToChar(nDias) + " Dia(s)", "Calculo de data")  
Return NIL
```

**Saiba Mais**

[SToD](https://tdn.totvs.com/display/tec/SToD)

[Operadores AdvPL](https://tdn.totvs.com/display/tec/Operadores+Comuns)
