---
content_hash: e7c2f5e6678592cf79f94f417661880d763817e519e0f18e38338c72c3110673
fetched_at: '2026-06-29T00:11:33.972619+00:00'
page_id: '763260381'
product: rm
source: tdn-rm
title: 10.1.2 - Novidades na Geração de Acordos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=763260381
version: 7
---

Para ser possível alterar o cliente na geração de um acordo, devemos marcar dentro do cadastro de template a nova opção .

Agora ao gerar acordo, temos duas opções no  de processos:

* **Gerar acordo ou Simples:** Se os lançamentos selecionados pertencerem ao mesmo Cliente/Fornecedor, o processo seguirá independente da regra do Template de Acordo permitir ou não alterar o Cliente/Fornecedor. Caso sejam selecionados lançamentos de Cliente/Fornecedor distintos, o sistema permitirá seguir com o processo somente se a flag '**'** estiver **marcada** no Template de acordo selecionado.

* **Gerar acordo em lote:** Esta nova opção de menu de "em lote" substituir a antiga pergunta "múltiplos acordos", mas sua funcionalidade continua a mesma conforme observado a seguir.

 

Nesta opção em lote, se houver lançamentos para Clientes/Fornecedores distintos na seleção. Nesse caso, o sistema agrupa os lançamentos por Cliente/Fornecedor para processar o Acordo e o critério adotado (juros, desconto, número de parcelas entre outros) prevalecerá para todos os lançamentos selecionados, por exemplo:

Selecionamos na visão 20 lançamentos de clientes distintos, sendo 5 lançamentos de cada, neste cenário o sistema criará 4 acordos agrupando por cliente.

Este processo será executado conforme a regra citada acima somente quando forem selecionados lançamentos de Clientes/Fornecedores distintos. Caso sejam selecionados lançamentos de Clientes/Fornecedores iguais, o sistema seguirá o processo de Acordo Simples.

O Acordo em Lote será utilizado sempre que houver a necessidade de se adotar o mesmo critério de negociação para todos os Lançamentos, como por exemplo, concessão de desconto de mesmo valor para todos os clientes que estiverem com seus pagamentos em dia. Nesse caso, a regra adotada no processo será válida para todos os Clientes/Fornecedores da seleção de lançamentos. Durante o processo, o(s) lançamento(s) financeiro(s) "objeto(s) do Acordo" será (ao) quitado (s), terão status alterado para "Baixados por Acordo" e o (s) valor (es) não afeta (rao) os saldos da Conta/Caixa. Serão gerados novos lançamentos conforme os critérios adotados. Os novos lançamentos classificados como "Gerados pelo Acordo" ainda poderão ser renegociados gerando novos Acordos.

Atenção

Existe uma validação na geração do Acordo em Lote, onde verificar a regra do Template de Acordo informado pelo usuário, pois poderá ser utilizado somente o Template que estiver com a flag '' **desmarcada**.
