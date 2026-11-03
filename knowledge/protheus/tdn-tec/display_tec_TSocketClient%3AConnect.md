---
content_hash: e33def7baaa21ea8c26eaee9455f35b70379d9943daeb70f0e3aa0b3c8608570
fetched_at: '2026-07-02T19:24:18.635405+00:00'
page_id: '219121391'
product: protheus
source: tdn-tec
title: TSocketClient:Connect
type: documentation
url: https://tdn.totvs.com/display/tec/TSocketClient%3AConnect
version: 3
---

TSocketClient:Connect

Estabelece uma conexão TCP genérica (socket).

## Sintaxe

false, < cAddress >, < nTimeout > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nPort | numérico | Indica o número da porta onde a conexão será realizada. | X |  |
| cAddress | caractere | Indica o número IP ou nome do servidor onde a conexão será realizada. | X |  |
| nTimeout | numérico | Indica o número em milissegundos onde o método deve esperar para conectar. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Retorna 0 (zero) se conectar com sucesso; caso contrário, a conexão falhou. |

## Detalhes de Retorno

| Status | Descrição |
| --- | --- |
| 0 | Sucesso |
| 1 | Erro de conexão |
| 5 | Timeout da conexão |
| 16 | Socket aberto/em uso |
| 17 | Criação do socket falhou |
| 19 | Conexão falhou |
| 100 | Endereço inválido |
