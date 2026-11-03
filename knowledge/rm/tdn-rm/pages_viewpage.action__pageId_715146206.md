---
content_hash: 2b8a5bb5eb70d88a525a010701cb2a67e7ce442cabc341ad7d07a7e601693ce5
fetched_at: '2026-06-29T00:11:25.724807+00:00'
page_id: '715146206'
product: rm
source: tdn-rm
title: Fórmulas Desconto por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715146206
version: 20
---

---

Caso seja necessário utilizar o valor dos Descontos por Antecipação em alguma fórmula, foram disponibilizadas as funções de fórmulas abaixo.  
   
Funções de Fórmulas no *TOTVS Gestão Financeira* que retornam o valor do desconto por antecipação:

Fórmula Desconto por Antecipação

Com o objetivo de disponibilizar o valor do desconto por antecipação no contexto de fórmula no TOTVS Gestão Financeira foram criadas fórmulas para que sejam utilizadas na baixa do lançamento, no cálculo do valor líquido do lançamento e em outros processos ou recursos do produto, as fórmulas criadas são:

ValorDescontoAntecipacao

Essa fórmula tem o objetivo de  retornar o valor do desconto por antecipação calculado no momento do cálculo do valor líquido ou na baixa de lançamento financeiro através da data da baixa ao calcular o valor líquido. Caso essa fórmula seja utilizada em algum processo que não execute o cálculo do valor líquido, o valor retornado será o valor calculado conforme a data parametrizada no parâmetro "Data Default da Baixa a Receber" presente nos parâmetros do *TOTVS Gestão Financeira*em Contas a Receber → Baixa → Manutenção de Baixa → Baixa a Receber.

Utilização da fórmula ValorDescontoAntecipacao é recomendada quando quiser retornar o valor do desconto por antecipação calculado no momento do cálculo do valor líquido ou na baixa de lançamento financeiro através da data da baixa ao calcular o valor líquido.

ValorDescontoAntecipacaoPorData

Essa fórmula tem o objetivo de retornar o valor do desconto por antecipação calculado conforme a data passada por parâmetro.

Vale ressaltar que já existe a fórmula TabLanBaixa no TOTVS Gestão Financeira que recebe dois parâmetros. Essa fórmula tem o objetivo retornar o valor do campo passado por parâmetro. A fórmula tem dois parâmetros. O primeiro parâmetro é o nome do campo que queira retornar o seu valor, e o segundo parâmetro é o tipo do campo passado no primeiro parâmetro.  
Exemplo: TabLanBaixa('VALORDESCONTOPONTUAL', 'V')

Fórmula Valor de Bolsa Condicional Conforme Desconto Por Antecipação VLRBOLSALANDESCANTPORDTBAIXA(‘ ’)

Essa fórmula tem o objetivo de  retornar o valor das bolsas condicionais processadas para o lançamento levando em consideração o desconto por antecipação que o aluno está ganhando ao efetuar a baixa, também será avaliado se existe alguma condicional de desconto por antecipação vinculada a bolsa que indica que o aluno poderá perder a bolsa.

**Importante:**  Quando parametrizado essa fórmula o valor da bolsa varia conforme o desconto por antecipação aplicado na baixa do lançamento.

Esta fórmula leva em consideração a “Data de Baixa” para identificar o desconto por antecipação que o aluno terá ou não.

Exemplo:

Parcela: 1000.00

Desconto por antecipação:

* Pagamento até dia  05 => 50%
* Pagamento até dia  15 => 5%

Bolsa Condicional (Considera o desconto):

* Bolsa você merece => 10% (**Válida para pagamento até o dia 05**)
* Bolsa sindicato => 10%

Cenários:

* Se o aluno efetuar o pagamento no dia 05, o valor total de bolsa será de:

1000,00 (Vlr Parcela) - 500,00 (Desconto Antecipação) = **500,00 (Vlr pagamento)**

=> Bolsa você merece = 50,00 (Vlr Bolsa de 10%)

=> Bolsa sindicato = 50,00 (Vlr Bolsa de 10 %)

=> **VLRBOLSALANDESCANTPORDTBAIXA(‘ ’) = 100,00**

* Se o aluno efetuar o pagamento no dia 15, o valor da bolsa será de:

1000,00 (Vlr Parcela) - 50,00 (Desconto Antecipação) = **950,00 (Vlr pagamento)**

=> Bolsa você merece = 0,00 ( o aluno perde a bolsa, pois efetuou o pagamento dia 15)

=> Bolsa sindicato = 95,00 (Vlr Bolsa de 10 %)

=> **VLRBOLSALANDESCANTPORDTBAIXA(‘ ’) = 95,00**

Observe que o valor da bolsa varia conforme o valor de pagamento que irá variar conforme o desconto por antecipação e neste caso a fórmula sempre traz o valor atualizado.

Ressaltamos que todo o comportamento é flexível e dependerá de parametrizações que relatamos neste documento.

Portanto, podemos concluir que esta fórmula retorna o valor de bolsa atualizado conforme a data da baixa do lançamento.

Se a função de fórmula for acionada sem nenhum parâmetro, por exemplo, **VLRBOLSALANDESCANTPORDTBAIXA(‘ ’)** o sistema levará em consideração todas as bolsas processadas para o aluno durante a geração do lançamento.

