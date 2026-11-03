---
content_hash: 9bbe3f8502f3b1236449454e0535635fe2335e8a0d17ebf20336476412d9a7c2
fetched_at: '2026-06-29T00:09:49.115525+00:00'
page_id: '435105237'
product: rm
source: tdn-rm
title: Medidor - Modelos de cálculo de rateio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105237
version: 4
---

Existem vários modelos de cálculo para o rateio das despesas de consumo. Cada modelo permite uma forma diferente de cálculo para o rateio. São eles:

* **Valor Fixo:** O valor é atribuído diretamente à uma única subunidade.
* **Rateio por CRD:** Valor total da despesa \* CRD (Coeficiente de Rateio de Despesa).
* **Rateio por Fração Ideal:** Valor Total da Despesa \* (Fração Ideal / 1000).
* **Rateio por M² Construído:** (Valor Total da Despesa / M² Construído) \* M² Locado Cliente.
  + **Exemplo:**
    - Valor total Luz: R$600,00.
    - Valor Total m² construído: 320m
    - Galpão: 1
    - Armazém: 101
    - Cliente: Empresa 01
    - T.m² Locado: 60,00
    - Rateio por M² Construído: (R$600,00 / 320) \* 60,00 = R$ 112,50

* **Rateio por M² Locado**:  (Valor Total da Despesa / M² Locado) \* M² Locado Cliente.
  + **Exemplo**:
    - Valor total água: R$230,00.
    - Valor total m² locado = 240m
    - Galpão: 1
    - Armazém: 101
    - Cliente: Empresa 01
    - T.m² Locado: 60,00
    - Rateio por M² Locado: (R$230,00 / 240) \* 60,00 = R$57,50

* **Rateio Linear por Total de Subunidade do Empreendimento**: (Valor Total da Despesa/ Quantidade Total Subunidades do Empreendimento).
* **Rateio Linear por Total de Subunidade da Unidade**: (Valor Total da Despesa/ Quantidade Total Subunidades da unidade).
* **Rateio Linear por Total de Unidades**: (Valor Total da Despesa/ Quantidade Total de Unidade).
