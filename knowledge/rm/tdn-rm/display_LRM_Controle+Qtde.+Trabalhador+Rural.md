---
content_hash: 6bb38b14ef8531ad73179fa953b0065fabc26e47aada18d173f767e7b7e93516
fetched_at: '2026-06-29T00:11:17.425863+00:00'
page_id: '680239835'
product: rm
source: tdn-rm
title: Controle Qtde. Trabalhador Rural
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+Qtde.+Trabalhador+Rural
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Controle de Quantidade Trabalhador Rural**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Relatório com o objetivo de apresentar o total de trabalhadores alocados nas seções de acordo com o período informado observando as datas de admissão, demissão, transferência, atestados e afastamentos e considerando o período informado. Relatório por seção.

Seleciona os filtros de funcionários por seção ou seleção de funcionários.

A Data Inicio Safra será utilizada para filtrar os funcionários da coluna do relatório Efetivos.

Seleciona o Período que o relatório será emitido.

O relatório “FOPREL00195 - Folha Agrária - Controle de Qtde de Trabalhador Rural” deve ser importado em Gestão /  RM Reports para ser selecionado no Código do Relatório.

No Relatório será listado as seguintes colunas:

**Efetivos** - São os funcionários ativos na seção em que a admissão ou transferência se deu até a data final do período solicitado ou estando demitido, a demissão ocorreu na data do início da safra ou posterior.

**Ativos** - Total de funcionários na seção que tiveram produção (tabela de produção PPRODUCAOAGRARIA) na data final do período informado para o relatório e que o evento na linha de produção NÃO seja igual evento de CAT ou Código de evento de atestado.

As colunas abaixo deverão levar em consideração as regras explicitadas no item “Ativos” além das condições particulares de cada coluna.

**Admitidos** - Total de funcionários que tiveram sua admissão ou transferência na seção no período na data inicial e final informado.

**Demitidos** - Número de demitidos na seção dentro do período, data inicial e final, informado para a geração do relatório.

**Homem** - Total de funcionários ativos do sexo masculino em que:

1. Estando demitido, a demissão ocorreu após a data final do período informado para o relatório inclusive;
2. Não esteja afastado na data final do período informado para o relatório;
3. Data de admissão ou transferência E, T seja anterior à data final do período informado inclusive.

**Mulher** - Total de funcionários ativos do sexo feminino em que:

1. Estando demitido, a demissão ocorreu após a data final do período informado para o relatório inclusive;
2. Não esteja afastado na data final do período informado para o relatório;
3. Data de admissão ou transferência E, T seja anterior à data final do período informado inclusive.

**Afastados** - Total de funcionários na seção em que a situação não seja demitido E esteja afastado na data final do período informado para o relatório.

**Férias** - Total de funcionários na seção em que a situação não seja demitido E a data final do período informado esteja entre o período de férias programado/gozada.

**Total geral** - Calculado com base no somatório de Homens, Mulheres, Afastados e Férias;

* Totalizador geral

Para cada coluna de valores existirá um totalizador que deverá proceder conforme regra informada em cada campo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi acessado o menu Folha Agrária / Produção / Controle Qtde Trabalhador Rural e a base exemplo existem vários casos parametrizados.

Na tela de parâmetros foi parametrizado da seguinte forma:

Depois de executado apresenta o relatório no seguinte modelo:

## **03.****TELA: Controle de Quantidade Trabalhador Rural**

**Principais Campos e Parâmetros**

| Ação | Descrição |
| --- | --- |
| Quebra de seção | Seleciona a seção |
| Seleção de Funcionários | Seleciona os funcionários |
| Data Inicio Safra | Utilizada para filtrar os funcionários da coluna do relatório Efetivos |
| Período | Seleciona o Período que o relatório será emitido. |
| Código do relatório | O relatório “FOPREL00195 - Folha Agrária - Controle de Qtde de Trabalhador Rural” deve ser importado em Gestão /  RM Reports para ser selecionado no Código do Relatório. |

## **04. TABELAS UTILIZADAS**

* PFUNC
* PFHSTAFT
* PFHSTSIT
* PPESSOA
* PPRODUCAOAGRARIA
* PSECAO
