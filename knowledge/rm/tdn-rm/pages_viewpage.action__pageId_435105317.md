---
content_hash: 68111cdcdad8a76cc24800456c94728c1bc397ec91e925f8430b31c355ba0125
fetched_at: '2026-06-29T00:09:49.552290+00:00'
page_id: '435105317'
product: rm
source: tdn-rm
title: Condomínio - Fechamento do Condomínio - Medidor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105317
version: 15
---

Esse cadastro é responsável por receber a aferição do consumo de despesas como água, luz e gás. Isso será insumo para a cobrança dos ocupantes do condomínio.  
Cada medidor terá sua identificação, o tipo de medição conforme o consumo e a forma como será rateada a cobrança para os condôminos.

**Aba Identificação:**

* **Grupo Dados Gerais:**

* + **Identificador:** Código identificador do cadastro do Medidor.
  + **Número do Equipamento:** Código único do equipamento de medição.
  + **Tipo de Medidor:** O medidor pode ser dividido em três tipos:

* + - Geral: É o medidor "pai" do condomínio. Responsável por fazer a aferição de todas as sub unidades daquele empreendimento. Além disso distribui o insumo para todas as áreas comuns do condomínio. Este tipo de medidor só deve ser associado a um empreendimento.
    - Por grupo: Pode ser dividido por um grupo de subunidades, ou unidades (quadras), no módulo de condomínio pode ser chamado de galpões ou lojas (caso for um shopping). Não deve possuir unidades e subunidades associadas ao mesmo medidor. Exemplo: Tentar associar o medidor de gás XYZ ao bloco A e ao mesmo tempo o apartamento 101 do bloco B. Este cenário não é permitido.
    - Individual: Nesse caso será criado um medidor para cada sub unidade / galpão / loja, sendo medido separadamente com cobranças específicas.
      * Observação: O tipo de medidor não pode ser alterado quando o medidor já estiver associado a algum empreendimento, unidade ou subunidade.

* **Tipo de Consumo:** Informe a finalidade do medidor, por exemplo: Medidor de água, luz, etc. O tipo de consumo deve ser cadastrado separadamente.
* **Descrição:** Informe uma descrição para o medidor e suas observações.

* **Grupo Situação:**

* + **Situação:** O medidor pode ter situações de acordo com o funcionamento do equipamento, como por exemplo Ligado ou Desligado. O equipamento pode entrar em manutenções, ser trocado ou ser desligado a qualquer momento. Esse status será alterado através de um processo.
  + **Data da Ligação:** Informe a data em que o equipamento do medidor entrará em produção.
  + **Data do Desligamento:** Informe a data em que o equipamento do medidor saiu de produção e não será utilizado.

* **Grupo Dados para cálculo:**

* + **Unidade de Medida:** Informe qual unidade de medida de consumo o equipamento irá utilizar na medição. Por exemplo, um padrão de energia elétrica utiliza KW/h para medição.
  + **Medição Inicial:** Será informado qual o valor de medição do equipamento no momento em que ele foi ligado e entrou em produção. Alguns equipamentos já podem começar com uma medição inicial maior que zero.
  + **Medição Final:** Quando o equipamento for desligado, será informado qual foi a medição final deste equipamento.
  + **Carga Contratada:** Alguns empreendimentos já contratam com as empresas de água, energia, etc, um valor prévio de consumo. Informe neste campo o valor da carga contratada, se necessário.
  + **Constante:** Esse valor é um multiplicador sobre o consumo do medidor para encontrar o consumo real. Depende da velocidade da rotação do equipamento medidor, mas na maioria dos casos é 1.
  + **Medidor superior:** Caso este não seja o medidor geral, deverá ser informado qual o medidor geral superior a este.
  + **Compõe cálculo do Medidor Superior:** Se informado o medidor superior, então deve ser informado se este medidor fará parte do cálculo do medidor superior. Ao marcar esta opção o sistema utiliza os valores de consumo periódico deste medidor e somará ao valor total de seu medidor superior, caso contrário seus valores não interferirão no medidor superior.
  + **Item de cobrança:** Informe o item de cobrança que será utilizado para o fechamento das despesas. Esse campo é obrigatório.
  + **Apuração na ausência de consumo:** Quando não houver medição no período, informe o comportamento deste medidor:

* + - Não processa: Este medidor não fará parte do cálculo de despesa.
    - Utiliza o valor do mês anterior: O medidor irá utilizar para a aferição o valor medido do mês anterior.

* + **Modelos de cálculo de rateio:** Há várias formas de se calcular a divisão das despesas entre o condomínio. A disponibilidade dos modelos de cálculo de rateio irá depender do **Tipo de Medidor** selecionado:

* + - Para o Tipo de Medidor Geral podem ser parametrizados os rateios:

* + - * [Rateio por Fração Ideal](http://tdn.totvs.com/pages/viewpage.action?pageId=435105183)

* + - Para o Tipo de Medidor Por Grupo podem ser parametrizados os rateios:



* + - Para o **Tipo de Medidor Individual** podem ser parametrizados os rateios:



* + - **Rateio do medidor geral:** Este parâmetro é responsável por indicar se o medidor fará parte do rateio do medidor geral. Neste caso não há faturamento apenas deste medidor.

Informações Complementares

---

**Anexos:**



**Processos:**

* Excluir ultimas medições
* [Importar Medições](https://tdn.totvs.com/pages/viewpage.action?pageId=827300487)

Veja Também

---
