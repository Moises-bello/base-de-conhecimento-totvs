---
content_hash: 779650a242d248047f8020a4f4dcbc5dc90d6d3be78783db7c6245ead42be314
fetched_at: '2026-06-29T00:11:45.027868+00:00'
page_id: '819051520'
product: rm
source: tdn-rm
title: FOPTRP0012 - Relatório de Solicitação de Abono Pecuniário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819051520
version: 10
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório Abono de Férias**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2402 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir os dados do Abono de Férias

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

* **Municipio da Filial**
* **Nome do Funcionario**
* **Departamento do Funcionário**
* **Data inicial do período aquisitivo**
* **Data final do período aquisitivo**
* **Data de início das férias**
* **Data de fim das férias**
* **Data de Retorno Das Férias**
* **Data de pagamento da férias**
* **Data do aviso de férias**
* **Nome da Filial**
* **Código da Coligada**
* **Chapa do Funcionário**
* **Código do Seção (Departamento)**
* **Código da Filial**
* **Situação das férias**
* **Quantidade Dias de Abono Concedidos**

A visualização do relatório será exibido de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

## **03. EXEMPLO DE UTILIZAÇÃO OBJETO DE NEGOCIO (VISAO DE DADOS)**

No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o Objeto de negócio do Aviso de Férias **( TOTVS Folha de Pagamento - RM | Aviso de Férias )**

Após a confirmação, será necessário preencher os parâmetros obrigatórios, que são:

* **Código da Coligada**(Poderá ser utilizado N Coligadas, basta clicar no ícone de adição )
* **Chapa do Funcionário**(Poderá ser utilizado N Chapa de Funcionários, basta clicar no ícone de adição )
* **Data Início das Férias >=** (Será utilizado o operador >= para filtragem das datas)
* **Data Início das Férias <=** (Será utilizado o operador <= para filtragem das datas)
* **Cod. Seção**(Pode ser utilizado como "Similaridade" Exemplo: Cód. Seção 02 Deverá ser retornado funcionários da Seção 01.02 / 02 / 02.01 / 03.02 / 04.02 )

  DICA
  + Caso queira retornar todos os valores, basta incluir -1 nos parâmetros

  Para melhor visualização e ramificação dos dados, é possível também incluir filtros na nossa busca, tornando a mais dinâmica possível. Para isso, basta incluir os filtros clicando em **Alterar filtro** através da **Edição de Filtro.**  
    
  Após acessarmos a funcionalidade de filtros, podemos customizar da melhor maneira para atender nosso objetivo. Sendo permitido a inclusão de um ou mais filtros, podendo escolher os filtros disponíveis, bem como na imagem abaixo.

## **04. RELATÓRIO ABONO DE FÉRIAS**

Para a execução do relatório, deveremos preencher necessariamente os parâmetros obrigatórios. Vale lembrar que o relatório leva em consideração os filtros pré-definidos no passo do Objeto de Negócio.  
  
Então, após o preenchimento, o relatório será exibido conforme abaixo:

## **05. TABELAS UTILIZADAS**

* GFILIAL
* PSECAO
* PFUNC
* PFUFERIAS
* PFUFERIASPER

##
