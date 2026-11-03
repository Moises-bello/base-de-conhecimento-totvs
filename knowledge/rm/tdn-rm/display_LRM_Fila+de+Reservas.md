---
content_hash: c158fa4b5f7ef703027c6cac3f61f462d5ada727e0d01e8258dceaff0226e7ea
fetched_at: '2026-06-29T00:09:35.270682+00:00'
page_id: '425459289'
product: rm
source: tdn-rm
title: Fila de Reservas
type: documentation
url: https://tdn.totvs.com/display/LRM/Fila+de+Reservas
version: 3
---

Através dela é possível controlar qual é o próximo usuário para realizar o empréstimo, quais reservas foram disponibilizadas, quais foram canceladas etc. É apenas uma tela de controle, ou seja, nela não existe a possibilidade de edição, inclusão e exclusão, ao passo que, os dados são alterados na medida em que:

* Há um cancelamento de uma reserva;
* Algum usuário cancela um empréstimo;
* Ocorre uma devolução de um exemplar;
* A biblioteca faz a inclusão de novos exemplares no acervo, seja por cadastro, importação ou recebimento de periódicos.

A atualização da fila de reservas acontece da seguinte forma:

* Quando um exemplar se torna disponível para empréstimo, são verificadas todas as reservas com status "Reservada", feitas para a publicação referente ao exemplar, por ordem de data do pedido de reserva;
* É verificado se o exemplar atende à reserva, no caso de ter preenchido os campos volume, edição e ano;
* É feita a liberação da reserva para o primeiro usuário que o exemplar atenda. Nesta liberação são atualizados os campos data de liberação (data que a reserva ficou disponível para empréstimo), data limite para empréstimo (calculada de acordo com a configuração da regra de empréstimo), filial/unidade onde o exemplar está disponível e o exemplar que confirmou a reserva. O status da reserva é alterado para "Confirmada".
