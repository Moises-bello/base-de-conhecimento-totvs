---
content_hash: 375fdc30b560adc8c614716a22f352feeab0bed7bbc54fc9f533f91acc9c39a9
fetched_at: '2026-06-29T00:10:41.957473+00:00'
page_id: '546683921'
product: rm
source: tdn-rm
title: Novo Cálculo de INSS múltiplos vínculos conforme o eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546683921
version: 36
---

# Objetivo:

---

       O objetivo deste documento é orientar como calcular o INSS para que os valores retornados pelo TOTVS Folha de Pagamento sejam os mesmos retornados pelo Governo.

---

01Parâmetro - Calcula INSS conforme eSocial

Para calcular o INSS conforme o eSocial será necessário marcar o parâmetro “Calcula INSS conforme eSocial” e informar a partir de quando o sistema iniciará a calcular desta forma, em Parametrizador | Folha Normal | Geral.

**Atenção:** Marcando esse parâmetro em uma coligada todas deverão estar marcadas.

**Observações:**

* Marcando este parâmetro o sistema sempre irá verificar se existe outras chapas/vínculos do mesmo funcionário para **encontrar a alíquota de** INSS, independente se o outro vinculo for na coligada corrente ou em outra coligada.
* Este parâmetro ficará habilitado quando o parâmetro “Calcula IRRF/INSS de múltiplos vínculos sem chapa centralizadora” estiver marcado. E deve ser marcado em **todas** as coligadas que existirem o vínculo relacionado aos múltiplos vínculos.
* Foram criados novos códigos de cálculo para controle do cálculo dos múltiplos vínculos:

+ [428 - Base Tributada De Inss Folha Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857540)
+ [429 - Base Tributada De Inss Folha Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857547)
+ [430 - Base Tributada De Inss Folha Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857555)
+ [431 - Base Tributada De Inss Folha Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857562)
+ [432 - Base Tributada De Inss 13º Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857570)
+ [433 - Base Tributada De Inss 13º Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857577)
+ [434 - Base Tributada De Inss 13º Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857583)
+ [435 - Base Tributada De Inss 13º Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)

* Os códigos de cálculo abaixo deixam de ser utilizados nesse processo:

+ [387 - Base Tributada de INSS Folha Múltiplos Vínculos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719615)
+ [388 - Base Tributada de INSS 13º Múltiplos Vínculos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718955)

**Observações:**

* Os códigos de cálculos serão criados na base de dados após qualquer cálculo no produto (folha, provisão, etc).
* O usuário deverá criar eventos com esses códigos de cálculo, sendo do tipo base de cálculo e valor.
* O cálculo da tag indMV passa a ser feito apenas a partir da competência 03/2020 onde se institui a nova forma de cálculo de INSS.

  Atenção:

  Ao final do lançamento de todos os vínculos o usuário deve recalcular a base de todos os vínculos novamente. O ideal é que seja processado um vínculo por vez e após o seu cálculo não sejam feitas alterações no vínculo anterior. Caso seja necessário alterações, indicamos que seja cancelada a movimentação dos vínculos seguintes e lançada novamente.
2Exemplo - Folha Normal

Nesse exemplo iremos demonstrar o cálculo de um funcionário que possui dois vínculos na mesma base de dados, um vínculo na coligada 1 e outro vínculo na coligada 6. Além disso será apresentado como fica a geração do indMV nos eventos S-1200 em cada coligada.

Definição do campo indMV:

Tabela de INSS considerada no exemplo:

Chapa 00004 na Coligada 1 possui remuneração de 1.500,00

Chapa 33333333 na Coligada 6 possui remuneração de 5.000,00

Os dois funcionários são de categorias de empregado geral(101)

Primeiro lançamento na coligada 1:

Observe que foram lançados os eventos de CC428 e CC429 pois houve tributação de INSS na primeira e segunda faixa.

Na ficha financeira foi gravado no campo "Ordem Cálculo" o número 1, pois foi o primeiro envelope do funcionário:

Esse campo servirá como indicação da ordem de cálculo na tag indMV nos eventos periódicos.

Obs.: Esse campo é incremental e será gravado a cada envelope do funcionário. No exemplo acima, caso ele possuísse outro período, seria gravado o número 2, e assim por diante.

