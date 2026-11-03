---
content_hash: 9d3a3252d9fb9ab5d0c6970211e0d1de47d55ada5dbf6c99f3835230191f7769
fetched_at: '2026-06-29T00:10:20.164733+00:00'
page_id: '486184335'
product: rm
source: tdn-rm
title: Revitalização da Cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=486184335
version: 9
---

A Revitalização da Cotação tem o objetivo de gravar na tabela TCITMORCAMENTOAGRUPADO do TOTVS Gestão de Estoque, Compras e Faturamento os itens agrupados, quando parametrizado para agrupar itens repetidos (Parâmetro "Não Agrupar itens Iguais na cotação" desmarcado na etapa "Movimentos 1/2" dos parâmetros da cotação).

Anteriormente, o agrupamento era realizado somente em tela, ou seja, ao editar a cotação os valores dos itens iguais eram concatenados momentaneamente, sendo apresentados agrupados.

A execução do processo pode ser realizada das seguintes formas:

1 - Ao editar a cotação sem a "Revitalização da Cotação", será apresentado:

* Clicando em **Sim**, o processo será executado para a cotação em questão (criando os registros na tabela TCITMORCAMENTOAGRUPADO) e a cotação será aberta para edição normalmente;
* Clicando em **Não**, a cotação não será aberta para edição (processo obrigatório).

2 - Selecionando as cotações desejadas, em seguida clique em: **Processos | Revitalização da Cotação.**

3 - Criar um filtro para todas as cotações que ainda estejam em aberto\*, selecionar todas as cotações retornadas e em seguida clique em: **Processos | Revitalização da Cotação. (OPÇÃO****RECOMENDADA)**

A **Revitalização da Cotação** é necessária para cotações criadas em versões anteriores a 12.1.25 e que ainda estejam em aberto\*.

A **Revitalização da Cotação**, é uma alteração estrutural de banco de dados e não traz impactos para o usuário e negócio.

*\*Cotações 'em aberto' são registros cujos status compreendem em: Composição, Aguardando Resposta dos Fornecedores ou Negociação da Melhor Oferta.*
