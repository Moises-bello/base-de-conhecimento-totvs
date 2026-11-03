---
article_id: 360016522272
category: ADVPL - Web Service
content_hash: 3d52e4fd2d6692394c94143745522025edbef684e79e1c42248522b9324702c0
fetched_at: '2026-06-28T22:40:10.425240+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Depuração em múltiplas
  threads
type: support-article
updated_at: '2021-12-29T13:21:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016522272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Depura%C3%A7%C3%A3o-em-m%C3%BAltiplas-threads
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como debugar uma rotina de webservice Protheus?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**Para realizar a depuração de rotinas *webservice* **Protheus**é necessário que o parâmetro **Permitir Depuração em múltiplas Threads**esteja ativado no TDS.  
No TDS 11.3, esta opção pode ser ativada diretamente na barra de botões conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012765672/mceclip0.png)

Ou no caminho Janela > Preferências > Developer Studio > Depuração, conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012765712/mceclip1.png)

Após conferir se esta opção está ativada, posicione os pontos de parada no arquivo fonte de *webservice* e inicie uma execução pela opção **Depurar**, mantenha essa execução aberta e faça a requisição do serviço ao qual deseja **depurar**, neste momento o compilador deve parar nos pontos solicitados.
