---
article_id: 4408065335831
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 292cc5976deed1381f0f01b423134d7f58f704807562f15e320b40bc5f6fa8ec
fetched_at: '2026-06-28T22:39:20.565850+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- PAUTA-ST X MVA
type: support-article
updated_at: '2024-03-21T18:13:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408065335831-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-PAUTA-ST-X-MVA
---

O regime de substituição tributária está previsto na Constituição Federal de 1988, artigo 150, § 7º, o qual estabelece que a lei poderá atribuir a sujeito passivo de obrigação tributária a condição de responsável pelo pagamento de imposto ou contribuição, cujo fato gerador deva ocorrer posteriormente, assegurada a imediata e preferencial restituição da quantia paga, caso não se realize o fato gerador presumido.

As normas estaduais presentam regras distintas sobre a composição do valor a ser pago pelo sujeito passivo responsável pelo recolhimento do imposto, por exemplo:

* Pela Pauta: onde a Base de ICMS ST é o valor divulgado em Ato Cotepe ou Portaria, multiplicado pela quantidade; ou
* Pelo MVA: onde a Base do ICMS ST é o Preço praticado pelo remetente + % MVA divulgado em Ato Cotepe.

As configurações abaixo auxiliarão os usuários do sistema Microsiga-Protheus nas mais diversas possibilidades de configuração do sistema, para tratamento do referido cálculo.

# Procedimentos para Configuração

**Parâmetros:**

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_ICMPAUT |
| **Tipo** | Lógico |
| **Descrição** | Informar se o ICMS de Pauta ( Solidário ) devera  ser calculado com base no valor da pauta, mesmo que o preço de venda seja maior. |
| **Valor Padrão** | .T. |

 

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_MKPICPT |
| **Tipo** | Logico |
| **Descrição** | Indica se as operações de venda para consumidor final terão, ou não, Margem de Lucro. |
| **Valor Padrão** | 1 |
| **Detalhes** | Indica se o cálculo do ICMS de pauta considera ou não a margem de lucro conforme a configuração do campo Marg. Solid. - F4\_MKPSOL do cadastro de TES, configurável com:  1 - Nunca (nunca aplica a margem de lucro informada do ICMS retido a base de cálculo);  2 - Configura (aplica conforme a configuração do Sistema padrão );  3 - Sempre (aplica a margem de lucro informada do ICMS retido a base de cálculo).  Para o parâmetro, informe:  1 - Não considera a margem de lucro no cálculo.  2 - Considera a margem de lucro conforme a configuração do campo Marg. Solid. |

 

|  |  |
| --- | --- |
| **Nome da variável** | MV\_REDPT |
| **Tipo** | Lógico |
| **Descrição** | Indica se a redução ST será aplicada sobre a base composta por pauta. |
| **Valor Padrão** | .T. |
| **Detalhes** | Indica se a redução do ICMS ST deve ser aplicada sobre base de cálculo do ICMS ST composta por pauta. **.T.**  indica que a base de cálculo do ICMS ST composta por valor de pauta deve sofrer redução de ICMS ST.  **.F.**   indica que a base de cálculo do ICMS ST composta por valor de pauta não deve sofrer a redução de ICMS ST. |

 

Parametro = MV\_ICMPFAT

Tipo = caracter

Descrição = Informe o campo que deverá ser multiplicado pela quantidade para o calculo do ICM-ST de pauta Ex. B1\_PESO 

Valor Padrão = em branco

Quando Preenchido o sistema aplicará o calculo

***Quantidade comercializada \* Valor do ICMS-ST de Pauta \* Parametro MV\_ICMPFAT***

Observação: Quando o parametro MV\_ICMPFAT não for definido, será assumido o calculo padrão do sistema definido pelo  B1\_VLR\_ICM ) ou a Exceção Fiscal

# Procedimentos de Utilização

Para indicar se cálculo do ICMS de pauta considera ou não a margem de lucro conforme a configuração do campo Marg. Solid. - F4\_MKPSOL do cadastro de TES deve ser configurado parâmetro **MV\_MKPICPT**com a opção **2 -****Configura (aplica conforme a configuração do Sistema padrão)**

Para que sistema utilize valor da mercadoria aplicado MVA quando este for maior que valor da pauta, é necessário configurar parâmetro **MV\_ICMPAUT**como**.F.**

