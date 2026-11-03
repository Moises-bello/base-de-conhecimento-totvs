---
article_id: 25827815813655
category: Financeiro - Cadastros
content_hash: 4a263f2fb119dbc632c6d86b33a99eb392c02bc0ba24398f4495a5b5e8bc550c
fetched_at: '2026-06-28T22:37:53.203820+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA490 - Cálculo de
  Comissão com retenção de IR para MEI
type: support-article
updated_at: '2024-08-22T18:46:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25827815813655-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA490-C%C3%A1lculo-de-Comiss%C3%A3o-com-reten%C3%A7%C3%A3o-de-IR-para-MEI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25827841492247)**Tempo aproximado para leitura: **05:00 min****Dúvida**Como calcular comissão com retenção de **IRRF** para MEI?

**Ambiente****Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões**

**Solução**

Ajustar o **Cadastro de Clientes** para que o sistema entenda que é um **cliente MEI** e **contribuinte do ICMS**. E no **Cadastro de Vendedores** ajustar os campos de Base de Cálculo para os impostos.

**Cadastro de Clientes**

**Contribuinte (A1\_CONTRIBU)** = Sim

**TPJ (A1\_TJP)** = MEI

**Inscrição Estadual =** (Em branco)

**Exemplo:**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25827841494423)](blob:https://totvssuporte.zendesk.com/1502e1a1-4955-4111-a152-490aa978bd0f)

**Cadastro de Vendedores**

**A3\_BaseIR - Base c/ IRF?** = Sim

**A3\_ICMS - Base com ICMS?** = Sim ou Não  (conforme regra fiscal)

**A3\_ICMSRET - Base c/ ICM Ret?** = Sim ou Não (conforme regra fiscal)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25827841494935)](https://centraldeatendimento.totvs.com/hc/article_attachments/25827841494935)

Alguns impostos retidos também podem ser considerados ou não, base de cálculo da comissão, pela configuração de parâmetros como:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/25827815792151)](https://centraldeatendimento.totvs.com/hc/article_attachments/25827815792151)

**Saiba mais:**

[Comissão de Vendedores](https://tdn.totvs.com/pages/releaseview.action?pageId=235598457)

[Cálculo de Comissão de vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017467492-MP-SIGAFIN-Calculo-de-comiss%C3%A3o-sobre-vendas)
