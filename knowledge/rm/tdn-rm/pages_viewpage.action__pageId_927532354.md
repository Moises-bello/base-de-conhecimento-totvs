---
content_hash: 71b19a2e971b121da30adfe39d8383aa6a6a8a422a3c4c6d0b3a5e91da6b47f1
fetched_at: '2026-06-29T00:12:07.889146+00:00'
page_id: '927532354'
product: rm
source: tdn-rm
title: FOPTRP0017 - Relatório de Relação de Pensão Alimentícia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=927532354
version: 2
---

## **CONTEÚDO**

1. **Versão**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Visão de Dados/Relatório**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

## **01. VERSÃO**

O Recurso estará disponível a partir das versões abaixo:

* 12.1.2506.1

## **02. VISÃO GERAL**

O objeto de negócio e relatório de Relação de Pensão Alimentícia tem como objetivo entregar para o usuário os valores armazenados na movimentação da pensão alimenticia.

A geração do relatório assim como na visão de dados poderão ser feitas utilizando parâmetros pré-definidos, como coligada, chapa, seção, **mês**/**ano competência.**

Abaixo os campos disponíveis no objeto de negócios e as regras de como os dados são obtidos.

| Nome | Descrição | Campo na Tabela do RM |
| --- | --- | --- |
| Nome da Coligada | Retorna o nome fantasia da Coligada do funcionário | GCOLIGADA.NOMEFANTASIA |
| Código da Coligada | Retorna o código da coligada do funcionário. | PFDEPEND.CODCOLIGADA |
| Estabelecimento | Retorna o nome fantasia da filial do funcionário | GFILIAL.NOMEFANTASIA |
| Código da Filial | Retorna o código da filial do funcionário | PFUNC.CODFILIAL |
| Matricula | Retorna a chapa do funcionário | PFDEPEND.CHAPA |
| Nome da pessoa colaboradora | Retorna o nome do funcionário | PFUNC.NOME |
| Código da Seção | Retorna o código da seção | PSECAO.CODIGO |
| Nome da Seção | Retorna o nome da seção | PSECAO.DESCRICAO |
| Número do Dependente | Retorna o numero do dependente | PFDEPEND.NRODEPEND |
| Nome do Dependente | Retorna o nome do dependente | PFDEPEND.NOME |
| Data início de desconto | Retorna a data inicio do desconto da pensão | PFDEPEND.DATAINICIODESCPENSAO |
| Data Final do desconto | Retorna a data fim do desconto da pensão | PFDEPEND.DATAFIMDESCPENSAO |
| Nome do Responsável | Retorna o nome do responsável pelo dependente | PFDEPEND.RESPONSAVEL |
| Banco de Pagamento | Retorna o banco do pagamento da pensão | PFDEPEND.BANCO |
| Agência de Pagamento | Retorna o agencia de pagamento da pensão | PFDEPEND.AGENCIA |
| Conta Pagamento/Operação | Retorna a conta e operação do pagamento da pensão | PFDEPEND.CONTACORRENTE / PFDEPEND.OPBANCARIA |
| Mês de Referência | Retorna o mês da competência que será gerado retornado os dados. Este campo é obrigatório | PFDEPMOV.MESCOMP |
| Ano de Referência | Retorna o ano da competência que será gerado retornado os dados. Este campo é obrigatório | PFDEPMOV.ANOCOMP |
| Valor | Retorna o valor da pensão | PFDEPMOV.VALOR |
| Percentual de desconto | Retorna o percentual equivalente | PFDEPMOV.PERCENTUALPENSAO |

**Dica**

Nem todos os campos do objeto de negócios serão utilizados ou visualizados no relatório disponibilizado pela TOTVS. Alguns campos servirão para parâmetros/filtros. Outros foram disponibilizados para facilitar para o usuário caso o mesmo queira customizar algum relatório com estes dados sem a necessidade de customizar por fórmulas por exemplo.

## **03. EXEMPLO DE UTILIZAÇÃO**

Visão de dados

Visão de dados utilizando o Objeto de Negócios disponibilizado que retorna os dados da relação da pensão alimenticia

Relatório

Gerando o relatório utilizando o SmartView:

## 

## **04. TELA VISÃO DE DADOS/RELATÓRIO**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Cód. Coligada | Neste campo deverá informar uma ou mais coligadas, clicando em + e adicionando o código da coligada que deseja informar. Caso o usuário queira gerar para todas as coligadas, deverá informar -1 |
| Chapa do Funcionário | Neste campo deverá informar uma ou mais chapas de funcionários, clicando em + e adicionando as chapas que deseja retornar os dados referente a provisão. Caso o usuário queira gerar para todas as chapas, deverá informar -1 |
| Cód. Seção | Neste campo deverá informar uma ou mais seção, clicando em + e adicionando as seções que deseja retornar. É possível utilizar este campo para retornar as seções a partir de uma quebra, informando por exemplo 01., onde irá retornar todas as seções a partir desta quebra. Caso o usuário queira gerar para todas as chapas, deverá informar -1 |
| Mês | Neste campo deverá informar o mês da competência que deseja gerar os dados/relatório de provisão, sendo o mesmo obrigatório, não podendo informar mais de um mês competência e não é aceito informar -1 como os demais parâmetros |
| Ano | Neste campo deverá informar o ano da competência que deseja gerar os dados/relatório de provisão, sendo o mesmo obrigatório, não podendo informar mais de um ano competência e não é aceito informar -1 como os demais parâmetros |

## **05. TABELAS UTILIZADAS**

* PFDEPEND
* GCOLIGADA
* GFILIAL
* PFUNC
* PSECAO
* PFDEPMOV
