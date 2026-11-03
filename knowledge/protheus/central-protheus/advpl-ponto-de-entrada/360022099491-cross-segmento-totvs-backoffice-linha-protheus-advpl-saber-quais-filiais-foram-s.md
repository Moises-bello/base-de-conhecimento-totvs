---
article_id: 360022099491
category: ADVPL - Ponto de Entrada
content_hash: 0d920213bcf2fe9546b41a40bf18f942786897b7b7d36a93fdf9de1f740da2be
fetched_at: '2026-06-28T22:40:12.875722+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Saber quais filiais
  foram selecionadas no momento da execução do PE SPDFISBLCK
type: support-article
updated_at: '2021-12-30T17:53:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022099491-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Saber-quais-filiais-foram-selecionadas-no-momento-da-execu%C3%A7%C3%A3o-do-PE-SPDFISBLCK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min****Dúvida**Como forneço para o PE a informação de qual ou quais filiais o usuário clicou na geração do SPED Fiscal quando eu usar o PE SPDFISBLCK ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**O ponto de entrada [SPDFISBLCK](http://tdn.totvs.com/pages/releaseview.action?pageId=203761344) não fornece a informação de qual ou quais filiais foram selecionadas para a geração do arquivo. Somente é possível identificar qual filial está sendo executada no momento da passagem pelo PE através da variável pública **cFilAnt**, este PE será invocado no processo de acordo com a quantidade de filiais selecionadas, uma execução para cada filial selecionada, em cada uma das execuções a variável **cFilAnt**conterá a filial processada no momento.
