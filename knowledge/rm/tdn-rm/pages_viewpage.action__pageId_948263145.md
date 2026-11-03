---
content_hash: f1c20306df34615641a44140a83b64e3e8c47b862b3b382e5514c2a8a33a476d
fetched_at: '2026-06-29T00:12:09.599167+00:00'
page_id: '948263145'
product: rm
source: tdn-rm
title: FOPTRP0018 - Relação de Saldo Devedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=948263145
version: 10
---

## **CONTEÚDO**

1. 1. **Versão**
   2. **Visão Geral**
   3. **Exemplo de utilização**
   4. **Tela Visão de Dados/Relatório**
      1. **Principais Campos e Parâmetros**
   5. **Tabelas utilizadas**

   ## **01. VERSÃO**

   O Recurso estará disponível a partir das versões abaixo:

   * 12.1.2410.237
   * 12.1.2502.149
   * 12.1.2506 e superiores

   ## **02. VISÃO GERAL**

   O objeto de negócio e relatório de Relação de Saldo Devedor têm como objetivo entregar para o usuário os valores armazenados na movimentação de empréstimos.

   Tanto a geração do relatório quanto a visão de dados podem ser feitas utilizando parâmetros pré-definidos, como **coligada, chapa, seção e modalidade do empréstimo.**

   Abaixo os campos disponíveis no objeto de negócio e as regras de como os dados são obtidos.

   | Nome | Descrição | Campo na Tabela do RM |
   | --- | --- | --- |
   | Nome da Coligada | String | GCOLIGADA.NOMEFANTASIA |
   | Código da Coligada | String | PFEMPRT.CODCOLIGADA |
   | Estabelecimento | String | GFILIAL.NOMEFANTASIA |
   | Código da Filial | String | PFUNC.CODFILIAL |
   | Matricula | String | PFEMPRT.CHAPA |
   | Matricula eSocial | String | PFUNC.MATRICULAESOCIAL |
   | Nome da pessoa colaboradora | String | PFUNC.NOME |
   | Código da Seção | String | PSECAO.CODIGO |
   | Nome da Seção | String | PSECAO.DESCRICAO |
   | Função | String | PFUNCAO.NOME |
   | Código do Empréstimo | String | PFEMPRT.CODIGO |
   | Data do Empréstimo | DateTime | PFEMPRT.DTEMPRESTIMO |
   | Valor Original | Decimal | PFEMPRT.VALORORIGINAL |
   | Saldo devedor | Decimal | PFEMPRT.SALDODEVEDOR |
   | Início do desconto | DateTime | PFEMPRT.INICIODESCONTO |
   | Tipo de Empréstimo | String | PFEMPRT.TIPOEMPRESTIMO |
   | Código do Banco | String | PFEMPRT.MATINSTCONS |
   | Contrato | String | PFEMPRT.NUMCONTEMPCONS |
   | Modalidade do Empréstimo | String | PFEMPRT.EMPCONSGARANTFGTS |
   | Valor da Parcela descontada | Decimal | PFDESCEMPRT.VALOR **(Valor Pago)** |
   | Insuficiência de saldo | Decimal | PFDESCEMPRT.INSUFSALDO |
   | Mês desconto | String | PFDESCEMPRT.MESCOMP |
   | Ano desconto | String | PFDESCEMPRT.ANOCOMP |
   | Período do desconto | String | PFDESCEMPRT.NROPERIODO |
   | N° Parcelas Pagas | Int | PFDESCEMPRT.NROPARCLANCADAS |
   | Valor Parcela | Decimal | **Somatório do valor da parcela + insuficiência do saldo (Campo calculado pelo sistema)** |

   **Dica**

   Nem todos os campos do objeto de negócios serão utilizados ou visualizados no relatório disponibilizado pela TOTVS. Alguns campos servirão para parâmetros/filtros. Outros foram disponibilizados para facilitar para o usuário caso o mesmo queira customizar algum relatório com estes dados sem a necessidade de customizar por fórmulas por exemplo.

   ## **03. EXEMPLO DE UTILIZAÇÃO**

   Visão de Dados

   Visão de dados utilizando o Objeto de Negócios disponibilizado que retorna os dados da relação do Saldo Devedor dos empréstimos

   Relatório de Empréstimos

   Gerando o relatório utilizando o SmartView:

## **04. TELA VISÃO DE DADOS/RELATÓRIO**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Cód. Coligada | Neste campo deverá informar uma ou mais coligadas, clicando em + e adicionando o código da coligada que deseja informar. Caso o usuário queira gerar para todas as coligadas, deverá informar -1 |
| Chapa do Funcionário | Neste campo deverá informar uma ou mais chapas de funcionários, clicando em + e adicionando as chapas que deseja retornar os dados referente a provisão. Caso o usuário queira gerar para todas as chapas, deverá informar -1 |
| Cód. Seção | Neste campo deverá informar uma ou mais seção, clicando em + e adicionando as seções que deseja retornar. É possível utilizar este campo para retornar as seções a partir de uma quebra, informando por exemplo 01., onde irá retornar todas as seções a partir desta quebra. Caso o usuário queira gerar para todas as chapas, deverá informar -1 |
| Modalidade do Empréstimo | Neste campo deverá informar qual o tipo de empréstimo |

## **05. TABELAS UTILIZADAS**

* GCOLIGADA
* GFILIAL
* PFUNC
* PSECAO
* PFEMPRT
* PFDESCEMPRT
