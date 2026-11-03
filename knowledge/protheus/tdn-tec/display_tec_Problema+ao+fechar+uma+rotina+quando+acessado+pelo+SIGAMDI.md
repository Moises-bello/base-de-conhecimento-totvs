---
content_hash: c8f27436fe988dc9e9fe45351207d599a1415f66247d616b34ea7ee0c09453b7
fetched_at: '2026-07-02T19:24:21.494780+00:00'
page_id: '267804716'
product: protheus
source: tdn-tec
title: Problema ao fechar uma rotina quando acessado pelo SIGAMDI
type: documentation
url: https://tdn.totvs.com/display/tec/Problema+ao+fechar+uma+rotina+quando+acessado+pelo+SIGAMDI
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Ao acessar qualquer rotina através do SIGAMDI e depois fechá-la através do botão X, ocorre o seguinte erro no console:  Unexpected token \*\* terminal.execMessage({type: MESSAGE.MS\_RUNINSESSION\_WITHOUT\_RETURN, comp: 1, connectionID: 'MAIN\_THREAD', command: 'APPDELTAB('\*\*\*\*0001')'}); |
| Correção | Corrigido o envio da mensagem quando a propriedade command tiver apóstrofo. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: BAS-1036 * Disponível a partir da build 7.00.131227A - 2.3.6 |
