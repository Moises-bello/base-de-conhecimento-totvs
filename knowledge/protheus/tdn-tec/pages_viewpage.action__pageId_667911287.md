---
content_hash: e61be770d9ee65f75f291aeaa5cc994cf327e61598553cdf37b1ae47d1bdcda8
fetched_at: '2026-07-02T19:24:27.672518+00:00'
page_id: '667911287'
product: protheus
source: tdn-tec
title: Correção - Captura de dominio/subdominio com a utilização de ponto - 20
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=667911287
version: 1
---

Correção para capturar dominio/subdominio

|  |  |
| --- | --- |
| Situação | Função para captura do dominio/subdominio esta cortando e trazendo informações incompletas |
| Ocorrência | Ao realizar autenticação por AD, a captura do dominio/subdominio esta sendo cortado |
| Correção | Foi feito ajuste na função que chama a api do windows para capturar o dominio corretamente |
| Informações adicionais | * Referente ao chamado: [#13143819](https://totvssuporte.zendesk.com/agent/tickets/13143819 "Visualizar o Ticket no portal do Zendesk") * Referente à ocorrência: [DTCLIENT01-3158](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-3158) * Disponível em builds superiores ou igual a 20.3.0.1 e 19.3.1.8 |
