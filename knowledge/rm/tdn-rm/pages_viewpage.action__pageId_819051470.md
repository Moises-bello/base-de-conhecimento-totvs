---
content_hash: 43bf08e0783ef9e4adb0725175d216c9cf7d8bebdec23fdbde8c8e969d5a1c87
fetched_at: '2026-06-29T00:11:45.021068+00:00'
page_id: '819051470'
product: rm
source: tdn-rm
title: FOPTRP0011 - Relatório de Aviso Prévio Trabalhado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819051470
version: 6
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório de Aviso Prévio Trabalhado**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2402 e Superiores

## **02. VISÃO GERAL**

Relatório para emitir os dados de Aviso Prévio Trabalhado  
  
Nesse relatório, temos os seguintes campos disponíveis:

* **Chapa**
* **Nome do Funcionário**
* **Código da Coligada**
* **Seção**
* **Nome da Seção**
* **Código da Filial**
* **Estabelecimento**
* **Cidade da Filial**
* **Data do aviso prévio indenizado**
* **Data do aviso prévio trabalhado**
* **Data atual**

A visualização do relatório será de acordo com o filtro inserido via visão de dados do Smart View, sendo esse filtro incluído pelo usuário.Vale ressaltar que há a necessidade da utilização dos filtros padrões já aplicados ao relatório, são eles: **Data do aviso prévio trabalhado não é nulo** / **Data do aviso prévio trabalhado entre dataInicioAviso e dataTerminoAviso**

## **03.** **EXEMPLO DE UTILIZAÇÃO OBJETO DE NEGOCIO (VISAO DE DADOS)**

No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o Objeto de negócio do Aviso Prévio **( TOTVS Folha de Pagamento - RM | Aviso Prévio)**  
Após a confirmação, será necessário preencher os parâmetros obrigatórios, que são:

* **Chapa do Funcionario**
* **Cód. Coligada**
* **dtFimAvisoMaior  >=**
* **dtFimAvisoMenor <=**

DICA

* Caso queira retornar todos os valores, basta incluir -1 nos parâmetros **(No caso dos filtros de data não é possível a filtragem utilizando o -1)**

Para melhor visualização e ramificação dos dados, é possível também incluir **filtros**na nossa busca, tornando a mais dinâmica possível.  Para isso, basta incluir os filtros clicando em **Alterar filtro** através da **Edição de Filtro.**

## **04. RELATÓRIO DE AVISO PRÉVIO TRABALHADO**

Para a execução do relatório, deveremos preencher necessariamente os parâmetros obrigatórios, vale lembrar que o relatório leva em consideração os filtros pré-definidos no passo do Objeto de Negócio.  
  
Então, após o preenchimento, o relatório será exibido conforme abaixo:

## **05. TABELAS UTILIZADAS**

* **PFUNC**
* **PSECAO**
* **GFILIAL**
