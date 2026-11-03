---
content_hash: 1f7b7e6a5061de2cbe079866b6ecb29c08d67f69f38e9b48f892d4e290d45af7
fetched_at: '2026-06-29T00:05:47.264716+00:00'
page_id: '1008704337'
product: rm
source: tdn-rm
title: DT - Integração Folha x Afferolab - Implementar filtro de Cargo, Departamento
  e Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1008704337
version: 11
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração Folha x Afferolab - Implementar filtro de Cargo, Departamento e Centro de Custo |
| País: | Brasil |
| Issue: | [DRHROTRM-14184](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14184 "View this issue") | [DRHROTRM-15797](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15797) |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.232
* 12.1.2506.181
* 12.1.2510.115 e superiores

## **03. SITUAÇÃO/REQUISITO**

Disponibilizar filtros por departamento, cargo e centro de custo na API de integração entre a Folha de Pagamento e LMS+LXP by Afferolab permitindo o controle de quais funcionário devem ser integrados.

**04. SOLUÇÃO**

Foi implementada na API **EmployeeDataContentController** a opção de filtrar por departamento, cargo e/ou centro de custo do funcionário.

**A API receberá os seguintes *query params*:**

| Query Param | Descrição | Obrigatório | Tipo |
| --- | --- | --- | --- |
| departmentCode | Departamento do funcionário (PFUNC.CODSECAO => PSECAO.CODDEPARTAMENTO) | Não | String |
| employeePositionCode | Cargo do funcionário (PFUNC.CODFUNCAO => PCARGO.CODIGO) | Não | String |
| costCenterCode | Centro de custo (PFUNC.NROCENCUSTOCONT=> PSECAO.NROCENCUSTOCONT) | Não | String |

**A API retornará as seguintes propriedades:**

| Propriedade | Descrição | Tipo |
| --- | --- | --- |
| hasNext | Indica se há registros na próxima página | Boolean |
| total | Indica o total de registros retornados | Integer |
| items | Lista dos líderes direto dos empregados | Array |

As propriedades do json podem ser encontradas  no link [API](https://api.totvs.com.br/apidetails/EmployeeDataContent_v1_000.json).

**Situações de erros tratados:**

| Código do status | Mensagem | Solução |
| --- | --- | --- |
| 400 | O parâmetro product é obrigatório. | Preencher o parâmetro product. |
| 400 | O parâmetro companyId é obrigatório. | Preencher o parâmetro companyId. |

**Situações de erros inesperados:**

| Código do status | Mensagem |
| --- | --- |
| 500 | Ocorreu uma falha no retorno da informação. |

**Múltiplos Filtros**

É possível realizar filtros múltiplos na API via oData, combinando várias condições com os operadores lógicos.

**Por exemplo:** {{baseURL}} /api/rh/v1/employeeDataContent?product=RM&companyId=1&$filter=( (roleCode eq '00017') and (sectionCode eq '02.01' or sectionCode eq '01.08') )

Esse filtro retorna os funcionários da função **00017** que estão alocados nas seções **02.01** ou **01.08**. Todos os critérios devem ser combinados em um único `$filter` para evitar erros de sintaxe.

**Exemplo – Postman**

250

## **05. DEMAIS INFORMAÇÕES**

* [Exemplo de configuração do REST](https://tdn.totvs.com/pages/viewpage.action?pageId=435098014).
