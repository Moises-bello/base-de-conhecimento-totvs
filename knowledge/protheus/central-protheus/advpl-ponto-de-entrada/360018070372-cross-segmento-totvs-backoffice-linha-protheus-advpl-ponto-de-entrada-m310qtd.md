---
article_id: 360018070372
category: ADVPL - Ponto de Entrada
content_hash: 38cba3f240d87e8b567469e803b9ab440c5e9eea67b27e67d50a129b6f0f2165
fetched_at: '2026-06-28T22:40:11.834650+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  M310QTD
type: support-article
updated_at: '2021-12-29T19:45:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018070372-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-M310QTD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como é feita a validação da quantidade da origem no ponto de entrada M310QTD?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Esse ponto é de validação para auxilio para customização pode utilizar as variáveis *privates*

|  |  |  |
| --- | --- | --- |
| nQuant | cProduto1 | dDtValid2 |
| nQuant2UM | cLocOrig | cNumSerie |
| cFilOrig | cLoteDigi | cNumseqCQ |
| cLocaliz | cNumLote | lValTes |

```
#Include 'Protheus.ch'  
  
USER FUNCTION M310QTD   
local lRet := .F.  
  
Alert("M310QTD")  
// Customização do cliente   
IF cProduto1 == "PRODUTO00000001"  
    nQuant:=1  
    lRet:=.T.  
Endif  
  
RETURN lRet
```

**Saiba mais**[M310QTD - Define sugestão de quantidade a ser transferida da origem ao destino](http://tdn.totvs.com.br/pages/releaseview.action?pageId=21856308)
