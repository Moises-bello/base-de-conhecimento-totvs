---
content_hash: 4012204795d35e39df535d4b6dc8dad642a750319a116b8bf2ae664481d8155b
fetched_at: '2026-06-29T00:09:18.126148+00:00'
page_id: '421388676'
product: rm
source: tdn-rm
title: Baixa por perda financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixa+por+perda+financeira
version: 4
---

Este processo atende as situações em que é necessário baixar o lançamento sem que o mesmo tenha sido efetivamente pago ou recebido.

**Efeitos sobre o lançamento:**

O campo Valor Baixado do lançamento ficará com valor zero e não será gerado extrato de caixa. O processo está disponível no menu Contas a Pagar/Receber | Lançamentos | Processos | Baixa.

O valor líquido do lançamento baixado por este processo será preenchido no campo VRPERDAFINANCEIRA da tabela FLAN.

**Obs.:** O saldo da Conta/Caixa não será afetado.

**Permissão:**

O processo pode ser restrito para alguns perfis utilizando a permissão de acesso a menus em Contas a Pagar/Receber | Operações Financeiras | Lançamentos | Baixar lançamentos por perda financeira.
