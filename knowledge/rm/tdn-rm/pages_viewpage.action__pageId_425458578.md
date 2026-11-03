---
content_hash: 02e998cbba0b58dab88a8d98f160d718dcaf8878bdbd4e5c01bbbc42eccbf449
fetched_at: '2026-06-29T00:09:31.252024+00:00'
page_id: '425458578'
product: rm
source: tdn-rm
title: Lista de espera de instalação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458578
version: 8
---

A lista de espera para reserva de instalação permite que **o instalação n****o período desejado caso já esteja reservado por outra pessoa**, ele seja incluído automaticamente nesta lista de espera da reserva.

No caso de **cancelamento da reserva da instalação no período desejado,** o sistema verifica se existe alguma solicitação na lista de reserva, e caso exista ele irá gerar automaticamente uma reserva para este solicitante que estava na espera.

Parâmetro "Utilizar lista de espera para recurso / instalação"

Para que esta funcionalidade esteja disponível, será necessário que o parâmetro "**Utilizar lista de espera para recurso / instalação**" esteja **marcado** em: **Configurações | Parâmetros | Secretaria | Geral 6/7**

Prioridade 

A prioridade da lista de espera é definida pela data da inclusão do registro, ou seja, terá prioridade aquele que primeiro entrou na lista e cujo horário seja idêntico ao disponibilizado.

Exemplo

Vamos exemplificar um cenário para melhor explicar o funcionamento

**Reserva de instalação já realizada**

| Usuário | Data inicio | Data Fim | Hora Inicio | Hora Fim | Sala |
| --- | --- | --- | --- | --- | --- |
| Professor001 | 02/10/2024 | 02/10/2024 | 08:00 | 10:00 | Laboratório de ciências |

**Reserva de instalação a ser realizada**

**Como já existe um reserva para a mesma instalação no mesmo período desejado, esta reserva será incluída em uma lista de espera da reserva**

| Usuário | Data inicio | Data Fim | Hora Inicio | Hora Fim | Sala |
| --- | --- | --- | --- | --- | --- |
| Professor099 | 02/10/2024 | 02/10/2024 | 08:00 | 10:00 | Laboratório de ciências |

Informações Complementares

---

[Excluir Lista de Espera](http://tdn.totvs.com/x/AgBjGQ)
