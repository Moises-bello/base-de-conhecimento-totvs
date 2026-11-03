---
content_hash: 805f19839ccd95eb05acdb7505cd23491a67c53e557cfe972f2d43bbbb2d330c
fetched_at: '2026-07-02T19:24:21.509637+00:00'
page_id: '267810107'
product: protheus
source: tdn-tec
title: Correção para que o comportamente do erro de função não encontrada não sai
  do bloco de BEGIN/END SEQUENCE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267810107
version: 1
---

Erro uso do retry do protocolo SSL com proxy

|  |  |
| --- | --- |
| Situação | Quando da utilização do comando BEGIN/END SEQUENCE, sem a cláusula RECOVER, na ocorrência de erro de função não encontrada o bloco BEGIN/END SEQUENCE não era executado. |
| Ocorrência |  |
| Correção | Correção no comportamento para continuar a execução do bloco. |
| Informações adicionais | * Disponível em builds superiores a 7.00.131227A - 2.0.5 |
