---
article_id: 360017701111
category: ADVPL - Classe e Função
content_hash: edb05d518224fa02fc3979018f8928f501afb45aac30678c91ec3e1dec684d5f
fetched_at: '2026-06-28T22:40:19.330349+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Função CTSMCONTA
  na integração excel
type: support-article
updated_at: '2022-01-10T18:52:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017701111-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-CTSMCONTA-na-integra%C3%A7%C3%A3o-excel
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**É possível que a função CTSMCONTA()traga todas as filiais, na integração do excel?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012959811/mceclip0.png)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Não é possível pois a função teria que ter como parâmetro filial. Neste caso é necessário criar uma função de usuário e gera uma planilha excel através da Classe **[FWMsExcelEx](http://tdn.totvs.com/display/framework/FWMsExcelEx)**
