---
content_hash: 8347f27be9f35ca4d410475dfdf937a72cfe64b2c487a36a2e6a295a720a6786
fetched_at: '2026-06-29T00:10:46.058440+00:00'
page_id: '553906081'
product: rm
source: tdn-rm
title: Registro 1500
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1500
version: 7
---

**Registro totalizador das saídas internas destinadas a contribuinte do Simples Nacional**

Este registro deve totalizar as notas fiscais de saída interna destinadas a contribuinte do Simples Nacional declaradas no Registro 1510, deduzidas as devoluções (entradas) que ocorreram no mês da emissão e foram relacionadas no registro 1520.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| L01 | REG | Registro 1500 | Texto fixo contendo 1500 |
| L02 | QTD\_TOT\_SAIDA | Quantidade total de saídas destinadas a contribuintes do Simples Nacional  Somatória dos campos M13 [QTD\_SAÍDA], menos a somatória dos campos M13d [QTD\_DEVOLVIDA], dos produtos comercializados nas operações de saídas para contribuinte do simples nacional | Totaliza os valores gerados no registro 1510  L02 = ∑ [M13] – ∑ [M13d] |
| L03 | VL\_ICMSST\_UNIT\_E NTR | É o valor do ICMS ST a recuperar por unidade | Totaliza os valores gerados no registro 1510  Valor obtido a partir do seguinte cálculo: (D04 / (1+MVA) ) x (Coeficiente da MVA X Percentual de Redução) x (B10)  Onde:   * D04 é o campo VL\_BC\_ICMSST\_UNIT\_MED * MVA é a MVA utilizada para retenção do ICMS ST * Percentual de redução a ser aplicado sobre a MVA (70% se alíquota de 18%, 50% se alíquota de 12% * B10 é campo ALIQ\_INTERNA     O MVA é recuperado do campo FATORSUBST, do anexo de Dados Fiscais do Produto para o estado da Filial. |
| L04 | APUR\_ICMSST\_REC UPERAR\_RESSARCIR | Apuração do ICMS ST a recuperar ou a ressarcir  Valor obtido pela multiplicação do campo L02 [TOT\_QTD\_SAÍDA] pelo campo L03 [VL\_ICMSST\_UNIT\_ENTR] | Totaliza os valores gerados no registro 1510  L04 = L02 \* L03 |
| L05 | MVA\_ICMSST | MVA da operação | MVA utilizada no calculo do campo L03.  Campo FATORSUBST, do anexo de Dados Fiscais do Produto para o estado da Filial. |
