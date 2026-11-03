---
content_hash: 5daf706a93d78bba522de67419f2d5abc6caed67df71ca69be52ad18b7cbb7b6
fetched_at: '2026-06-29T00:11:55.672560+00:00'
page_id: '862613353'
product: rm
source: tdn-rm
title: 'DT - API Global de Funcionários - Campos: CPF, Seção/Descrição e Código/Descrição
  da categoria do eSocial'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862613353
version: 6
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | API Global de Funcionários |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-12974](https://jiraproducao.totvs.com.br/browse/DRHHCM-12974)  [DRHHCM-13424](https://jiraproducao.totvs.com.br/browse/DRHHCM-13424) |

## **02. LIBERAÇÃO**

Disponível a partir dos patches:

* 12.1.2310.256
* 12.1.2402.226
* 12.1.2406.154 e superiores

## **03. SITUAÇÃO/REQUISITO**

Alterar a API Global de Funcionários ([employeeDataContent](https://api.totvs.com.br/apidetails/EmployeeDataContent_v1_000.json)) para que retorne as informações de CPF, Seção e sua descrição, Código da categoria do eSocial e sua descrição.

## **04. SOLUÇÃO**

Foi alterada a API [employeeDataContent](https://api.totvs.com.br/apidetails/EmployeeDataContent_v1_000.json) para que retorne as informações de CPF, Seção e sua descrição, Código da categoria do eSocial e sua descrição.

Abaixo a identificação das novas propriedades:

| Propriedade | Descrição | Tipo | Origem do valor |
| --- | --- | --- | --- |
| employeeCpf | CPF | String | PPESSOA.CPF |
| sectionCode | Seção | String | PFUNC.CODSECAO |
| sectionDescription | Descrição da Seção | String | PSECAO.DESCRICAO |
| esocialCategoryCode | Código da categoria do eSocial | Int | PFUNC.CODCATEGORIAESOCIAL |
| esocialCategoryDescription | Descrição da categoria do eSocial | String | PESOCIALCATTRAB.DESCRICAO |

## **05. DEMAIS INFORMAÇÕES**

[Exemplo de configuração do REST](https://tdn.totvs.com/pages/viewpage.action?pageId=435098014).
