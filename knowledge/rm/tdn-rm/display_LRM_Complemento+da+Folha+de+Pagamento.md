---
content_hash: b70161326efecbe208e52812b4eb22c14e3866a75291cefcd674d86f9c093656
fetched_at: '2026-06-29T00:11:55.573470+00:00'
page_id: '862119773'
product: rm
source: tdn-rm
title: Complemento da Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Complemento+da+Folha+de+Pagamento
version: 17
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Complemento da Folha de Pagamento**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

## **01. VERSÕES**

Versão do cálculo do "Complemento de folha de pagamento para recolhimento de FGTS retroativo" disponível a partir de:

* 12.1.2502.244
* 12.1.2506.196
* 12.1.2510.126
* 12.1.2602 e superiores

## **02. VISÃO GERAL**

Nesse processo será feito o  lançamento de Complemento da Folha de Pagamento conforme o [artigo nº 27 da Instrução Normativa 2110/2022](https://tdn.totvs.com/pages/releaseview.action?pageId=738253118#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosDiferen%C3%A7asSalariaisIN2110-3.4eSocial).

Para utilizar o processo é necessário fazer as seguintes configurações:

* Informar valor no parâmetro geral “Período Complemento Folha ” em “Configurações | Parametrizador | Folha Normal | Geral 2/2” que deve ser maior que 1000 e não pode ser igual a nenhum período do RRA seja Folha/Férias, 13o Salário ou Rescisão.
* Cadastrar em dados do dissídio apenas com o tipo de acordo "J - Parcelas complementares conhecidas após o fechamento da folha".

Na execução do processo, o usuário deverá:

* Informar a competência e o período que será complementada
* No lookup “Dados do dissídio/convenção/acordo coletivo” não será filtrado por código do tipo de acordo, ficando a critério do usuário a seleção correta para o preenchimento do campo "Código do acordo/ Dissídio" na pasta Verbas geradas por diferença da ficha financeira.
* O lançamento do envelope de pagamento será feito na competência atual e no período do campo “Período” no processo de  Complemento Folha de Pagamento. Caso o usuário queira poderá informar um período diferente de 1000 ou necessitar fazer mais de um complemento relacionado ao mesma competência complementada, deverá informar um novo período a ser lançado diferente do existente. Lembrando que este campo dever ser informado a partir de 1000.

Ao executar o processo, os valores serão lançados na Ficha financeira e também na PFVERBASDIS do mês, ano e período informados na Competência a ser complementada, para que seja enviado para o eSocial.

Dica

Para cancelar o período do complemento da folha de pagamento será necessário selecionar o período do complemento da folha previamente informado nos parâmetros locais e selecionar o mesmo no processo de cancelamento da folha. Ou então cancelar todos os períodos.

## **03.** **EXEMPLO DE UTILIZAÇÃO**

Lançamento do complemento

Lançamento da folha de pagamento em Janeiro

Lançamento da folha de pagamento em Fevereiro

Lançamento do complemento da folha de pagamento em Fevereiro referente ao mês de Janeiro

Lançamento do complemento da folha de pagamento em Fevereiro

Envio do XML para o e-Social

Utilizando a base fictícia do eSocial

PERÍODO 1 - Folha normal

PERÍODO 1000 - Complemento da Folha de Pagamento

Enviado para a base do Governo através do XML  - S1200

Retorno do Governo - Veja que somando os valores do INSS dos dois períodos temos o mesmo valor retornado pelo

176,56 + 30,68 = 207,24

Complemento de folha de pagamento para recolhimento de FGTS retroativo

Utilizando a base fictícia do eSocial

Histórico de afastamento cadastrado como P - pela previdência e alterado para T - Acidente de trabalho referente aos meses 08 e 09/2024

A competência atual da base de dados é 01/2025, então foi feito o complemento do FGTS com o código de cálculo 315 - BASE DE FGTS DE AFASTADOS

No envelope de pagamento foram lançados os períodos com os respectivos complementos

Na ficha financeira dos meses de complemento foram lançados os dados e valores nas verbas

No XML do S1200 foram discriminados os valores para envio

No XML do S5003 foram discriminados os valores retornados do RET

## **04. TELA****Complemento da Folha de Pagamento**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Informar a quebra da seção |
| Seleção de funcionários | Selecionar o(s) funcionário(s) |
| Competência a ser complementada | Informar mês, ano e período a que se refere o complemento da folha de pagamento |
| Dados do dissídio/convenção/acordo coletivo | Informar o código do tipo de acordo “J - Parcelas complementares conhecidas após o fechamento da folha" |

## **05. TABELAS UTILIZADAS**

* PFFINANC
* PFVERBASDIS
