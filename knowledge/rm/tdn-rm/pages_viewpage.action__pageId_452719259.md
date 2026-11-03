---
content_hash: 4c89f6b46866bc5792ceda3b8e695b8bd50161a688f5d6d3d9f8e58c583e1daf
fetched_at: '2026-06-29T00:10:04.829786+00:00'
page_id: '452719259'
product: rm
source: tdn-rm
title: Movimentação dos Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719259
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Cadastro do Movimento do Convênio do Funcionário**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Registrar as compras e serviços utilizados pelos funcionários, em que algumas a empresa arca com um percentual podendo ser lançados em folha de pagamento de forma parcelada.

Com os parâmetros do convênio criados, vinculação dos convênios com seus serviços e valores, passará a ser possível criar movimentação para os funcionários, ou seja, realizar lançamento no sistema dos convênio utilizados pelos funcionários e os valores gastos.

## **02. EXEMPLO DE UTILIZAÇÃO**

11Informando campos manualmente

Supondo um cadastro de parâmetros do convênio conforme abaixo:

Inserindo valores:

Dica

Veja o número de parcela pode ser informado dentro do limite que está informado na parametrização do convênio.

A data do movimento está dentro do período cadastrado anteriormente e essa data cadastrada na base exemplo coincide com a competência.

Após salvar será apresentado na visão do cadastro do movimento sendo apresentado também o anexo das parcelas do movimento.

Dica

Esse cadastro também pode ser preenchido pela [Importação da Movimentação de Convênios](https://tdn.totvs.com/pages/viewpage.action?pageId=822226192).

2Utilização da tabela de cálculo

A seguir será apresentado um exemplo de cálculo das **parcelas** de acordo com a tabela de cálculo vinculada.

Para o cálculo iremos considerar a tabela abaixo cadastrada previamente no Cadastro de Tabelas de Cálculo:

| **Nº Faixa** | **Limite Superior** | **Val****or à Acrescentar** |
| --- | --- | --- |
| 1 | 832,00 | 71,00 |
| 2 | 1055,00 | 105,00 |
| 3 | 1644,00 | 165,00 |
| 4 | 2115,00 | 232,00 |
| 5 | 3172,00 | 350,00 |
| 6 | 4228,00 | 464,00 |
| 7 | 5645,00 | 620,00 |
| 8 | 999999,99 | 1000,00 |

Será considerado também um funcionário com salário de R$ 832,00, sendo assim, o valor máximo que poderá ser descontado do funcionário será de R$ 71,00 por mês (vide tabela), independentemente da quantidade de convênios.   
Obs.: Considere os campos “Limite Superior” e “Valor à Acrescentar” como “Salário do funcionário” e “Valor máximo para desconto da parcela”.

Vinculados a este funcionário, temos os seguintes convênios e valores:

| **Convênio** | **Data** | **Valor total** | **Parte empresa** | **Parte funcionário** |
| --- | --- | --- | --- | --- |
| Odontológico - Obturação | 05/2021 | 300,00 | 180,00 | 120,00 |
| Odontológico - Extração | 05/2021 | 220,00 | 132,00 | 88,00 |
| Odontológico - Canal | 05/2021 | 400,00 | 240,00 | 160,00 |

Tendo ciência da tabela acima, os valores a descontar do funcionário (Parte funcionário) será divido de acordo com a tabela abaixo. Lembre-se que o valor limite a ser descontado por mês (Competência) será de R$ 71,00.

| **Convênio** | 05/2021 | 06/2021 | 07/2021 | 08/2021 | 09/2021 | 10/2021 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Odontológico - Obturação | R$ 71,00 | R$ 49,00 | - | - | - | - | R$ 120,00 |
| Odontológico - Extração | - | R$ 22,00 | R$ 66,00 | - | - | - | R$ 88,00 |
| Odontológico - Canal | - | - | R$ 5,00 | R$ 71,00 | R$ 71,00 | R$ 13,00 | R$ 160,00 |
| Total | R$ 71,00 | R$ 71,00 | R$ 71,00 | R$ 71,00 | R$ 71,00 | R$ 13,00 | - |

## **03.** **TELA Cadastro do Movimento do Convênio do Funcionário**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Data do lançamento | Preenchida por default no caso de digitação manual |
| Data do movimento | Data em que ocorreu a movimentação |
| Chapa do funcionário | Chapa do funcionário que irá usufruir do convênio |
| Código do serviço do convênio | Informar um dos serviços disponíveis, o mesmo será liberado automaticamente ao preencher os itens anteriores. Sendo que para o campo Código do serviço do convênio será listado apenas os serviços que foram adicionados conforme **Parâmetros do Convênio.** |
| Código do convênio | Será informado automaticamente de acordo com o convênio vinculado ao serviço selecionado |
| Código do fornecedor | Informar código do fornecedor |
| Número da NF | Informar o número da NF |
| Valor da compra | Informar o valor da compra ou do serviço usado |
| Nº parcelas | Informar o número de parcelas, sendo:   01 - Condicionado ao 'Nº limite de parcelas' quando a forma de pagamento for 'Parcelamento fixo'   02 - Não será habilitado caso forma de parcelamento no parâmetro do convênio for 'Utilizar tabela de cálculo' |
| Parte do funcionário | será calculada automaticamente |
| Parte da empresa | será calculada automaticamente, com base no parâmetro pelo campo  '% Empresa' |
| Observação |  |

## **04. TABELAS UTILIZADAS**

* PFMOVCONVENIO