**Exemplos de cálculo com Pauta ou MVA.**

MV\_ESTADO =  MS

Cliente do estado = MS

**Cadastro de TES (MATA080)**

Calcula ICMS = SIM

Livro Fiscal de ICMS = Tributado

Aplica Margem = Não

 Aliq Crd ST = 8,50

**Cadastro de UFXUF (FISA080)**

UF origem = MS

UF Destino = MS

ICMS P. Pauta = 11,77

ICMS Pauta = 11,77

**Cadastro de exceção fiscal (MATA540)**

Estado = MS

Cliente = todos

Margem de lucro = 36,00

% Red do ICMS = 23,53

Pauta Prod = Sim

% Red ICMS ST = 23,53

**1º cenário - o valor unitário menor que o preço de Pauta**

Pauta – R$ 11,77

Valor unitário R$ 10,00

Quantidade 324,80

Como o valor unitário é menor que o preço de pauta o sistema deverá considerar a pauta para calcular o ICMS e o ST

Base do ICMS R$ 899, 53

Alíquota 17%

Valor do ICMS 152,92

Base do ICMS ST R$ 899,53 + 36 % = R$ 1.223,36

Alíquota 17%

899, 53 x 8,50 % = 76,46

Valor do ICMS ST R$ 207,97 – 76,46 = 131,51

**2º cenário - o valor unitário igual ao preço de Pauta**

Pauta – R$ 11,77

Valor unitário R$ 11,77

Quantidade 324,80

Como o valor unitário é igual ao preço de pauta o sistema deverá considerar a pauta para calcular o ICMS e o ST

Base do ICMS R$ 899, 53

Alíquota 17%

Valor do ICMS 152,92

Base do ICMS ST R$ 899,53 + 36 % = R$ 1.223,36

Alíquota 17%

899, 53 x 8,50 % = 76,46

Valor do ICMS ST R$ 207,97 – 76,46 = 131,51

**3º cenário - o valor unitário é MAIOR que o preço de Pauta**

Pauta – R$ 11,77

Valor unitário R$ 18,50014

Quantidade 324,80

Como o valor unitário é MAIOR que o preço de pauta o sistema deverá considerar o valor unitário para calcular o ICMS e o ST

Base do ICMS R$ 1.413,88

Alíquota 17%

Valor do ICMS 240,36

Base do ICMS ST R$ 1.413,88 + 36 % = R$ 1. 922,87

Alíquota 17%

1.413,88 x 8,50 = 120,18

Valor do ICMS ST R$ 326,89 – 120,18 = 206,68

**4º cenário - o valor unitário é MAIOR que o preço de Pauta e utilizado parâmetro MV\_ICMPAUT = .T. para sempre aplicar valor da pauta.**

Pauta – R$ 11,77

Valor unitário R$ 18,50014

Quantidade 324,80

Base do ICMS R$ 1.413,88

Alíquota 17%

Valor do ICMS 240,36

Base do ICMS ST R$ 899,53 + 36 % = R$ 1.223,36

Alíquota 17%

1.413,88 x 8,50 % = 120,18

Valor do ICMS ST R$ 207,97 – 120,18 = 87,79

**5º cenário - o valor unitário é MAIOR que o preço de Pauta e utilizado parâmetro MV\_ICMPAUT = .T. para sistema utilize valor da mercadoria aplicado MVA quando este for maior que valor da pauta e parâmetro MV\_MKPICPT diferente de 2 - Configura (aplica conforme a configuração do Sistema padrão )**

Importante

**Neste cenário é necessário utilizar TES com campo**

**APLICA MARGEM (F4\_APLIIVA)**

* **Se = SIM (PADRÃO)** - Aplica margem de lucro quando o preço de venda for maior ou igual ao valor da Pauta.

Pauta – R$ 11,77

Valor unitário R$ 18,50014

Quantidade 324,80

Como o valor unitário é MAIOR que o preço de pauta o sistema deverá considerar o valor unitário para calcular o ICMS e o ST

Base do ICMS R$ 1.413,88

Alíquota 17%

Valor do ICMS 240,36

Base do ICMS ST R$ 1.413,88 + 36 % = R$ 1. 922,87

Alíquota 17%

1.413,88 x 8,50 = 120,18

Valor do ICMS ST R$ 326,89 – 120,18 = 206,68
