---
content_hash: 2bf3779b895876c0843c2113841590dd0e6943999166d5622cdac6ef08f4b1c9
fetched_at: '2026-06-29T00:09:33.905004+00:00'
page_id: '425459078'
product: rm
source: tdn-rm
title: Controlar a Perda dos Descontos por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459078
version: 17
---

---

No momento da *geração* (inclusão) do lançamento, não temos a certeza que o aluno receberá o benefício, muito menos qual item (ou faixa) de desconto será considerado, uma vez que o Desconto por Antecipação somente será concedido mediante a liquidação antecipada, mas, como neste momento o sistema precisa calcular todos os valores que irão compor os lançamentos para registrar cada um destes valores nos seus devidos campos, então, na geração (inclusão) do lançamento, para compor o valor base para os cálculos, o sistema irá considerar sempre o *maior* desconto a que o aluno tiver direito.

Isto é necessário, pois as bolsas do tipo "*Aplicar bolsas em cascata*" (seja a bolsa por contrato ou bolsa por classificação) e do tipo "*Exclusiva*" (para bolsas por classificação), são calculadas somente após a aplicação dos devidos descontos.

Porém, na *geração* (inclusão) do lançamento, todos os descontos por antecipação aplicados à parcela são calculados e gravados internamente no banco de dados, mas o *maior* desconto, aquele considerado para compor o valor base para o cálculo de bolsas, receberá uma marcação especial no banco de dados e o sistema poderá utilizá-lo futuramente no momento da baixa, fazendo um confrontamento entre o maior valor previsto para o desconto (calculado na geração) e o valor realmente concedido de desconto que neste caso dependerá diretamente da quantidade de dias em que a baixa estiver sendo realizada antecipadamente.

Para que o sistema possa fazer o confrontamento destes valores, é necessário que ele esteja previamente parametrizado com a indicação de um campo de  para receber esta diferença. Este campo de valor de integração deverá ser criado no Educacional, exclusivamente para este fim.

Feitas estas parametrizações, no momento da baixa do lançamento, o sistema fará um confrontamento entre o *maior* desconto, aquele considerado para compor o valor base para o cálculo de bolsas (calculado na geração e registrado internamente) e o valor realmente concedido de desconto (calculado conforme a quantidade de dias em que a baixa estiver sendo realizada antecipadamente) e registrará esta diferença no campo de valor de integração parametrizado anteriormente para receber o valor da perda do Desconto por Antecipação, que poderá ser visualizada no respectivo item de baixa do lançamento.

O controle dos valores de Perda dos Descontos por Antecipação é um recurso que poderá ser muito útil futuramente na emissão de relatórios gerenciais específicos que podem ser criados para auxiliar Auditorias e conferências de valores.

Controle da perda do Desconto por Antecipação ao Baixar o Lançamento

Na geração do lançamento o cálculo da bolsa para tipo cascata sempre vai ser executado considerando a aplicação do desconto por antecipação, ou seja, primeiro calcula o desconto por antecipação e depois aplica o cálculo da bolsa. Para calcular a bolsa do tipo cascata será considerando o maior desconto por antecipação cadastrado para o aluno.

Exemplo:

Um aluno possui um desconto por antecipação cadastrado com a seguinte regra:

* Pagamento até o dia 05 = 50% de desconto
* Pagamento do dia 06 até o dia 10 = 20% de desconto

Parcela:

* Valor da mensalidade de R$ 1000,00
* Bolsa = 10 %

O cálculo do valor da bolsa levara em consideração o desconto por antecipação considerando que o aluno irá pagar a mensalidade no dia 05.

Valor da bolsa = valor mensalidade (R$ 1000.00) – desconto por antecipação (R$ 500,00 – 50%) \* percentual da bolsa(10%)  = R$ 50,00;

O cálculo acima é realizado durante a geração do lançamento, porem o aluno poderá realizar o pagamento no dia 06.

Com a possibilidade de possíveis auditorias ou conferencias será possível controlar o valor da perda do desconto por antecipação através de um valor de integração previamente parametrizado que será processado durante a baixa do lançamento financeiro.

Exemplo:

Um aluno possui um desconto por antecipação cadastrado com a seguinte regra:

* Pagamento até o dia 05 = 50% de desconto

* Pagamento do dia 06 até o dia 10 = 20% de desconto

* Valor da mensalidade de R$ 1000,00.

Vamos considerar que o aluno realizou o pagamento no dia 07, então o desconto por antecipação será de R$ 200,00 com isso será lançado no campo do valor de integração parametrizado como “Valor de perda do desconto por antecipação” o valor de R$ 300,00 que representa a perda do desconto por antecipação em relação ao maior desconto que o aluno teria direito caso realizasse o pagamento até o dia 05.

O valor de perda do desconto por antecipação será processado somente se o aluno tiver algum desconto por antecipação processado durante baixa.

**Parametrização:**

Para utilizar este recurso deverá ser preenchido nos parâmetros (Educacional >> Integração >> Financeiro >> Educacional >> Fin – Vlrs. Opcionais/Integração 1/3) o campo “Valor de parda do desconto por antecipação” que identifica qual o valor de integração controlará a informação durante a baixa.

* O campo valor de integração que será utilizado deverá estar cadastrado no cadastro de valores de integração do Educacional com ação igual a “Nada”, pois o objetivo deste campo é apenas informativo e seu valor não terá nenhum impacto sobre o valor líquido do lançamento financeiro.
* O parâmetro "Valor de perda do desconto por antecipação" uma vez já preenchido não poderá ser alterado se o valor de perda do desconto por antecipação já foi processado em algum item de baixa.

Após a baixa do lançamento financeiro, será possível consultar o valor da perda do desconto por antecipação, no anexo "Baixas do lançamento".

Acesse a parcela e acesse a aba "Lançamentos/Boletos da parcela":

Edite o lançamento, para que o sistema carregue suas informações:

Acesse o menu de anexos e clique sobre o item "Baixas do Lançamento":

Edite o registro de baixa do lançamento:

Acesse a aba "Dados Adicionais" e poderá visualizar todos os valores registrados para os campos de valores de integração, incluindo o valor destinado ao campo configurado nos parâmetros referente a perda de desconto por antecipação. (Opcionais/Integração 1/3)

* Para baixa parcial sempre ocorrerá a perda do desconto por antecipação, neste caso se o sistema estiver parametrizado o valor da perda do desconto por antecipação será apurado.
* Quando houver um pagamento a menor, seja pela baixa manual ou retorno bancário também ocorrerá a perda do desconto por antecipação.
