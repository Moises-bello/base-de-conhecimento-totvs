---
content_hash: 61fec0218cbcb0eaf84d33d2b4bb066abe921a5a48afd543f7b64fa3a8d6883c
fetched_at: '2026-06-29T00:11:20.736512+00:00'
page_id: '687754768'
product: rm
source: tdn-rm
title: Relatório de Distribuição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687754768
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Distribuição**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O relatório tem o objetivo de apresentar o rateio de INSS de acordo com os programas da produção. Serão apresentados os valores de INSS (percentual aplicado ao total de INSS usando o percentual de produção) de acordo com os dias trabalhados dos funcionários em cada programa filtrado por eventos de produção selecionados pelo usuário.

As informações serão agrupadas e totalizadas por centros de custos e programas e os valores de INSS serão recuperados dos funcionários com base na competência (mês/ano) informada pelo usuário e todos os registros estarão restritos ao período de datas a serem informados pelo usuário.

Selecionar os filtros de funcionários por seção ou seleção de funcionários.

Selecionar o período que o relatório será emitido, informando a data de início e fim do período.

Selecionar a competência para INSS, informando Mês e Ano para que o relatório seja emitido.

Deverá ser informado/selecionado o código do relatório “**FOPREL00198 - Folha Agrária - Distribuição**”.

**Observação:** Este relatório deverá ser importado em **Gestão** | **RM Reports**.

Informar os eventos a serem considerados na coluna Ganho Total para que seja calculado o percentual na emissão do relatório.

No Relatório serão listadas as seguintes colunas:

**Centro de custo** - Serão listados os centros de custo vinculados ao programa recuperado através do programa e as informações constantes na tabela de programas. Os programas serão filtrados de acordo com os eventos selecionados nos parâmetros e filtros na geração do relatório.

1. Caso o usuário não selecione nenhum evento na interface de parâmetros/filtros, serão listados TODOS os programas constantes na produção para o período informado.

**Programa** - Serão listados os campos código e descrição dos programas recuperados através do programa e as informações constantes na tabela de programas. Os programas serão filtrados de acordo com os eventos selecionados nos parâmetros e filtros na geração do relatório.

1. Caso o usuário não selecione nenhum evento na interface de parâmetros/filtros, serão listados TODOS os programas constantes na produção para o período informado.

**Perc** - Serão listados os percentuais calculados de acordo com o total de INSS do programa que representa em relação ao total de INSS da seção, considerando os valores de INSS (coluna BASE INSS) e apresentando o percentual calculado.

**Base INSS** -Serão listados os percentuais dos funcionários nos programas, considerando o cálculo da base de INSS do programa, levando em consideração os dias trabalhados no programa com relação aos dias trabalhados independente do programa por funcionário da tabela de produção. Será considerado o valor de base de INSS do funcionário de acordo com a competência informada.

**Base INSS Fer** -Serão listados os percentuais dos funcionários nos programas, considerando o cálculo da base de INSS Férias do programa, levando em consideração os dias de férias no programa com relação aos dias férias independente do programa por funcionário da tabela de produção. Será considerado o valor de base de INSS Férias do funcionário de acordo com a competência informada.

**Valor produção** -Será listado o somatório do valor da produção (campo VALOR GANHO) no período informado para os eventos selecionados por programa.

**Total geral** - Serão listados totalizadores para as colunas código e nome de seção, percentual (totalizando em 100%), Soma Base INSS, Soma Base INSS Ferias, Soma Valor Produção e Total.

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi acessado o menu Folha Agrária | Produção | Distribuição e na base criado um exemplo onde existem casos parametrizados.

Na tela de parâmetros foi parametrizado da seguinte forma:

Depois de executado, será apresentado o relatório no seguinte modelo:

## **03.****TELA: Distribuição**

**Principais Campos e Parâmetros**

| Ação | Descrição |
| --- | --- |
| Quebra de seção | Seleciona a seção |
| Seleção de Funcionários | Seleciona os funcionários |
| Período | Seleciona o Período que o relatório será emitido |
| Competência para INSS - Mês | Informar Mês da competência de INSS que deseja emitir o relatório |
| Competência para INSS - Ano | Informar Ano da competência de INSS que deseja emitir o relatório |
| Código do Relatório | O relatório “**FOPREL00198 - Folha Agrária - Distribuição**” deve ser importado em Gestão /  RM Reports para ser selecionado no Código do Relatório. |

## **04. TABELAS UTILIZADAS**

* PFUNC
* PFPERFF
* PFFINANC
* PEVENTO
* PPRODUCAOAGRARIA
* PSECAO
* PRGRCALCTAREFAAGRARIA
* PFUFERIASPER
* PFUFERIASRECIBO
