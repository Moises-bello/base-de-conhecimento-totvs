---
article_id: 9074546844311
category: SIGAEST - CÁLCULOS
content_hash: 645f11129f0ec8624789d311e342af7f50afbeca41fb94f9a799f7dbcfd4d703
fetched_at: '2026-06-28T22:39:04.129379+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA290 - Conceitos
  e utilização do Cálculo do Lote Econômico
type: support-article
updated_at: '2026-02-20T20:53:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9074546844311-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA290-Conceitos-e-utiliza%C3%A7%C3%A3o-do-C%C3%A1lculo-do-Lote-Econ%C3%B4mico
---

O lote econômico determina a quantidade ideal de compra ou produção, equilibrando custos e evitando excessos de estoque. Seu cálculo considera consumo médio, periodicidade de aquisição e classificação ABC, podendo ser ajustado conforme a disponibilidade financeira. O Protheus realiza também cálculos de ponto de pedido, estoque de segurança e consumo médio, otimizando a gestão de estoques.

**Dúvida**  
Qual a funcionalidade do lote econômico e os conceitos para configuração de seus parâmetros?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Passos**

## **01.****VISÃO GERAL**

A decisão de estocar ou não determinado item é básica para o volume de estoque em qualquer momento.

Porém, atualmente há um consenso em torno de estoque: manter o estoque alto é prejudicial à empresa, tanto financeiramente quanto logisticamente ("onde guardar tanto material?").

Deve-se manter um estoque no nível em que não comprometa, por exemplo, a entrega de um pedido a um cliente. Esse é o tipo de prejuízo que não pode ser mensurado, mas que sem dúvida alguma é extremamente prejudicial.

A principal vantagem de se manter um estoque em patamares baixos é financeira. Estoques baixos demandam menor capital de giro. Não é preciso recorrer a financiamentos externos, e com isso não se paga juros. E se houver capital próprio, o mesmo é liberado para ser aplicado, oferecendo um rendimento para a empresa.

Quando o nível de estoques é reduzido, temos vantagens como:

* Menor quantidade de espaço físico para armazenamento;
* Menor risco de obsolescência e deterioração;
* Menor custo de seguro;
* Menor risco de desperdício.

O conflito entre as vantagens e desvantagens na quantidade a encomendar a cada nova compra e/ou produção é resolvido através do cálculo do Lote Econômico.

O Protheus disponibiliza esta rotina para o recalcular o consumo mensal por pesos ou pela tendência, calcular o lote econômico, ponto de pedido e classificação ABC.

Por meio dessa rotina podemos obter:

* O cálculo do lote econômico pela disponibilidade financeira
* A Classificação ABC dos materiais
* O consumo médio de produtos, por peso ou por tendência
* O cálculo do ponto de pedido

## **02.** **CÁLCULO DE LOTE ECONÔMICO**

O lote econômico informa a quantidade ideal para se produzir ou comprar toda vez que se fizer necessário, sendo calculado em função do consumo médio mensal e da periodicidade de compra ou produção dos produtos classificados pela curva ABC.

O período de aquisição deve ser definido em meses para cada classe de material (ABC). Desta forma, pode-se representar o cálculo do lote econômico pela fórmula:

LE = CM x PA

em que:

CM = Consumo Médio

PA = Periodicidade de Aquisição

**Exemplo:**

* Para os Produtos de Curva A, comprar a cada 30 Dias ( 1 mês )
* Para os Produtos de Curva B, comprar a cada 60 Dias ( 2 meses )
* Para os Produtos de Curva C, comprar a cada 90 Dias ( 3 meses )

O que significa que a quantidade a ser comprada para os produtos do grupo C, deve garantir que o produto fique armazenado 3 meses no estoque.

Assim, um Produto A com consumo médio de 200 peças, estando classificado na Curva B do estoque, terá Quantidade do Lote Econômico em 400 peças.

## **a.** **Ajuste pela Disponibilidade Financeira**

