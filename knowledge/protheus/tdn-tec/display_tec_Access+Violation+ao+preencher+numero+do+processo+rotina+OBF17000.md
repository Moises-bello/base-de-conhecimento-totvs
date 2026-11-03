---
content_hash: f7bf7b19317a2b0f1c8e41782b7adb8e54014e8867be451fab020c698ff912ff
fetched_at: '2026-07-02T19:24:25.074406+00:00'
page_id: '497199500'
product: protheus
source: tdn-tec
title: Access Violation ao preencher numero do processo rotina OBF17000
type: documentation
url: https://tdn.totvs.com/display/tec/Access+Violation+ao+preencher+numero+do+processo+rotina+OBF17000
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Ao ser informado campo tipo Float em em query que espera campo do tipo char é gerado Access Violation |
| Correção | Inserido proteção e mensagem de erro para que não seja realizado o acesso inválido de memória |
| Informações adicionais | * Referente ao chamado: MTEC-2545 * Disponível em builds iguais ou superiores a [13.1.3.44](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.44). |
