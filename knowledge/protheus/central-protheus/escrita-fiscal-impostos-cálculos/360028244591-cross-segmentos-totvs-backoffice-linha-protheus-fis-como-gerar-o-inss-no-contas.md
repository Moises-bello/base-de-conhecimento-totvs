---
article_id: 360028244591
category: Escrita Fiscal - Impostos - Cálculos
content_hash: c0cc58d26349064ad6f32b9a086ca103be2d58bb1230499f9a667ed00d98117c
fetched_at: '2026-06-28T22:39:31.158703+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS-Como gerar o INSS no
  contas a pagar pelo faturamento
type: support-article
updated_at: '2021-07-29T12:40:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028244591-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-o-INSS-no-contas-a-pagar-pelo-faturamento
---

**Dúvida**

Cliente gera um pedido de vendas pelo faturamento com INSS mas o imposto é de sua responsabilidade, qual a configuração necessária para essa situação?

**Ambiente**  
Protheus - Faturamento - A partir da versão 11.80.

**Solução**

Para realizar essa tratativa o cliente deve realizar a seguinte configuração:

**Cliente:**

Calcula INSS = **NÃO**

**Natureza:**

Calcula INSS **=**SIM

Porc. INSS = 11% ou alíquota necessária

Ded.INSS (ED\_DEDINSS): = **2 (Não)**

**Produto:**

Calcula INSS = SIM