O cálculo do lote econômico pode ser ajustado pela disponibilidade financeira da empresa. Neste caso, o sistema multiplica o lote pelo último preço de compra e compara com o valor que pode ser gasto.

Caso o montante disponível seja menor, verifica-se a diferença e esta é subtraída em porcentual de todos os lotes. Observe o quadro de exemplo a seguir.

|  |  |  |  |
| --- | --- | --- | --- |
| **Produto** | **LE** | **Último Preço** | **Total (LE\*Últ. Preço)** |
| Produto A | 50 | 26,00 | 1300,00 |
| Produto B | 40 | 20,00 | 800,00 |
| Produto C | 60 | 10,00 | 600,00 |
| Produto D | 70 | 8,00 | 560,00 |
| Produto E | 180 | 2,00 | 360,00 |
| Produto F | 165 | 2,00 | 330,00 |
| Total dos Lotes | | | 3950,00 |
| Disponibilidade Financeira | | | 3160,00 |
| Diferença | | | 790,00 ou 20% |

**LE Ajustado = LE - 20%**

|  |  |  |
| --- | --- | --- |
| **Material** | **LE** | **LE Ajustado (20%)** |
| Produto A | 50 | 40,00 |
| Produto B | 40 | 32,00 |
| Produto C | 60 | 48,00 |
| Produto D | 70 | 56,00 |
| Produto E | 180 | 144,00 |
| Produto F | 165 | 132,00 |

Dica:

Na explosão das necessidades, os valores obtidos para o Lote Econômico serão ajustados para o múltiplo da quantidade por embalagem, no case de compra, e para o múltiplo de lote mínimo, no caso de produção.

## **03.** **CLASSIFICAÇÃO ABC**

O objetivo da classificação de produtos através da curva ABC é de permitir à Administração de Estoques saber quais produtos tiveram maior movimento médio em determinado período e quais foram os produtos de maior custo, facilitando a identificação dos produtos que devem receber maior atenção no gerenciamento dos estoques. O método leva este nome devido a classificação que é dada aos produtos.

Os produtos da Classe A são aqueles itens mais importantes que devem ser tratados com especial atenção. São os produtos cuja média de consumo multiplicada pelo custo (Standard ou último preço) é alta em relação aos demais, portanto são aqueles produtos que têm maior custo de estocagem e alta rotatividade, devendo ser adquiridos com maior frequência.

Por sua vez, os produtos da Classe B são aqueles que se encontram em uma situação intermediária entre as classes A e C.

Os produtos da Classe C são aqueles cujo consumo médio multiplicado pelo custo não é tão elevado, portanto, estes produtos têm custo de estocagem menor e menor rotatividade, podendo ser adquiridos com menor frequência e em maiores quantidades.

Para a classificação dos produtos, deve ser definido um percentual a cada classe (no total de 100%), de modo a obter um valor limite para que os produtos se enquadrem nas respectivas classificações. Assim, ordena-se os produtos pelo resultado do consumo médio multiplicado pelo custo e classifica-se os produtos em ordem descendente, enquanto o somatório deste resultado for menor que o percentual informado para cada classe.

**Síntese:**

A Classificação ABC, calculada no Lote Econômico, é feita da seguinte maneira:

O sistema calcula o valor do consumo médio total da Empresa, e sobre este total aplica os percentuais das classes A, B e C, encontrando assim os valores que serão utilizados para comparação com o consumo médio de cada produto. Receberá classe "A" o produto que representar maior valor de giro no estoque, e classe "C" o que representar menor valor de giro no estoque.

Dica:

O campo Custo Standard no Cadastro de Produtos (B1\_CUSTD) deve conter um preço standard do produto, que será utilizado no cálculo.

**Exemplo:**

Considere os seguintes produtos já ordenados pelo total resultante do custo standard multiplicado pelo consumo médio (campo total):

