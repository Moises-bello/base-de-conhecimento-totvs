---
content_hash: 0be6666d77375c8a24f9a246624bede11f7476332e831d3ebdf7144b0ecb3dcf
fetched_at: '2026-07-02T19:24:22.254937+00:00'
page_id: '269085606'
product: protheus
source: tdn-tec
title: REST - Mensagem Invalid IsConnected
type: documentation
url: https://tdn.totvs.com/display/tec/REST+-+Mensagem+Invalid+IsConnected
version: 1
---

Método IsConnected lançava exceção quando o socket estava fechado.

|  |  |
| --- | --- |
| Situação | Na chamada do método IsConnected, caso o socket estivesse fechado era gerado um erro. |
| Ocorrência | Não era possível verificar a existência do socket. |
| Correção | Alteração no método IsConnected da classe tSocketConnClass não gerar erro quando o socket está fechado. |
| Informações adicionais | * Referente à ocorrência: TTEC-1007 * Disponível em builds superiores a 7.00.131227a - 1.3.1 |
