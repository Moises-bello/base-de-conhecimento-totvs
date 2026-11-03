---
article_id: 115013374368
category: ADVPL - Classe e Função
content_hash: 876e5a80984a346ac86b8204c8fe6ec9eb4ab203766f33321ef54965784689e1
fetched_at: '2026-06-28T22:40:14.115583+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Classe FwDefsize
type: support-article
updated_at: '2021-09-01T20:01:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013374368-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FwDefsize
---

**Dúvida**Após a migração para o Protheus 12 onde os botões de ação foram para o Cabeçalho das rotinas, algumas rotinas customizadas tiveram os primeiros campos da tela sobrepostos pela barra de botões padrão (do cabeçalho), como ajustar?

![](https://tdn.totvs.com/download/attachments/306841356/image2017-10-11_11-33-9.png?version=1&modificationDate=1507732389000&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/306841356/image2017-10-11_11-33-33.png?version=1&modificationDate=1507732413000&api=v2)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**É necessário utilizar a classe [FWDefSize](https://tdn.totvs.com/display/framework/FWDefSize) pois o posicionamento da sua customização devem está chumbados. Na MSDIalog basta manipular os valores do posicionamento " @ 05,005 " ou utilizar a classe [FWDefSize.](https://tdn.totvs.com/display/framework/FWDefSize)  
  
**Saiba mais**  
[ADV0037 FWDEFSIZE](http://tdn.totvs.com/display/PROT/ADV0037_FUN_FWDEFSIZE)