|  |  |  |  |
| --- | --- | --- | --- |
| **Produto** | **Custo** | **Consumo Médio** | **Total** |
| MP0001 | 8,24 | 354 | 2.916,96 |
| MP0005 | 6,87 | 350 | 2.404,50 |
| MP0003 | 9,65 | 246 | 2.373,90 |
| MP0002 | 7,45 | 258 | 1.922,10 |
| MP0008 | 6,24 | 254 | 1.584,96 |
| MP0006 | 5,24 | 289 | 1.514,36 |
| MP0011 | 5,65 | 245 | 1.384,25 |
| MP0009 | 5,48 | 245 | 1.342,60 |
| MP0004 | 5,46 | 214 | 1.168,44 |
| MP0010 | 6,24 | 157 | 979,68 |
| MP0007 | 2,54 | 152 | 386,08 |
| Total em Estoque | | | 17.977,83 |

Agora, supondo que sejam definidos percentuais de 20%, 30% e 50% para as classes A, B e C, respectivamente. Os produtos seriam então classificados da seguinte maneira:

Os produtos serão classificados como pertencentes à classe A enquanto o somatório do total for menor que o percentual definido para esta classe, ou seja, 3.595,57 (20% do total em estoque).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Produto** | **Custo** | **Consumo Médio** | **Total** | **Curva** |
| MP0001 | 8,24 | 354 | 2.916,96 | A |
| MP0005 | 6,87 | 350 | 2.404,50 | A |
| MP0003 | 9,65 | 246 | 2.373,90 | B |
| ... | ... | ... | ... | ... |

**Dica:**

Note que o próximo produto (MP0003) já não pôde ser classificado como pertencente à classe A, pois o somatório dos totais dos dois primeiros (2.916,96 + 2.404,50) já ultrapassou o limite definido de 20% (3.595,57).

Observe o produto MP0005. Se o total deste produto não for adicionado, o limite não é alcançado, mas por outro lado, se o adicionarmos, o limite será ultrapassado. Nestes casos, o sistema mantém este produto na classe que está tratando e começa a classificação na nova classe somente a partir do próximo produto da lista.

Do mesmo modo, agora continuamos a classificar os produtos como pertencentes à classe B enquanto o somatório dos totais for menor que o percentual definido a esta classe somada a classe anterior (20+30=50% ou 8.988,915).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Produto** | **Custo** | **Consumo Médio** | **Total** | **Curva** |
| MP0003 | 9,65 | 246 | 2.373,90 | B |
| MP0002 | 7,45 | 258 | 1.922,10 | B |
| ... | ... | ... | ... | ... |

Os produtos levam a classificação B enquanto o somatório do total for menor que 8.988,915. Como na faixa anterior, houve um produto que ultrapassou o limite e foi mantido na classificação.

Os produtos restantes podem ser classificados como classe C. Após a classificação, a tabela deverá estar como se segue:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Produto** | **Custo** | **Consumo Médio** | **Total** | **Curva** |
| MP0001 | 8,24 | 354 | 2.916,96 | A |
| MP0005 | 6,87 | 350 | 2.404,50 | A |
| MP0003 | 9,65 | 246 | 2.373,90 | B |
| MP0002 | 7,45 | 258 | 1.922,10 | B |
| MP0008 | 6,24 | 254 | 1.584,96 | C |
| MP0006 | 5,24 | 289 | 1.514,36 | C |
| MP0011 | 5,65 | 245 | 1.384,25 | C |
| MP0009 | 5,48 | 245 | 1.342,60 | C |
| MP0004 | 5,46 | 214 | 1.168,44 | C |
| MP0010 | 6,24 | 157 | 979,68 | C |
| MP0007 | 2,54 | 152 | 386,08 | C |
| Total em Estoque | | | 17.977,83 |  |

**Dica:**

A classificação ABC é atualizada no campo "Classe ABC" (B3\_CLASSE), no cadastro de Consumos Médios.

