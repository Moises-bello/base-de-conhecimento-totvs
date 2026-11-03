---
content_hash: 535a531a67e0ed9a9d15364b10b8f1188121c10fd637714e64021a767e32fd03
fetched_at: '2026-07-02T19:24:22.193498+00:00'
page_id: '269060113'
product: protheus
source: tdn-tec
title: Alteração do comportamento do método IsConnected
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269060113
version: 2
---

O comportamento do método IsConnected da classe tSocketConnClass retornada pela função GetTCPObj

|  |  |
| --- | --- |
| Situação | Quando o método IsConnected era chamado após o encerramento (close) do socket era gerado um erro no Aplication Server. |
| Ocorrência | Erro no Aplication Server após a execução do método IsConnected. |
| Correção | Quando o método IsConnected é chamado será exibido uma mensagem de warning e retornado falso (.F.). |
| Informações adicionais | * Disponível em builds superiores a 7.00.131227A - NG 2.0.9 |
