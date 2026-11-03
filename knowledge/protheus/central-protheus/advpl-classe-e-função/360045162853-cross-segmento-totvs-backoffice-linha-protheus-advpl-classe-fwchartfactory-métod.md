---
article_id: 360045162853
category: ADVPL - Classe e Função
content_hash: e8d8e83de92e07c96e6b897075c60a82f26a11d06214b49324b48eb730667244
fetched_at: '2026-06-28T22:40:14.567429+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe FWChartFactory
  método para gerar imagem
type: support-article
updated_at: '2025-05-03T22:17:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045162853-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWChartFactory-m%C3%A9todo-para-gerar-imagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**É possível gerar uma imagem do gráfico utilizando a classe **FWChartFactory** ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Solução**A classe **FWChartFactory** e seus gráficos passaram por uma modernização, utilizando de novos componentes do binário, esses componentes por sua vez não possuem o método **SaveToPng**, portanto a sua implementação não será possível.Com isso ainstância de gráfico gerada pela [**FWChartFactory**](https://tdn.totvs.com/display/public/PROT/FwChartFactory) teve seu método **SaveToPng** depreciado.  
  
**Saiba mais**  
[FWChartFactory](https://tdn.totvs.com/display/public/PROT/FwChartFactory)