## **04.****CONSUMO MÉDIO**

O consumo médio representa a demanda média ocorrida no mês, utilizada para cálculo do Lote Econômico e do Ponto de Pedido, sendo fornecido na forma de um cadastro no Ambiente Estoque/Custos.

O campo “Cons. Inicial” (B1\_CONINI) no cadastro de produtos permite a informação da data inicial de movimentação do produto. Esta data será utilizada no cálculo do Lote Econômico, possibilitando que a média de consumo seja calculada somente para os períodos válidos.

No Ambiente Estoque/Custos, o seu cálculo pode ser efetuado de duas maneiras:

* Por Pesos
* Por Tendência

Assim, o cálculo é baseado no critério da Curva ABC dos materiais. Para se obter o cálculo, fazemos uma média de consumo, mês a mês, item a item.

## **A.** **Cálculo por Pesos**

O usuário atribui pesos de 0 a 9 aos últimos 12 meses de forma a retratar as demandas ocorridas. A atribuição de peso se dá quando o consumo em um determinado mês é significativamente diferente dos demais para não comprometer o resultado final no cálculo do consumo médio. Para definir pesos para os meses, deve-se alterar o parâmetro "MV\_PESOS" que possui o conteúdo padrão "111111111111" (uma posição para cada mês).

**Exemplo:**

O consumo médio de uma empresa que trabalha com produtos sazonais, por exemplo, sorvete, nos meses em que o clima é quente, vende muito mais do que nos demais meses do ano. O consumo aumenta muito nestes meses de picos de vendas, e o resultado final do consumo médio pode ser prejudicado por um valor muito maior do que a realidade de todos os outros meses. O resultado final seria influenciado por este valor e o consumo médio não representaria a realidade.

Para sanar este problema a empresa pode atribuir pesos a esses meses de maior consumo. Quanto mais fora da realidade maior o peso atribuído.

Assim, supondo que em um mês no início do verão as vendas sobem o dobro do normal, o peso atribuído a este mês será dois, se as vendas somam o triplo do normalmente comercializado o peso atribuído deve ser três e assim por diante. Ao final do processo o sistema divide o total de consumo pelo total dos pesos atribuídos e o resultado do cálculo é mais preciso.

O sistema efetua o somatório dos consumos e pesos e divide um pelo outro, obtendo assim o custo médio.

Observe a tabela a seguir:

|  |  |  |  |
| --- | --- | --- | --- |
| **Meses** | **Consumos** | **Pesos** | **Consumos x Pesos** |
| 6 | 88 | 1 | 88 |
| 7 | 90 | 1 | 90 |
| 8 | 96 | 1 | 96 |
| 9 | 155 | 2 | 310 |
| 10 | 85 | 1 | 52 |
| 11 | 150 | 2 | 300 |
| 12 | 150 | 2 | 300 |
| 1 | 145 | 2 | 290 |
| 2 | 200 | 3 | 600 |
| 3 | 210 | 3 | 630 |
| 4 | 290 | 4 | 1160 |
| 5 | 300 | 4 | 1200 |
| TOTAL | | 26 | 5148 |

**Em que:**

CM = Consumo Médio do mês corrente

TC = Total de Consumo dos últimos 12 meses X os Pesos

TP = Total de Pesos dos últimos 12 meses

**CM = TC/TP**

CM = 5148/26 = 198

Caso haja uma previsão de um consumo acentuado para o mês em questão, o Módulo Estoque/Custos permite ao usuário definir um percentual de incremento a ser aplicado sobre o valor calculado.

**Exemplo:**

O resultado do consumo médio é 198, porém existe a expectativa de uma demanda de 4% a mais este mês.

I = Incremento

CM = 198

I = 4%

CM = CM + I\*CM

CM = 198 + 4/100\*198 = 206

## **B.** **Cálculo por Tendência**

Nesse cálculo, o usuário informa o número de meses anteriores a serem considerados na formação da tendência para o mês corrente.

