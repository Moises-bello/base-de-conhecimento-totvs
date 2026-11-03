---
content_hash: f5068717ed13cb0226610e0cb287ddaae005811e02c8d3a17af56babfc42e70a
fetched_at: '2026-06-29T00:10:35.512073+00:00'
page_id: '530186732'
product: rm
source: tdn-rm
title: Movimento Mensal
type: documentation
url: https://tdn.totvs.com/display/LRM/Movimento+Mensal
version: 17
---

**Pagamento** será mensal, salvo acordo entre as partes que estipule prazo menor.

* ao final de cada mês, o empregado receberá o pagamento imediato das seguintes parcelas: remuneração; décimo terceiro salário proporcional; e férias proporcionais com acréscimo de um terço e sobre todo o montante incidirá a alíquota mensal de dois por cento à título de FGTS.
* as parcelas referidas à décimo terceiro e férias proporcionais são devidas ao empregado **independentemente** do número de dias trabalhados no mês.

**A indenização sobre o saldo do Fundo de Garantia do Tempo de Serviço – FGTS** poderá ser paga pela metade, quando antecipada ao empregado juntamente com as parcelas mensais sendo o seu pagamento irrevogável, independentemente do motivo de demissão do empregado, mesmo que por justa causa. Deverá ser **paga diretamente ao empregado**, sem necessidade de depósito em conta vinculada. Tal valor, deverá ser obrigatoriamente discriminado na folha de pagamento.

Para atender a determinação acima, orientamos os clientes a criarem eventos com código de Cálculo 0 (Zero), calculados por fórmulas, para as verbas de os avos de 13º Salário e Férias e a multa rescisória para os casos de antecipação da mesma. Abaixo iremos exemplificar algumas sugestões de fórmulas:

**Observação:**A orientação para criação do evento para pagamento do 13º salário com “código de cálculo 0 – Sem Código de Cálculo Existente”, foi antes da liberação do “[código de cálculo 441 - 13º SALÁRIO CONTRATO VERDE AMARELO](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572516387)”, portanto a partir de agora (11/2020) o evento deverá ter o “código de cálculo 441 - 13º SALÁRIO CONTRATO VERDE AMARELO”.

Para a alteração do contrato de verde amarelo para tempo indeterminado durante o ano deverá ser feita a alteração do evento criado anteriormente com “código de cálculo 0 – Sem Código de Cálculo Existente” para “código de cálculo 441 - 13º SALÁRIO CONTRATO VERDE AMARELO”.

Essa alteração também deve ser feita para o evento de média.

Considerando que o Salário Contratual do funcionário é  R$1500,00 com data de admissão dia 13/01 e o mesmo obteve as seguintes remunerações:

Competência 01:

Competência 02

***Férias***

Para o cálculo do avo de Férias poderá retornar o salário nominal  e dividir por 12: **((RC / 12)/30)\*ND**

Para o cálculo de Médias por valor, poderá retornar a soma dos valores dos eventos que compões a média e dividir por 12: **(C('0082')+C('0083'))/12.**

Para o cálculo de Média por Hora, poderá usar a função de fórmula CALCMED, conforme o exemplo: **((CALCMED('101')\*(NDFERIASAQ /2.5))/12)- (MV (17,0,'7002'))**

Assim, ao lançar as verbas de Férias, o envelope ficará conforma abaixo na competência 02:

Para o cálculo do Adicional de Férias, poderá retornar os valores dos eventos de Férias e dividir por 3:  **(C('7000')+C('7001')+C('7002'))/3.**

Na competência 02, lançou o adicional conforme abaixo:

***13º Salário***

Para o cálculo do avo de 13º Salário poderá retornar o salário nominal  e dividir por 12: **((RC / 12)/30)\*ND**

Para o cálculo de Médias por valor, poderá retornar a soma dos valores dos eventos que compões a média e dividir por 12: **(C('0082')+C('0083'))/12.**

Para o cálculo de Média por Hora, poderá usar a função de fórmula CALCMED, conforme o exemplo: **(((CALCMED(201)\* INCMES(NMESES,1))/12)) - MV (18,0,'7012')**

Assim ao Lançar as verbas de 13º Salário, o envelope ficará conforme abaixo na competência 02

***Antecipação da Indenização sobre o saldo do FGTS***

Para o cálculo da antecipação da indenização sobre o saldo do FGTS, poderá somar as bases de FGTS folha e FGTS 13º, multiplicar por 0.02 e multiplicar por 0.20:

**((BSFGTS13 + BASEFGTS)\* 0.02)\* 0.20**

Atenção

As fórmulas acima são somente **sugestões** para calcular o 13º Salário e Férias proporcional que devem ser pagos junto com a remuneração do funcionário. As mesmas podem ser alteradas ou o usuário pode utilizar outras conforme a sua necessidade.
