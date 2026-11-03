---
content_hash: dc7a8dcb7d88df0677fb96cdc9741481cc4d236d25da75d19c22f08be3060862
fetched_at: '2026-06-29T00:10:37.793810+00:00'
page_id: '540889290'
product: rm
source: tdn-rm
title: Lançamento de Empréstimo na Rescisão - Fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540889290
version: 5
---

Limitar o desconto dos empréstimos a 30% do líquido de uma rescisão é uma tarefa que pode ser feita de várias formas.

Vamos imaginar uma situação em que determinado funcionário possua os seguintes empréstimos a serem descontados na rescisão :

1) Empréstimo Habitacional              1.000,00

2) Empréstimo Educacional               1.200,00

3) Empréstimo Particular                   1.500,00

Vamos imaginar ainda que 30% sobre o líquido da rescisão do funcionário seja igual a 1.100,00.

Como proceder neste caso ?

1) Descontar o valor integral do empréstimo 1 e descontar 100,00 do empréstimo 2 ?

2) Priorizar o desconto de algum tipo de empréstimo, por exemplo o Empréstimo Particular ?

3) Descontar proporcionalmente ao saldo devedor de cada empréstimo ?

Empréstimo 1     297,30

Empréstimo 2     356,76

Empréstimo 3     445,94

Na verdade esta pergunta não tem uma resposta única, cada empresa pode ter uma forma de interpretar como deve ser realizada a limitação de descontos de empréstimo a 30% do líquido da rescisão.

Desta forma, esta implementação foi realizada no sistema utilizando o recurso de  fórmulas de cálculo para definir como deve ser feito o desconto dos empréstimos do funcionário. Através do recurso de fórmulas cada empresa poderá efetuar o desconto conforme sua necessidade.

## **Solução Adotada**

Para facilitar o desenvolvimento da fórmula foi criada uma função chamada InfEmp (Informações do empréstimo), que será utilizada para retornar as informações dos empréstimos pendentes do funcionário. A documentação do funcionamento da Função de Formula pode ser consultada [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=452719547)

Iremos exemplificar um cenário com a utilização da Fórmula, considerando que o desconto será limitado a 30% do líquido de rescisão:

Funcionário possuí 3 empréstimos, com saldo maior que zero, no valor total de R$ 3.700,00. E seu salário é de R$ 377,20:

Criada a fórmula que será calculada 30% sobre o salário líquido do funcionário. A lógica desenvolvida é de rateiro e proporção em relação ao saldo devedor, pois o saldo devedor pode ser maior que o salário.

c#Exemplo de Fórmula que calcula 30% de desconto do empréstimo na Rescisão 0
Entao
Se MaxEmp >= SaldoTot
Entao
repita
SetVar(ItemEmp,ItemEmp + 1);
SetVar(aDistribuir, InfEmp( ItemEmp, 'SALDODEVEDOR' ) );
SetVar(aDistribuir,val( str(aDistribuir, '999999999,99')));
SetVar(Retorno, Concat(Retorno, InfEmp( ItemEmp, 'CODIGO' )));
SetVar(Retorno,Concat(Retorno,':'));
SetVar(Retorno, Concat(Retorno, str(aDistribuir,'999999999,99')));
SetVar(Retorno,Concat(Retorno,';'))
Ate ItemEmp = TotEmp
Senao
repita
SetVar(ItemEmp,ItemEmp + 1);
Se ItemEmp = TotEmp
Entao
SetVar(aDistribuir,MaxEmp-saldodist)
Senao
SetVar(aDistribuir, (MaxEmp / SaldoTot ) \* InfEmp( ItemEmp, 'SALDODEVEDOR' ) );
SetVar(aDistribuir,val( str(aDistribuir, '999999999,99')))
FimSe;
SetVar(saldodist, saldodist + aDistribuir);
SetVar(Retorno, Concat(Retorno, InfEmp( ItemEmp, 'CODIGO' )));
SetVar(Retorno,Concat(Retorno,':'));
SetVar(Retorno, Concat(Retorno, str(aDistribuir,'999999999,99')));
SetVar(Retorno,Concat(Retorno,';'))
ate ItemEmp = TotEmp
FimSe
FimSe;
Retorno]]>

O retorno do resultado da fórmula deverá seguir o seguinte padrão:

CódigoDoEmprestimo: ValorEmprestimo;

Os demais empréstimos serão concatenados ao primeiro empréstimo, conforme a tela abaixo:

O funcionário será demitido em 31/12/2019 e será lançado o saldo devedor de empréstimo, utilizando a nova implementação através da fórmula. Na tela de rescisão será associado a fórmula cadastrada:

O valor foi lançado na Ficha Financeira, conforme retornado pela fórmula:

O cadastro de empréstimo foi atualizado com o valor de descontado rateado por empréstimo:
