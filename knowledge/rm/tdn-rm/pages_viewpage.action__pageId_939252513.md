---
content_hash: 43e1189a1416679cfd264c8dd79f9288f19019631cbb5ffdbf6a2fdd737814f3
fetched_at: '2026-06-29T00:12:09.107333+00:00'
page_id: '939252513'
product: rm
source: tdn-rm
title: DT - Integração RM X Afferolab - API retorna a lista do líderes diretos dos
  Subordinados ter filtro de data -  HIERARQUIA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=939252513
version: 9
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Integração RM X Aferrolab - API retorna a lista do líderes diretos dos Subordinados ter filtro de data |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-15184](https://jiraproducao.totvs.com.br/browse/DRHHCM-15184) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.267
* 12.1.2410.220
* 12.1.2502.135 e superiores

## **03. SITUAÇÃO/REQUISITO**

Disponibilizar na API que retorna a lista dos líderes direto dos Subordinados a possibilidade para inserir um filtro de data para base de dados parametrizada para utilização da hierarquia por posição.

## **04. SOLUÇÃO**

Foi ajustada a API **EmployeesManagerDataContent** para retornar apenas os chefes cujo campo `RECCREATEDON` seja maior ou igual à data fornecida na requisição.

Isso garantirá que sejam retornados todos os chefes cadastrados a partir da data informada. A busca será realizada com base na data de criação registrada na tabela.

A API receberá os seguintes *query params*:

| Query Param | Descrição | Obrigatório | Tipo |
| --- | --- | --- | --- |
| companyId | Código do grupo de empresas para filtro | Sim | String |
| branchId | Código da filial do empregado para filtro | Sim | String |
| page | Página que está sendo requisitada | Não | Integer |
| pageSize | Quantidade de registros por página | Não | Integer |
| employeeCode | Código da matrícula do empregado para filtro | Não | String |
| employeeCostCenterCode | Código do centro de custo do(s) empregado(s) para filtro | Não | String |
| managerCreationStartDate | Data início de pesquisa conforme a vinculação do chefe na estrutura | Sim | string formato (aaaa-mm-dd) |
| managerCreationEndDate | Data fim de pesquisa conforme a vinculação do chefe na estrutura | Sim | string formato (aaaa-mm-dd) |

A API retornará as seguintes propriedades:

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| hasNext | Indica se há registros na próxima página | Boolean |
| total | Indica o total de registros retornados | Integer |
| items | Lista dos líderes direto dos empregados | Array |

Contém as seguintes propriedades:

| Propriedade | Descrição | Tipo | Origem do valor |
| --- | --- | --- | --- |
| managerBranch | Filial do líder | String | PSECAO.CODFILIAL |
| managerCode | Matrícula do líder | String | VSUBSTITUICAO.CODEXTERNO, VSUBSTITUICAO.CHAPASUBSTITUTO, VSUBSTITUICAO.IDHIERARQUIASUBSTITUTA, VHIERARQUIACOLIGADAEXTERNA.CODEXTERNO, VHIERARQUIACOLIGADAEXTERNA.CHAPAFUNC, VPOSICAO.CHAPAFUNCIONARIO |
| managerName | Nome do líder | String | PPESSOA.NOME |
| managerFullName | Nome completo do líder | String | PPESSOA.NOME |
| managerEmail | E-mail do líder | String | PPESSOA.EMAIL |
| managerDepartmentCode | Código do departamento do líder | String | PSECAO.CODSECAO, PEXTERNO.CODSECAO |
| managerDepartmentDescription | Descrição do departamento do líder | String | PSECAO.DESCRICAO |
| managerCostCenterCode | Código do centro de custo do líder | String | PCCUSTO.CODIGO |
| managerCostCenterDescription | Descrição do centro de custo do líder | String | PFUNC.CODCCUSTO |
| managerExternal | É externo? | bool | VHIERARQUIACOLIGADAEXTERNA, VSUBSTITUICAO.CODEXTERNO |
| employeeBranch | Filial do empregado | String | PFUNC.CODFILIAL |
| employeeCode | Matrícula do empregado | String | PFUNC.CHAPA |
| employeeName | Nome do empregado | String | PPESSOA.NOME |
| employeeFullName | Nome completo do empregado | String | PPESSOA.NOME |

Situações de erros tratados:

| Código do status | Mensagem | Solução |
| --- | --- | --- |
| 400 | O parâmetro companyId é obrigatório. | Preencher o parâmetro companyId. |
| 400 | O parâmetro branchId é obrigatório. | Preencher o parâmetro branchId. |

Situações de erros inesperados:

| Código do status | Mensagem |
| --- | --- |
| 500 | Ocorreu uma falha no retorno da informação. |

## **05. DEMAIS INFORMAÇÕES**

[Exemplo de configuração do REST](https://tdn.totvs.com/pages/viewpage.action?pageId=435098014).
