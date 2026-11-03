---
content_hash: 8611ead5ada180972fd45bb8083958a9bced9c2045037b01d9f85aaadde667e7
fetched_at: '2026-06-29T00:09:35.293890+00:00'
page_id: '425459298'
product: rm
source: tdn-rm
title: Atualizar situação da biblioteca
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459298
version: 6
---

Este processo tem o objetivo de realizar atualizações nas movimentações do Totvs Gestão Bibliotecária. Durante a execução os seguintes subprocessos são executados:

* Atualizar o Status dos Empréstimos dos Usuários

* O sistema verificará todos os [empréstimos](http://tdn.totvs.com/x/Mv5bGQ)  da coligada atual que estão com status igual a "Emprestado" e data de   prevista menor que a data atual. O status destes empréstimos será atualizado para "Atrasado". Quando o empréstimo for por hora, o sistema deverá verificar data e hora de devolução prevista.
* O sistema verificará todos os empréstimos da coligada atual que estão com status igual a "Atrasado" e data de devolução prevista maior que a data atual. O status destes empréstimos será atualizado para "Emprestado". Quando o empréstimo for por hora, o sistema deverá verificar data e hora de devolução prevista.
* O sistema deverá verificar se existem   de [publicações](http://tdn.totvs.com/x/Af5bGQ) com status "Reservado" e com data de liberação menor que a data atual. Devem ser listadas somente publicações que não tenham outras reservas válidas, ou seja, com data de liberação ainda não preenchida ou maior que a data atual.

* Atualizar o Status dos Usuários da Biblioteca

* O sistema deverá atualizar a situação de todos os  irregulares da coligada atual que já cumpriram o prazo de suspensão. Para isso ele deverá verificar todos os usuários cujo status é "Irregular" e a data de liberação da suspensão somada ao número de dias de suspensão. Se for menor que a data atual o status destes usuários deverá ser atualizado para "Regular", a data de liberação da suspensão e o número de dias suspenso devem ser limpos.
* O sistema deverá atualizar a situação do usuário para "Irregular" para todos os usuários da coligada atual com data de liberação da suspensão maior que a data atual..
* Os supervisores podem selecionar usuários para renovar o prazo de validade. Se o sistema está parametrizado para "Utilizar integração financeira" e "Utilizar cobrança de taxas para renovação de usuários", estes usuários devem ter seu status alterado para "Cadastro pendente" e serão gerados lançamentos para ele com o valor de renovação informado no parâmetro 'Valor da taxa de renovação do usuário'.
* Quando sistema está parametrizado para "Utilizar integração financeira" e "Utilizar cobrança de taxas para cadastro de usuários", será verificado se todos os usuários com o status "Cadastro pendente" já pagaram a taxa de cadastrou ou de renovação, ou seja, não tem lançamento do tipo "Cadastro de usuário" em aberto. Estes usuários terão seu status alterado para "Regular".

* Enviar E-mails para Usuários com Reservas Vencidas

* O sistema deverá verificar se existem reservas de publicações com status "Reservado" e com data de liberação menor que a data atual e terão o seu status alterado para "Cancelado". Após esta alteração, a fila de reservas é atualizada.
* Se o sistema estiver configurado para enviar e-mails automáticos para usuários com reservas vencidas, serão enviados e-mails para todos os usuários nesta situação. O texto do e-mail, assim como suas configurações serão de acordo com a parametrização.

* Cancelar Usuários Expirados

* O sistema verifica todos usuários com prazo de validade vencido, cujo tipo de usuários esteja configurado para verificar a validade e altera a situação deste usuários para "Cancelado".
* Pode ser configurado através dos parâmetros da atualização da situação da biblioteca para permitir cancelar manualmente os usuários expirados, somente pelos usuários que forem supervisor. Neste caso, será exibido mais um passo no processo com a lista de usuários com prazo de validade vencido, com o código do usuário, nome e data de expiração. Será possível selecionar quais os usuários terão o prazo de validade prorrogado e informar por quantos meses. Aqueles que não forem selecionados serão cancelados.

Todas as atualizações feitas serão informadas no log do processo.  
   
Permite configurar através de parâmetros para que o processo de atualização da situação da biblioteca ocorra sempre ao realizar login no sistema.  
   
**Importante:** para realizar configuração de parâmetros do processo de atualização da biblioteca acesse:
