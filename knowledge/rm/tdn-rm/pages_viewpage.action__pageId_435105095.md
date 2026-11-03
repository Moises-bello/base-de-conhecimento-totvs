---
content_hash: 9912e5c7432261173a4c29a56a048a2341b311805445b4fd51f12f5671cafcc8
fetched_at: '2026-06-29T00:09:47.899904+00:00'
page_id: '435105095'
product: rm
source: tdn-rm
title: 'Dados Reajuste - Exemplo - Rateio de Índice: Mês Comercial e Aplicação de
  Índice: Mês Civil'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105095
version: 3
---

**Dados do Contrato de Locação:**

* **Aluguel do mês de competência:** 14/05/2014 a 13/06/2014
* **Vencimento do aluguel:** 14/06/2014
* **Reajuste anual no mês de 06/2014:** 10%
* **Valor do Aluguel:** R$ 1.000,00

**Cálculos do Reajuste:**

* Período: 14/05/2014 a 31/05/2014 (**18 dias**)   Valor do Aluguel \* (Dias Período / Dias do Mês)   R$ 1.000,00 \* (18 / 30) = R$ 600,00
* Período: 01/06/2014 a 13/06/2014 (**13 dias**)   Valor do Aluguel \* Variação CM Anual   R$ 1.000,00 \* 1,10 = R$ 1.100,00
* Valor do Aluguel Corrigido \* (Dias Período / Dias do Mês)   R$ 1.100,00 \* (13 / 30) = **R$ 476,67**
* Valor a ser cobrado na parcela do mês de reajuste:   R$ 600,00 + R$ 476,67 = **R$ 1.076,67**

**Cálculo do "Resíduo" da parcela do mês de reajuste:** Valor Corrigido Pro Rata Dia - Valor cobrado sem reajuste R$ 1.076,67 – R$ 1.000,00 = R$ 76,67    
**Cálculo do Valor da Parcela do mês seguinte:** Parcela Corrigida + Resíduo R$ 1.100,00 + R$ 76,67 = R$ 1.176,67

* O valor da parcela de 14/06/2014: **R$ 1.000,00** (Sem reajuste por causa da ausência da defasagem ou índice no mês de reajuste)
* O valor da parcela de 14/07/2014: **R$ 1.176,67** (Parcela corrigida anualmente + resíduo da parcela do mês anterior)
* O valor da parcela de 14/08/2014: **R$ 1.100,00** (Parcela corrigida anualmente)
* O valor da parcela de 14/09/2014: **R$ 1.100,00** (Parcela corrigida anualmente)
