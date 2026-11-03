---
content_hash: 980c4fd80b98f2037742288353d5d63b49050ee4811a19db7e8e1deaab90ecc8
fetched_at: '2026-06-29T00:08:30.170577+00:00'
page_id: '272406427'
product: rm
source: tdn-rm
title: 598602 MEDU-3108 DT Renovacao Emprestimos Atraso
type: documentation
url: https://tdn.totvs.com/display/LRM/598602+MEDU-3108+DT+Renovacao+Emprestimos+Atraso
version: 109
---

# MOVIMENTAÇÕES - RENOVAÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentações - renovações* |
| **Situação/Requisito:** | *Foi identificado que o sistema está permitindo efetuar uma renovação de um empréstimo mesmo quando este está atrasado, o sistema só bloqueia a renovação se for executado o processo de atualização da biblioteca que altera o status do empréstimo para atrasado, após esta alteração o mesmo não permite a renovação.* |
| **Solução/Implementação:** | ***Foi feito o ajuste para que o sistema além de considerar o status "atrasado", considere também empréstimos com status de "emprestado" e com data de devolução prevista menor que a data atual e também considerar a regras de empréstimos para permitir ou não a renovação quando o usuário possui empréstimos atrasados.*** |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
