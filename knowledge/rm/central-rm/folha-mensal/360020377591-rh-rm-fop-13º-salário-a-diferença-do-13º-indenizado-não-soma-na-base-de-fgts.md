---
article_id: 360020377591
category: Folha Mensal
content_hash: 01e52966e7b626af62e6d4f5ded9aba35847b5bd66e55e1801e239041695d62a
fetched_at: '2026-06-28T22:46:59.560874+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - 13º Salário: A diferença do 13º indenizado não soma na Base
  de FGTS'
type: support-article
updated_at: '2025-03-12T19:50:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020377591-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-A-diferen%C3%A7a-do-13%C2%BA-indenizado-n%C3%A3o-soma-na-Base-de-FGTS
---

**Ocorrência**Ao gerar uma Rescisão Complementar ou Diferença Salarial, o evento de código de calculo 109 - BASE DE FGTS DE DIFERENÇA SALARIAL DE 13º SALÁRIO, não está somando com o valor do evento de código de calculo 98 - DIFERENÇA 13º SALÁRIO INDENIZADO RESCISÃO.  
   
 **Ambiente**RM - Folha de Pagamento - Todas as versões  
  
**Solução**Nesse caso o evento de código de calculo 109 não considera o evento de código de calculo 98 devido as verbas indenizatórias serem consideradas na GRRF. Sendo assim, o evento de código de calculo 109 será levado somente para a SEFIP. Portanto, neste caso não poderá ser somado para que não seja considerado em duplicidade na GRRF.
