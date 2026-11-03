---
content_hash: 7296b191f717e9ae4739694b55834d0225dc9ede4d94e94e21d85816ab77e8bb
fetched_at: '2026-06-29T00:08:22.128630+00:00'
page_id: '269075852'
product: rm
source: tdn-rm
title: 113798_DT_Reserva_Vinculo_Exemplar
type: documentation
url: https://tdn.totvs.com/display/LRM/113798_DT_Reserva_Vinculo_Exemplar
version: 111
---

# MOVIMENTAÇÕES - EMPRÉSTIMOS COM RESERVAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Movimentações - empréstimos com reservas* |
| **Situação/Requisito:** | *Quando existe um exemplar reservado (reserva confirmada) para um determinado usuário sendo que a publicação possui no momento do empréstimo outros exemplares disponíveis, quando é feito a tentativa de empréstimo para este usuário utilizando um exemplar da publicação diferente do que está na confirmação da reserva, o sistema exibe uma mensagem de erro (O objeto nulo deve ter um valor.) e não permite o empréstimo, só permite quando o exemplar da confirmação da reserva é emprestado para este usuário.* |
| **Solução/Implementação:** | *Foi feito um ajuste na validação da reserva, caso existam mais exemplares disponíveis no momento do empréstimo, o sistema permitirá o empréstimo de qualquer exemplar para este usuário, assim não vinculando o usuário um exemplar específico, porém mantendo a reserva do usuário caso os demais exemplares sejam emprestados, pois o vínculo da reserva deve ser com a publicação, não com o exemplar, respeitando as reservas já existentes.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