O Sistema verifica o consumo nos meses referenciados e traça uma reta o mais próximo possível dos dados coletados, obtendo a tendência.

**Exemplo:**

Para se obter o cálculo da média de consumo (B3\_MEDIA) e do lote econômico (B1\_LE) por tendência, é necessário configurar o campo de consumo inicial do produto (B1\_CONINI) que será somado ao número de meses desejado para efeito de cálculo. Nesse modelo de cálculo não é considerado tratamento por peso do parâmetro (MV\_PESO). Consideremos a tabela abaixo como exemplo.

|  |  |  |
| --- | --- | --- |
| **Número do Mês** | **Meses** | **Quantidade** |
| 1 | Janeiro | 1502 |
| 2 | Fevereiro | 3500 |
| 3 | Março | 150 |
| 4 | Abril | 9500 |
| 5 | Maio | 1522 |
| 6 | Junho | 3000 |
| 7 | Julho | 0 |
| 8 | Agosto | 0 |
| 9 | Setembro | 0 |
| 10 | Outubro | 0 |
| 11 | Novembro | 0 |
| 12 | Dezembro | 0 |

Ao rodar a rotina de lote econômico no sistema, existe a pergunta ATUALIZAÇÃO DO CONSUMO DO MÊS, se este estiver marcado o sistema não irá considerar a quantidade existente no arquivo referente ao mês da DATA BASE DO SISTEMA, ( Ex.: Data Base do sistema 31/06/99 ao ao rodar a rotina o mês 06 é zerado pois este esta marcado, isto só não ocorre se existir a movimentação do produto neste período) caso contrário ele irá considerar esta quantidade.

**Em que:**

A = Número de meses

X  = Média da soma dos meses

Y  = Média da soma das quantidades

W = A + 1

TX   = ∑ ( Mês – X )

TY   = ∑ ( Qtd. Mês – Y )

TX2 = ∑ ( ( Mês – X ) ²)

TY2 = ∑ (( Qtd. Mês – Y ) ² )

TXY = ∑ ((Mês – X ) \* ( Qtd. Mês – Y ) )

K  =  TXY / ( A \* √ TX2/ A  \*  √ TY2/A   )

K’ = K \* ( (√ TY2/A ) / (√ TX2/ A ) )

Média = ( K’ \* W ) + ( Y – ( K’ \* X ) )

**Então:**

A = 6

X = 1 + 2 + 3  + 4 + 5 + 6 / 6 = 3.5

Y  = 1502 + 3500 + 150 + 9500 + 1522 + 3000 / 6 = 3195.66

W = 6 + 1 = 7

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Mês** | **TX** | **TY** | **TX2(meses)** | **TY2(meses)** | **TX\*TY** |
| 1 | (1-3.5) = -2.5 | (1502 –3195.66) = -1693.67 | 6.25 | 2868506.7778 | 4234.1667 |
| 2 | (2-3.5) = -1.5 | (3500 –3195.66) = 304.33 | 2.25 | 92618.778 | -456.5000 |
| 3 | (3-3.5) = -0.5 | (150 –3195.66) = -3045.67 | 0.25 | 9276085.4444 | 1522.8333 |
| 4 | (4-3.5) = 0.5 | (9500 –3195.66) = 6304.33 | 0.25 | 39744618.7778 | 3152.1650 |
| 5 | (5-3.5) = 1.5 | (1522 –3195.66) = -1673.67 | 2.25 | 2801160.1111 | -2510.5000 |
| 6 | (6-3.5) = 2.5 | (3000 –3195.66) = -195.67 | 6.25 | 38285.4444 | -489.1667 |
| Total |  |  | 17.5 | 54821275.3335 | 5453.0000 |

K  = 5453 / ( 6 \* ( √ 17.5 / 6 ) \* ( √ 54821275.3335 / 6 ) )

K  = 0.1758

