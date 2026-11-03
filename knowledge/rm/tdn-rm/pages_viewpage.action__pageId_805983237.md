---
content_hash: 9c343242ff6490085e0b6a49befb1be36b2f0b9396eba21e06016478325bc053
fetched_at: '2026-06-29T00:11:43.405384+00:00'
page_id: '805983237'
product: rm
source: tdn-rm
title: FOPTRP0009 - Relatório Líquido Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=805983237
version: 10
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório Líquido Salarial**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2402 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir os dados do Líquido Salarial

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

* **Cód. Coligada**
* **Chapa do Funcionário**
* **Nome**
* **Função do Funcionário**
* **Função**
* **Seção**
* **Nome da Seção**
* **Nro da Conta Bancária**
* **Valor Liquido Salarial**
* **Cód. do Banco**
* **Nome do Banco**
* **Cód. Agencia**
* **Nome da Agencia**
* **Nro do Período**
* **Mov. Importação**
* **Mês Competência**
* **Ano Competência**
* **Data Pagamento**
* **Cód. Centro de Custo**
* **Total Banco**
* **Total Geral**
* **Total Filial**
* **Quant. Funcionários**
* **Funcionários por Banco**

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário.

## **03. EXEMPLO DE UTILIZAÇÃO OBJETO DE NEGOCIO (VISAO DE DADOS)**

No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o Objeto de negócio do Líquido Salarial **(TOTVS Folha de Pagamento - RM | Líquido Salarial)**

Após a confirmação, será necessário preencher os parâmetros obrigatórios, que são:

* **Cód. Coligada**
* **Chapa do Funcionário**
* **Cód. Seção** (Este parâmetro utiliza o Like como operador em sua busca, então podemos digitar os primeiros digitos de um código de seção e retornar todos os valores proximos a ele, exemplo: Se digitarmos 01.0 irá retornar todos as seções que **comecem** com 01.0, exemplo 01.04 / 01.0 / 01.02 )
* **Cód. Do Banco**
* **Nro do Período**
* **Mov. Importação**
* **Mês Comp**
* **Ano Comp**
* **Data Pagamento**
* **Cód. Centro de Custo** (Este parâmetro utiliza o Like como operador em sua busca, então podemos digitar os primeiros digitos de um código de centro de custo e retornar todos os valores proximos a ele, exemplo: Se digitarmos 01.0 irá retornar todos os cc que **comecem** com 01.0, exemplo 01.04 / 01.0 / 01.02 )

DICA

* Caso queira retornar todos os valores, basta incluir -1 nos Parâmetros

Para melhor visualização e ramificação dos dados, é possível também incluir Filtros na nossa busca, tornando a mais dinâmica possível.  Para isso basta incluir os filtros clicando em **Alterar filtro** através da **Edição de Filtro.**

Após acessarmos a funcionalidade de filtros, podemos customizar da melhor maneira para atender nosso objetivo. Sendo permitido a inclusão de um ou mais filtros, podendo escolher os filtros disponíveis bem como na imagem abaixo.

## **04. RELATÓRIO DO LÍQUIDO SALARIAL**

Para a execução do relatório deveremos preencher necessariamente os parâmetros obrigatórios, vale lembrar que o relatório leva em consideração os filtros pré-definidos no passo do Objeto de Negócio.  
  
Então, após o preenchimento o relatório será exibido conforme abaixo:

## **05. TABELAS UTILIZADAS**

* PFUNC
* PFUNCAO
* PSECAO
* PFPERFF
* PCCUSTO
* GAGENCIA
* GBANCO
* GFILIAL
* PFFINANC