Se desejar retornar o valor de uma bolsa específica, poderá passar, via parâmetro, o código das bolsas desejadas separadas por “;”, por exemplo: **VLRBOLSALANDESCANTPORDTBAIXA(‘35;01;10’)**.

VLRBOLSALANDESCANT

**VLRBOLSALANDESCANT(' ', DATA DESEJADA) :** esta fórmula executa o mesmo comportamento da fórmula VLRBOLSALANDESCANTPORDTBAIXA(‘ ’), a diferença está somente na passagem de parâmetro.

Para esta fórmula o usuário poderá passar uma data em que o sistema considerará como data de baixa para que os cálculos sejam realizados.

Lembrando que caso o primeiro parâmetro esteja vazio o sistema levará em consideração todas as bolsas processadas para o aluno durante a geração do lançamento.

Se desejar retornar o valor de uma bolsa específica, poderá passar, via parâmetro, o código das bolsas desejadas separadas por “;”, por exemplo: **VLRBOLSALANDESCANT** (‘35;01;10’,’01/01/2017’).

Importante ressaltar que para os casos em que houver baixa parcial, devemos tratar na fórmula para que o valor de bolsa não seja processado na segunda baixa, pois a primeira baixa já processa o valor da bolsa.

Veja o exemplo abaixo:

Fórmula VALORBOLSALAN

Durante o processamento da contabilização ou geração da nota fiscal é possível recuperar o valor da bolsa processado para o lançamento com ou sem o valor do desconto por antecipação utilizando a fórmula VALORBOLSALAN.

**Declaração da fórmula:** ValorBolsaLan(int campoValor, int tipoBolsa, string codBolsa), essa formulá tem três parâmetros.

O primeiro parâmetro é o tipo de valor que quer que seja retornado:

=>  int campoValor

0 = Será retornado o valor da bolsa

1 = Será retornado o valor da bolsa na baixa

2 = Será retornado o valor da bolsa sem considerar o valor do desconto por antecipação da parcela

3 = Será retornado o (valor da bolsa sem o desconto por antecipação - valor da bolsa considerando o maior desconto por antecipação)

o segundo parâmetro é o tipo da bolsa:

=>  int tipoBolsa

    Escalável = 0,

    Especial = 1,

    Todas = -1

E o terceiro parâmetro é o código da bolsa:

=>   string codBolsa

Pode passar o código da bolsa, se for passado vazio ou -1 indica que o sistema vai somar todas as bolsas.

Exemplo: ValorBolsaLan(0, -1, 'BOL001'),

                      

Para geração de lançamento parametrizado com essa fórmula o valor da bolsa no lançamento não irá variar conforme o desconto por antecipação e nem perder a bolsa, neste caso a fórmula sempre traz o valor da bolsa.

Contabilização

Na contabilização do lançamento quando o evento contábil estiver parametrizado para aplicar na “Bolsa”, a fórmula pode ser utilizada conforme o exemplo abaixo.

VALORBOLSALAN(0,-1,TABBOLSALAN('CODBOLSA','S'))

=>  TABBOLSALAN('CODBOLSA','S')  -  retorna o código da bolsa corrente, ou seja, que está sendo processada.

Fórmula SLANDESCOPONTUALPORDTBAIXA(CAMPO):

Fórmula responsável em recuperar o valor de um determinado campo da tabela SLANDESCPONTUAL do registro que compreenda a data da baixa do lançamento, ou seja, será carregado o desconto processado para o lançamento conforme a data da baixa.

**Exemplo:**

Data vencimento lançamento: 30/03

**Descontos processados para o lançamento:**

1º Desconto – Pagamento dia 05/03 – Valor para pagamento: 500,00

2º Desconto – Pagamento dia 10/03 – Valor para pagamento: 600,00

3º Desconto – Pagamento dia 20/03 – Valor para pagamento: 700,00

4º Desconto – Pagamento dia 30/03 – Valor para pagamento: 1000,00

Executando a fórmula **SLANDESCOPONTUALPORDTBAIXA(‘VALORPARAPAGTO’)** para uma baixa no dia 09/03, o resultado da fórmula será de 600,00.

Observação:

Se a data da baixa for maior que a data do vencimento do lançamento então será considerado o desconto por antecipação processado para o vencimento

Fórmulas Desconto por Antecipação para Bolsa na Geração de Lançamento

Na geração de lançamento o valor do **tipo percentual ou do tipo valor** da bolsa do contrato do aluno pode ser calculado via fórmula. As fórmulas podem ser para calcular o valor ou o percentual da bolsa considerando o contexto da bolsa presente no contrato. As fórmulas são cadastradas no cadastro da bolsa. Desta forma, na geração do lançamento será considerado o contexto da bolsa do aluno no contrato para obter o valor do desconto por antecipação podendo usar as fórmulas **VLRDESCONTOANT e PERCENTUALDESCANT.**

Vale ressaltar que as fórmulas **VLRDESCONTOANT e PERCENTUALDESCANT somente** podem ser utilizadas durante a geração de lançamento para o contexto das bolsas do contrato.

Mais informações sobre [Documento Técnico - Customização do percentual / valor da bolsa por fórmula](https://tdn.totvs.com/pages/viewpage.action?pageId=354469739)
