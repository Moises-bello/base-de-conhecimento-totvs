---
article_id: 4530595808663
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 09b2bd61575e55bc6f7dc6c7fc25d9d02a16d897509dfb3cd9d5b287c492419e
fetched_at: '2026-06-28T22:38:29.933098+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Nota sobre relatórios Pré-DANFE e Pré-nota (MATR730)
type: support-article
updated_at: '2023-02-16T19:30:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4530595808663-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Nota-sobre-relat%C3%B3rios-Pr%C3%A9-DANFE-e-Pr%C3%A9-nota-MATR730
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30min** **Dúvida**Qual a nota sobre Pré-DANFE e Pré-nota?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - SIGAFAT - Todas as versões  
  
**Solução**

O módulo de faturamento não possui um **Pré-DANFE**, a geração da nota através da preparação, seja pelo pedido ou pelo faturamento, faturamento documento de saída, irá gerar as informações de SD2 e SF2 da nota e as integrações com os demais módulos do Protheus. Porém, a transmissão e geração do Danfe é uma etapa posterior.  
  
Neste caso, a formas de consulta antes de transmitir seria a consulta de nota fiscal (**MATC090**), se o que precisa é antes da geração só teremos a planilha financeira do pedido , que dará uma simulação do que poderá conter na nota após o faturamento.  
  
Existe também o relatório **MATR730 Pré-Nota** também, porém, ele não conterá os impostos que só serão gerados na nota, como o imposto PCC.
