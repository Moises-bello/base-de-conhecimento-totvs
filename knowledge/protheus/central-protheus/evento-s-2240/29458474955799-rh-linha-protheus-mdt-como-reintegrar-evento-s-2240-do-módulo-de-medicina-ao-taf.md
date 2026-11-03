---
article_id: 29458474955799
category: Evento S-2240
content_hash: dfcbdee762406c271ca2bcf8344e5beacab72a3a03d83e81ed5eded1b993cc0a
fetched_at: '2026-06-28T22:45:23.498004+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - Como reintegrar evento S-2240 do módulo de Medicina
  ao TAF
type: support-article
updated_at: '2025-03-11T19:22:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29458474955799-RH-Linha-Protheus-MDT-Como-reintegrar-evento-S-2240-do-m%C3%B3dulo-de-Medicina-ao-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29458474916375) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como reintegrar evento S-2240 do módulo de Medicina ao TAF?

**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões

**Solução**

O módulo de medicina possui diversas rotinas que podem gerar/integrar o evento S-2240. Para que o evento seja reintegrado, é necessário alterar qualquer informação em uma das rotinas mencionadas abaixo:

**Riscos (MDTA180):** Atualizações > PPRA > Riscos  
**Ficha médica (MDTA005):** Atualizações > Atendimento Médico > Ficha Médica  
**Risco x EPI (MDTA125):** Atualizações > PPRA > Risco x EPI  
**EPI x Risco (MDTA130):** Atualizações > EPI > EPI x Risco  
**Relacionamentos (MDTA181):** Atualizações > PPRA > Relacionamentos  
**Laudos x Risco (MDTA215):** Atualizações > Laudos > Laudos x Risco  
**Risco x Laudos (MDTA216):** Atualizações > Laudos > Risco x Laudos  
**Entrega de EPI (MDTA695):** Atualizações > EPI > Funcionário x EPI  
**Ambiente Físico (MDTA165):** Atualizações > PPRA > Ambiente Físico

**Transf. Funcionário (GPEA180):** Módulo 07 > Atualizações > Funcionários > Tranferências

**Funcionário (GPEA010):** Módulo 07 > Atualizações > Funcionários > Funcionários

**Observações:**

A rotina de funcionários (GPEA010) irá gerar o S-2240 alterando qualquer campo somente se, em nenhum momento, o evento tiver sido integrado. Caso o evento já tenha sido integrado e precise ser reintegrado, será necessário alterar os campos de código da função, data da demissão ou alteração de salário.

**Não é possível realizar a reintegração em lote deste evento, somente funcionário por funcionário.**

**Saiba Mais**[Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
