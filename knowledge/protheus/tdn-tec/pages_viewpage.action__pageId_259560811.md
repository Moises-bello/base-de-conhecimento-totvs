---
content_hash: ee713940b4ff76ec95951bc517f4927561305293ebb5ae3f3d02b7cac7955217
fetched_at: '2026-07-02T19:24:20.743849+00:00'
page_id: '259560811'
product: protheus
source: tdn-tec
title: Correção - Comportamento da função TCLink()
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=259560811
version: 1
---

Esta build contém uma correção no comportamento da função TCLink()

|  |  |
| --- | --- |
| Situação | Utilização da função TCLink() para abrir uma nova conexão com um determinado DBAccess, quando já existe uma conexão ativa. |
| Ocorrência | Quando ocorre falha na conexão ( Erro -2 ) ao tentar conectar com um segundo DBAccess, a primeira conexão era perdida e encerrada sem aviso com o primeiro DBAccess, impedindo a aplicação de continuar o processo, e gerando log de erro "Disconnected Prematurely (RECEIVEBLOCK)" no log de console do primeiro DBAccess, onde a conexão estava ativa. |
| Correção | Corrigido o tratamento de conexão, para não afetar as conexões anteriormentes estabelecidas em caso de falha na tentativa de uma nova conexão pelo mesmo processo. |
| Informações adicionais | * Referente ao chamado: TWD309 * Referente à ocorrência: SSIM-1232 * Disponível a partir da build 7.00.131227A, com data de geração igual ou superior a |
