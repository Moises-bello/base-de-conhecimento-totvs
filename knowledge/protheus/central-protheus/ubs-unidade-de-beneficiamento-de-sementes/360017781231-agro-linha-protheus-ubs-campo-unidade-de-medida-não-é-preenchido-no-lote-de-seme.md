---
article_id: 360017781231
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: bbcc5a5d1457fe86656731644085fd785dc30500aa62d3751ff8baf39eb01f7d
fetched_at: '2026-06-28T22:45:34.791326+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - UBS - Campo unidade de medida não é preenchido no lote
  de sementes
type: support-article
updated_at: '2025-06-20T15:37:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017781231-Agro-Linha-Protheus-UBS-Campo-unidade-de-medida-n%C3%A3o-%C3%A9-preenchido-no-lote-de-sementes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22238134221079) Tempo aproximado para leitura: **00:00:35 min  
  
Dúvida**Ao selecionar o produto na rotina de **Lote de Sementes**, o campo **Unidade de Medida** não é preenchido. Como proceder?

![Campo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/6949136302103)

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBS - Unidade de Beneficiamento de Sementes - Versão 12  
  
**Solução**Esse problema ocorre porque o tamanho dos campos referentes à **Unidade de Medida** está divergente.   
Para solucionar o problema, realize os seguintes passos:

**1.** Acesse o **SIGACFG**;

**2.** Verifique o tamanho dos campos: **B1\_UM**, **D3\_UM** e **NP9\_UM.** Estes campos necessitam ter o mesmo tamanho.

**3.** Altere o tamanho dos campos deixando-os compatíveis. O ideal é que estejam como determina o campo **B1\_UM**.
