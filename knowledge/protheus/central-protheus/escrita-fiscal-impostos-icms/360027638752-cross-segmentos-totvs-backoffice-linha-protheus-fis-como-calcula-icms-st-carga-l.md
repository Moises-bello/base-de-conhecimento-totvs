---
article_id: 360027638752
category: Escrita Fiscal - Impostos - ICMS
content_hash: bd537282b2a9691cbc7576f9d50a39071d3c1723cb96595c974000fdce79a10f
fetched_at: '2026-06-28T22:39:24.150992+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcula ICMS
  ST carga liquida - Ceará?
type: support-article
updated_at: '2021-07-28T03:28:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027638752-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcula-ICMS-ST-carga-liquida-Cear%C3%A1
---

**Dúvida**

Como calcula ICMS ST carga liquida - Ceara?

**Ambiente**

Protheus - Fiscal - A partir da versão 11.80

**Solução**

O cálculo de ICMS ST com aplicação da carga líquida tem como base de cálculo o valor da operação (considerando seguro, despesas acessórias, descontos e IPI , se houver ),

acrescido de uma margem e aplicação de alíquota para chegara o valor do ICMS Retido.

A princípio, este cálculo deverá ser efetuado por alguns contribuintes no estado do Ceará, para

as operações internas ou de entradas neste estado.

Exemplo de cálculo de ICMS ST com carga líquida:

Valor da mercadoria:

R$1.000,00

Valor de despesas acessórias:

R$ 57,00

Valor da operação:

R$ 1.057,00

Margem:

30%

Alíquota ICMS ST:

3,70%

Carga Líquida

Base de cálculo + 30 % = 1.057,00 + 30% = 1374,10

Valor do ICMS ST = 1374,10 \* 3,70 % = 50,84

Para que seja efetuado este cálculo, a configuração será realizada na tabela UFxUF e cadastro de TES, descrito abaixo:

UF Origem (CFC\_UFORIG) Informe a Unidade Federativa de origem da operação.

UF Destino (CFC\_UFDEST) Informe a Unidade Federativa de destino da operação.

Cod.Prod.(CFC\_CODPRD) = Informe o código do produto da operação.

Mar.Liq.ST.(CFC\_MGLQST) = Informe a margem para efetuar o cálculo de ICMS ST com carga

líquida.

Alíq.Liq.ST (CFC\_ALQSTL) = Informe a alíquota para cálculo do ICMS ST com carga líquida

Calc.ST Liq. (F4\_STLIQ) = Informe 1 (Sim) para que o cálculo de ICMS ST com carga líquida seja realizado.

Ao escriturar documento fiscal com um TES com campo F4\_STLIQ = 1 (Sim), a rotina irá aplicar a margem da tabela CFC e a alíquota para efetuar o cálculo.
