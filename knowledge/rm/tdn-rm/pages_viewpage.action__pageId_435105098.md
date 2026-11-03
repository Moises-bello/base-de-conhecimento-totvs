---
content_hash: c83a2612139da029887507207e55ab7eabc3eded9a379400a58085f59fb282e5
fetched_at: '2026-06-29T00:09:47.910610+00:00'
page_id: '435105098'
product: rm
source: tdn-rm
title: 'Dados Reajuste - Exemplo - Rateio de Índice: Mês Comercial e Aplicação de
  Índice: Mês Comercial'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105098
version: 3
---

**Dados do Contrato de locação**

* **Aluguel do mês de competência:** 14/05/2014 a 13/06/2014
* **Vencimento do aluguel:** 14/06/2014
* **Reajuste anual no mês de 06/2014:** 10%
* **Valor do Aluguel:** R$ 1.000,00

**Cálculos do Reajuste:**

* Período: 14/05/2014 a 31/05/2014 (**18 dias**)   Valor do Aluguel \* (Dias Período / Dias do Mês)   R$ 1.000,00 \* (18 / 30) = R$ 600,00
* Período: 01/06/2014 a 13/06/2014 (**12 dias**)   Valor do Aluguel \* Variação CM Anual   R$ 1.000,00 \* 1,10 = R$ 1.100,00
* Aplicação de Dias = 30 – 18 = 12 dias
* Valor do Aluguel Corrigido \* (Dias Período / Dias do Mês)   R$ 1.100,00 \* (12 / 30) = **R$ 440,00**
* Valor a ser cobrado na parcela do mês de reajuste:   R$ 600,00 + R$ 440,00 = **R$ 1.040,00**

**Cálculo do "Resíduo" da parcela do mês de reajuste:** Valor Corrigido Pro Rata Dia - Valor cobrado sem reajuste R$ 1.040,00 – R$ 1.000,00 = R$ 40,00  
**Cálculo do Valor da Parcela do mês seguinte:** Parcela Corrigida + Resíduo R$ 1.100,00 + R$ 40,00 = R$ 1.140,00

* O valor da parcela de 14/06/2014: **R$ 1.000,00** (Sem reajuste por causa da ausência da defasagem ou índice no mês de reajuste)
* O valor da parcela de 14/07/2014: **R$ 1.140,00** (Parcela corrigida anualmente + resíduo da parcela do mês anterior)
* O valor da parcela de 14/08/2014: **R$ 1.100,00** (Parcela corrigida anualmente)
* O valor da parcela de 14/09/2014: **R$ 1.100,00** (Parcela corrigida anualmente)
