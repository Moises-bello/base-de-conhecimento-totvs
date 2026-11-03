---
article_id: 18259717715223
category: Configurações
content_hash: b516061f2899d9f63e7c03a5347b7fed56183bf77a7b2dd5b982a1b88692eb85
fetched_at: '2026-06-28T22:46:49.463997+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Inibe reversão de valores na provisão mensal de férias para
  situações onde houve abatimento de férias
type: support-article
updated_at: '2025-04-08T18:01:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18259717715223-RH-RM-FOP-Inibe-revers%C3%A3o-de-valores-na-provis%C3%A3o-mensal-de-f%C3%A9rias-para-situa%C3%A7%C3%B5es-onde-houve-abatimento-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18259740891159) Tempo aproximado para leitura: **00:01:07 min****Dúvida**Qual a funcionalidade do parâmetro Inibe reversão de valores na provisão mensal de férias para situações onde houve abatimento de férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O parâmetro Inibe reversão de valores na provisão mensal de férias para situações onde houve abatimento de férias está localizado em: **Módulo Folha de Pagamento | Configurações | Parametrizador | Folha Normal | Contabilização.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18259669109911)**

Com esse parâmetro desmarcado, no momento da contabilização das provisões de férias, o RM Labore gera o lançamento contábil sendo o valor da provisão do mês atual menos o valor da provisão do mês anterior, que ficará negativo ocorrendo então a inversão das contas contábeis. Caso ele seja marcado, o procedimento é ao contrário.

Saiba mais:  
[Contabilização - FOP](https://tdn.totvs.com/pages/releaseview.action?pageId=452719364)
