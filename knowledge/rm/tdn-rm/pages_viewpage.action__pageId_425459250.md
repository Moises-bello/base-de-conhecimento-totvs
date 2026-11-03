---
content_hash: b730415a61618c0aa4226c46bb68bd8a511f53d0dab60b80dc1635761f1f911b
fetched_at: '2026-06-29T00:09:34.797225+00:00'
page_id: '425459250'
product: rm
source: tdn-rm
title: Empréstimos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459250
version: 3
---

No serviço da movimentação o empréstimo pode ser iniciado através dos seguintes estados:

**Operações em andamento (Usuário Identificado):** Existe um usuário identificado e um exemplar disponível é informado para realizar o empréstimo.

**Empréstimo iniciado (Identificar usuário):** Neste estado um exemplar disponível foi identificado e o serviço aguarda que seja informado o usuário para realizar o empréstimo. Após o usuário identificado o estado vai para

**Operações em andamento (Usuário Identificado)**.

Os exemplares identificados são inseridos na lista de empréstimo e ao informar o código de identificação do exemplar novamente ou através do ícone alterar presente na lista de empréstimo é exibido a janela de operações em andamento - empréstimos. Nesta janela é possível:

**Remover:** Remove o exemplar(es) selecionado(s) da lista de empréstimo.  
 Observação: o exemplar pode ser removido  também através do ícone remover presente na lista de empréstimo.

**Alterar:** Permite alterar o prazo de devolução prevista e/ou inclui /altera observações do(s) exemplar(es) selecionado(s). Na alteração do prazo de devolução o operador deverá informar o número de dias/horas (de acordo com o definido na regra de empréstimo) que o exemplar ficará emprestado, sendo este prazo adicionado à data do empréstimo, podendo ser menor ou maior que o definido na regra de empréstimo (mas se for maior, o parâmetro Alterar prazo devolução maior que o definido na regra (Dias / Horas) deverá estar marcado), ou o operador poderá informar uma data e hora fixas que corresponderão à nova data e hora de devolução prevista.

**Marcar Todos:** Permite selecionar todos os exemplares da lista de empréstimo.

**Voltar:** Fecha a janela de operações em andamento.  
 Para concluir o empréstimo dos exemplares inseridos na lista de empréstimos utilize o comando Confirmar ou  a tecla F9. E ao final será emitido o recibo de empréstimo de acordo com o parametrizado no sistema.