K’ = 0.1758 \* ( (√54821275.3335 / 6 ) / (√17.5 / 6 ) )

K’ = 310,7581

Média = ( 310.7581 \* 7 ) + ( 3195.66 – ( 310.7581 \* 3.5 ) )

Média = 4283

## **05.PONTO DE PEDIDO**

O ponto de pedido é a quantidade em estoque que uma vez atingida, inicia o processo de compra ou produção, considerando o consumo médio mensal, o tempo de reposição e o estoque de segurança.

Dessa forma, a fórmula para cálculo do ponto de pedido é PP = (CM\*TR) + ES.

**em que:**

CM = consumo médio

TR = tempo de reposição, que é o prazo de entrega do cadastro do produto

ES = estoque de segurança

PP = ponto de pedido

**Exemplo:**

CM = 30

TR = 02 meses

ES = 20

PP = (CM\*TR) + ES

PP = (30\*2) + 20 = 80

## **06.****CONFIGURANDO A ROTINA**

## **A.** **Procedimentos**

Para efetuar o cálculo do lote econômico:

1. Na janela de Manutenção do Lote Econômico, preencha os dados conforme as orientações a seguir:

* Atualização do Consumo do Mês

Marque este campo para que o cálculo atualize o consumo mensal tendo como referência a data base.

## **B.** **Cálculos**

* Cálculo Por Peso

Marque este campo para que o cálculo do consumo médio aplique-se por peso, conforme orientação do tópico Consumo Médio.

* Cálculo Pela Tendência

Marque este campo para que o cálculo do consumo médio aplique-se por tendência, conforme orientação do tópico Consumo Médio.

* Incremento

Informe neste campo, se necessário, o incremento para o cálculo do consumo médio do mês por pesos, conforme orientação do tópico Consumo Médio.

* Número de Meses

Informe neste campo o número de meses a serem considerados para o cálculo do consumo médio pela tendência. Quanto maior o número maior a precisão.

* Lote Econômico
* Cálculo do Lote Econômico

Marque este campo para calcular o lote econômico. Lembre-se que esta rotina permite efetuar os cálculos de Classificação ABC, Consumo Médio, Lote Econômico e Ponto de Pedido.

* Cálculo do Ponto de Pedido

Marque este campo para calcular o ponto de pedido. Este campo somente é habilitado se estiver, também, marcado o campo para cálculo do Lote Econômico.

* Cálculo do Estoque de Segurança

Marque este campo para calcular o estoque de segurança. Deve ser habilitado quando a opção de cálculo do estoque de segurança for marcada e o conteúdo digitado deve ser validado para que esteja entre 1 e 12.

O cálculo e atualização do estoque de segurança deve ser processado somente após a atualização do consumo do mês, isto para que o cálculo não seja realizado com valores desatualizados e deve ser realizado apenas para produtos que tenham o campo Dias p/ ES com valor informado.

É possível selecionar qual o tipo de cálculo para média de consumo: por consumo ou por previsão de vendas.

* Ajusta Lote Econômico pela disponibilidade financeira

Se selecionado os campos Cálculo do Lote Econômico e Ponto de Pedido, o o cálculo do lote econômico poderá ser ajustado pela disponibilidade financeira da empresa, conforme orientação do tópico "Cálculo do Lote Econômico".

* Classificação ABC
  + Período de Aquisição (meses)

Informe nestes campos quantos são os meses de referência para cálculo do lote econômico conforme curva ABC, um para cada classe: A, B e C, conforme orientação dos tópicos Lote Econômico e Classificação ABC.

* Distribuição Percentual (%)

Informe nestes campos qual o percentual de distribuição das classificações nos meses informados anteriormente, um para cada classe: A, B e C.

* Gravar a Classificação ABC

As porcentagens dos campos são default, podendo ser alterados para execução da rotina. Marque este campo, se quiser atualizar a classificação ABC dos produtos no campo Classe ABC (B3\_CLASSE).

