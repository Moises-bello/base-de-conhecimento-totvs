---
content_hash: fb4e103de4d9bdb488e894eba40f66c7b8b8c32f7c090f1d04e108e663bed804
fetched_at: '2026-06-29T00:08:41.486109+00:00'
page_id: '286730797'
product: rm
source: tdn-rm
title: RMCTB00002_Alteração do código de Contas Gerenciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286730797
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Alteração do código de Contas Gerenciais |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do Processo**  Através deste processo será possível alterar o código de uma ou de várias contas de uma só vez, mesmo que a conta esteja sendo utilizada em um ou mais lançamentos:                  **Regras Gerais**  Ao alterar o código de uma conta deve ser considerada a hierarquia do plano, ou seja, se a conta for transferida de um grupo para outro, as contas sintéticas do novo grupo já devem estar criadas quando da alteração do código.  **Parametrização Necessária**  1 - Ao acessar o processo informe a conta atual e seu novo código, após clique em incluir para que os dados sejam informados na lista de alteração:                                  2 - A quantidade de dígitos da nova conta deve ser a mesma da conta anterior.  **Atenção** Será possível fazer a alteração do código de contas, desde que:   * Não seja uma conta sintética (restrição válida somente para contas gerenciais); * O novo código não esteja cadastrado; * O novo código não seja uma conta analítica para o primeiro grau; * O novo código tenha conta superior cadastrada (restrição válida para contas não globais); * Não seja encontrada nenhuma inconsistência (caso encontre, todo o processo será abortado); |
| **Observações:** | Embora seja possível alterar os códigos de todas as contas de uma só vez, sugerimos que, para otimizar ainda mais este processo, a alteração dos códigos seja feita por partes, informando-se um pequeno número de contas de uma só vez, pois, devido à sua complexidade e dependendo também do número de registros a serem alterados, este processo poderá ser um pouco longo, além do mais, somente no final do processo é que o sistema retornará certos tipos de inconsistência encontrada, como por exemplo, se o Novo Código informado for igual a um código já existente no plano de contas cadastrado. Caso isto ocorra, todo o processo será cancelado sem que nenhum código da lista seja alterado. Além disso, é altamente recomendável que o exercício esteja encerrado, e que se faça antes um Backup da base de dados, uma vez que a alteração refletirá em todos os dados existentes até o momento. |
