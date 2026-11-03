---
article_id: 360051139193
category: Financeiro - Comissão
content_hash: f001d0146295049b4cf38e8de4a1c02e7de755cba20ffd5ec6da369d059cd18f
fetched_at: '2026-06-28T22:37:50.694880+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Comissão com abatimento
type: support-article
updated_at: '2026-01-14T16:46:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051139193-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Comiss%C3%A3o-com-abatimento
---

**Dúvida**  
Qual a finalidade do parâmetro **MV\_COMISAB** ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Comissão - Todas as versões   
  
**Solução**  
O tratamento de comissão para títulos de abatimento do tipo **AB-** é determinado pelo parâmetro **MV\_COMISAB**, aplicando-se exclusivamente à comissão no momento da baixa.

**Exemplos:**

O conteúdo: **.F.** Será considerado o valor cheio do título para comissão.  
Título 1.000,00  
AB- 100,00  
Ao baixar o título:  
Base para comissão = 1000,00  
Comissão (10%)**=** 100,00  
  
Com o conteúdo:  **.T.**será subtraído o valor do **AB-** para cálculo da comissão na baixa.  
Título 1.000,00  
AB-  100,00  
Ao baixar o título:  
Base para comissão = 900,00  
Comissão (10%)= 90,00  
  
**Saiba Mais**  
[Recálculo de Comissões (FINA440 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528#tabs-2)
