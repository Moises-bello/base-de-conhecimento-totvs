---
article_id: 360034818993
category: ADVPL - Ponto de Entrada
content_hash: 321570926b5697e12d7c03a7d1362e41d8e7f7419b0c31df5f525ac7df1aae52
fetched_at: '2026-06-28T22:40:12.636507+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  MT110COR
type: support-article
updated_at: '2022-12-30T16:31:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034818993-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MT110COR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Estou utilizado o PE MT110COR e o mesmo não obedece a condição e não altera a legenda   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.8  
  
**Solução**

Para a condição criada pelo usuário funcionar é necessário que esteja na primeira opção do do Array, conforme o Exemplo abaixo:

```
#Include "PROTHEUS.CH"   
#include "TopConn.ch"   
#include "TOTVS.CH"  
  
User Function MT110COR()  
Local aNewCores := aClone(PARAMIXB[1])  
  
AAdd(aNewCores, { "C1_ZTIPOPR=='S'", "BR_PINK"})  
ASORT(aNewCores,,, { |x, y| x > y } )   
  
Return (aNewCores)
```
