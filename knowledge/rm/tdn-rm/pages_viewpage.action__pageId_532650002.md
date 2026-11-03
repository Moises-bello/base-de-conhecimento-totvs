---
content_hash: add8c4e14b0f29414b1d021fd88257f6d08151b8a2e74368d43006e9256f4d23
fetched_at: '2026-06-29T00:10:36.520904+00:00'
page_id: '532650002'
product: rm
source: tdn-rm
title: Saldo de Produto - Factor/SPED (Esclarecimentos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532650002
version: 1
---

Esse documento tem como objetivo esclarecer dúvidas relacionadas a quantidade reportadas no saldo de produtos SPED FISCAL, e a interação entre os valores do **estoque próprio** e das quantidades no **chão de fábrica “Estoque Factor”**:

* **H010** - Inventário
* **K200** - Estoque Escriturado

Primeiro teremos um bloco de premissas que são parâmetros que vamos considerar para todos os exemplos.

Segundo teremos um bloco dedicado a “esclarecimentos de conceitos e regras” que visa facilitar o entendimento de exemplos posteriores.

## Premissas (Parâmetros)

As premissas é um conjunto de configurações que vão valer para todos os exemplos sem que seja preciso repetir a mesma informação toda vez:

Considera-se “**Data Atual**” =  **20-08-2019**

Considera-se “**Período SPED**” = **01-07-2019 até 31-07-2019**

Considera-se “**Data Final**” =  **31-07-2019 23:59:59** (Último dia\hora do “Período SPED”)

## Esclarecimentos de conceitos e regras:

### Período do SPED vs Data Atual

É importante esclarecer a diferença do que deve ser considerado no SPED no período gerado (saldo em data específica) em relação ao que se tem de estoque no momento que a solicitação é gerada (saldo atual).

Para atendermos com exatidão as informações solicitadas pela receita precisamos sempre considerar a posição de estoque na data final do SPED e não considerando o estoque na data atual;

 A quantidade do produto a ser reportada é sensível ao tempo, “varia ao longo do tempo”.

Diferente do estoque atual, a quantidade do produto a ser reportado para SPED é a quantidade que existia até o último segundo da data final do SPED gerado, nesse caso “**Data Final**”.

### Estoque SPED (Inventário / Estoque Escriturado)

O estoque a ser considerado no SPED é todo produto em poder da empresa:

**(Saldo próprio + Saldo no chão de fábrica + Saldo de terceiros) -  (Saldo com terceiros)**

Em todos os casos o saldo é relativo a “**Data Final**”

### Estoque (Gestão de Estoque, Compras e Faturamento)

Informação abaixo vale para (Saldo Próprio e Saldo de Terceiros). 

O estoque registrado e controlado no sistema de “Gestão de Estoque, Compras e Faturamento” é facilmente verificado através da ficha física financeira, sendo possível determinar qual quantidade do produto foi considerada como “em estoque” e levada para os blocos H010 e K200. 

Deve-se observar a última movimentação registrada na FFF anterior a data final do SPED, olhando para essa movimentação na ficha tem-se a quantidade considerada, essa última movimentação pode ser anterior ao período selecionado.

Um produto comprado a um ano que permanece em estoque vai ser reportado mesmo sem nenhuma movimentação no período, por isso reforço o termo “*Última movimentação registrada na FFF anterior a data final do SPED*”.

 A principal tabela para os dados da ficha física financeira é a tabela TRELSLD, acompanhar a ficha é  mais amigável que consulta direta a tabela.

### Estoque (Factor) - Chão de Fábrica

O estoque chamado de chão de fábrica é composto por todos os produtos que foram baixados (estoque -> Factor) ou que foram produzidos dentro do próprio Factor e aguardam entrada de produção, devolução de matéria-prima, entrada de subproduto gerado (Factor -> Estoque).

Produtos movimentados do Estoque para o Factor através da baixa deixa de aparecer na ficha física financeira, no entanto, enquanto está no chão de fábrica sem ter passado por nenhum processo de transformação, para efeito de inventário deve ser considerado normalmente. 

Quando olhamos para o sistema de gestão de produção é preciso considerar vários fatores para chegar ao correto valor a ser reportado, em que data cada produto foi consumido, quando a produção foi apontada, quando foi gerado o subproduto. Com essas informações ainda precisamos considerar as movimentações e revertendo tudo que ocorreu após a data alvo podemos deduzir o estoque na data específica. Em exemplos posteriores essas regras vão ficar mais claras.

### Reversão de Operações FACTOR

O processo de reversão de operações do FACTOR tem objetivo de atender a premissa de obter o saldo no chão de fábrica em data específica, consiste em desfazer todas as operações geradoras ou consumidoras de produtos em momento posterior a data final do SPED gerado.

 

#### Operações Geradoras

* Apontamento de acabado
* Apontamento de semiacabado
* Apontamento de subproduto

**Exemplo (a)**:

Ao apontar a geração de subproduto “**Serragem, 5KG**” em **10-08-2019** passamos a ter no chão de fábrica “**5KG de Serragem**”, mas ao gerar SPED “**Data Final - 31-07-2019 23:59:59**“ esse produto não pode ser considerado. 

Utilizando informação da tabela KATVORDEMMP é verificado os apontamentos que foram efetivados após “**Data Final**”, nesse caso onde tivemos uma operação de adição de estoque ao chão de fábrica invertermos a operação para subtração.

E onde vamos aplicar essa operação?

A operação de reversão parte do cenário atual e desfaz tudo de mais recente para o mais antigo até chegar a “**Data Final**”.

Nesse caso considera-se o saldo atual do chão de fábrica onde temos “**Serragem, 5KG**”.

Desfazemos nossa única operação do período, a inclusão do subproduto vira subtração, então, “Chão de Fábrica” - “Operação”. Nesse caso “5KG Serragem“ - “KG Serragem” = “ZERO KG Serragem”.

Assim foi anulado a operação futura.

O mesmo procedimento é válido para todos os geradores citados acima.

 **Observação**:

* Apontamento de perda de acabado ou semi acabado não entra como parte do estoque e seu registro quando é feito tem fins gerenciais, devido suas características é desnecessário olhar esses valores.

#### Operações Consumidoras

* Apontamento de consumo de matéria prima
* Apontamento de perda de matéria prima

**Exemplo (b)**:

No chão de fábrica temos em “**Data Final**” os materiais abaixo, parte da produção do acabado “Carro X”:

4 Pneus

16 parafusos

4 rodas

Em “02-08-2019” foi feito a atividade montagem das rodas que consumiu os itens acima citados e finalizou a produção de uma unidade do “Carro X”, após a execução dessa atividade nosso chão de fábrica ficou da seguinte forma:

0 Pneus

0 parafusos

0 rodas

1 Carro X

Em “**Data Atual**” foi solicitado a geração do SPED para “**Período SPED**” que deve reportar o saldo de produtos considerando “**Data Final**”.

Considerando que devemos partir do chão de fábrica atual e esse permaneceu inalterado desde “02-08-2019”, temos como ponto inicial:

0 Pneus

0 parafusos

0 rodas

1 Carro X

Revertemos então a operação mais recente, onde adicionou 1 Carro X vamos subtrair

0 Pneus

0 parafusos

0 rodas

0 Carro X   (1 - 1)

Revertemos em seguida o consumo, onde subtraiu do chão de fábrica agora adiciona (4 pneus, 16 parafusos, 4 rodas), agora temos as quantidades a ser reportada no SPED.

04 Pneus  (0 + 4)

16 parafusos (0 + 16)

04 rodas (0 + 4)

00 Carro X  

#### Operações de Movimentações

* Entradas / Devoluções
* Baixas

**Exemplos**:

Dando continuidade ao exemplo (**a**) acima, no dia “**12-08-2019**” foi feita entrada do subproduto “5KG Serragem”, agora esse saldo de produto está no estoque padrão.

Em data atual, se verificar saldos e custos do produto “Serragem” vai ver que tem 5KG.

Em data atual, se verificar o chão de fábrica vai ver “Serragem” está ZERADO.

Novamente foi solicitado a geração do SPED para “**Período SPED**” que deve reportar o saldo de produtos considerando “**Data Final**”.

Nesse caso ao buscar informação de Serragem no estoque padrão, que pode ser acompanhado através da ficha física financeira, o sistema vai procurar a última referência do produto “**Serragem**” anterior a “**Data Final**”. Nesse ponto a entrada realizada em “**12-08-2019**” vai ser ignorada, a última referência foi a venda de todo saldo desse subproduto 2000 KG em “**15-03-2019**” que deixou o saldo igual a ZERO. Considerado do estoque padrão temos o **valor ZERO**.

**Agora a reversão do FACTOR**:

Chão de Fábrica (**Atual**)

0 KG de Serragem

**Onde tivemos a operação de entrada que subtraiu saldo do chão de fábrica revertemos**:

Chão de Fábrica em (**12-08-2019**)

5 KG de Serragem (0 + 5)

**Onde tivemos a geração do subproduto que adicionou saldo do chão de fábrica revertemos**:

Chão de Fábrica em (**10-08-2019**)

0 KG de Serragem (5 - 5)

**Sem mais alterações**...

Chão de Fábrica em (**31-07-2019**)

0 KG de Serrage

Observe a importância de considerar as movimentações registradas em KMOVESTOQUE, TIPOMOV = ‘B’ quantidades positivas e negativas. 

Nesse exemplo se a movimentação fosse desconsiderada terminaríamos com um chão de fábrica em “31-07-2019” com “-5KG de Serragem”.

O SPED não aceita saldo negativo, e saldo ZERO não precisa ser reportado. Para esse caso o valor negativo seria ZERADO e descartado e não faria diferença na entrega, mas vamos supor que na operação de venda do cliente em “**15-03-2019**” a quantidade vendida fosse de 1900 KG de serragem, teria sobrado 100 KG de serragem no estoque padrão.

Dessa forma teríamos um erro pois iria considerar:

100Kg de serragem estoque padrão

-5Kg de serragem do chão de fábrica.

Saldo de **serragem**  no SPED, 95 Kg (**ERRADO**)

Temos momento que esse valor negativo é correto e deve ser realizado, vamos considerar o exemplo (**b**) onde temos no chão de fábrica:

4 Pneus

16 parafusos

4 rodas

Se realizamos o apontamento de consumo sem ter feito a baixa dos produtos nosso chão de fábrica teria ficado assim: 

-4 Pneus

-16 parafusos

-4 rodas

Ao gerar o SPED essas quantidades seriam localizados no estoque padrão e seria irreal reportar, então ao juntar o estoque padrão encontrado com o chão de fábrica esses valores se anulam.

Chão de Fábrica Estoque Padrão Resultado SPED

-4 Pneus +4 Pneus 0 Pneu

-16 Parafusos +16 Parafusos 0 Parafuso

-4 Rodas + 4 Rodas 0 Roda

### Empenho

O empenho de materiais apenas movimenta o produto entre locais de estoque no intuito de reserva para produção, o produto não deixa o estoque físico da empresa, continua sendo exibido na ficha física financeira, produtos empenhados segue o tratamento padrão de contagem de estoque sem consulta ao sistema de controle de produção RMFactor.

### Sobre tabela **KMOVESTOQUE**:

Campo: **TIPOMOV**

'**S**' = Movimento de solicitação de matéria prima originado de ordem de produção.

'**P**' = Movimento de solicitação de matéria prima originando do planejamento.

'**A**' = Movimento de solicitação de matéria prima originando do planejamento.

'**B**' = Movimento de **baixa** de materiais quando **QTDE (quantidade) positiva**.

'**B**' = Movimento de **entrada** de materiais quando **QTDE (quantidade) negativa**.

'**E**' = Movimento de empenho de materiais.

'**D**' = Movimento de desempenho de materiais.

'**M**' = Movimento de perda de matéria prima.

Entende-se “**Baixa de Materiais**” o material que sai do estoque e vai para o chão de fábrica.

Entende-se “**Entrada de Materiais**” o material que sai do chão de fábrica e vai para o estoque.

**Material no estoque** é visível na ficha física financeira.

Material no chão de fábrica é o todo material considerado no sistema de gerenciamento de produção, matéria prima, acabado, semi-acabado, subproduto, materiais perdidos.

### Entendimento de campos com **valor** **multiplicado por 10 mil**

No sistema de produção existe a possibilidade de uso de até 8 oito casas decimais, essa possibilidade por padrão é indisponível e o recomendado é a utilização de unidades de medidas menores ao invés de frações tão longas. 

Para acomodar esse tipo de fracionamento os valores relacionados à quantidade são gravados multiplicado por 10 mil em várias tabelas, o sistema faz automaticamente o controle de dividir e multiplicar por 10 mil, por padrão a base de dados suporta apenas 4 casas decimais.

Fica aqui o esclarecimento para essa que tem sido dúvida de alguns clientes.

## Exemplos para ajudar no entendimento

## Exemplo - 01

Reversão de operações do Factor e obtenção do estoque (chão de fábrica) na “**Data Final**”.

**Produto X, estoque ao longo do tempo**:

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Estoque (Nucleus)** | **Estoque (Factor) Chão de Fábrica** | **Movimentação** |
| 05-06-2019 | 3000 | 0 | (**a**) Inicial 3000 no estoque, ZERO no Factor |
| 30-06-2019 | 1800 | 1200 | (**b**) Baixa 1200 unidades produto X |
| 10-07-2019 | 0 | 810 | (**c**) Consumo 1200 (Factor)  (**d**) Baixa 810 (Estoque -> Factor)  (**e**) Venda 990 (Estoque -> Estoque) |
| **31-07-2019** | **810,00** | **100** | (**f**) Devolução 810 (Factor -> Estoque)  (**g**) Correção apontamento (consumo, 1200 para 1100), agora sobre 100 no chão de fábrica. |
| 01-08-2019 | 0 | 910 | (**h**) Baixa 810 (Estoque -> Factor) |
| **20-08-2019** | **2000** | **0** | (**i**) Consumo 910 (Factor -> Factor)  (**j**) Compra 2000 (Estoque -> Estoque) |

Se realizar a consulta de saldos e custos na data atual 20-08-2019 teremos 2000 unidades do produto X, e estaria errado reportar esse valor, deve considerar saldo do produto na “**Data Final**”.

Ao emitir ficha física financeira é possível buscar a quantidade do produto no dia 31-07-2019, no caso 810 unidades, essa é a quantidade a ser considerada observando apenas o sistema de gestão de estoque. Seria incorreto reportar esse valor, observe que no chão de fábrica nessa data existia 100 unidades.

Para fins do SPED a informação correta com data base igual “**31-07-2019**” é  **910,00**

* 810 Estoque Nucleus +
* 100 Estoque chão de fábrica;

E como se chega a quantidade no chão de fábrica utilizando o processo de Reversão?

Para chegar às 100 unidades do produto X existente em 31-07-2019 é feito a reversão das operações posteriores a 31-07-2019. E deve-se considerar  apenas operações que interferem no FACTOR, então, para o caso acima:

1. Reverter o consumo em 20-08-2019 (**j**), o saldo ZERO volta a ter 910
2. Reverter a baixa em 01-08-2019 (**h**), o saldo 910 volta a ser 100
3. A próxima operação é do dia 31-07, está dentro do prazo e não precisamos mais voltar no tempo, **resultado 100**;

A data em que ocorreu o consumo e a quantidade consumida é verificado com dados da tabela KATVORDEMMP.

As movimentação de baixa, sua data e quantidade é verificada com dados da tabela KMOVESTOQUE, movimento tipo B com quantidade positiva.

As movimentações de entrada, sua data e quantidade é verificada com dados da tabela KMOVESTOQUE, movimento tipo B com quantidade negativa.

Nesse ponto uma ideia deve estar bem clara, o estoque no tempo específico é muito diferente do estoque atual, só entendendo o conjunto das operações pode-se chegar aos números reportados nos blocos H010 e K200. 

 

## Exemplo - 02

Importância de considerar tanto movimento de baixa quanto de entrada, operações registradas em KMOVESTOQUE.

**Produto A**:

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Estoque (Nucleus)** | **Estoque (Factor) Chão de Fábrica** | **Movimentação** |
| 05-06-2019 | 100 | 0 | Estoque pré existente. |
| 05-07-2019 | 0 | 100 | Baixa 100 unidades |
| 10-08-2019 | 100 | 0 | Devolução 100 unidades |

Estoque próprio, última movimentação com data anterior a “**Data Final**”, 05-07-2019, saldo ZERO.

Chão de Fábrica:

Saldo Atual = 0

Saldo (05-07-2019) = 100 Reversão da devolução de 100

Vai ser reportado ao SPED 100 unidades consideradas do chão de fábrica.

**Se não considerasse as movimentações deixaria de reportaria esse produto ao SPED, teria considerado saldo igual a ZERO**. 

## Exemplo - 03

Importância de considerar tanto movimento de baixa quanto de entrada, operações registradas em KMOVESTOQUE.

**Produto A**:

|  |  |  |  |
| --- | --- | --- | --- |
| **Data** | **Estoque (Nucleus)** | **Estoque (Factor) Chão de Fábrica** | **Movimentação** |
| 05-07-2019 | 100 | 0 | Estoque pré existente. |
| 05-08-2019 | 0 | 100 | Baixa 100 unidades |
| 10-08-2019 | 100 | 0 | Devolução 100 unidades |

Estoque próprio, última movimentação com data anterior a “**Data Fina**l”, 05-07-2019, saldo 100.

Chão de Fábrica:

Saldo Atual (20-08-2019)= 0

Saldo em (10-08-2019) = 100 Reversão da devolução de 100

Saldo em (05-08-2019) = 0 Reversão da baixa de 100

Vai ser reportado ao SPED 100 unidades do estoque próprio.

**Toda sequência de reversão é importante, deixar de considerar movimentações gera divergência em casos específicos como o citado no Exemplo 02 e no Exemplo 03 onde não iria impactar também não provoca divergência**.
