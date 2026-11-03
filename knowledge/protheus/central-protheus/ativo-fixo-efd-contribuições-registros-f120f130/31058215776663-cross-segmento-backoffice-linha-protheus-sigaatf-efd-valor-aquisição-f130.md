---
article_id: 31058215776663
category: Ativo Fixo - EFD Contribuições - Registros F120/F130
content_hash: 3835fb27735b4329698b2ee907bed39c3abdea7d9bc0cddbd88d4495ed7c3f93
fetched_at: '2026-06-28T22:41:36.212310+00:00'
product: protheus
section_id: 31045161075991
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - EFD - Valor Aquisição
  - F130
type: support-article
updated_at: '2025-03-31T20:25:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31058215776663-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-EFD-Valor-Aquisi%C3%A7%C3%A3o-F130
---

**Dúvida:**

É possível utilizar como base um valor de aquisição diferente do valor contido no cadastro do bem?

**Ambiente:**

Microsiga Protheus - Ativo Fixo - Todas as versões

**Solução:**

O ativo possuem dois campos de controle de valores:

* Val Orig M1 (N3\_VORIG1),
* N1\_VLAQUIS,

Para cenários em que os campos possuem valores diferentes, a apuração prioriza o campo VL. AQUISIÇÃO (N1\_VLAQUIS) para a CL2. 

Para as apurações através dos valores contidos na nota de entrada de aquisição (registro F130) foi criado o parâmetro MV\_AFVL130 que possibilita a determinação do campo ou condição, onde o sistema registrará o valor de aquisição do item. 

Esta ação foi aplicada, pois foi notado a necessidade de ajuste para regras de negócios que indicam o valor de custo (líquido) no momento do cadastro no Ativo FIxo. 

***Para o uso através de condições, utilizamos o parâmetro MV\_BSCREPC, que possui os conteúdos 1 e 2:***

* *MV\_BSCREPC = 1: O sistema utiliza preferencialmente o valor da Moeda 1 do ativo (N3\_VORIG) no momento da apuração.*
* *MV\_BSCREPC = 2: O sistema considera os valores do documento de entrada, utilizando os dados da tabela SD1.*

***`Para personalizar o valor do bem indicado no F130 ao utilizar o parâmetro MV\_BSCREPC:***

1. *Cenário MV\_BSCREPC = 1:*
   * *É possível usar o parâmetro MV\_VLRATF para personalizar o valor que será preenchido no VAL ORIG M1 (N3\_VORIG1), deduzindo impostos determinados pela empresa. O valor do campo  original da moeda 01 será apurado no F130.*
2. *Cenário MV\_BSCREPC = 2:*
   * *Utilizando o parâmetro MV\_AFVL130, você pode definir uma fórmula personalizada para o cálculo do valor a ser preenchido no CL2\_VLAQUI, que será usado como base de apuração.**Exemplo de fórmula:****SD1->D1\_TOTAL - SD1->D1\_VALDESC + SD1->D1\_DESPESA***

***Saiba Mais:***

[TDN - MV\_AFVL130](https://tdn.totvs.com/pages/releaseview.action?pageId=840774850)

[TDN - MV\_VLRATF](https://tdn.totvs.com/pages/releaseview.action?pageId=916396227)
