---
content_hash: 29689c1ac5256e8309c34cfd56df978e73af4f9dcfb48b2044e47b73d6e92184
fetched_at: '2026-06-29T00:09:31.244557+00:00'
page_id: '425458576'
product: rm
source: tdn-rm
title: Lista de espera de recurso
type: documentation
url: https://tdn.totvs.com/display/LRM/Lista+de+espera+de+recurso
version: 6
---

A lista de espera para reserva de recurso permite que **o recurso n****o período desejado caso já esteja reservado por outra pessoa**, ele seja incluído automaticamente nesta lista de espera da reserva. 

No caso de **cancelamento da reserva da recurso no período desejado,** o sistema verifica se existe alguma solicitação na lista de reserva, e caso exista ele irá gerar automaticamente uma reserva para este solicitante que estava na espera.

Parâmetro "Utilizar lista de espera para recurso / instalação"

Para que esta funcionalidade esteja disponível, será necessário que o parâmetro "**Utilizar lista de espera para recurso / instalação**" esteja **marcado** em: **Configurações | Parâmetros | Secretaria | Geral 6/7**

Prioridade 

A prioridade da lista de espera é definida pela data da inclusão do registro, ou seja, terá prioridade aquele que primeiro entrou na lista e cujo horário seja idêntico ao disponibilizado.

Exemplo

Vamos exemplificar um cenário para melhor explicar o funcionamento

**Reserva de recurso já realizada**

| Usuário | Data inicio | Data Fim | Hora Inicio | Hora Fim | Recurso |
| --- | --- | --- | --- | --- | --- |
| Professor001 | 02/10/2024 | 02/10/2024 | 08:00 | 10:00 | Projetor |

**Reserva de recurso a ser realizada**

**Como já existe um reserva para a mesma instalação no mesmo período desejado, esta reserva será incluída em uma lista de espera da reserva**

| Usuário | Data inicio | Data Fim | Hora Inicio | Hora Fim | Recurso |
| --- | --- | --- | --- | --- | --- |
| Professor099 | 02/10/2024 | 02/10/2024 | 08:00 | 10:00 | Projetor |

Informações Complementares

---

[Excluir Lista de Espera](http://tdn.totvs.com/x/AgBjGQ)
