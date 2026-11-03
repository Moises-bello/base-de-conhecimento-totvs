---
article_id: 360020731812
category: ADVPL - Ponto de Entrada
content_hash: e1686d9809ba5517511a3f2c2baae5c8c8334e8a743b3baae92a151f401b7953
fetched_at: '2026-06-28T22:40:12.898678+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização do Ponto
  de entrada F260BUT
type: support-article
updated_at: '2021-12-30T18:05:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020731812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-do-Ponto-de-entrada-F260BUT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Cliente alega que ao utilizar o PE F260BUT esta carregando o botão porém esta sumindo os demais botões do ações relacionadas.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Neste exemplo o ponto de entrada será acionado porém manterá os demais botões do ações relacionadas pois a variável implementada no caso aTeste esta recebendo por PARAMIXB

```
#include "PROTHEUS.CH"           
  
User Function F260BUT()  
local aTeste := PARAMIXB  
      aAdd(aTeste,{'Texto do Item','TST0023( )',0,5 })  
Return aTeste
```

Por exemplo se fizer dessa maneira declarando o aRotina como local e atribuindo a ele um *Array* na tela da rotina FINA260 vai sumir o ações relacionadas e manter só a sua mensagem no caso Texto do Item como botão:

```
#include "PROTHEUS.CH"           
User Function F260BUT()  
Local aRotina := {}  
      aAdd(aRotina,{'Texto do Item','TST0023( )',0,5 })  
Return aRotina
```
