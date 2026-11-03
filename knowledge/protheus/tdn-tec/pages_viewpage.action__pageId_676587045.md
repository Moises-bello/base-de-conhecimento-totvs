---
content_hash: 816f77ca1e444ae9f39ad33bc257c26b838cebb1a0b7d086e25b37358491f307
fetched_at: '2026-07-02T19:24:27.695171+00:00'
page_id: '676587045'
product: protheus
source: tdn-tec
title: Correção - Função GetUserFromSID trazendo nome de dominio invalido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676587045
version: 1
---

Criação de um parametro para permitir incluir a palavra ".local" ou não na execução da função GetUserFromSID para capturar o dominio

|  |  |
| --- | --- |
| Situação | Quando executa a função GetUserFromSID com a finalidade de capturar o dominio |
| Ocorrência | Foi feito um ajuste para pegar o dominio completo no passado e causou um efeito colateral trazendo o texto ".local" |
| Correção | Foi criado um novo parametro opcional na chamada da função que permite a retirada ou não do texto ".local" ao buscar o dominio |
| Informações adicionais | * Referente ao chamado: [#13690116](https://totvssuporte.zendesk.com/agent/tickets/13690116 "Visualizar o Ticket no portal do Zendesk") * Referente à ocorrência: [DTCLIENT01-3275](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-3275) * Disponível em builds iguais ou superiores a 20.3.0.3 no SmartClient e 20.3.0.9 no AppServer |
