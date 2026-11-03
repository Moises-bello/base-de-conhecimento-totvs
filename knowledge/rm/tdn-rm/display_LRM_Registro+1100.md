---
content_hash: b267ae5a3766a0ce83497f6e0b0cbb3136034b19511ec9b6bb709197d58fb5a0
fetched_at: '2026-06-29T00:10:45.980486+00:00'
page_id: '553905978'
product: rm
source: tdn-rm
title: Registro 1100
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1100
version: 6
---

**Registro totalizador das entradas**

Este registro totaliza as notas fiscais de entrada do período declaradas no registro 1110, deduzidas das devoluções ocorridas no próprio mês da aquisição.

O registro considera somente os cálculos referente ao período das Entradas e Devoluções ocorridas no mesmo período da geração do arquivo.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| D01 | REG | Registro 1100 | Texto fixo contendo 1100 |
| D02 | QTD\_TOT\_ENTRADA | Quantidade total do item adquirido no período.  Somatória dos campos E14 [QTD\_ENTRADA], menos a somatória dos campos E13d [QTD\_DEVOLVIDA] | D02 = ∑ [E14] - ∑ [E13d] |
| D03 | MENOR\_VL\_UNIT\_ITEM | Menor valor unitário do item adquirido no período | Gerar com o **menor valor unitário** declarado no Campo E15 do Registro 1110 dentro do período para o item em referência. |
| D04 | VL\_BC\_ICMSST\_UNIT\_MED | Valor unitário médio da base de cálculo do ICMS ST.  Resultado da somatória dos campos E16 [VL\_BC\_ICMS\_ST], menos a somatória dos campos E15d [VL\_BC\_ICMS\_ST], dividido pelo campo D02 [QTD\_TOT\_ENTRADA] | D04 = ( ∑ E16 - ∑ E15d ) / D02 |
| D05 | VL\_TOT\_ICMS\_SUPORT\_ENTR | Valor total do ICMS do item suportado na entrada.  Somatória dos campos E17 [VL\_ICMS\_SUPORT\_ENTR], menos a somatória dos campos E16d [VL\_ICMS\_SUPORT\_ENTR] | D05 = ∑ E17 - ∑ [E16d] |
| D06 | VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR | Valor unitário médio do ICMS suportado na entrada.  É o resultado da divisão do campo D05 [VL\_TOT\_ICMS\_SUPORT\_ENTR] pelo campo D02 [QTD\_TOT\_ENTRADA] | D06 = D05 / D02 |
