---
content_hash: 2d88797cd47aba0af6cf772fb3861faeecab6ae8fce627f48318a9fba7c78ba3
fetched_at: '2026-06-29T00:08:52.406781+00:00'
page_id: '340362705'
product: rm
source: tdn-rm
title: Rubricas de Banco de Horas
type: documentation
url: https://tdn.totvs.com/display/LRM/Rubricas+de+Banco+de+Horas
version: 2
---

As rubricas correspondentes ao banco de horas, devem ser informativas conforme a orientação do Manual de Orientação do eSocial 2.4 (Março 2018) pág. 66:

**No Chronus:**

* Poderá criar dois eventos calculados por fórmula, e essas fórmulas deverão retornar o valor das horas positivas ou negativas que o funcionário possui no banco;
* No sindicato deve realizar a associação desses eventos a eventos do tipo de base de cálculo do Labore;
* Realizar o lançamento de eventos calculados por fórmula para o movimento do espelho;
* Realizar a integração com o Labore.

**No Labore:**

* Nos eventos de base de cálculo que foram associados no Chronus, deve informar as rubricas correspondentes ao banco de horas(9950, 9951);
* Realizar o lançamento do movimento da integração para a folha de pagamento.

Essas verbas serão levadas nos eventos periódicos(S-1200). O valor retornado pelo Chronus será informado no campo de horas no envelope do Labore. Ficará ao critério da empresa a informação a ser levada no campo valor pois no eSocial não é possível enviar uma rubrica no S-1200 com valor zerado conforme o leiaute.

Para as outras rubricas questionadas, continuará a realizar o processo natural de quando realiza compensação do banco de horas para pagamento/desconto do funcionário e informa-las nos devidos eventos associados do Labore.
