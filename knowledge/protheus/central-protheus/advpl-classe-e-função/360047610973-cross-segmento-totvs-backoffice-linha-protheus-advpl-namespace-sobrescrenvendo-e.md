---
article_id: 360047610973
category: ADVPL - Classe e Função
content_hash: 946ce5ea4934b30f9db991473957e7609ba420ea789c7e349e10e90a38ee3a55
fetched_at: '2026-06-28T22:40:17.054802+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - NameSpace Sobrescrenvendo
  em TL++
type: support-article
updated_at: '2022-06-13T17:02:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047610973-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-NameSpace-Sobrescrenvendo-em-TL
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Problemas em criar classes em **Namespace** diferentes  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**Atualmente a compilação não contempla o uso de fontes com o mesmo nome em caminhos (paths) diferentes.  
Isso ocorre independente do uso de **Namespace** ou **TL++**, o mesmo ocorre com fontes **ADVPL** (PRW).  
A compilação **ADVPL/TL++** tem por característica não fazer relacionamento com o caminho do fonte.  
Alterar esse comportamento não é viável pois envolve outras funcionalidades.  
Com isso é necessário o uso de nomes de programas diferentes.