Quando gerar o XML do S-1200 para esse funcionário, não será levado o grupo de remuneração de outros empregos, nem o indMV. Isso porque é o primeiro funcionário a ser calculado:

Segundo lançamento na Coligada 6:

Observe que no log são considerados os valores na primeira e segunda faixa que foram tributadas no primeiro funcionário.

Na ficha financeira a ordem de cálculo foi gravada como 2:

Ao gerar o XML do evento S-1200 para o funcionário da coligada 6, o campo **indMV irá gerar com o valor 2**:

Conclusão: O primeiro funcionário calculado não levou o **indMV 1** pois o valor a ser calculado de INSS corresponderá a apenas o valor de base de INSS que está indo no próprio funcionário, ou seja, foi o primeiro a ser calculado.

O segundo funcionário foi com o valor de **indMV 2** pois para o cálculo de INSS dele foi considerado a base enviada no primeiro funcionário. Além disso não houve desconto do teto no primeiro funcionário.

6Exemplo - 2ª parcela de 13º salário

**Exemplol:**

Cálculo da 2ª parcela na **coligada 1**

Primeiro calculo :

Evento S432 - Codigo de calculo 432

  Na ficha financeira foi gravado no campo "Ordem Cálculo" o **número 1**, pois foi o primeiro lançamento no envelope do funcionário.

**Exemplo XML**

  Na coligada 1 não será gerado a tag indMV no primeiro calculo conforme manual do eSocial.

Cálculo da 2ª parcela na **coligada 6**

Segundo calculo:

Evento S432 - Codigo de calculo 432

Evento S433 - Codigo de calculo 433

Na ficha financeira foi gravado no campo "Ordem Cálculo" o **número 2** pois foi o segundo lançamento no envelope do funcionário.

**Exemplo XML**

**Exemploll:**

Cálculo da Folha no periodo 1 e Segunda Parcela de 13º no periodo 2

**C****oligada**: **1**

**Ordem**: **1**

 Primeiro lançamento da folha sem indMV

  Lançamento da Folha- Periodo 1

**Coligada 6**

**Ordem 2**

   XML gerado com indMV=2

Voltamos a **coligada1** para fazer o lançamento do 13º salario.

Sendo este lançamento o primeiro de 13 salário não haverá no xml a tag indMV

**Periodo: 2**

**Ordem: 3**

**Coligada 6**:Lançamento do 13º salario

Ordem: 4

  XML gerando o indMV=2

7Exemplos de INDMVExemplos de INDMV

**Exemplo 1:** **Trabalhador com vínculos em 4 empresas – Remuneração total não atinge o teto**

|  |  |  |  |
| --- | --- | --- | --- |
| Empregador | Categoria | Remuneração | Ordem |
| A | 101 | 2.000,00 | 1º |
| B | 101 | 1.500,00 | 2º |
| C | 101 | 1.000,00 | 3º |
| D | 101 | 1.000,00 | 4º |

 

1) Empregador A:

É o primeiro a descontar. Não deve informar o grupo {infoMV}.

A tributação será:

- Remuneração: Categoria 101 - 2.000,00

- 1ª Faixa: 1.045,00 x 7,5% = 78,37 , e

- 2ª Faixa: (2.000,00-1.045,00) = 955,00 x 9% = 85,95.

Contribuição descontada: 164,32 (categoria 101).

 

2) Empregador B:

É o segundo a descontar. Deve informar no registro {remunOutEmpr} apenas o empregador ordenado antes dele, no caso o Empregador A (R$ 2.000,00). Informar indMV=[2].

A tributação será:

- Remuneração: Categoria 101 - 1.500,00

- Remuneração já tributada em outras empresas: 2.000,00 (1ª Faixa e parte da 2ª já tributada na categoria 101)

- 2ª Faixa: (2.089,60 – 2.000,00) = 89,60 x 9% = 8,06, e

- 3ª Faixa: (3.134,40 – 2.089, 60) = 1044,80 x 12% = 125,37, e

- 4ª Faixa: (1.500,00 – 89,60 – 1044,80) = 365,60 x 14% = 51,18.

Contribuição descontada: 184,61 (categoria 101)

 

3) Empregador C:

É o terceiro a descontar. Deve informar no registro {remunOutEmpr} os empregadores ordenados antes dele, no caso o Empregador A (R$ 2.000,00) e o Empregador B (R$ 1.500,00). Informar indMV=[2].

