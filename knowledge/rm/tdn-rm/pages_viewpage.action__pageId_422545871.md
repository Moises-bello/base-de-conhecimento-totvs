---
content_hash: b6b377e4e830aefa6abb395d71166f8993b62c39951557896a4958e9cd6faf01
fetched_at: '2026-06-29T00:09:21.368472+00:00'
page_id: '422545871'
product: rm
source: tdn-rm
title: DeSTDA - Declaração de Substituição Tributária, Diferencial de Alíquota e Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545871
version: 4
---

É a Declaração de Substituição Tributária, Diferencial de Alíquota e Antecipação – DeSTDA, que se compõe de informações em meio digital dos resultados da apuração do ICMS de que tratam as alíneas:

* "a" (substituição tributária) ,
* "g" (antecipação) e
* "h" (diferencial de alíquotas) do inciso XIII do § 1º do art. 13 da [LC 123/2006](http://www.planalto.gov.br/ccivil_03/Leis/LCP/Lcp123.htm), de interesse das administrações tributárias das unidades federadas.

A declaração também inclui a repartição do Diferencial de Alíquota entre os Estados de origem e destino, quando há venda para não contribuinte do ICMS (pessoa física), criada pela [Emenda Constitucional nº. 87/2015](http://www.planalto.gov.br/ccivil_03/Constituicao/Emendas/Emc/emc87.htm) e, num segundo momento, os valores destinados ao Fundo de Combate à Pobreza também poderão ser declarados na DeSTDA. No TOTVS Gestão Fiscal será disponibilizado um relatório onde constará os lançamentos fiscais que geraram débito/crédito do imposto e sua totalização por Estado da operação, seguindo as regras abaixo.

**ICMS ST**

**Operações Subsequentes** - Serão selecionados todos os lançamentos de saída que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:

* Tipo de Tributação "Tributado";
* Situação da Retenção ICMS ST "Substituto Tributário";
* E o Código do CFOP seja DIFERENTE de: "5.651 à 5.667, 6.551 à 6.667 e 7.651 à 7.667".

**Operações Antecedentes** - Serão selecionados todos os lançamentos de entrada internas que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:

* Tipo de Tributação "Tributado";
* Situação da Retenção ICMS ST "Substituto Tributário";
* E o Código do CFOP seja DIFERENTE de: "1.351 à 1.356, 1.360 à 1.931 à 1.932, 2.351 à 2.356, 2.931 à 2.932, 3.351 à 3.356".

**Operações Concomitantes (Transporte)** - Serão selecionados todos os lançamentos de entrada que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:

* Tipo de Tributação "Tributado";
* Situação da Retenção ICMS ST "Substituto Tributário";
* E o Código do CFOP seja: "1.351 à 1.356, 1.360 à 1.931 à 1.932, 2.351 à 2.356, 2.931 à 2.932, 3.351 à 3.356".

**Operações com Combustíveis**: Serão selecionados todos os lançamentos de saída que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:

* Tipo de Tributação "Tributado";
* Situação da Retenção ICMS ST "Substituto Tributário";
* E o Código do CFOP seja: "5.651 à 5.667, 6.651 à 6.667, 7.651 à 7.667".

**ICMS ENTRADA**

Antecipação: Serão selecionados todos os lançamentos de entrada interestaduais que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:

* Com encerramento da tributação:

1
incomplete
Tipo de Tributação "Outros" com Substituição Tributária;

2
incomplete
Situação da Retenção ICMS ST "Antecipação";

* Sem encerramento da tributação:

3
incomplete
Tipo de Tributação "Tributado";

4
incomplete
Situação da Retenção ICMS ST "Antecipação";

* Diferencial de alíquotas: Serão selecionados todos os lançamentos de entrada interestaduais que possuírem valor de diferencial de alíquota cujo Código do CFOP seja:

5
incomplete
Ativo Fixo: 1.406, 2.406, 1.551, 2.551 e 3.551.

6
incomplete
Uso e Consumo: 1.407, 2.407, 1.556, 2.556 e 3.556

***Observação:*** Os lançamentos de entrada/saída referente operações de devolução que gerem crédito do imposto serão detalhadas com valor negativo para destacar seu efeito na apuração dos tributos.
