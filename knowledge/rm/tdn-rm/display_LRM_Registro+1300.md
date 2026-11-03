---
content_hash: d9222562ce6b92a7ad0eeee953de1eff79fed78b6655a3d7f1b8a6e0a17ba57a
fetched_at: '2026-06-29T00:10:46.022424+00:00'
page_id: '553906009'
product: rm
source: tdn-rm
title: Registro 1300
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1300
version: 8
---

**Registro totalizador das saídas para outros estados**

Este registro deve totalizar as saídas emitidas para outros estados declaradas no Registro 1310, deduzidas as devoluções (entradas) que ocorreram no mês da emissão e foram relacionadas no registro 1320.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| H01 | REG | Registro 1300 | Texto fixo contendo 1300 |
| H02 | QTD\_TOT\_SAIDA | Quantidade total de saídas para outros estados  Somatória da quantidade, campo I13 [QTD\_SAIDA], menos a somatória dos campos I13d [QTD\_DEVOLVIDA], dos produtos comercializados nas operações de saídas para outros estados | Totaliza os valores gerados no registro 1310 menos o registros totalizados no registro 1320  H02 = ∑ [I13] - ∑ [I13d] |
| H03 | VL\_TOT\_ICMS\_EFETIVO | Valor total do ICMS efetivo nas saídas para outros estados  É a somatória dos campos I15 [VL\_ICMS\_EFETIVO], menos a somatória dos campos I15d [VL\_ICMS\_EFET] | Totaliza os valores gerados no registro 1310 menos o registros totalizados no registro 1320  H03 = ∑ [I15] - ∑ [I15d] |
| H04 | VL\_CONFRONTO\_ICMS\_ENTRADA | Valor de confronto do ICMS das entradas  É o resultado da multiplicação do campo H02 [QTD\_TOT\_SAÍDA] pelo campo D06 [VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR] do registro 1100 | Multiplica a Quantidade de Saídas do registro 1300 com o campo D06 do registro 1100  H04 = H02 \* D06 |
| H05 | RESULT\_RECUPERAR\_RESSARCIR | Resultado do valor a recuperar ou a ressarcir  Obtido pela diferença positiva do valor do campo H04 [VL\_CONFRONTO\_ICMS\_ENTRADA] pelo campo H03 [VL\_TOT\_ICMS\_EFETIVO] | Se o campo A12 for ”0 (Recuperação)”, será gerado com o valor do campo H04.  Se o campo A12 for “1 (Ressarcimento)” será gerado com:  H05 = H04 – H03  Preencher com zero quando o resultado for negativo. |
| H06 | APUR\_ICMSST\_RECUPERAR\_RESSARCIR | Apuração do ICMS ST a recuperar ou a ressarcir  É o resultado da subtração do campo H05 [RESULT\_RECUPERAR\_RESSARCIR] pelo campo H07 [APUR\_FECOP\_RESSARCIR] Equação: H06 = H05 - H07 | H06 = H05 - H07 |
| H07 | APUR\_FECOP\_RESSARCIR | Apuração do FECOP a ressarcir  É o resultado da multiplicação dos campos D04 [VL\_BC\_ICMSST\_UNIT\_MED], B11 [ALIQ\_FECOP] e H02 [QTD\_TOT\_SAIDA] Equação: H07 = (D04 \* B11) \* H02 | H07 = (D04 \* B11) \* H02 |
