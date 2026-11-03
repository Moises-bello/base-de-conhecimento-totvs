---
article_id: 360022352872
category: ADVPL - Rotina Automática
content_hash: bd1c80b4e3ca2ea5107c8205386bbb9b5de12fc7d6e1240ad912331309bdac12
fetched_at: '2026-06-28T22:40:25.058346+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática
  via web service
type: support-article
updated_at: '2022-06-21T17:22:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022352872-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-via-web-service
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Rotina automática funciona normalmente quando executada no SmartClient ou TOTVS *Developer Studio*, porém gera erro ao ser executada via *web service*.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 11.8  
  
**Causa**Algumas rotinas (ex: EICPO400) trabalham de formas diferentes se executadas em módulos que não sejam o seu de origem, pois de acordo com o módulo informado, campos são adicionados ou removidos e obrigatoriedades são acrescentadas ou retirados.  
  
**Solução**Utilizar a função StartJob() para iniciar uma nova thread sem ambiente preparado e por meio desta, realizar a preparação do ambiente utilizando a função RPCSetEnv() para o módulo correto.  
  
**Saiba mais**  
[RpcSetEnv - Abertura do ambiente em rotinas automáticas](http://tdn.totvs.com/pages/releaseview.action?pageId=6814927)  
[StartJob](http://tdn.totvs.com/display/tec/StartJob)
