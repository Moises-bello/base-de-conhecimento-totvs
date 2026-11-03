---
content_hash: fcc6be3c8bef3356273abb1a5a0d7096835bd3313cca31c74c1aedb940565012
fetched_at: '2026-06-29T00:11:05.054471+00:00'
page_id: '628111098'
product: rm
source: tdn-rm
title: Retornar o total de SobreAviso por nome
type: documentation
url: https://tdn.totvs.com/display/LRM/Retornar+o+total+de+SobreAviso+por+nome
version: 1
---

Este serviço é utilizado para retornar o total de sobre aviso de um funcionário do time com filtro por nome do funcionário.

GET - /team/onCallTotalizer/{coordinatorId}

Exemplo:

<http://localhost/MeuRH/rm/api/rest/team/onCallTotalizer/1%7C00047?initDate=01%2F01%2F2021&endDate=07%2F06%2F2021&name=HORARIO%20FLEXIVEL%20COM%20SOBREAVISO&requesterName=RODRIGO%20FIALHO%20BARRICHELLO&status=pending&page=200&pageSize=40>

| Parâmetro | Descrição do Parâmetro |
| --- | --- |
| coordinatorID | Coligada e chapa do gestor Exemplo: 1%7C00047 (coligada 1 e chapa 00047) |
| initDate | string($date-time) data início do período da pesquisa |
| endDate | string($date-time) data de término do período da pesquisa |
| name | Nome do funcionário |
| requesterName | Nome do solicitante |
| status | Status da Solicitação |
| page | Número da página que está sendo carregada |
| pageSize | Quantidade de registros da página requisitada |
