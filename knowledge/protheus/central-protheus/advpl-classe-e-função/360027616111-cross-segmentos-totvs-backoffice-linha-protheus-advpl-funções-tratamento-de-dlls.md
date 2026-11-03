---
article_id: 360027616111
category: ADVPL - Classe e Função
content_hash: 3a105dcf03f7d713ddfd6abecd85011758f60ea29abbe1748bf9a074c999c54e
fetched_at: '2026-06-28T22:40:19.365351+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Funções tratamento
  de DLLs
type: support-article
updated_at: '2022-01-10T18:06:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616111-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%B5es-tratamento-de-DLLs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:00 min****Dúvida**Existe alguma função padrão do protheus para comunicação com periféricos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 11.80  
  
**Solução**Não temos uma classe ou função especifica integração do hardware ao sistema, como por exemplo balanças, maquina, leitores e etc.

Nesses casos é necessário desenvolvimento como a criação de uma DLL como **Middleware**, no modelo da documentação fornecida pelo autor da DLL, pois as funções [ExecInDLLRun](http://tdn.totvs.com.br/display/tec/ExecInDLLRun), [ExeDLLRun2](http://tdn.totvs.com.br/display/tec/ExeDLLRun2). [ExeDLLRun3](http://tdn.totvs.com.br/display/tec/ExeDLLRun3), não executam DLLs de terceiros.   
  
**Observação**  
É necessário o conhecimento de criação de DLLs. Segue as funções tratamento de DLLs:  
[ExecInDLLOpen](http://tdn.totvs.com/display/tec/ExecInDLLOpen)  
[ExecInDLLRun](http://tdn.totvs.com/display/tec/ExecInDLLRun)  
[ExecInDLLClose](http://tdn.totvs.com/display/tec/ExecInDLLClose)  
  
**Saiba mais**  
[Pagina da arvore de funções](http://tdn.totvs.com/pages/viewpage.action?pageId=6063481)