A tributação será:

- Remuneração: Categoria 101 - 1.000,00

- Remuneração já tributada em outras empresas: 3.500,00 (1ª, 2ª, 3ª e parte da 4ª faixa já tributada na categoria 101)

- 4ª Faixa: 1.000,00 x 14% = 140,00

Contribuição descontada: 140,00 (categoria 101)

 

4) Empregador D:

É o quarto a descontar. Deve informar no registro {remunOutEmpr} os empregadores ordenados antes dele, no caso o Empregador A (R$ 2.000,00), o Empregador B (R$ 1.500,00) e o Empregador C (R$ 1.000,00). Informar indMV=[2].

A tributação será:

- Remuneração: Categoria 101 - 1.000,00

- Remuneração já tributada em outras empresas: 4.500,00 (1ª, 2ª, 3ª e parte da 4ª faixa já tributada na categoria 101)

- 4ª Faixa: 1.000,00 x 14% = 140,00

Contribuição descontada: 140,00 (categoria 101)

 

**Exemplo 2: Trabalhador com vínculos em 4 empresas – Remuneração total alcança o teto.**

Situação hipotética:

|  |  |  |  |
| --- | --- | --- | --- |
| Empregador | Categoria | Remuneração | Ordem |
| A | 101 | 2.000,00 | 1º |
| B | 101 | 1.500,00 | 2º |
| C | 101 | 3.500,00 | 3º |
| D | 101 | 1.000,00 | 4º |

 

1) Empregador A:

É o primeiro a descontar. Não deve informar o grupo {infoMV}.

A tributação será:

- Remuneração: Categoria 101 - 2.000,00

- 1ª Faixa: 1.045,00 x 7,5% = 78,37 , e

- 2ª Faixa: (2.000,00-1.045,00) = 955,00 x 9% = 85,95.

Contribuição descontada: 164,32 (categoria 101).

 

2) Empregador B:

É o segundo a descontar. Deve informar no registro {remunOutEmpr} apenas o empregador ordenado antes dele, no caso o Empregador A (R$ 2.000,00). Informar indMV=[2].

A tributação será:

- Remuneração: Categoria 101 - 1.500,00

- Remuneração já tributada em outras empresas: 2.000,00 (1ª Faixa e parte da 2ª já tributada na categoria 101)

- 2ª Faixa: (2.089,60 – 2.000,00) = 89,60 x 9% = 8,06, e

- 3ª Faixa: (3.134,40 – 2.089, 60) = 1044,80 x 12% = 125,37, e

- 4ª Faixa: (1.500,00 – 89,60 – 1044,80) = 365,60 x 14% = 51,18.

Contribuição descontada: 184,61 (categoria 101)

 

3) Empregador C:

É o terceiro a descontar. Deve informar no registro {remunOutEmpr} os empregadores ordenados antes dele, no caso o Empregador A (R$ 2.000,00) e o Empregador B (R$ 1.500,00). Informar indMV=[2].

A tributação será:

- Remuneração: Categoria 101 - 3.500,00

- Remuneração já tributada em outras empresas: 3.500,00 (1ª, 2ª, 3ª e parte da 4ª faixa já tributada na categoria 101).

- 4ª Faixa: (6.101,06 – 3.500,00) = 2.601,06 x 14% = 364,14

Contribuição descontada: 364,14 (categoria 101)

 

4) Empregador D:

É o quarto a descontar. Deve informar no registro {remunOutEmpr} os empregadores ordenados antes dele, no caso o Empregador A (R$ 2.000,00), o Empregador B (R$ 1.500,00) e o Empregador C (R$ 3.500,00) . Informar indMV=[3].

- Remuneração: Categoria 101 – 1.000,00

- Remuneração já tributada em outras empresas: 6.101,06 – Limite Máximo

Não haverá tributação pois já alcançou o teto nas empresas anteriores.

**Exemplo 3:** **Trabalhador Contribuinte Individual com remuneração de 6.000,00 e com vínculo em outra empresa na categoria Empregado.**

Situação hipotética:

|  |  |  |  |
| --- | --- | --- | --- |
| Empregador | Categoria | Remuneração | Ordem |
| A | 101 | 2.000,00 | 1º |
| B | 701 | 6.000,00 | 2º |

 

