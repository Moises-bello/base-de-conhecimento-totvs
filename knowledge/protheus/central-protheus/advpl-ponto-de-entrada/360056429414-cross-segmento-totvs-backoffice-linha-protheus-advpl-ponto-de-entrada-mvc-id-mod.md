---
article_id: 360056429414
category: ADVPL - Ponto de Entrada
content_hash: cbcb6d4f68971fd0af6608e12a8375ddba4553b5aaa76e2e93e02046a5e07436
fetched_at: '2026-06-28T22:40:11.590896+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL  - Ponto de entrada
  MVC id modelpos: Executa duas vezes'
type: support-article
updated_at: '2024-09-12T19:26:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056429414-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MVC-id-modelpos-Executa-duas-vezes
---

**Dúvida**Por qual motivo o ID MODELPOS do ponto de entrada MVC é chamado duas vezes?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12  
  
**Solução**Esse comportamento é **padrão** dos **pontos de entrada** utilizados em rotina **MVC.** O ponto de entrada **ModelPos** é executado na validação do modelo e também na execução do evento do modelo.

**Saiba Mais  
[Ponto de Entrada Padrão do MVC](https://tdn.totvs.com/pages/releaseview.action?pageId=208345968)**
