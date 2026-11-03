---
content_hash: abe0dc6ff7ce386ebc92ef53938400e8a02be19a755eacb8d451904672a2eeb0
fetched_at: '2026-06-29T00:10:14.434036+00:00'
page_id: '461899361'
product: rm
source: tdn-rm
title: Evento-2230- Afastamento  tipo - Q (Cárcere/prisão)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461899361
version: 14
---

Criado no cadastro do funcionário o tipo de afastamento Q-Cárcere/prisão para atender ao eSocial.

**O usuário deverá seguir os procedimentos abaixo****:**

* Executar um recálculo na base, o recálculo poderá ser apenas para um funcionário. Com isso o sistema  irá  criar a situação Q-Prisão/Cárcere no cadastro do funcionário **.**
* Retirar o relacionamento no parametrizador : De/Para Afastamento , caso exista algum relacionamento referente ao Cárcere/Prisão.

**Exemplo: Alterando a situação de um funcionário.**

1-Alterada situação  A-Ativo para Q-Prisão/Cárcere.

2-Será gerado gatilho na fila de eventos  para  o evento S-2230-Afastamento.

3- XML gerado na fila de eventos. Motivo de afastamento igual a 11 conforme tabela 18 do eSocial.

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.24  12.1.23 |
| 12.1.22 |
| 12.1.21 |

falsefalse

**Status:** Finalizado

false

**Data:22/02/2019**

false

**Autor:Andreia Valquiria Pereira**
