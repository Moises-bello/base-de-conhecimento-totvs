---
article_id: 360021393591
category: RH - Provisão
content_hash: 327080c78763ef0a5178c0953a3df9f8acaffc501a14ecabce05089bcfbfa35b
fetched_at: '2026-06-28T22:43:56.856898+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE- Adicional de Cargo de Confiança, que incorpora salário,
  não está sendo calculada na provisão
type: support-article
updated_at: '2025-10-24T12:57:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021393591-RH-Linha-Protheus-GPE-Adicional-de-Cargo-de-Confian%C3%A7a-que-incorpora-sal%C3%A1rio-n%C3%A3o-est%C3%A1-sendo-calculada-na-provis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998014000919)**Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**A verba de Adicional de Cargo de Confiança, que incorpora salário não está sendo calculada na provisão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Verifique no **SIGACFG - Ambiente - Cadastros - Parâmetros:** MV\_CSALINC  (Ex. 201601).

Ajuste este parâmetro para que sejam considerados os valores dos novos identificadores, além do salário do mês, gravado no identificador de cálculo 0318.

Verbas Obrigatórias:

* ID 0671 (Base Adicional Tempo Serviço Mês)
* ID 0672 (Base Adicional Insalubridade Mês)
* ID 0673 (Base Adicional Periculosidade Mês).
* ID 1421 (Base Adicional Confiança Mês)
* ID 1422 (Base Adicional Transferência Mês)

Crie as verbas com tipo Base Provento, Percentual 100%.

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
