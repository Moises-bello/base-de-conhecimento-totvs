---
article_id: 360051123993
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c6cdc5208f4b62c669b37d7e6b63e035a1a124872e8e45316a49b2ecd884f74f
fetched_at: '2026-06-28T22:42:03.861125+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - SIGAFIS - CAMPO 02 COD_DA REGISTRO C112 SPED FISCAL
type: support-article
updated_at: '2021-04-28T14:25:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051123993-MP-SIGAFIS-CAMPO-02-COD-DA-REGISTRO-C112-SPED-FISCAL
---

**Dúvida**

Como preencher o campo **02** **COD\_DA** do registro **C112** como documento estadual de arrecadação ou GNRE?  
   
 **Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
   
**Solução**Para o sistema levar a informação no campo **02** **COD\_DA** do registro **C112** como documento de arrecadação no sped fiscal, precisa preencher o campo **F6\_TIPOIMP** na guia nacional de recolhimento igual a 0 (**Guia Estadual**), com o campo diferente de 0 (zero) o arquivo será gerado com o campo COD\_DA = 1 (**GNRE**).