* Tipos de Material

Se quiser restringir os cálculos para apenas alguns tipos de materiais conforme o Cadastro de Produtos, marque apenas os tipos de materiais que devem ser considerados.

* Grupos de Material

Se quiser restringir os cálculos para apenas alguns grupos de materiais conforme o Cadastro de Produtos, marque apenas os grupos que devem ser considerados.

2. Confira os dados e confirme o cálculo.  
Conforme a configuração da rotina, serão atualizados os campos Lote Econômico e Ponto de Pedido no Cadastro de Produtos, e os campos Consumo no Mês e Classe ABC no Cadastro de Consumos Médios.

## **C.** **Entrega**

(Informado no cadastro de produtos)

É a quantidade de horas, dias, semanas, meses, etc, que indica para o sistema, qual o tempo de entrega ou fabricação de um produto, a partir do recebimento de seu pedido, ou da abertura de sua OP.

Para produtos cujo prazo de entrega dependem de outras grandezas ou características, não sendo um período fixo, pode ser utilizada fórmula que deve ser cadastrada no Configurador.

Neste caso, informa-se o campo Fórmula Prazo, pois o campo Prazo de Entrega utiliza-se para prazos fixos.

O sistema utiliza preferencialmente o campo Fórmula Prazo e na sua falta o Prazo de Entrega tradicional.

Utiliza-se a variável QUANTIDADE na fórmula do prazo de entrega para se obter a quantidade real que se pretende avaliar o prazo de entrega. Por exemplo:

Supondo um produto cujo prazo de entrega seja de 10 lotes econômicos por dia.

A fórmula para expressar o prazo de entrega deste produto  no campo Fórmula Prazo é:

 Round((QUANTIDADE/(10\*B1\_LOTE)),0)

Esta fórmula retorna o prazo em DIAS, necessários para a produção de uma determinada quantidade planejada pelo MRP ou o tempo total a ser gasto para a produção de uma determinada Ordem de Produção e demais rotinas que tratam o prazo de entrega.

## **D.** **Estoque de segurança**

(informado no cadastro de produtos)

O estoque de segurança, também chamado de estoque mínimo, é a quantidade mínima que deve existir em estoque, que se destina a cobrir eventuais atrasos no suprimento, objetivando a garantia do funcionamento ininterrupto e eficiente do processo produtivo sem risco de faltas.

Entre as causas que ocasionam estas faltas podemos citar:

* Oscilação no consumo.
* Oscilação nas épocas de aquisição (atraso no tempo de reposição).
* Variação na qualidade, quando o Controle de Qualidade rejeita um lote.
* Remessas por parte do fornecedor divergentes do solicitado.
* Diferenças de inventário.

A importância do estoque de segurança é a chave para o adequado estabelecimento do ponto de pedido.

O estabelecimento de uma margem de segurança é o risco que a companhia está disposta a assumir com respeito à ocorrência de falta de estoque. Assim, o estoque mínimo pode ser determinado por:

* Fixação de determinada projeção mínima (estimada no consumo).
* Cálculos e modelos matemáticos.
* Confiança nos fornecedores e/ou prazo de entrega.

## **07.****TABELAS UTILIZADAS**

* SB1 - Arquivo de Descrição Genérica do Produto
* SB2 - Arquivo de Saldos Físico e Financeiro
* SB3 - Arquivo de Demandas
* SB5 - Dados Adicionais do Produto
* SC1 - Arquivo de Solicitações de Compra
* SC4 – Previsões de Venda
* SC7 - Arquivo de Pedidos de Compra
* SD2 - Arquivo de Itens da NF's de Venda
* SD3 - Arquivo de Movimentações Internas
* SF4 - Arquivo de Tipos de Entrada e Saída
* SD1 - Arquivo de itens da NF de entrada

## **08.****PARÂMETROS**

* MV\_USANPRC

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cálculos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550082-SIGAEST-C%C3%81LCULOS)
