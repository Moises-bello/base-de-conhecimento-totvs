---
content_hash: 2b412a8c9c39ed0c93f5ff5080defb018021a5ecba3f8f32e7a479b2292f5719
fetched_at: '2026-06-29T00:11:54.879719+00:00'
page_id: '859060885'
product: rm
source: tdn-rm
title: DT - Integração RM X Quírons - API retorna a lista do líderes diretos dos Subordinados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859060885
version: 24
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Quírons - API retorna a lista do líderes diretos dos Subordinados |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10231](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10231) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.195
* 12.1.2406.122 e superiores

## **03. SITUAÇÃO/REQUISITO**

Disponibilizar uma API que retorne a lista dos líderes direto dos Subordinados.

## **04. SOLUÇÃO**

Foi criada uma API  **EmployeesManagerDataContent** que retorna a lista dos líderes direto dos Subordinados, similar à API "employeeDataContent", que fornece a lista de empregados.

A API receberá os seguintes *query params*:

| Query Param | Descrição | Obrigatório | Tipo |
| --- | --- | --- | --- |
| companyId | Código do grupo de empresas para filtro | Sim | String |
| branchId | Código da filial do empregado para filtro | Sim | String |
| page | Página que está sendo requisitada | Não | Integer |
| pageSize | Quantidade de registros por página | Não | Integer |
| employeeCode | Código da matrícula do empregado para filtro | Não | String |
| employeeCostCenterCode | Código do centro de custo do(s) empregado(s) para filtro | Não | String |

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
| managerCode | Matrícula do líder | String | PSUBSTCHEFE.CHAPASUBST, PSUBSTSUP.CHAPASUBST, PCHEFEEXTERNO.CODEXTERNO, PSUPERVEXTERNO.CODEXTERNO |
| managerName | Nome do líder | String | PPESSOA.NOME |
| managerFullName | Nome completo do líder | String | PPESSOA.NOME |
| managerEmail | E-mail do líder | String | PPESSOA.EMAIL |
| managerDepartmentCode | Código do departamento do líder | String | PSECAO.CODSECAO |
| managerDepartmentDescription | Descrição do departamento do líder | String | PSECAO.DESCRICAO |
| managerCostCenterCode | Código do centro de custo do líder | String | PCCUSTO.CODIGO |
| managerCostCenterDescription | Descrição do centro de custo do líder | String | PFUNC.CODCCUSTO |
| managerExternal | É externo? | bool | PCHEFEEXTERNO, PSUPERVEXTERNO |
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
