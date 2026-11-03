---
content_hash: 74f97cc761ed4e0642315bbf6df7b1b20952b6ee8a8551954afee11127b278de
fetched_at: '2026-06-29T00:09:11.666803+00:00'
page_id: '415697370'
product: rm
source: tdn-rm
title: Validação de dados da base para demitidos antes da data de obrigatoriedade
  de eventos não periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415697370
version: 6
---

Existe o parâmetro para validar considerando demitidos em data anterior a obrigatoriedade da entrega do eSocial.

Será considerada a data inserida no parametrizador em “Não Periódicos” para validar o parâmetro nos eventos S-2200 e S-2300, exceto quando para competência atual que será considerada a data da competência para a validação

Será verificado data do último movimento

Data no parametrizador

Sem o parâmetro marcado filtrando pelo funcionário

Marcando o parâmetro

**Observações:**

Será validado se o demitido está com data de último movimento maior ou igual a competência atual e neste caso o parâmetro marcado ou desmarcado não será considerado pois esta regra já era validada anteriormente.

Esta validação será processada para os eventos [S-2200- Admissão /Ingresso de Trabalhador](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2200.aspx) e [S-2300 - Trabalhados sem vinculo de emprego/Estatutário-inicio](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2300.aspx).

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
| 12.1.19 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
