---
article_id: 11651428486039
category: ADVPL - Classe e Função
content_hash: 3602cddb5a6086037b0f0e474111d1920dc94f0fcd8c3d7d268b9cfc2ecdfb0e
fetched_at: '2026-06-28T22:40:20.633692+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Diferença no funcionamento
  das funções GetNewPar e GetMv. '
type: support-article
updated_at: '2023-01-13T19:36:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11651428486039-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Diferen%C3%A7a-no-funcionamento-das-fun%C3%A7%C3%B5es-GetNewPar-e-GetMv
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual a diferença no funcionamento das funções GetNewPar e GetMv?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - a partir da versão 12.1.27  
  
**Solução**

O **GetNewPar** utiliza o **SuperGerMV** que utiliza cache dos parâmetros(Melhor performance), desta forma caso o parâmetro seja alterado (**PutMV**) durante a execução da *thread* o novo conteúdo somente será atualizado ao abrir uma nova *thead* ;  
O **GetMv** não faz o uso de cache, ele sempre consulta direto no banco.  
O uso de cada um vai depender da necessidade da rotina; Se é algo mais "fixo", poderá utilizar o **GetNewPar** ou **SuperGetMv**, se for algo dinâmico, alterado durante o uso, poderá utilizar o **GetMv**.

**Saiba mais**[GetNewPar](https://tdn.totvs.com/pages/releaseview.action?pageId=24346931)  
[SuperGetMv](https://tdn.totvs.com/pages/releaseview.action?pageId=24347112)  
[GetMv](https://tdn.totvs.com/pages/releaseview.action?pageId=24346929)  
[Performance SuperGetMV x GetMV](https://tdn.engpro.totvs.com.br/display/public/framework/Desempenho+SuperGetMV+x+GetMV)
