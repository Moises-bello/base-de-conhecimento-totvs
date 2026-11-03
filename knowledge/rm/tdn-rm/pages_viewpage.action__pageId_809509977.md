---
content_hash: 056bb7b31b2155b35c2936f2f347a1a91769bacbc3bc54f474b0a89ca408b91a
fetched_at: '2026-06-29T00:11:44.034373+00:00'
page_id: '809509977'
product: rm
source: tdn-rm
title: FOPTRP0010 - Relatório Líquido de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=809509977
version: 5
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório Líquido de Férias**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2402 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir os dados relacionado ao Líquido de Férias

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

* **Matrícula**: Retorna a chapa do funcionário
* **Nome do Funcionario:**Retorna o nome do Funcionario referente a Chapa
* **Data Pagamento Férias:**Retorna a data de pagamento das férias
* **Banco:**Retorna o nome do banco
* **Agencia:**Retorna o numero da  Agencia
* **Número da Conta:**Retorna o numero da conta de pagamento
* **Líquido de Férias:** Retorna o líquido de férias que foi pago
* **Total Geral**: Retorna uma soma geral dos líquidos de férias

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

## **03. EXEMPLO DE UTILIZAÇÃO OBJETO DE NEGOCIO (VISAO DE DADOS)**

No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o Objeto de negócio da Líquido de Férias **( TOTVS Folha de Pagamento - RM | Líquido de Férias )**

Após a confirmação, será necessário preencher os parametros obrigatórios, que são:

* **Cód. Coligada**
* **Chapa do Funcionario**
* **Data de Ínicio das Férias**
* **Cód. do Banco**
* **Data de Pagamento das Férias  ( >= e <= , caso preencha apenas uma data entenderá como = )**

DICA

* Caso queira retornar todos os valores, basta incluir -1 nos Parametros

Para melhor visualização e ramificação dos dados, é possível também incluir Filtros na nossa busca, tornando a mais dinamica possível.  Para isso basta incluir os filtros cliclando em **Alterar filtro** através da **Edição de Filtro.**

Após acessarmos a funcionalidade de filtros, podemos customizar da melhor maneira para atender nosso objetivo. Sendo permitido a inclusão de um ou mais filtros, podendo escolher os filtros disponíveis bem como na imagem abaixo.

       

## **04. RELATÓRIO DO LÍQUIDO DE FÉRIAS**

Para a execução do relatório deveremos preencher necessáriamente os parametros obrigatórios, vale lembrar que o relatório leva em consideração os filtros pré-definidos no passo do Objeto de Negócio.  
  
Então, após o preenchimento o relatório será exibido conforme abaixo:

Podemos então apartir desse relatório gerado, realizar a exportação para os tipos de extensões suportadas pela ferramenta.  
  
Abaixo podemos ver uma impressão no modelo PDF:

## **05. TABELAS UTILIZADAS**

* PFUNC
* GCOLIGADA
* PFUFERIAS
* PFUFERIASPER
* PFUFERIASRECIBO
* GAGENCIA
* GBANCO
* PFUFERIASVERBAS
* PSECAO
