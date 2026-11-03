---
content_hash: 04cf9ffd5d58b14e46b70bfd2ea501601d9a5b99521f6277b6d4b1fc6e6a2bad
fetched_at: '2026-06-29T00:09:34.723041+00:00'
page_id: '425459235'
product: rm
source: tdn-rm
title: Movimentações Bibliotecárias via WebServices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459235
version: 5
---

A partir da Versão 12.1.18 foi implementada uma melhoria no Sistema Totvs Gestão Bibliotecária para que seja possível executar as movimentações Bibliotecárias: empréstimo(s), renovação(ões), devolução(ões) e cancelamento(s) via Webservices. Obs.: é necessário ter os webservices publicados e disponíveis para acesso. Para que estas Movimentações de empréstimos sejam realizadas foram desenvolvidos dataservers de movimentações e foi ajustado o dataserver de reserva.

Dataserver utilizados disponibilizados:

**BibMovimentacaoWSEmprestimo:** Através deste dataServer podemos realizar somente exclusivamente uma movimentação de empréstimos

**BibMovimentacaoWSDevRenCan:** Através deste dataServer podemos realizar somente os tipos de operações como: devolução, renovação e cancelamento. BibReservaData - DataServer: Este Dataserver é responsável por efetivar o cadastro das Reservas.

Renovação

Para os casos em que o serviço consumido for uma “**Renovação**”, a informação retornada no campo “Data de devolução prevista” já será a data atualizada considerando uma possível renovação (é aplicada a mesma regra utilizada no RM na tela de “Movimentações / Renovação rápida”).

Regra ajustada partir das versões 12.1.31.295 / 12.1.32.242/ 12.1.33.180 /12.34.101

Para uma melhor visualização de utilização das Movimentações Bibliotecárias via WebServices leia também o documento do TDN.

 Informações Complementares

---

[Movimentação de empréstimos via WebServices](http://tdn.totvs.com/pages/viewpage.action?pageId=286018520)
