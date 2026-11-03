---
content_hash: 4fedc1b3ed7d33570896cb270031b314be100a8bc7bb5b065e4b49b5b008b02f
fetched_at: '2026-06-29T00:09:18.144154+00:00'
page_id: '421388687'
product: rm
source: tdn-rm
title: Cancelamento de Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelamento+de+Baixa
version: 6
---

**Cancelamento de baixa em extrato agrupador de vários itens**

Numa baixa que gerou apenas um extrato de caixa agrupando vários lançamentos, podemos cancelar a baixa de um dos itens de baixa isoladamente. Nesse caso, será gerado um extrato de estorno no mesmo valor do lançamento original e em seguida gerado um novo extrato de caixa com o valor das baixas não relacionadas no cancelamento.

Para que esta operação seja realizada, deve-se selecionar a opção **Cancelar somente baixas selecionadas**, disponível na tela de cancelamento de baixa.

Esta operação será possível **apenas** quando o [meio de pagamento](https://tdn.totvs.com/display/public/LRM/Meio+Pagamento) utilizado na baixa for dos tipos primitivos Dinheiro, Boleto Bancário ou Outros. Para os demais meios de pagamento, entende-se que representam um documento único, não justificando estornar apenas uma parte do montante.

Nestes casos, o cancelamento de baixa deve ser realizado selecionando a opção **Cancelar todas as baixas do extrato**.
