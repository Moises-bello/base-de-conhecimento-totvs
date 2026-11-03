---
content_hash: 28d7db0d91d3559874729c91168bfd7132764de15408df0b70f28ff32456df7d
fetched_at: '2026-06-29T00:11:39.019444+00:00'
page_id: '786553670'
product: rm
source: tdn-rm
title: Valor Dedução do Rendimento Tributável no Cadastro de Dependentes - Alterações
  no cálculo para atender ao leiaute S-1.2 que irá substituir a DIRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=786553670
version: 18
---

**CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **O que é necessário**
4. **Exemplo de utilização**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2302.144
* 12.1.2306.140
* e Superiores

Alteração posterior de comportamento conforme Documento Técnico - [DT - eSocial: Envio de dedução de Dependentes](https://tdn.totvs.com/pages/viewpage.action?pageId=1068186521)

## **02. VISÃO GERAL**

Pensando no envio das informações dos valores dedutíveis do rendimento tributável no evento S-1210, criamos uma nova tabela para armazenar esses dados. 

Será discriminado mensalmente os dados do dependente que foram utilizados no cálculo do Imposto de Renda Retido na Fonte (IRRF), incluindo o valor utilizado para a dedução.

No momento do cálculo de folha, férias e 13º salário quando o dependente incidir em IRRF, dentro das condições legais, os valores serão inseridos neste anexo.

## **03. O QUE É NECESSÁRIO**

Atualização da base de dados para que seja criada a tabela PFDEPIRRFDED. E para que possamos utilizar essa nova funcionalidade, se faz necessário a inclusão da permissão de acesso a menus nos perfis de segurança. 

Podemos visualizar esse dados através da nova tela “Valor Dedução do Rendimento Tributável”, que encontra-se nos anexos do cadastro de dependentes. Para a criação da tabela acima é necessárioexecutar o script através do sistema **RM.Atualizador.exe**

## **04. EXEMPLO DE UTILIZAÇÃO**

Quando utilizarmos códigos de cálculos que carreguem formulas em sua composição, será necessário a inclusão **manual** do tipo de rendimento. Isso se deve ao fato de que não é possível a identificação do valor dedutível utilizado na fórmula.  
Para isso podemos utilizar a funcionalidade de inserção manual da tela de Valor dedução do rendimento tributável, como no exemplo abaixo:

Incluir, Campos da telapasso1,passo2yespasso1

Funcionalidade para incluir novos dados na tabela

nopasso2

Preencher os campos obrigatórios da tela.

Regras para inclusão

1. Não será possível a inclusão de registros em anos e meses competências onde não existem registros de Ficha Financeira.
2. Quando utilizar o Tipo de Movimento 3- Férias, é necessário o preenchimento dos campos **Dt. Vencimento Férias** e **Data Pagto. Férias**

Além da inclusão manual de valores através da funcionalidade mencionada acima, essa nova tela e tabela receberá valores da **Folha de Pagamento, Calculo de Férias, Rescisão e 13º Salário.**

Folha de Pagamento, Calculo de Férias, Rescisão, 13º Saláriopasso1,passo5,passo3,passo4yespasso1

Log de Calculo do Envelope de Pagamento de um funcionário com 2 dependentes que incidem IRRF. Neste caso será armazenado valores em ambos os cadastros de dependentes.

Registro em tela do dependente numero 1.

nopasso5

Log de Calculo do IRRF de Férias, onde o funcionário tem apenas 1 dependente que incide o IRRF.   
  
  
  
Registro em tela do dependente numero 1, que incide o IRRF.

Regras do Calculo de Férias

**Para o calculo das férias, o vínculo dos valores dedutíveis dos dependentes com o recibo de férias são as datas de vencimento e data de pagamento das férias. Então, caso esse o recibo seja calculado e após o calculo tenha a sua data de pagamento alterada, os valores dedutíveis ficarão duplicados na tabela. Neste caso, a exclusão deverá ocorrer manualmente.**

nopasso3

Log de Calculo da Rescisão de apenas 1 funcionário que tem 1 dependente incidente de IRRF. 

Registro em tela do dependente 1, neste caso os eventos de 13º salário e Férias rescisão incidiram o IRRF.

nopasso4

Log de Calculo do 13º Salario, onde o funcionário tem 2 dependentes que incidem o IRRF.  
  
  
  
  
Registro em tela do funcionário 1, com o registro de 13º Salário .

**Atenção:**

1-Na utilização dos eventos de IRRF: **Código de Calculo 84 - IRRF CALCULADO PELO USUARIO,** **Código de Calculo 106 - IRRF 13º CALCULADO PELO USUARIO** e **Código de Calculo 107 - IRRF FERIAS CALCULADO PELO USUARIO**, também deverá preencher o registro manualmente.

2 - No caso de múltiplos vínculos, cada vínculo recalcula toda a base de IRRF onde os dependentes são os mesmos para todos os vínculos da mesma pessoa, independente de qual chapa que esteja cadastrado. Na gravação dos valores dedutíveis na tabela PFDEPIRRFDED os dados serão armazenados na chapa do último vínculo calculado. No eSocial sempre é unificado pelo código da pessoa.

* Para identificar que o dependente é o mesmo, será verificado a junção de 3 campos:
  + CPF + Data de Nascimento + Grau de Parentesco. Caso não informe o CPF do dependente será considerado Data de Nascimento + Grau de parentesco.
  + Se os dependentes possuir a mesma data de nascimento, ou seja, forem gêmeos, obrigatoriamente deverá informar o CPF distinto para os dependentes para que o Cálculo reconheça os mesmos como dependentes distintos.
* Quando um dos envelopes dos vínculos for cancelado ou excluído o evento que incide em IRRF, então será excluída a linha na tabela PFDEPIRRFDED porque no caso de múltiplos vínculos tem que recalcular todos para ficar correto. Recalculando o vínculo que ainda tem evento que incide em IRRF então os dados serão gravados novamente.

## **05. TABELAS UTILIZADAS**

* PFDEPEND
* PFUNC
* PFPERFF
* PFDEPIRRFDED
