---
content_hash: 1c28125167f4d0f13dc03a90d9c6c9adc1cce806f4c6f48b697707041665580e
fetched_at: '2026-06-29T00:10:46.002748+00:00'
page_id: '553905993'
product: rm
source: tdn-rm
title: Registro 1200
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1200
version: 6
---

**Registro totalizador das saídas internas para consumidor final**

Este registro deve totalizar as saídas de venda a consumidor final em operações internas declaradas no Registro 1210, deduzidas as devoluções (entradas) que ocorreram no mês da emissão e foram relacionadas no registro 1220.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| F01 | REG | Registro 1200 | Texto fixo contendo 1200 |
| F02 | QTD\_TOT\_SAIDA | Quantidade total de saídas para consumidor final.  Somatória dos campos G13 [QTD\_SAIDA] menos a somatória dos campos G13d [QTD\_DEVOLVIDA] | Totaliza os valores gerados no registro 1210 menos o registros totalizados no registro 1220  F02 = ∑ [G13] - ∑ [G13d] |
| F03 | VL\_TOT\_ICMS\_EFETIVO | Valor total do ICMS efetivo nas saídas para consumidor final.  Somatória dos campos G15 [VL\_ICMS\_EFETIVO] menos a somatória dos campos G15d [VL\_ICMS\_EFETIVO] | Totaliza os valores gerados no registro 1210 menos o registros totalizados no registro 1220  F03 = ∑ [G15] - ∑ [G15d] |
| F04 | VL\_CONFRONTO\_ICMS\_ENTRADA | Valor de confronto do ICMS das entradas.  Obtido pela multiplicação do campo F02 [QTD\_TOT\_SAÍDA] pelo campo D06 [VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR] do registro 1100 | Multiplica a Quantidade de Saídas do registro 1400 com o campo D06 do registro 1100   F04 = F02 \* D06 |
| F05 | RESULT\_RECUPERAR\_RESSARCIR | Resultado do valor a recuperar ou a ressarcir  Obtido pela diferença positiva do valor do campo F04 [VL\_CONFRONTO\_ICMS\_ENTRADA] pelo campo F03 [VL\_TOT\_ICMS\_EFETIVO] **Observação:** Caso o resultado da subtração seja negativo, informar o campo com zero | F05 = F04 - F03  Preencher com zero quando o resultado for negativo. |
| F06 | RESULT\_COMPLEMENTAR | Resultado do valor a complementar  Obtido pela diferença negativa do valor do campo F04 [VL\_CONFRONTO\_ICMS\_ENTRADA] pelo campo F03 [VL\_TOT\_ICMS\_EFETIVO] **Observação:** Caso o resultado da subtração seja positiva, informar o campo com zero | F05 = F04 - F03  Preencher com zero quando o resultado for positivo. |
| F07 | APUR\_ICMSST\_RECUPERAR\_RESSARCIR | Apuração do ICMS ST a recuperar ou a ressarcir  Obtido a partir da equação: RESULT\_RECUPERAR\_RESSARCIR \* ((ALIQ\_ICMS\_ITEM – ALIQ\_FECOP) / ALIQ\_ICMS\_ITEM) | F07 = F05 \* ((B10 - B11) / B10) |
| F08 | APUR\_ICMSST\_COMPLEMENTAR | Apuração do ICMS ST a complementar  Obtido a partir da equação: RESULT\_COMPLEMENTAR \* ((ALIQ\_ICMS\_ITEM – ALIQ\_FECOP) / ALIQ\_ICMS\_ITEM) | F08 = F06 \* ((B10 - B11) / B10) |
| F09 | APUR\_FECOP\_RESSARCIR | Apuração do FECOP a ressarcir  Obtido a partir da equação: RESULT\_RECUPERAR\_RESSARCIR \* (ALIQ\_FECOP) / ALIQ\_ICMS\_ITEM) | F09 = F05 \* (B11 / B10) |
| F10 | APUR\_FECOP\_COMPLEMENTAR | Apuração do FECOP a complementar  Obtido a partir da equação: RESULT\_COMPLEMENTAR \* (ALIQ\_FECOP) / ALIQ\_ICMS\_ITEM) | F10 = F6 \* (B11 / B10) |
