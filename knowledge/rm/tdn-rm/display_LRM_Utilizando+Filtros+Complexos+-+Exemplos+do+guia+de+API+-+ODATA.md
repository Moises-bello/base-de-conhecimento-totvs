---
content_hash: eef5594c45c1829429888075a1c1a05afd58bec8e9c87a74062f1c8e1c56a4d3
fetched_at: '2026-06-29T00:10:11.869592+00:00'
page_id: '453294751'
product: rm
source: tdn-rm
title: Utilizando Filtros Complexos - Exemplos do guia de API - ODATA
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+Filtros+Complexos+-+Exemplos+do+guia+de+API+-+ODATA
version: 5
---

# Sumário

---

Sumário

# Objetivo

---

As APIs expostas no RM.Host, suportam filtros no padrão ODATA. A seguir, serão mostrados alguns exemplos de utilização.

# 1 - Exemplos de filtro no padrão ODATA

---

Veja a seguir exemplos de filtros no padrão odata.

|  |  |  |
| --- | --- | --- |
| **Operador** | **Descrição** | **Exemplo** |
| Logical Operators | | |
| eq | Equal | /Suppliers?$filter=Address/City eq 'Redmond' |
| ne | Not equal | /Suppliers?$filter=Address/City ne 'London' |
| gt | Greater than | /Products?$filter=Price gt 20 |
| ge | Greater than or equal | /Products?$filter=Price ge 10 |
| lt | Less than | /Products?$filter=Price lt 20 |
| le | Less than or equal | /Products?$filter=Price le 100 |
| and | Logical and | /Products?$filter=Price le 200 and Price gt 3.5 |
| or | Logical or | /Products?$filter=Price le 3.5 or Price gt 200 |
| not | Logical negation | /Products?$filter=not endswith(Description,'milk') |
| Grouping Operators | | |
| ( ) | grouping | /Products?$filter=(Price lt 5) |

Ao utilizar campos do tipo data é importante saber:

* Datas devem ser informadas com Time Zone. Exemplo: 2014-07-07T18:32:15Z ou 2014-07-07T15:32:15-03:00
* Datas enviadas na requisição entre aspas, por exemplo: "2014-07-07T15:32:15-03:00", serão tratadas internamente como string. Recomenda-se usar o Time Zone.

Observação:

Quando o filtro do tipo datetimeoffset usa um valor de timezone positivo (fuso horário positivo) pode acontecer de retornar uma exceção pois o + (mais) tem um significado diferente, quando usado em uma URL, sendo codificado automáticamente por um espaço em branco.

Para corrigir isso, é necessário utilizar uma codificação especial.  
Substitua o "+" por "%2b"

Por exemplo:  
2014-07-07T15:32:15**+**03:00 => 2014-07-07T15:32:15**%2b**03:00

# 1.2 - Aplicação

---

Para contextualizar o uso dos filtros, utilizamos a API de usuários como exemplo.

Para filtrar todos os usuários que tem a data de criação igual a  "2014-07-07T18:32:15Z", a seguinte requisição será feita:

http://localhost:8051/api/framework/v1/users?$filter=(meta.created eq 2014-07-07T18:32:15Z)
