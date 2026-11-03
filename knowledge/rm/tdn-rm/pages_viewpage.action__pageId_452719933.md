---
content_hash: d374881c5f6ddb28d79eb77c97af9f9593cb7898d753cb3b4c3632ba3d1e69e5
fetched_at: '2026-06-29T00:10:11.076885+00:00'
page_id: '452719933'
product: rm
source: tdn-rm
title: Código de Cálculo 12 - Contribuição Sindical
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719933
version: 2
---

Desconto do tipo dia com porcentagem de incidência igual a 1,00 (um). O sistema somará ao valor fixo os proventos do mês que "Incide contribuição sindical" e encontrará o valor de INC. CONTRIBUIÇÃO SINDICAL.

Os cálculos serão os seguintes:

*Para quinzenalistas e mensalistas:*

INC. CONTRIBUIÇÃO SINDICAL/ 30

O sistema buscará o salário-mês no cadastro do funcionário, somará os eventos que incidem salário e dividirá por 30 (número de dias no mês).

*Para horistas, diaristas ou semanalistas:*

(INC. CONTRIBUIÇÃO SINDICAL/ # HORAS MES) \* PORC. INCIDENCIA

O sistema buscará o salário, dividirá pela jornada do cadastro do funcionário e multiplicará pela porcentagem de incidência.

*Para funcionários Comissionistas Misto:*

Maior Valor (Mínimo Garantido / 30, (Salário Fixo + Comissão Anterior) / 30)

O sistema calculará o maior valor entre o (mínimo Garantido informado no cadastro do Sindicato na pasta Identificação dividido por 30) ou (salário do funcionário + Comissão do mês anterior / 30).

*Para funcionários Comissionistas Puro:*

Maior Valor (Mínimo Garantido / 30, Comissão Mês Anterior / 30)

O sistema calculará o maior valor entre o (mínimo Garantido informado no cadastro do Sindicato na pasta Identificação dividido por 30) ou (Comissão do mês anterior / 30).

O sistema realizará o lançamento também do código de cálculo 375 - Salário Contratual Contribuição Sindical, exceto em caso de cálculo de diferença de contribuição sindical.

**Observação**

Será lançado automaticamente este evento de código de cálculo 12 - Contribuição Sindical para os funcionários que estiverem com o campo Contribuição Sindical no Cadastro de Funcionários em Dados do Sindicato, preenchido com "N" - NÃO DESCONTOU. Para que seja lançado existe a condição do lançamento do código de cálculo 5 – salário família, ou seja, no momento que for feito o lançamento da folha com o salário família será verificado a necessidade de desconto de contribuição sindical. Esta condição se faz necessária para que nos funcionários semanalistas ou quinzenalistas sejam identificados o período de fechamento mensal.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
