---
content_hash: ef2212b19d510da48c9934ea2f2762e713010e802cbfdeb09a28ad36d31fe60e
fetched_at: '2026-06-29T00:11:38.077967+00:00'
page_id: '781211331'
product: rm
source: tdn-rm
title: Situações e possíveis soluções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=781211331
version: 14
---

dados-situacoes-solucoesSituações e Soluções

Confira abaixo algumas situações, alertas e erros que poderão ocorrer durante o uso do módulo de caixa e possíveis soluções:

Tela em branco ou erro ao acessar a Sessão de Caixa

Ao acessar a sesão de caixa, o sistema apresenta uma tela em branco, ou um erro de conexão.

**Possíveis impedimentos:**

* O Módulo de Caixa, 2.0 exige uma configuração técnica de API para o correto funcionamento. Tá tudo explicadinho neste link

Selecionei um registro, mas ao avançar para a tela de Pagamento é exibida uma mensagem informando que alguns lançamentos apresentam erro

Ao selecionarmos o(s) lançamento(s) e tentarmos avançar para a tela de definição do pagamento, é exibida uma mensagem indicando que alguns lançamentos apresentaram erro.

Isso ocorre pois, nesse momento são realizadas algumas validações para verificar se o(s) lançamento(s) estão apto(s) a serem baixado(s).

Com isso, será exibido ao lado direito do(s) lançamento(s) um ícone indicativo, e ao clicar, será apresentada a mensagem que informa o impedimento daquele lançamento.

Para prosseguir com o recebimento, é necessário ajustar o impedimento ou retirar a seleção do(s) lançamento(s) que consta(m) algum problema.

**Possíveis impedimentos:**

* Lançamento baixado: indica que o lançamento já foi baixado.

* Lançamento com pagamento confirmado via Sitef: indica que o pagamento já foi realizado com o Sitef e que existe uma transação de cartão de crédito/débito com status de Pagamento Confirmado para o lançamento. Como solução, deve-se realizar o processo de [Ajuste de Transações](https://tdn.totvs.com/x/9eAdGQ) para efetuar a baixa.

Selecionei dois ou mais registros, mas ao clicar no botão de receber é exibida uma mensagem informando que os lançamentos selecionados devem ser da mesma natureza Pagar/Receber

Ao selecionarmos dois ou mais lançamentos para realizar o recebimento e clicarmos no botão Receber, poderá ser exibida uma mensagem indicando que os lançamentos devem possuir a mesma natureza Pagar/Receber. Isso ocorre pois não é possível realizar o recebimento de dois lançamentos com naturezas distintas.

* Lançamentos com  possuem Natureza a **Receber**, já Lançamentos com possuem a Natureza a **Pagar**.

Não encontrei um lançamento com valor Líquido zerado na tela de pesquisa de lançamentos

Nessa revitalização do Módulo de Caixa, entendemos objetivo é torná-lo mais prático para o recebimento, melhorando sua usabilidade além da simples realização de baixas de lançamentos financeiros. Por conta disso, lançamentos com **Valor Líquido** igual a **zero** não serão mais baixados pelo módulo de caixa, sendo necessário realizar essa baixa manualmente através da visão de lançamentos.

Selecionei um registro, mas no recebimento o valor está somado a outro registro do mesmo fornecedor

Quando selecionamos um registro que esteja vinculado a um boleto que tenha mais de um lançamento, quando avançamos para a tela de recebimento, será exibida uma mensagem informativa como a demonstrada a seguir e o valor de recebimento estará no valor total de todos os registros que foram agrupados nesse boleto.

Nesse caso o recebimento precisa ser feito no valor total do boleto gerado, caso o cliente queira fazer o pagamento físico de somente um lançamento do boleto em questão, é necessário realizar o processo Desvincular Lançamentos do Boleto selecionando o registro que o cliente deseja pagar de forma separada.

Ao receber o pagamento é exibida uma mensagem informando que não foi possível receber o pagamento

Ao clicar no botão para confirmar o pagamento, poderá ser exibida uma mensagem informando que não foi possível realizar o pagamento. Isso ocorre pois, nesse momento são realizadas algumas validações para verificar se o(s) lançamento(s) estão apto(s) a serem baixado(s).

Será apresentada na mensagem o Código da Coligada e a Referência do Lançamento que apresentou algum impedimento e ao lado esquerdo, um expansor, em que ao ser clicado, será relatado o problema daquele registro.

Para prosseguir com o recebimento, é necessário ajustar o impedimento.

**Possíveis impedimentos:**

* Lançamento baixado: indica que o lançamento já foi baixado.

* Lançamento com pagamento confirmado via Sitef: indica que o pagamento já foi realizado com o Sitef e que existe uma transação de cartão de crédito/débito com status de Pagamento Confirmado para o lançamento. Como solução, deve-se realizar o processo de [Ajuste de Transações](https://tdn.totvs.com/x/9eAdGQ) para efetuar a baixa.

Transação com status "Pagamento solicitação sessão caixa" ou "Pagamento confirmado sessão caixa" e lançamento não baixado

Caso ocorra cenário onde a transação realizada no Módulo de Caixa via pagamento Sitef fique com status "Pagamento solicitado sessão caixa" ou "Pagamento confirmado sessão caixa", ao realizar o encerramento da sessão, as referidas transações terão status alterado, respectivamente, para "Pagamento solicitado" / "Pagamento confirmado", liberando assim o registro para algum dos processos de ajuste de transação. Importante, para o ajuste de transação o lançamento lançamento financeiro ter um bloqueio do campo Baixa Pendente.

A mesma regra vale para cenário onde a transação PIX ficou com status "Pagamento solicitado sessão caixa", será alterado para "Pagamento Solicitado". Já para o status "Pagamento confirmado sessão caixa", será alterado para "Pagamento Confirmado".

Observação:

* É necessário que exista no histórico da sessão de caixa um registro de baixa do respectivo boleto/lançamento.
* No encerramento da sessão atualizará as transações geradas por aquela sessão. Ao acessar uma sessão, atualizará as transações de todas as sessões já encerradas naquela coligada.
0solid

#### [Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517)
