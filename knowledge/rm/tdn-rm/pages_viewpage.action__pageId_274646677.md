---
content_hash: 9a46ba4c1619cbaf37da9e415a77eceb6c1467286c6daad62275332955538a41
fetched_at: '2026-06-29T00:08:34.106307+00:00'
page_id: '274646677'
product: rm
source: tdn-rm
title: Interpretação de Incidentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274646677
version: 105
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

Com o cadastro de um incidente com as informações de linha de produtos, aplicação, versão, mensagem e stacktrace, o software deve extrair informações de modulo afetado e tipo de erro.

Para a identificação podem ser utilizados modelos especialistas para cada linha de produto, aplicação e versão do software monitorado.

O incidente cadastrado pode ter diferentes formatos de stacktrace, como um erro de consulta ao banco de dados ou um stacktrace.

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Snowden | **Módulo** | service |
| **Segmento Executor** |  | | |
| **Projeto1** | [FRW\_FRW004](http://jiraproducao.totvs.com.br/browse/FRW_FRW004) | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | 1. [FRW\_FRW004-40](http://jiraproducao.totvs.com.br/browse/FRW_FRW004-40 "Algoritmo de identificação do módulo") | **Subtarefa1** | 1. [FRW\_FRW004-41](http://jiraproducao.totvs.com.br/browse/FRW_FRW004-41) |
| **País** | Brasil | | |

### Objetivo

Construção de um interpretador de erros que seja capaz de identificar o tipo do erro e o modulo do software afetado, sendo capaz de criar fluxos para identificação diferentes para cada linha de produtos totvs.

### Definição da Regra de Negócio

 

Para que seja possível realizar a identificação, um objeto com a interface IIncident deve ser utilizada no objeto de parsing.

A escolha padrão para estrategia de identificação do incidente é por Database caso seja encontrados elementos SQL no stracktrace ou message, caso contrario é a estrategia de Parsing do StrackTrace.

A escolha pela especialização de um driver é feito pela implementação das interfaces: IProductExpertDriver, sendo que deve ser implementado também o modelo de driver para a estrategia especifica sendo elas: IStackTraceDriver, IDatabaseDriver ou IDriverStrategy.

Em caso de falhas de um driver especialista, outro deve ser escolhido para realizar a tarefa, sendo este outro especialista de menor nível ou o padrão

### Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
