---
content_hash: 10dd68a594761e1a2b1d2b4a549279e8d3ad67383f8da298465c4279597e2fa8
fetched_at: '2026-06-29T00:05:47.791977+00:00'
page_id: '1017446251'
product: rm
source: tdn-rm
title: Verbos HTTP
type: documentation
url: https://tdn.totvs.com/display/LRM/Verbos+HTTP
version: 2
---

Os recursos gerenciados por uma aplicação, e identificados unicamente por meio de sua URI, geralmente podem ser manipulados de diversas maneiras. É possível criá-los, atualizá-los, excluí-los, dentre outras operações.

Quando um cliente dispara uma requisição HTTP para um serviço, além da URI que identifica quais recursos ele pretende manipular, é necessário que ele também informe o tipo de manipulação que deseja realizar no recurso. É justamente aí que entra um outro conceito da Web, que são os métodos do protocolo HTTP.

O protocolo HTTP possui diversos métodos, sendo que cada um possui uma semântica distinta, e devem ser utilizados para indicar o tipo de manipulação a ser realizada em um determinado recurso.

Vejamos agora os principais métodos do protocolo HTTP e o cenário de utilização de cada um deles:

* GET: Obter os dados de um recurso.
* POST: Criar um novo recurso.
* PUT: Substituir os dados de um determinado recurso.
* PATCH: Atualizar parcialmente um determinado recurso.
* DELETE: Excluir um determinado recurso.
* HEAD: Similar ao GET, mas utilizado apenas para se obter os cabeçalhos de resposta, sem os dados em si.
* OPTIONS: Obter quais manipulações podem ser realizadas em um determinado recurso.

Geralmente as aplicações apenas utilizam os métodos GET, POST, PUT e DELETE, mas se fizer sentido em sua aplicação utilizar algum dos outros métodos, não há nenhum problema nisso.

|  |  |  |
| --- | --- | --- |
| OPTIONS | 2 complete | 9 complete |
| GET | 3 complete | 10 complete |
| HEAD | 4 complete | 11 complete |
| PUT | 5 complete | 12 complete |
| POST | 6 complete | 13 complete |
| DELETE | 7 complete | 14 complete |
| PATCH | 8 complete | 15 complete |

**Idempotente** significa que o endpoint pode ser chamado várias vezes sem resultados diferentes. Não importa se o método é chamado apenas uma ou dez vezes. O resultado deve sempre o mesmo. Isso se aplica apenas ao resultado, não ao próprio recurso.

**Safe** são métodos Read-only. Isso significa que são seguros e não importa quantas vezes chamar, ele não irá alterar o estado do **resource**.
