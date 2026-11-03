---
article_id: 360051618833
category: RH - Rescisão
content_hash: 8b30ae9cbb991bcd6942b73be85adb66f6bfa66bf89388b095ac94fa1b3c44ee
fetched_at: '2026-06-28T22:43:52.216412+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Melhoria para conferência de rescisão complementar
type: support-article
updated_at: '2025-06-16T17:54:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051618833-RH-Linha-Protheus-GPE-Melhoria-para-confer%C3%AAncia-de-rescis%C3%A3o-complementar
---

**Dúvida**Melhoria para conferência de rescisão complementar.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Criação do campo RR\_VALORI (Valor Original), onde será gravado, no cálculo da rescisão complementar, o valor original da verba calculada na rescisão anterior, facilitando assim a conferência dos valores gerados na rescisão complementar.

Este campo será exibido em tela apenas no cálculo ou visualização de rescisões complementares.  
  
**Importante**

* Nas rescisões complementares dentro do mesmo mês da rescisão original o campo não será apresentado ou preenchido;
* A verba de Id 0318 não terá o campo RR\_VALORI preenchido;
* Ao calcular uma segunda rescisão complementar o campo RR\_VALORI será alimentado com a soma das rescisões anteriores;
* Verbas de horas/dias informadas terão a referência somadas com as rescisões anteriores, afim de facilitar a conferência do cálculo.
