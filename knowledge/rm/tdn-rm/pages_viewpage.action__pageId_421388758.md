---
content_hash: 4bda941210cfc64a3b9ecfc80ec5e3d2980d3c10157948a50644e0910d0cc74a
fetched_at: '2026-06-29T00:09:18.710641+00:00'
page_id: '421388758'
product: rm
source: tdn-rm
title: FIN - Aplicação Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388758
version: 31
---

**Como Funciona**

Quando uma nova aplicação financeira é definida no TOTVS Gestão Financeira, estamos na prática definindo uma "conta de investimento", que poderia ser entendida como uma conta/caixa muito especializada. Esta estrutura de dados dispõe de recursos para lidar com cotas, assim como as valorizações destas cotas no tempo (cotações). Dispõe de regras de negócio otimizadas para os cálculos dos impostos (IR e IOF) no contexto de cada uma das aplicações financeiras suportadas (Fundos DI, CDB e Poupança). Diferente de uma estrutura baseada em conta/caixa e extratos, o módulo de aplicação financeira dispõe de dados em tabelas especiais (ex: FAPLFIN), que podem ser usadas para elaboração de relatórios específicos. Neste contexto, ocorrem efeitos em extratos na respectiva "conta corrente", na forma de extratos, para as operações de aplicação (Saque na conta corrente), e resgate (Depósito na conta corrente).

**Tipos de Aplicação Financeira**

Poupança

É regulamentada pelo Governo Federal, através do C.M.N. – Conselho Monetário Nacional, pelas mãos do Banco Central. Os aspectos de crédito de rendimentos e Imposto de Renda são iguais em todos os bancos. A remuneração da caderneta de poupança é regulamentada pelo Governo Federal e padronizada em todas as instituições financeiras. O aniversário ocorre sempre no mesmo dia do mês, todos os meses. Caso você realize um depósito em um dia do mês que não seja a data de aniversário da sua poupança, será aberta outra data de aniversário para aquele dia.   

Subcontas: 

São formadas pelos dias de depósitos nas contas de poupança, ou seja, a mesma data de aniversário para rendimentos. Os depósitos realizados nos dias 29, 30 e 31 serão redirecionados para o dia 1º do mês seguinte.

Poupança PJ

Um dos benefícios da poupança para Pessoa Jurídica está a liquidez imediata, onde seu investimento pode ser resgatado a qualquer momento sem nenhuma carência ou incidência de IOF (embora para resgates fora das datas de aniversários não são computados rendimentos), assim, poderá usar aquele recurso sempre que precisar.

O Totvs Gestão Financeira desenvolveu uma nova natureza de aplicação que funciona da seguinte forma:

* Criada natureza de aplicação financeira “Poupança PJ” com cálculo separado do modelo já existente hoje, essa nova natureza está disponível para seleção no cadastro da aplicação financeira.
* O tratamento do aniversário considera para rentabilidade o saldo de cada aplicação a cada 3 meses. Sendo considerado para cálculo da rentabilidade o saldo residual de cada aplicação por data de aniversário.
* Será considerado a cotação do primeiro mês após a data da aplicação, multiplicado por 3, referente aos 3 meses.
* Quanto ao cálculo do IR será considerada a alíquota de 22,5% incidente sobre o rendimento.

Ex:

Data Aplicação: 01/10/2019

Valor : 100.000,00

Cotação do índice em 01/11/2019: 0,2455

Cálculo do fechamento mês a mês:

10/2019 - 100.000,00

11/2019 - 100.000,00

12/2019 - 100.000,00

01/2020 - 100.570,79

Rendimento bruto: 736,50 (0,2455 x 3 = 0,7365)

IR: 165,71 (736,50 - 22.5%)

Rendimento líquido: 570,79

CDB

Os CDB's são títulos privados, emitidos por banco comercial, múltiplo, de investimento ou caixas econômicas, junto aos seus clientes pessoa física, jurídica ou outros bancos, com o intuito de captar dinheiro para realizar financiamento para outros clientes. O CDB é um tipo de aplicação financeira para quem procura rendimentos pré ou pós - fixados, liquidez diária ou no vencimento. Ao realizar um investimento em CDB, é como se você estivesse emprestando dinheiro ao banco por determinado período, pode ser meses ou anos, e este banco emprestará este dinheiro para outras pessoas por uma taxa maior. Ao final deste período, você recebe de volta seu dinheiro e mais uma taxa de juros (rendimentos). Esta taxa é acordada no momento da aplicação. Quando há muita procura por crédito no mercado, o banco poderá pagar juros mais altos pelo CDB, tentando atrair mais investidores. Quando a procura por crédito é pouca, o banco reduzirá o valor da taxa para desestimular o investimento. Como o CDB é uma aplicação com remuneração negociada, as instituições financeiras concedem taxas melhores de acordo com o volume do investimento e dos prazos da aplicação, ou seja, quanto maior o investimento, maior a chance de conseguir taxas melhores. Assim, é importante negociar bem a taxa e ficar atento às diferentes ofertas.

