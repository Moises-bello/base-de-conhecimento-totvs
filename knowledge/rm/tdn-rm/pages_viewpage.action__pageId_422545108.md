---
content_hash: a49a5551518ad70fa5fdf6d87dae83f368535ae78c80d211641d9adb8ac3e398
fetched_at: '2026-06-29T00:09:19.474965+00:00'
page_id: '422545108'
product: rm
source: tdn-rm
title: DEDUANALYTICS-607 Fast Analytics - Parametrização de Agrupamento de Períodos
  Letivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545108
version: 2
---

# Parametrização de Período Letivo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional (Fast Analytics). |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parametrização de Período Letivo. | N/A. | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | Sql Server e Oracle |
| **Tabelas Utilizadas:** | HCPARAMETROS  EDUKPI\_PLETIVOEDUCACIONAL |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | N/A |

## Descrição

Criado a parâmetro "Utilizar agrupamento de períodos letivos" no parametrizador de períodos letivos (RM Integração | Parâmetros | Gerais | Agrupamentos).

Esse parâmetro deve ser marcado quando for necessário trabalhar com os agrupamentos criados no "TOTVS Educacional | Integrações | Cadastro de Agrupamentos" e não apenas com os períodos letivos de forma individual. Dessa forma, o filtro de período letivo irá exibir o agrupamento, evitando assim a duplicidade de informações que ocorre quando existem períodos letivos semelhantes em coligadas diferentes.
