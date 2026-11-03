---
content_hash: f7fb92ed1940bec516483780dd3e627cde926db21a8800e494099d754278cf96
fetched_at: '2026-06-29T00:09:28.119881+00:00'
page_id: '423938662'
product: rm
source: tdn-rm
title: Alteração do Código da Conta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938662
version: 6
---

Através deste processo será possível alterar o código de uma ou de várias contas de uma só vez, mesmo que a conta esteja sendo utilizada em um ou mais lançamentos. Para isto, informe o código atual da conta e o novo código, em seguida acione o botão Incluir para que a conta seja incluída na ralação de contas a serem alteradas. Inclua todas as contas que desejar na relação de contas a serem alteradas e, finalmente, mande executar o processo. Se for preciso excluir alguma conta da relação de contas a serem alteradas, basta selecionar a(s) conta(s) desejada(s) e acionar o botão Excluir.

Em se tratando de contas contábeis/gerenciais, este processo poderá ser usado para alterar o código de contas analíticas ou de contas sintéticas. Quando se alterar o código de uma conta sintética, todos os códigos de suas contas analíticas serão automaticamente alterados. Quando se alterar o código de uma conta global o sistema criará, caso ainda não exista, em todas as outras coligadas que utilizam contas globais, as contas de níveis superiores à conta global que se está alterando.

**Atenção**

Será possível fazer a alteração do código de contas, desde que:

* O novo código não esteja cadastrado;
* O novo código não seja uma conta analítica para o primeiro grau;
* O novo código tenha conta superior cadastrada (restrição válida para contas não globais);
* Não seja encontrada nenhuma inconsistência (caso encontre, todo o processo será abortado);

Embora seja possível alterar os códigos de todas as contas de uma só vez, sugerimos que, para otimizar ainda mais este processo, a alteração dos códigos seja feita por partes, informando-se um pequeno número de contas de uma só vez, pois, devido à sua complexidade e dependendo também do número de registros a serem alterados, este processo poderá ser um pouco longo, além do mais, somente no final do processo é que o sistema retornará certos tipos de inconsistência encontrada, como por exemplo, se o Novo Código informado for igual a um código já existente no plano de contas cadastrado. Caso isto ocorra, todo o processo será cancelado sem que nenhum código da lista seja alterado. Além disso, é altamente recomendável que o exercício esteja encerrado, e que se faça antes um Backup da base de dados, uma vez que a alteração refletirá em todos os dados existentes até o momento.
