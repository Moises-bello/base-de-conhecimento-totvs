---
article_id: 360021888352
category: RH – DIRF
content_hash: a4d679648334f1dad4169ee1be3c867cd252a3a8d2864cdab532f60f9bd841dd
fetched_at: '2026-06-28T22:44:06.917188+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar a incidências para DIRF referente
  aos verbas de adiantamento
type: support-article
updated_at: '2025-08-15T17:25:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021888352-RH-Linha-Protheus-GPE-Como-parametrizar-a-incid%C3%AAncias-para-DIRF-referente-aos-verbas-de-adiantamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34212671064727)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como devem ser parametrizadas as incidências para DIRF, referente as verbas de adiantamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.  
  
**Solução**As empresas que pagam a folha no **mês seguinte à competência** (por exemplo: 5º dia útil) e que pagaram adiantamento, devem informar **incidência** para DIRF tipo **A** no código de pagamento (Id. Cálculo **0006**) e incidência para DIRF tipo **N** no código do desconto do adiantamento (Id. Cálculo **0007**).   
A verba de **IR Adiantamento**, no Código de Base (Id. Cálculo **0012**), deve permanecer com a incidência do tipo **N**.  
  
Para empresas que pagam a folha **dentro do mês de competência**, os códigos de pagamento e desconto de adiantamento devem ser preenchidos com**N** na **incidência** da DIRF.

**Saiba Mais**  
[Sugestão de Incidências de Verbas para a DIRF](http://tdn.totvs.com/pages/viewpage.action?pageId=223177735)

[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
