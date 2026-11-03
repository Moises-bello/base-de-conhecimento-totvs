---
content_hash: de3be20bd635acdb18602228180dd630f90d6f21a9b3e90fd4b3f16df588e316
fetched_at: '2026-07-02T19:24:21.452419+00:00'
page_id: '267796520'
product: protheus
source: tdn-tec
title: Correção - Falha na conexão via broker.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267796520
version: 1
---

Ocorria falha na conexão do SmartClient via broker.

|  |  |
| --- | --- |
| Situação | Ao utilizar a tela de Parâmetros Iniciais do SmartClient e escolher uma seção de conexão do broker, a conexão não era realizada. |
| Ocorrência | Não era possível fazer uma conexão do SmartClient ao Application Server via broker iniciada através da tela de Parâmetros Iniciais do SmartClient. A conexão ocorria com sucesso somente através do SmartClient via Parâmetros de Linha. |
| Correção | A conexão do SmartClient ao Application Server via broker através da tela de Parâmetros Iniciais foi corrigida. |
| Informações adicionais | * Referente à ocorrência: TEC-7481 * Disponível a partir da build 7.00.131227A-20161017. |
