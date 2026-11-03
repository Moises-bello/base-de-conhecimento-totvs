---
content_hash: 0d4380fde02a910e86664e2e2a256e6e4267ccf382838db538509136fa3647dc
fetched_at: '2026-06-29T00:08:59.441116+00:00'
page_id: '362453824'
product: rm
source: tdn-rm
title: Quais são os possíveis status dos eventos na Fila de Eventos do RM?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362453824
version: 2
---

Relação de Status na Fila de Eventos do RM:

* 0 - Pendente
* 1 - Gerado
* 2- Erro na geração
* 3 - Enviado para o TAF
* 4 - Aceito TAF
* 5 - Erro na integração TAF
* 6 - Rejeitado TAF
* 7 - Cancelado
* 8 - Retificado
* 9 - Rejeitado RET
* 10 - Aceito RET
* 11 - Excluído RET

 O sistema não gera um novo gatilho  e realiza a inclusão da alteração sobre o mesmo registro sem incluir um novo evento quando o registro está com os seguintes Status:

* 0 - Pendente
* 1 - Gerado
* 2 - Erro na geração
* 5 - Erro na integração TAF
* 6 - Rejeitado TAF
* 9 - Rejeitado RET

 O sistema gera um novo gatilho automático e inclui uma nova linha na fila de eventos quando realizamos uma alteração em registros relacionados a eventos com os seguintes Status:

* 3 - Enviado para o TAF
* 4 - Aceito TAF
* 10 - Aceito RET

 No momento o sistema ainda não utiliza os Status abaixo:

* 7 - Cancelado
* 8 - Retificado
