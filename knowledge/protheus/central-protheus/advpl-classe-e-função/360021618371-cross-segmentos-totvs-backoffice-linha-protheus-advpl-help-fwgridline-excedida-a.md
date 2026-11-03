---
article_id: 360021618371
category: ADVPL - Classe e Função
content_hash: ca127ae382e994669ea758621db43542dabd63aeb37d247769388d9c5acb64bf
fetched_at: '2026-06-28T22:40:19.565088+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Help: FWGRIDLINE excedida
  a quantidade máxima de linhas'
type: support-article
updated_at: '2023-09-11T13:18:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021618371-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Help-FWGRIDLINE-excedida-a-quantidade-m%C3%A1xima-de-linhas
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17430261287319)*Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**HELP: FWGRIDLINE   
EXCEDIDA A QUANTIDADE MÁXIMA DE LINHAS  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**   
Esse incidente ocorre, pois no padrão a Grid em **MVC**suporta uma quantidade máxima **990 de linhas**.   
  
**Solução**Para solucionar essa ocorrência, utilize os métodos abaixo:  
**SetMaxLine()**  -> Determina quantas linhas uma grid pode possuir;  
**GetMaxLines()** -> Retorna quantas linhas o grid pode possuir.

**Observação**

Caso o incidente ocorra em rotinas padrões, deve ser verificado o comportamento junto a equipe do módulo.

**Saiba mais**[FWFormGridModel](http://tdn.totvs.com/display/framework/FWFormGridModel)
