---
content_hash: 9fbe977445885648f306571e838546ad775e2bedf18ad1a1dd96f57ce647709b
fetched_at: '2026-06-29T00:09:24.510073+00:00'
page_id: '423937943'
product: rm
source: tdn-rm
title: Número de Série
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937943
version: 4
---

A opção Número de Série são cadastrados os números de séries que serão amarrados aos produtos. Os campos Filial e Local de Estoque somente podem ser modificados através de movimentos.

* O status inicial é sempre "Fora Estoque".
* Um número de série não poderá ser removido caso seu status seja diferente de "Fora Estoque" ou esteja incluído em um item de movimento.
* O número de série leva em conta a unidade usada no movimento. Por exemplo, se a unidade de controle do produto é UND e a unidade de compra foi "Caixa com 10" o usuário deverá selecionar 10 números de série, pois será levado em conta a unidade de controle do produto.
* Após realizar a movimentação com o produto que apresenta o número de serie, os campos Lote e Data de Fabricação não poderão ser modificados.
* O número de série poderá ser utilizado em movimentação que afetam qualquer um dos saldos, como poderá afetar mas de um saldo, criou-se um campo de Status de estoque para cada saldo ( campos Saldo Físico 1 à Saldo Físico 10 na tabela TNUMSERIE). Se o valor do Saldo Físico for 1(Um), significa que o número de série está em estoque para o saldo 1, caso seja 0(zero), não estará em estoque. A mesma regra vale para os demais saldos. Na visão do Número de Série na tela de produto, o Status aparecerá como 'Em Estoque ", se o número de série estiver em estoque para pelo menos um dos saldos, e 'Fora Estoque 'se para todos os saldos estiverem fora de estoque.

***Observação**:*O sistema permite restringir o acesso que o usuário terá sobre as séries do cadastro de produto, onde poderá ser definido dentro do perfil do usuário, se o mesmo poderá Visualizar, Incluir, Excluir ou Editar as séries no cadastro de produtos.
