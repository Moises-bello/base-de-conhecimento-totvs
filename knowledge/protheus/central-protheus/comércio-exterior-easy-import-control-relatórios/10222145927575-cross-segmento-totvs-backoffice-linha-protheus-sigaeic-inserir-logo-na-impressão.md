---
article_id: 10222145927575
category: Comércio Exterior - Easy Import Control - Relatórios
content_hash: bd7ff8849026bd14fe15fab0cdbb7527226a2c4e06d5fd84d6080cc4fb925755
fetched_at: '2026-06-28T22:39:43.404252+00:00'
product: protheus
section_id: 1500001549662
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Inserir logo na
  impressão da Purchase Order (EICPO150) no modelo em HTML
type: support-article
updated_at: '2024-05-07T14:47:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10222145927575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Inserir-logo-na-impress%C3%A3o-da-Purchase-Order-EICPO150-no-modelo-em-HTML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como faço para inserir um logo na rotina de Impressão do Purchase Order (**EICPO150**) no modelo HTML?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*– Todas versões  
  
**Solução**

Para que seja impresso o logotipo, deverá seguir os seguintes passos:

1. Possuir um arquivo do logo com extensão PNG.
2. Colocar o arquivo do logo na pasta do StartPath(pasta **\system\**).
3. O nome do arquivo deverá ser: **logo\_po.png**

Caso seja necessário um logotipo por empresa:

1. O nome do arquivo deverá ser (sem espaços nas extremidades): **99logo\_po.png .**

Caso seja necessário um logotipo por empresa + filial do registro

1. O nome do arquivo deverá ser (sem espaços nas extremidades): **9901logo\_po.png .**

Caso seja um único logotipo para todos:

1. O nome do arquivo deverá ser (sem espaços nas extremidades): **logo\_po.png .**

**Saiba mais**[Impressão do Purchase Order - EICPO150](https://tdn.totvs.com/pages/releaseview.action?pageId=306858818)
