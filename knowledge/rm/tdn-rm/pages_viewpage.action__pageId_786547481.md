---
content_hash: fe5cb44e4911246cf1847f24f436bfe224c4ddd7d4cb3d929a8c6d167c923d9b
fetched_at: '2026-06-29T00:11:38.994584+00:00'
page_id: '786547481'
product: rm
source: tdn-rm
title: FOPTRP0001 - Relatório Aviso de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=786547481
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

Relatório para emitir aviso de férias dos funcionários, exceto para férias nas situações G - Aguardando aprovação do Gestor e D - Aguardando aprovação do DP.

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

* **Chapa**: Retorna a chapa do funcionário, mesmo não sendo exibido no relatório, deve estar no objeto. PFUNC.CHAPA.
* **Estabelecimento:** Retorna o nome da Filial de Trabalho do Funcionário. Este campo será retornado da PFUNC.CODFILIAL fazendo JOIN com a GFILIAL.
* **Nome:** Retorna o nome do Funcionário. Informação da PFUNC.
* **Departamento:** Retorna a seção do cadastro de funcionários.
* **Data início do período aquisitivo:** Retorna a data PFUFERIAS.INICIOPERAQUIS.
* **Data Final do Período aquisitivo:** Retorna a data PFUFERIAS.FIMPERAQUIS.
* **Data inicio de Gozo:** Retorna  a data PFUFERIASPER.DATAINICIO.
* **Data Fim de Gozo:** Retorna a data PFUFERIASPER.DATAFIM.
* **Data de retorno do trabalho:** Retorna o próximo dia útil do funcionário após a informação do campo PFUFERIASPER.DATAFIM.
* **Data de pagamento:** Retorna a data de pagamento do campo PFUFERIASPER.DATAPAGTO.
* **Data de Aviso:** Retorna a data do campo PFUFERIASPER.DATAAVISO.
* **Situação Férias** - Retorna a data do campo PFUFERIASPER.SITUACAOFERIAS.

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

O único filtro que estará disponível dentro desse relatório será o código da coligada, sendo obrigatório a informação para que seja impresso o relatório. Caso seja informado -1 no filtro serão visualizados os relatórios de todas as coligadas.

**Exemplo de filtro:**

Emitir aviso de férias dentro de um período de datas.

No Smart View cadastre o filtro:

DICAS

01 - Utilize os campos relacionados nos objetos de negócios para criar filtros.

02 - Para filtrar somente férias marcadas crie o filtro Situação Férias igual a M.

03 - Utilize a informação dentro do filtro para ser apresentada no momento de passar os dados. Como no exemplo abaixo foi informado 

* 1DTAVDE = 1 - Data Aviso De
* 2DTAVATE = 2 - Data Aviso Até

**Observação:** Adicione os números para ordenar no momento de mostrar os parâmetros e não utilize acentos.

Quando for executar o relatório, seja na MDI ou no Smart View informe as datas solicitadas:

 

IMPORTANTE

A partir da versão 12.1.2402, será incluido novos parametros em nossa busca, são eles:

* **Chapa do Funcionário**
* **Data Início das Férias >=**
* **Data Início das Férias <=**
* **Cod. Seção**

## **03. EXEMPLO DE UTILIZAÇÃO**

Dados fictícios da base exemplo

Funcionário 00001 com os seguintes dados de férias:

Relatório FOPTRP0001 - Aviso de Férias importado em Gestão / Smart View 

Marcar o relatório e acessar Anexo / Execução de Recurso do Smart View

Como foi criado o filtro no exemplo anterior, foram informadas as datas do aviso correspondente ao período das férias de 01/09/2023 que no caso deve ser assinada até 02/08/2023.

**Observação:** O filtro do código da coligada é obrigatório.

Após clicar em enviar será apresentado o relatório:

DICA

* Clicando no ícone do filtro o relatório é apresentado em tela inteira.
* Nos ícones acima do relatório permitem salvar, imprimir, dentre outros serviços disponíveis.

## **04. RELATÓRIO AVISO DE FÉRIAS**

Relatório gerado conforme exemplo acima:

## **05. TABELAS UTILIZADAS**

* GFILIAL
* GDEPTO
* PSECAO
* PFUNC
* PFUFERIAS
* PFUFERIASPER
