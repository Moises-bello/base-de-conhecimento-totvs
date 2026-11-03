---
article_id: 360057462654
category: ADVPL - Relatório
content_hash: a570ddb34bc05810c0fb04b4ab68a9549a28d82db5032d81172f9f1da8133f0d
fetched_at: '2026-06-28T22:40:22.856281+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Formula personalizada
  em relatório não funciona.
type: support-article
updated_at: '2023-03-15T22:43:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057462654-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Formula-personalizada-em-relat%C3%B3rio-n%C3%A3o-funciona
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Formula personalizada em relatório não funciona.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.23  
  
**Solução**Houve uma mudança no tratamento de fórmulas no **TReport** ,no binário **Lobo guará,** é necessário utilizar o *Return*, como no exemplo abaixo:

```
IF CELL(AC)>0  
 Return 0  
ELSE  
 Return 1  
ENDIF
```

![finr140.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360097403654/finr140.gif)

**Saiba mais:**  
**[TReport](https://tdn.totvs.com/display/PROT/TReport)**  
**[TOTVS | Platform](https://tdn.totvs.com/display/tec/TOTVSTEC)**
