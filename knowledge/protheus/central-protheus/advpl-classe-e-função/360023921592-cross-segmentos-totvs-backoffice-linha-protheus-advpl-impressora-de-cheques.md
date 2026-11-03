---
article_id: 360023921592
category: ADVPL - Classe e Função
content_hash: 1e33ac36a6e77b9efec00541e3c5cc3053b33296b77794c9c6cab60c095d96af
fetched_at: '2026-06-28T22:40:20.437506+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Impressora de cheques
type: support-article
updated_at: '2022-01-11T22:43:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023921592-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Impressora-de-cheques
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Preciso criar uma integração do Protheus com a impressora de cheques Menno, para tal eu preciso enviar um comando em hexadecimal direto para a porta de impressão.

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**O Protheus no padrão não possui integração com modelo de impressora Menno e não temos uma classe especifica para esse tipo de impressora.  
Será necessário o desenvolvimento de DLL’s que integrem o hardware ao sistema.  
  
As informações disponíveis são as funções tratamento de DLLs:   
[ExecInDLLOpen](http://tdn.totvs.com/display/tec/ExecInDLLOpen)  
[ExecInDLLRun](http://tdn.totvs.com/display/tec/ExecInDLLRun)  
[ExecInDLLClose](http://tdn.totvs.com/display/tec/ExecInDLLClose)  
  
**Saiba mais**  
[Pagina da arvore de funções](http://tdn.totvs.com/pages/viewpage.action?pageId=6063481)