O CDB é dividido em duas modalidades:

CDB Pós-Fixado

No CDB pós-fixado, você só conhecerá a valorização de seu rendimento no vencimento da aplicação.  
Remuneração: É composta por uma taxa de juros pré-estabelecida na data da aplicação mais uma taxa variável que utiliza certo índice.  
Liquidez: Diária.  
No fluxo de Caixa, quando uma aplicação financeira do tipo CDB pós-fixado não possui cotação em uma determinada data, o sistema irá levar em consideração a última cotação anterior à Data.  
Obs.: A aplicação financeira do Tipo CDB pós-fixado só irá aparecer no fluxo de caixa, caso o vencimento da aplicação esteja dentro do período do fluxo.

**Observação:**

Em determinados casos, o banco pode arbitrar uma taxa diferente daquela contratada no momento da aplicação, em caso de um resgate antecipado. Nestes casos, o extrato costuma detalhar no resgate indicando o valor do capital sobre o qual o resgate está incidindo, além do rendimento e impostos desta operação (vide abaixo). O procedimento recomendado pelo sistema é: 1) Fazer um resgate pelo valor do capital indicado no resgate na aplicação principal, na data de início da aplicação, reduzindo assim o principal que será rentabilizado até a data de vencimento contratada; 2) Cadastrar uma nova aplicação de CDB no sistema para cada resgate informado, indicando o valor do capital como valor investido na mesma data de investimento da aplicação original, e a data efetiva do resgate indicada como data de vencimento. Normalmente a taxa efetiva praticada no resgate antecipado não vem destacada no extrato (se o banco puder informar, indique-a), caso não esteja indicada use a mesma taxa da aplicação original e efetue os devidos ajustes a maior e a menor, na rentabilidade e nos impostos.

CDB Pré-Fixado

É a única modalidade de aplicação financeira dentre as disponíveis no mercado em que o investidor sabe, no ato da aplicação, o valor do resgate, pois a taxa no prazo contratado é mantida independentemente da situação do mercado financeiro.  
Remuneração: É composta unicamente por uma taxa de juros fixa determinada na data da aplicação, sempre referida ao ano.  
Liquidez: Somente no vencimento da aplicação.  
Os resgates realizados nos 30 primeiros dias de aplicação terão incidência de IOF calculados através da tabela regressiva de IOF, já a incidência de IR é calculada utilizando 20% nos rendimentos gerados em 2004 e pelo uso da tabela regressiva de IR para os rendimentos gerados a partir de 2005.  Tais impostos serão pagos sobre os rendimentos proporcionais ao valor resgatado, ou seja, se for realizado um resgate de 50% sobre valor principal da aplicação serão pagos 50% de IOF e IR.

Fundo de Investimento

As aplicações de Fundo de Investimento não possuem prazos definidos e o investidor passa a ter cotas (frações ideais) de todo o patrimônio. Desta forma, o investidor pode realizar quantas aplicações adicionais for conveniente e o cálculo será realizado para cada aplicação adicional realizada.  
Como o intervalo entre o resgate total e uma nova aplicação financeira no mesmo fundo pode ser indeterminado (pode ser de um dia para o outro, ou separados por meses, ou anos) o procedimento que entendemos como mais correto é manter a parte inicial da aplicação no fundo encerrado, e a criar uma nova aplicação de fundo no sistema.  
Os rendimentos serão calculados pela variação do valor das cotas, havendo inclusive casos de prejuízos. O valor da cota deverá ser informado no cadastro de moedas / cotações. Entretanto, não há uma cotação padrão fornecida pelos órgãos competentes semelhante ao CDB e a Poupança, já que depende diretamente do investimento total realizado pelo gestor da aplicação.  
Os impostos sobre os resgates são calculados de forma semelhante ao cálculo do CDB com relação ao uso das tabelas regressivas e contagem de tempos. As exceções são que a contagem de tempo para o Fundo de Investimento Curto Prazo (duração até 365 dias) é no dia 29/12/2004, em vez do dia 22/12/2004, utilizado para CDB e Fundo de Investimento Médio Prazo e que surge uma nova forma de tributação de IR denominada IR Come Cotas, onde no momento do resgate deverá ser descontado o IR Come Cotas já ocorrido.

**Importante**: sistema trata somente fundos DI.

Cotas:

São as parcelas da divisão do fundo de investimento, onde os investidores (cotistas) são proprietários de um determinado número de cotas proporcionais ao dinheiro investido.

IR Come-Cotas:

