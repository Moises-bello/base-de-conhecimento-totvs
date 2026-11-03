---
content_hash: 6b76d2990d61657da6998151bf11895da952398ba8cab2871de38aa3214e649b
fetched_at: '2026-06-29T00:11:39.987175+00:00'
page_id: '793207485'
product: rm
source: tdn-rm
title: FOPTRP0004 - Relatório Aviso Prévio Indenizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=793207485
version: 8
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório Aviso de Férias**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2310 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir aviso indenizado dos funcionários que já tenham rescisão cadastrada e a data do aviso prévio indenizado esteja preenchido.

Nesse relatório temos os seguintes campos disponíveis:

* **Nome da Seção** - Retorna o Nome da Seção do Funcionário - PSECAO.DESCRICAO
* **Estabelecimento** - Retorna o nome Fantasia da Filial - GFILIAL.NOMEFANTASIA
* **Cidade da Filial** - Município da Filial - GFILIAL.CIDADE
* **Nome do Funcionário** - Retorna o nome do Funcionário - PFUNC.NOME
* **Data do aviso prévio indenizado** - Retorna a data do aviso prévio cadastrado - PFUNC.DTAVISOPREVIO
* **Data atual** - Data atual
* **Chapa do Funcionário** - Retorna a Chapa do Funcionário - PFUNC.CHAPA
* **Código da Seção** - Retorna o código da seção - PFUNC.CODSECAO
* **Código da Coligada** - Retorna o Código da Coligada - PFUNC.CODCOLIGADA
* **Código da Filial** - Retorna o código da Filial - PFUNC.CODFILIAL

A visualização do relatório será de acordo com o filtro inserido via visão de dados do Smart View, sendo esse filtro incluído pelo usuário.Vale ressaltar que há a necessidade da utilização dos filtros padrões já aplicados ao relatório, são eles: **Data do aviso prévio indenizado não é nulo** / **Data do aviso prévio indenizado entre dataInicioAviso e dataTerminoAviso**

## **03. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios da base exemplo

No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o Objeto de negócio do Aviso Prévio **( TOTVS Folha de Pagamento - RM | Aviso Prévio)**  
Após a confirmação, será necessário preencher os parâmetros obrigatórios, que são:

* **Chapa do Funcionario**
* **Cód. Coligada**
* **dataInicioAviso**
* **dataTerminoAviso**

DICA

* Caso queira retornar todos os valores, basta incluir -1 nos parâmetros **(No caso dos filtros de data não é possível a filtragem utilizando o -1)**

Para melhor visualização e ramificação dos dados, é possível também incluir **filtros**na nossa busca, tornando a mais dinâmica possível.  Para isso, basta incluir os filtros clicando em **Alterar filtro** através da **Edição de Filtro.**

## **04. RELATÓRIO AVISO INDENIZADO**

Relatório gerado após o envio dos parametros:

## **05. TABELAS UTILIZADAS**

* GFILIAL
* GDEPTO
* PSECAO
* PFUNC
* PFUFERIAS
* PFUFERIASPER
