---
content_hash: 69ec82b4558ca5894798e6936f961a9dba0e8c5f6251910a1378cada8d3c8b65
fetched_at: '2026-06-29T00:10:46.039556+00:00'
page_id: '553906021'
product: rm
source: tdn-rm
title: Registro 1400
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1400
version: 7
---

**Registro totalizador das saídas internas que trata o art. 119 do RICMS/17**

Este registro deve totalizar as notas fiscais de venda emitidas em operações internas declaradas no registro 1410 do produto que foi identificado no registro 1000.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| J01 | REG | Registro 1400 | Texto fixo contendo 1400 |
| J02 | QTD\_TOT\_SAIDA | Quantidade total de saídas internas  Somatória dos campos K13 [QTD\_SAIDA], menos a somatória dos campos K13d [QTD\_DEVOLVIDA], dos produtos comercializados nas operações de saídas para outros estados | Totaliza os valores gerados no registro 1410 menos o registros totalizados no registro 1420  J02 = ∑ [K13] – ∑ [K13d] |
| J03 | VL\_TOT\_ICMS\_EFETIVO | Valor total do ICMS efetivo nas saídas  Somatória dos campos K15 [VL\_ICMS\_EFETIVO], menos a somatória dos campos K15d [VL\_ICMS\_EFET] | Totaliza os valores gerados no registro 1410 menos o registros totalizados no registro 1420  J03 = ∑ [K15] – ∑ [K15d] |
| J04 | VL\_CONFRONTO\_ICMS\_ENTRADA | Valor de confronto do ICMS das entradas  Obtido pela multiplicação do campo J02 [QTD\_TOT\_SAÍDA] pelo campo D06 [VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR] do registro 1100 | Multiplica a Quantidade de Saídas do registro 1400 com o campo D06 do registro 1100  J04 = J02 \* D06 |
| J05 | APUR\_ICMSST\_RECUPERAR\_RESSARCIR | Apuração do ICMS ST a recuperar ou a ressarcir  Obtido pela diferença positiva do valor do campo J04 [VL\_CONFRONTO\_ICMS\_ENTRADA] pelo campo J03 [VL\_TOT\_ICMS\_EFETIVO] | Se o campo A13 for ”0 (Recuperação)”, será gerado com o valor do campo J04.  Se o campo A13 for “1 (Ressarcimento)” será gerado com:  J05 = J04 – J03 |