Trata-se do IR recolhido semestralmente, a partir de 2005, nas aplicações de fundo de investimento com alíquotas de 15% (Fundo de Investimento Médio Prazo) e 20% (Fundo de Investimento Curto Prazo). É uma espécie de antecipação do IR a ser pago no resgate, já que o fundo de investimento não possui data de vencimento. Caso a**[aplicação financeira](https://tdn.totvs.com/pages/releaseview.action?pageId=421388618)** esteja marcada com a opção "Rendimento do último dia do período come-cotas não será considerado no come-cotas posterior", o cálculo do próximo período de come-cotas irá desconsiderar estes rendimentos. **Exemplo:** Para o cálculo do come-cotas no período de maio, se a opção estiver **desmarcada**, são considerados os meses desde o início de **dezembro até o último dia de maio**. Caso a opção esteja **marcada**, o cálculo considera o período desde o início de **dezembro até o dia anterior ao último dia de maio**.

Processo de Resgate do IR Come-Cotas

Esse processo permite realizar o **resgate do come-cotas de forma separada** das demais movimentações. Com essa alteração, é possível registrar **outro resgate no mesmo dia do come-cotas,** diminuindo o **valor do Imposto de Renda** já realizado no resgate do Come-Cotas para a nova movimentação, o objetivo da criação do processo é **refletir de forma mais precisa o tratamento fiscal das movimentações**. Ao separar o processo de resgate do come-cotas, evita-se que o valor retido nesse evento seja calculado indevidamente na apuração do IR de outros resgates efetuados na mesma data.

Essa funcionalidade está disponível para aplicações do tipo fundo e foi implementada para garantir o tratamento correto dos valores de IR conforme o tipo de operação realizada. Abaixo segue a localização do processo: 

Seu menu de funcionamento se assemelha ao menu do processo de Encerramento, segue imagem de exemplo: 

Detalhes sobre os campos: 

* **Mês e Ano:** Campos ficam inativos para edição e são automaticamente editados para o período de come-cotas;
* **Exibir IR Come-Cotas:** Botão para realizar o calculo prévio do Saldo Real, Rendimento e o Imposto de Renda do Come-Cotas;
* **Saldo Real:** Após realizado o calculo pelo botão "Exibir IR Come-Cotas", o saldo real sobre a aplicação é exibido;
* **Rendimento:** Exibe o valor do rendimento calculado;
* **IR Come-Cotas:** Exibe o valor do IR Come-Cotas calculado;
* **Ajuste do IR Come-Cotas:** 
  + **Valor:** Campo de preenchimento para ajustar o valor calculado do IR Come-Cotas;
  + **Positivo:** Quando marcado, o campo preenchido no "Valor" é considerado pelo sistema como positivo;
  + **Valor Cota:** Exibe o valor da cotação para a data do calculo;
  + **Quantidade Cotas:** Exibe a quantidade de cotas de acordo com o valor preenchido no campo "Valor";

Observação

No dia em que ocorre o resgate do come-cotas, é necessário primeiro realizar o resgate do come-cotas, para só depois processar o resgate normal pendente naquele mesmo dia.

**Observações:**

Para o correto cálculo dos rendimentos para aplicações do tipo Fundo de Investimentos, não deverão ser cadastradas cotações em feriados e finais de semana.

Ao inserir movimentação na aplicação financeira caso não tenha cotação cadastrada para um dia útil "dentro do período atual da aplicação", o sistema exibirá mensagem e o processo em execução não será finalizado.

Ao calcular o saldo da Aplicação financeira o sistema informará que obrigatório o cadastramento da cotação até a data D-1, ou seja, um dia antes data atual nas aplicações de natureza CDB e Fundos de Investimento.

Nas Aplicações Financeiras de natureza Poupança o sistema só exigirá o cadastramento de cotação de aplicações com vencimento em 29, 30,31 no 1º dia útil do mês seguinte.

Na aplicação financeira é possível fazer um resgate ao longo do mês e ainda fazer uma nova aplicação antes do encerramento mensal, mas se ao final do mês a aplicação financeira estiver com saldo zerado, esta será considerada como encerrada no sistema.

Quando uma aplicação tem o saldo zerado, mesmo que momentaneamente, todo o histórico passado é totalmente encerrado e inicia uma nova etapa de cálculos, totalmente independente, ou seja, se a aplicação financeira conseguir aceitar uma nova aplicação partindo de um saldo zerado, todo o histórico passado é ignorado para efeito de cálculos.

[Aplicações Financeiras - Perguntas e Respostas](https://tdn.totvs.com/x/x4wdGQ)

**Equivalência com estrutura de conta/caixa e extratos**

Caso a aplicação financeira não se enquadre nas suportadas pelo TOTVS Gestão Financeira, o efeito de uma aplicação financeira pode ser recriada usando-se apenas uma conta/caixa e o registro das movimentações na forma de extratos. Neste contexto não há nenhuma regra de negócio otimizada para o cálculo dos impostos, mas as operações nos extratos podem ser feitas da seguinte forma: uma **aplicação** pode ser representado como um extrato de tipo  "Depósito Transferência" tendo como origem uma outra conta/caixa que represente uma "Conta/Corrente", um **resgate** pode ser representado como um extrato de tipo "Saque Transferência" tendo como destino uma outra conta/caixa que represente uma "Conta/Corrente", os **impostos** (IR e IOF) pode ser representado como um extrato do tipo "Saque Manual", e o **rendimento** pode ser representado como um "Depósito Manual".

Veja Também
