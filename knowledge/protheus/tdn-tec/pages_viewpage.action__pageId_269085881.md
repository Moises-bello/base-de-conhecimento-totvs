---
content_hash: 97a9a04eca0b560d844d2db82ca4569c1905ff47558b032335ce944622a1ca5f
fetched_at: '2026-07-02T19:24:22.301554+00:00'
page_id: '269085881'
product: protheus
source: tdn-tec
title: REST - Mensagem Invalid IsConnected.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269085881
version: 1
---

Método IsConnected lançava exceção quando o socket estava fechado.

|  |  |
| --- | --- |
| Situação | Na chamada do método IsConnected, caso o socket estivesse fechado era gerado um erro. |
| Ocorrência | Não era possível verificar a existência do socket. |
| Correção | Alteração no método IsConnected da classe tSocketConnClass não gerar erro quando o socket está fechado. |
| Informações adicionais | * Referente à ocorrência: TTEC-1007 * Disponível em builds superiores a 7.00.131227a - 2.3.1 |
