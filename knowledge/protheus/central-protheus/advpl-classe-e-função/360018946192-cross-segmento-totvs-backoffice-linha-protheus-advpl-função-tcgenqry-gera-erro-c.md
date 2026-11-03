---
article_id: 360018946192
category: ADVPL - Classe e Função
content_hash: 7c0e27eb4a286b9b16f351d2d464f57e7d1e52f659ea27faffc61b35c9b2471c
fetched_at: '2026-06-28T22:40:16.842507+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função TCGENQRY
  gera erro com procedure
type: support-article
updated_at: '2022-01-03T19:51:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018946192-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-TCGENQRY-gera-erro-com-procedure
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**A Função **TcGenQry()** gera erro quando executa uma *Procedure*  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A função **TcGenQry()** é especifica para execução de *Query's* e não para *Procedures*, ou seja a *Query* se inicia com *SELECT*. Isto vale para o comando **ADVPL TCQuery**, que por trás executa **TcGenQry()**. Para a necessidade de executar um sintaxe SQL, deve-se utilizar a **TCSqlExec()**

**Saiba mais  
[TCGenQry](http://tdn.totvs.com/display/tec/TCGenQry)  
[TCSqlExec](http://tdn.totvs.com/display/tec/TCSQLExec)**
