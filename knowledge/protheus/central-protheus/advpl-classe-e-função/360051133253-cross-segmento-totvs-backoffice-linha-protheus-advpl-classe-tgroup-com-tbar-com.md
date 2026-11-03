---
article_id: 360051133253
category: ADVPL - Classe e Função
content_hash: a2f0747e2d3b7d7588cef6b898a310d31cfc513a352cfc5d7775c1e529035407
fetched_at: '2026-06-28T22:40:14.560902+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe  TGroup com
  TBar com comportamentos divergentes Desktop e via Webapp
type: support-article
updated_at: '2022-01-04T21:12:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051133253-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-TGroup-com-TBar-com-comportamentos-divergentes-Desktop-e-via-Webapp
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Utilizando a classe TGroup() com a classe TBar() apresenta comportamentos distintos no ambiente **Desktop** e via **Webapp** (HTML).

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**Trata-se de uma limitação.  
As classe **[TBar](https://tdn.totvs.com/display/tec/TBar)**e **[TGroup](https://tdn.totvs.com/display/tec/TGroup)**pertence a hierarquia da classe **[TSrvObject](https://tdn.totvs.com/display/tec/TSrvObject)**e a mesma não é suportados ou com comportamento diferenciado entre as versões HTML e Desktop.  
  
**Saiba mais**[Diferenças entre as versões HTML e Desktop](https://tdn.totvs.com/pages/viewpage.action?pageId=118885352)