1) Empregador A:

É o primeiro a descontar. Não deve informar o grupo {infoMV}.

A tributação será:

- Remuneração: Categoria 101 - 2.000,00

- 1ª Faixa: 1.045,00 x 7,5% = 78,37 , e

- 2ª Faixa: (2.000,00-1.045,00) = 955,00 x 9% = 85,95.

Contribuição descontada: 164,32 (categoria 101).

 

2) Empregador B:

Deve informar no registro {remunOutEmpr} o empregador ordenado antes dele, no caso o Empregador A (R$ 2.000,00). Informar indMV=[2].

A tributação será:

Categoria 701

- Remuneração: 6.000,00

- Remuneração já tributada em outras empresas: 2.000,00 na categoria 101. Observar o limite máximo do salário de contribuição para identificar a parcela da remuneração tributável.

- (6.101,06 – 2.000,00) = 4.101, 06 x 11% = 451,11

Contribuição descontada: 451,11 (categoria 701)

**Exemplo 4: Trabalhador com vínculo em duas empresas, atinge o teto na segunda empresa.**

Situação hipotética:

|  |  |  |  |
| --- | --- | --- | --- |
| Empregador | Categoria | Remuneração | Ordem |
| A | 101 | 500,00 | 1º |
| B | 101 | 7.000,00 | 2º |

1) Empregador A:

É o primeiro a descontar. Não deve informar o grupo {infoMV}.

A tributação será:

- Remuneração: Categoria 101 - 500,00

- 1ª Faixa: 500,00 x 7,5% = 37,50

Contribuição descontada: 37,50 (categoria 101).

2) Empregador B:

É o segundo a descontar. Deve informar no registro {remunOutEmpr} apenas o empregador ordenado antes dele, no caso o Empregador A (R$ 500,00). Informar indMV=[2].

A tributação será:

- Remuneração: Categoria 101 - 7.000,00

- Remuneração já tributada em outras empresas: 500,00 (1ª Faixa já tributada na categoria 101)

- 1ª Faixa: (1.045,00 – 500,00) = 545,00 x 7,5% = 40,87, e

- 2ª Faixa: (2.089,60 – 1.045,00) = 1.044,60 x 9% = 94,01, e

- 3ª Faixa: (3.134,40 – 2.089, 60) = 1.044,80 x 12% = 125,37, e

- 4ª Faixa: (6.101,06 - 3.134,40) = 2.966,66 x 14% = 415,33.

Contribuição descontada: 675,58 (categoria 101)

Contribuição total descontada: 713,08

**Exemplo 5: Trabalhador com vínculo em duas empresas, atinge o teto na primeira empresa.**

Situação hipotética:

|  |  |  |  |
| --- | --- | --- | --- |
| Empregador | Categoria | Remuneração | Ordem |
| A | 101 | 7.000,00 | 1º |
| B | 101 | 500,00 | 2º |

1) Empregador A:

É o primeiro a descontar. Não deve informar o grupo {infoMV}.

A tributação será:

- Remuneração: Categoria 101 - 7.000,00

- Remuneração já tributada em outras empresas: 500,00 (1ª Faixa já tributada na categoria 101)

- 1ª Faixa: (1.045,00) = 1.045,00 x 7,5% = 78,37, e

- 2ª Faixa: (2.089,60 – 1.045,00) = 1.044,60 x 9% = 94,01, e

- 3ª Faixa: (3.134,40 – 2.089, 60) = 1.044,80 x 12% = 125,37, e

- 4ª Faixa: (6.101,06 - 3.134,40) = 2.966,66 x 14% = 415,33.

Contribuição descontada: 713,08 (categoria 101)

2) Empregador B:

É o segundo a descontar. Deve informar no registro {remunOutEmpr} apenas o empregador ordenado antes dele, no caso o Empregador A (R$ 7.000,00). Informar indMV=[3].

- Remuneração: Categoria 101 - 500,00

- Remuneração já tributada em outras empresas: 6.101,06 – Limite Máximo

Não haverá tributação pois já alcançou o teto nas empresas anteriores.

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.28.103 |
| 12.1.27.167 |
| 12.1.26.212 |
| 12.1.25.267 |

falsefalse

**Status: Concluido**

false

**Data:**
