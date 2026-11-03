---
content_hash: 0b6e6588f3343f8f3645dd9102d1c3e48281745b54800e53539a8a26d323b4c5
fetched_at: '2026-06-29T00:11:50.296239+00:00'
page_id: '840373035'
product: rm
source: tdn-rm
title: FOPTRP0014 - Relatório Escala de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=840373035
version: 4
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório Escala de Férias**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2406 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir os dados da Escala de Férias

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

* **Código da Filial**
* **Nome da Filial**
* **Código do Centro de Custo**
* **Nome do Centro de Custo**
* **Chapa**
* **Nome do Funcionário**
* **Data de Admissão**
* **Codigo da Seção**
* **Data de Início do Período Aquisitivo**
* **Data Fim do Período Aquisitivo**
* **Data Início de Gozo de Férias**
* **Data Fim de Gozo de Férias**
* **Periodo Aberto**
* **Status das Férias**
* **Numero de Dias de Férias**
* **Numero de Dias de Abono**
* **1ª Parcela do 13º Salário**
* **Código da Coligada**
* **Data limite de Gozo**
* **Numero de dias de direito**
* **Saldo de Férias**
* **Férias em Dobro**
* **Numero de dias de falta**

A visualização do relatório será conforme o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário.

## **03. EXEMPLO DE UTILIZAÇÃO OBJETO DE NEGOCIO (VISAO DE DADOS)**

 No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o objeto de negócio da Escala de Férias **(TOTVS Folha de Pagamento - RM | Escala de Férias).**

Após a confirmação, será necessário preencher os parâmetros obrigatórios, que são:

* **Código da Coligada** (Poderá ser utilizado N Coligadas, basta clicar no icone de adição )
* **Chapa do Funcionário** (Poderá ser utilizado N Chapa de Funcionarios, basta clicar no icone de adição )
* **Filial** (Poderá ser utilizado N Filiais de Funcionarios, basta clicar no icone de adição )
* **Cod. Seção** (Pode ser utilizado como "Similaridade" Exemplo: Cód. Seção 02 Deverá ser retornado funcionarios da Seção 01.02 / 02 / 02.01 / 03.02 / 04.02 )
* **Data Início Periodo Aquisitivo >=**
* **Data Início Periodo Aquisitivo <=**
* **Data Início de Gozo >=**
* **Data Início de Gozo <=**
* **Situação de Férias**

DICA

* Caso queira retornar todos os valores, basta incluir -1 nos Parâmetros

Para melhor visualização e ramificação dos dados, é possível também incluir filtros na nossa busca, tornando a mais dinâmica possível.  Para isso, basta incluir os filtros clicando em **Alterar filtro** através da **Edição de Filtro.**

Após acessarmos a funcionalidade de filtros, podemos customizar da melhor maneira para atender nosso objetivo. Sendo permitido a inclusão de um ou mais filtros, podendo escolher os filtros disponíveis, bem como na imagem abaixo.

## **04. RELATÓRIO ESCALA DE FÉRIAS**

Para a execução do relatório, deveremos preencher necessariamente os parâmetros obrigatórios. Vale lembrar que o relatório leva em consideração os filtros pré-definidos no passo do Objeto de Negócio.

Então, após o preenchimento, o relatório será exibido conforme abaixo:

Vale lembrar

 Esse relatório tem uma particularidade. Pensando justamente no melhor controle gerencial, pensamos em "alertar" o usuário que está emitindo o relatório sobre funcionários que estão passíveis de férias em dobro ou até 3 meses antes que chegue a esta situação.  
Como no exemplo acima, temos alguns funcionários em **Preto e Vermelho.**A cor **Preta** simboliza que o funcionário ainda não está com férias em dobro ou já teve seu período de gozo marcado, não restando saldo.  
  
A cor **Vermelho** simboliza que o funcionário está com a situação de férias em dobro ou está há 3 meses de chegar a este status, tornando-o passível de receber o pagamento de suas férias em dobro.

## **05. TABELAS UTILIZADAS**

* **PFUNC**
* **GFILIAL**
* **PSECAO**
* **PCCUSTO**
* **PFUFERIAS**
* **PFUFERIASPER**
* **PFUFERIASRECIBO**
* **PFUFERIASVERBAS**
