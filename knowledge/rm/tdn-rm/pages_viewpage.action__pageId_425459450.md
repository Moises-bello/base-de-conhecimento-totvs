---
content_hash: e8a3f93f3df3eecc5bdde673028aaf0a86c2eba7de3ee80b230615d36897c7ae
fetched_at: '2026-06-29T00:09:35.958540+00:00'
page_id: '425459450'
product: rm
source: tdn-rm
title: Baixa de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459450
version: 4
---

---

Ao realizar a Baixa dos lançamentos financeiros o sistema calculará o valor líquido dos lançamentos conforme parametrização prévia da base e também levando em consideração os valores que são controlados através dos campos de Valores Opcionais ou Valores de Integração criados especificamente para este fim, tais como Bolsa Condicional, Bolsa Incondicional, Pagamento a Maior, Pagamento a Menor e os valores aproveitados da Conta Corrente. Destes campos, somente os campos que controlam **Pagamento a Maior** e **Pagamento a Menor** são campos editáveis no momento da Baixa, pois os outros traduzem valores específicos já calculados.

   
 Assim no momento da Baixa dos lançamentos estes dois campos estarão normalmente habilitados para digitação conforme seja necessário, ora na aba que contém os Valores Opcionais denominada *'Saldos dos Lançamentos'*, para os casos de baixas em lançamentos que foram criados utilizando Valores Opcionais ou na aba que contém os Valores de Integração denominada *'Saldos dos Valores de Integração'*, para os casos de baixas em lançamentos que foram criados após a parametrização dos Valores de Integração.

**Baixa de Lançamento com utilização de Valores de Integração**

Com a evolução do sistema para contemplar os  na geração dos lançamentos, valores como Bolsa condicional, Bolsa incondicional, Pagamento a maior e Pagamento a menor, antes controlados somente através de campos opcionais, poderão ser baixados através dos Valores de Integração.

Como vai funcionar?  
Clientes que já utilizam valor opcional:

Para estes clientes a baixa do lançamento financeiro irá respeitar a parametrização presente nos parâmetros "Educacional | Integração | Financeiro | Fin - Vlrs Opcionais / Integração", seguindo a seguinte regra:

 - Depois de parametrização, toda baixa de lançamento do Educacional no TOTVS Gestão Financeira a partir da data da parametrização passa a efetuar a baixa do valor no campo do valor de integração parametrizado.

 - Para as baixas dos lançamentos que já foram gerados antes da parametrização, continuaram a efetuar a baixa do valor no campo valor opcional configurado antes da data da parametrização, por exemplo:

**Exemplo 1:**

 → Lançamento 1 gerado com data de criação no dia 10/03/2017 utilizando valor opcional.  
  → Dia 01/04/2017 o sistema foi parametrizado para utilizar o campo "Pagamento a maior" no valor de integração X.  
  → Na baixa do lançamento 1 o sistema não vai utilizar o valor de integração parametrizado para efetuar a baixa do valor, e sim o valor opcional utilizado antes da mudança da parametrização.

**Exemplo 2:**  
 → Lançamento 2 gerado com data de criação no dia 05/04/2017 utilizando valor opcional para "Pagamento a menor" e valor de integração para "Pagamento a maior".  
 → Dia 01/04/2017 o sistema foi parametrizado para utilizar o campo "Pagamento a maior" no valor de integração X.  
 → Dia 06/04/2017 o sistema foi parametrizado para utilizar o campo "Pagamento a menor" no valor de integração Y.  
 → Na baixa do lançamento 2 o sistema não vai utilizar o valor de integração parametrizado para efetuar a baixa do valor "Pagamento a menor", e sim o valor opcional utilizado antes da parametrização. E no valor "Pagamento a maior", o sistema irá efetuar a baixa usando o valor de integração parametrizado para o "Pagamento a maior".

**Mais exemplos da Utilização do Valor Integração basta clicar** **[aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=325851924)****:**

Não será obrigatório fazer com que todos os valores sejam baixados pelo valor de integração, ou seja, a migração poderá ser aos poucos juntamente com a geração / regeração de lançamento.

Vale ressaltar que após lançamentos serem gerados com utilização de valor de integração não será possível modificar a parametrização, e seus valores serão baixados pelo valor de integração parametrizado.

Clientes que irão implantar o sistema:

Para estes clientes a baixa do lançamento financeiro irá respeitar a parametrização presente nos parâmetros "Educacional | Integração | Financeiro | Fin - Vlrs Opcionais / Integração". Lembrando que se já existir lançamentos gerados utilizado o valor de integração não será possível modificar a parametrização.

Na baixa dos lançamentos utilizando valor de integração, os valores poderão ser consultados na etapa de "Edição do Lançamento" na aba "Saldo dos Valores de Integração" e irão refletir no cálculo do valor líquido na baixa lançamento.

**Baixa de Lançamento com utilização de Desconto por Antecipação**

Na baixa de lançamento financeiro proveniente do TOTVS Educacional, o  poderá ser concedido para o aluno conforme a ordem de verificação descrita abaixo:

* Contrato.
* Campus/Polo da Matriz Aplicada (Somente no Ensino Superior).
* Matriz Aplicada.

Desta forma, para conceder os Descontos por Antecipação aos alunos, o sistema sempre procurará pelos descontos que tiverem associados na seguinte ordem: primeiro procurará pelos descontos associados nos *contratos* dos alunos e os aplicará, caso não existam Desconto por Antecipação associados nos contratos, irá procurar por Descontos por Antecipação associados aos *campus/polo das matrizes aplicadas* às quais pertencem e os aplicará, caso não encontre, irá por último, procurar pelos Descontos por Antecipação associados às *matrizes aplicadas* às quais pertencem e os aplicará.

**ATENÇÃO:**   
O desconto por antecipação só será concedido para o aluno na realização da baixa total do valor a ser pago do lançamento financeiro, isto é, na baixa parcial o desconto por antecipação não será concedido.   
Exemplo:

A) Lançamento financeiro 1:

* + Valor original de R$ 1000,00
  + Valor desconto por antecipação de R$ 100,00
  + Valor restante a ser pago de R$ 900,00
  + Se o aluno realizar o pagamento no valor de R$ 500,00. Isto é, realizar uma baixa parcial. O desconto por antecipação não será concedido para o aluno. E o valor restante a ser pago será de R$ 500,00.

B) Lançamento financeiro 2:

* + Valor original de R$ 1000,00
  + Valor desconto por antecipação de R$ 100,00
  + Valor restante a ser pago de R$ 900,00
  + Se o aluno realizar a baixa do lançamento no valor de R$ 900,00, valor total a ser pago. O desconto por antecipação será concedido para o aluno.

Os dados base para o cálculo do Desconto por Antecipação serão os dados presente no lançamento financeiro.

Os lançamentos financeiros que *não* terão o Desconto por Antecipação concedidos para os alunos são:

* Lançamento financeiro de contratos gerados por Acordo financeiro.
* Lançamento financeiro de parcela onde o *serviço* não irá considerar o desconto por antecipação.
* Lançamento financeiro com pagamento parcial do valor a ser pago, isto é, a realização de uma baixa parcial.
* Lançamento financeiro com pagamento a menor via retorno bancário ou via baixa manual.
