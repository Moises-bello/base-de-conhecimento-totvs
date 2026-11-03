---
content_hash: ebb606f3f7eac2e8a97fb516890da6ea2eb0cf6ed2130cc9eee9499d145524ed
fetched_at: '2026-06-29T00:10:00.965376+00:00'
page_id: '452718655'
product: rm
source: tdn-rm
title: Código de Cálculo 128 - Estorno de Faltas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718655
version: 2
---

Evento do tipo Base de Cálculo com características que deverão ser iguais ao evento de Código de Cálculo 008 (faltas). Este evento será utilizado para estornar faltas lançadas e descontadas em períodos anteriores que posteriormente foram justificadas pelo funcionário. Neste caso, estas faltas não serão consideradas para o cálculo das férias e do 13º salário.

O evento é utilizado exclusivamente para estorno de faltas justificadas pelo funcionário. Caso o usuário queira pagar as faltas justificadas no próprio mês em que elas ocorreram, obrigatoriamente ele deverá pagar em outro evento com as características do CC001 e lançar o CC128 para estorno das faltas.

Caso o funcionário tenha justificado as faltas em meses seguintes, o usuário deverá inserir o evento de CC128 via ficha financeira no mês em que a falta ocorreu. Assim o estorno anula a falta daquele mês e o período aquisitivo de férias do funcionário não é prejudicado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
