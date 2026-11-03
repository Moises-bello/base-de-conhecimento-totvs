---
article_id: 4413942366615
category: ADVPL - Ponto de Entrada
content_hash: ae2f8471d36090feb8ce3451c7a8ff086b5dbc00ccad89bd846053e86afac00a
fetched_at: '2026-06-28T22:40:11.551419+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo ponto de entrada
  MTC010MNU
type: support-article
updated_at: '2021-11-23T20:49:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413942366615-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-ponto-de-entrada-MTC010MNU
---

**Dúvida**Há um exemplo para utilização do Ponto de Entrada **MTC010MNU**?  
  
**Ambiente**Cross Segmento - BackOffice (Linha Protheus) - ADVPL - A partir da versão P12  
  
**Solução**Para utilizar o ponto de entrada **MTC010MNU** temos o exemplo abaixo:

```
#Include 'Protheus.ch'  
  
User Function MTC010MNU()  
  
AADD (aRotina,   {"Teste","Alert('Passou pelo PE MTC010MNU')", 0 , 2, 0,nil})  
  
Return
```

**Saiba mais**  
[MTC010MNU - Adiciona opções em formação de preços](https://tdn.totvs.com/pages/releaseview.action?pageId=6087830)
