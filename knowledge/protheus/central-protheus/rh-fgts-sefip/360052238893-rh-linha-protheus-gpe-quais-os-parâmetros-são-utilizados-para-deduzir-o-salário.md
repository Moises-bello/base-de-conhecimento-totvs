---
article_id: 360052238893
category: RH - FGTS / SEFIP
content_hash: 6ddff778df693b8cb9c482d4de6cb92bfc2d549901e918ece903ec4d0bc00a0b
fetched_at: '2026-06-28T22:43:41.464130+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Quais os parâmetros são utilizados para deduzir
  o salário família e salario maternidade no SEFIP
type: support-article
updated_at: '2021-07-17T03:26:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052238893-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-s%C3%A3o-utilizados-para-deduzir-o-sal%C3%A1rio-fam%C3%ADlia-e-salario-maternidade-no-SEFIP
---

**Dúvida**Quais os parâmetros que são utilizados para deduzir o salário família e o salário maternidade no SEFIP?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Os parâmetros **MV\_****SALFDED** e o**MV\_SALMDED** são os responsáveis por levar as verbas de Salário Família e Maternidade que estiverem no conteúdo dele como dedução na **SEFIP**.

**Exemplo:**Se eu tiver as seguintes verbas:

400 - verba 1  
450 - verba 2  
500 - verba 3

O conteúdo do parâmetro deverá ficar da seguinte forma:

400 (Para uma verba).  
400450 (Para duas verbas)  
400450500 (Para três verbas)  
  
**Saiba mais:**<https://tdn.totvs.com/display/public/PROT/FGTS>
