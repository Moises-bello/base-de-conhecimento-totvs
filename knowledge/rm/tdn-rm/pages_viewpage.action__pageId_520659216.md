---
content_hash: cd0ae3ed57792d5635a78679484930a57ade880d5a665d4c3f4fb5d9b240ea47
fetched_at: '2026-06-29T00:10:30.996706+00:00'
page_id: '520659216'
product: rm
source: tdn-rm
title: Contrato de Locação - Gestão - Aluguel em Dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659216
version: 14
---

## **Finalidade**

---

O Aluguel em Dobro em contratos de locação comercial permite a cobrança de um valor dobrado em meses específicos, conforme definido no contrato.

## **Como utilizar**

---

Para inclusão de um aluguel em dobro, realize a edição do contrato de locação e no Menu: Gestão selecione a opção: Aluguel em dobro.   
Na tela apresentada será necessário preencher os campos a seguir:

* **Descrição:** Nessa campo é possível inserir uma descrição sobre o Aluguel em Dobro. Campo obrigatório.
* **Competência**: Esse campo determina qual o mês será aplicado o Aluguel em Dobro no Contrato de Locação.

**Observação:** Em nosso exemplo, caso a competência seja em Junho:

* + - Se o Contrato de Locação for do Tipo "Mês Vencido", a cobrança do aluguel em dobro será feita no mês seguinte, em nosso exemplo em JULHO.
    - Se o Contrato de Locação for do Tipo "Mês Vincendo", utilizando nosso exemplo, neste caso a cobrança do aluguel em dobro será feita no mesmo mês, ou seja JUNHO.

* **Percentual:** Esse campo determina qual o percentual de aumento do valor de Locação. Esse campo vem com o valor default igual à 100%, porém pode ser alterado. Não é permitido inserir valor igual ou menor que 0;
* **Considerar dobro apenas para CTO:** Ao marcar esse parâmetro o sistema irá compor o aluguel em dobro baseando-se somente do valor do CTO cadastrado na faixa do aluguel complementar.
* **Data Inicial:** Determina qual o mês/ano, será o inicio de vigência do parâmetro cadastrado. Por default, o campo vem preenchido com a data de Inicio de Vigência do Contrato de Locação, mas pode ser editado para uma outra data desejada. Campo obrigatório;
* **Data Final:** Determina qual o mês/ano, será o final de vigência do parâmetro cadastrado. Por default, o campo vem preenchido com a data de Final de Vigência do Contrato de Locação, mas pode ser editado para uma outra data desejada.
  + **Observação:**
  + - O mesmo mês pode ser definido apenas uma vez durante a vigência de um parâmetro já cadastrado para o mesmo;
    - Caso a competência selecionada não esteja dentro do período de vigência cadastrada, o sistema não irá permitir o cadastro. Pois dessa forma o Aluguel em Dobro não será aplicado no Contrato de Locação;
    - Esse anexo só pode ser alterado em Contratos de Locação que estejam na situação "Em Preparação";
* **Forma de cobrança do aluguel em dobro:** *Geração não agregada:* **(quando marcada)** permite ao usuário parametrizar o "Aluguel em Dobro" para gerar um **lançamento separado** ao invés de um **valor de integração**.   
  Se o checkbox não estiver marcado, o sistema continuará a gerar o valor de integração, conforme a parametrização anterior.
* **Lançamentos de Repasse:** É possível efetuar o repasse financeiro para a imobiliária considerando o aluguel em dobro em casos onde existe um contrato de administração para um imóvel que será utilizado em um contrato de locação.

## **Alternativas Disponíveis para esta tela:**

---

* Possibilidade de cadastrar mais de uma competência por contrato de locação;
* O valor do Aluguel em Dobro será gerado em um Valor de Integração, que no RM pode ser visualizado através da edição do Lançamento da parcela correspondente ao mês de competência. *(quando o parâmetro Geração não agregada) estiver desmarcado (Obs: Exceto em lançamentos de repasse).*
* Para a parametrização do Aluguel em Dobro, além deste anexo, é necessário inserir o valor de Integração nos Parâmetros do TOTVS Incorporação. Para saber mais .
* Quando o aluguel em dobro é considerado somente no CTO, o cálculo de faturamento de uma competência também irá valer-se deste valor em dobro para compor o cálculo.

## **Geração não agregada (Disponível a partir da versão 12.1.2502)**

---

Com a opção de geração não agregada, o sistema gerará lançamentos separados de aluguel em dobro, durante o processo de geração de lançamentos.

Esta separação além de permitir um controle mais detalhado de cada parcela gerada em dobro, permite que sejam utilizados parâmetros financeiros distintos, possibilitando então realizar rateios de centro de custo / naturezas orçamentárias financeiras diferentes do lançamento original.

Todos os lançamentos em dobro gerados dessa forma, passam a compor um novo evento financeiro que abriga todos os registros gerados pelo processo.

* É importante notar que apesar do cadastro ser flexível, não deve ser utilizado gerações hibridas, ou seja, em determinada competência não agregada e em outra competência, agregada. Recomendamos que siga o mesmo padrão para todas as competências onde deve incidir cobrança em dobro.
* A geração não agregada também está disponível para o CTO, se comportando da mesma maneira do que o dobro do aluguel.
* No processo de cancelamento de lançamento financeiros, além da exclusão das parcelas do contrato de locação, o sistema irá automaticamente também excluir as parcelas do evento financeiro gerado para o processo de aluguel em dobro, desde que estejam dentro do período escolhido para cancelamento.
* Não será possível cancelar através do processo quando um dos lançamentos (Origem ou Em Dobro) esteja com o status igual a "Baixado" ou "Baixado Parcialmente". O cancelamento é sempre feito para as duas parcelas. Caso uma destas esteja, por algum motivo, bloqueada o sistema não prosseguirá com o cancelamento.
* As parcelas da cobrança agregada em dobro, podem ser acessadas no anexo de parcelas do contrato de aluguel.

**Obs: Com a reforma tributária**, passamos a gerar no lançamento financeiro, os tributos IBS e CBS com base de cálculo, alíquota e valor, de acordo com a regra tributária informada no contrato de locação.: Para maiores informações acesse: [Geração de lançamento financeiros - Locação, Aluguel Complementar e Aluguel em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1024340646)

Veja Também

---
