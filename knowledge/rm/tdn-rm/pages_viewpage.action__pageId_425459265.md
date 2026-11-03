---
content_hash: 5f6dddab4a2f564e4c7aeab7533a0377dcc9444aedc24217a8cf06d88c72da0e
fetched_at: '2026-06-29T00:09:34.854189+00:00'
page_id: '425459265'
product: rm
source: tdn-rm
title: Devolução e Renovações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459265
version: 3
---

No serviço da movimentação a devolução do exemplar pode ser iniciado através dos seguintes estados:

* Operações em andamento (Usuário Identificado):\* Existe um usuário identificado e  é informado o código de um exemplar que está na lista de empréstimos realizados.
* Operações em Andamento (Usuário anônimo):\* Ao identificar um exemplar que está emprestado, o serviço inicia a operação de devolução sem que seja necessário que o usuário esteja identificado.

**Dica**

Quando há integração com o TOTVS Gestão Financeira, no momento da devolução, o sistema exibe uma mensagem informando o número(ID) e o valor do lançamento que foi gerado no TOTVS Gestão Financeira.

**Atenção**

O sistema somente permitirá a realização da devolução caso seja feita na mesma Filial e Unidade que foi feito o empréstimo. Caso o sistema integre com o TOTVS Gestão Financeira, não será possível prosseguir com a devolução se o usuário não possuir um responsável financeiro cadastrado.   
 Ao identificar o(s) exemplar(es) que possuem status de emprestado o(s) mesmo(s)  é(são) inserido(s) na lista de devoluções. Quando o código de identificação do exemplar é informado novamente ou quando é clicado no ícone alterar presente na lista de devoluções,  a janela de operações em andamento - devoluções é exibida. Nesta janela é possível:

* **Remover:** Remove o(s) exemplar(es) selecionado(s) da lista de devoluções. Observação: O exemplar pode ser removido também através do ícone remover presente na lista de devoluções.
* **Marcar Todos:** Permite selecionar todos os exemplares da lista de devoluções.
* **Renovar:** Insere o(s) exemplar(es) selecionado(s) na lista de renovações.Quando o exemplar é inserido na lista de renovações é possível remover o exemplar da lista informando o código de identificação do exemplar novamente ou quando é clicado no ícone alterar presente na lista de renovações para exibir a janela de operações em andamento - Renovações. Outra opção disponível é  o comando "Não renovar" que retorna o exemplar para a lista de devoluções.Atenção: A renovação do empréstimo será bloqueada caso a regra de empréstimo não permita a renovação para o tipo de usuário e o grupo de publicação em questão. Não é permitido fazer uma renovação na mesma data do empréstimo ou da última renovação.

**Abonar multa:** O sistema atualiza o valor da multa para zero do(s) exemplar(es) selecionado(s), recalcula o valor total do empréstimo e solicita que seja informado a justificativa para o abono da multa.  
 Atenção: A permissão de abono de multa pode ser definida também por perfil de usuário. Caso o sistema esteja configurado para não permitir o abono da multa, esta permissão pode ser concedida para determinados perfis de usuário.

**Desconto multa:** O operador deverá informar o valor a ser descontado no valor total da multa do(s) exemplar(es) selecionado(s) e a justificativa do desconto. O valor informado pelo operador deverá ser menor ou igual ao valor total da multa.

**Alterar prazo:** Permite alterar o prazo de devolução prevista do(s) exemplar(es) selecionado(s). Na alteração do prazo de devolução o operador deverá informar o número de dias/horas (de acordo com o definido na regra de empréstimo) que o exemplar ficará emprestado, sendo este prazo adicionado à data da alteração, podendo ser menor ou maior que o definido na regra de empréstimo (mas se for maior, o parâmetro permitir alteração da data prevista de devolução deverá estar marcado), ou o operador poderá informar uma data e hora fixas que corresponderão à nova data e hora de devolução prevista.

**Cancelar:** Insere o(s) exemplar(es) selecionado(s) na lista de cancelamento.  
 Quando o exemplar é inserido na lista de cancelamento é possível remover da lista informando o código de identificação do exemplar novamente ou ou quando é clicado no ícone alterar presente na lista de cancelamentos para exibir a janela de operações em andamento - Cancelamento. Outra opção disponível é o comando "Não cancelar" que retorna o exemplar para a lista de devoluções.  
 Atenção: Para publicações atrasadas, o sistema pode ser parametrizado para permitir ou não o cancelamento de empréstimos.  
 Para concluir a devolução dos exemplares inseridos na lista de devoluções utilize o comando Confirmar ou a tecla F9. E ao final será emitido o recibo de empréstimo de acordo com a parametrização do sistema.

**Atenção**  
 Quando se está na lista de devolução é possível inserir o exemplar na lista de renovações ou cancelamentos; para que estas operações sejam realizadas é preciso confirmar a operação. Assim ao realizar a confirmação poderá ocorrer  renovações, cancelamentos, devoluções e até mesmo empréstimos ao mesmo tempo.
