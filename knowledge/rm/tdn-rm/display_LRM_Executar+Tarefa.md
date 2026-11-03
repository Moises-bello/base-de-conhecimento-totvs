---
content_hash: 157f92cde6587de2e2ac0e3f21a1b621641d6f2f8f10defe9970042200b6c43a
fetched_at: '2026-06-29T00:09:28.542716+00:00'
page_id: '423938704'
product: rm
source: tdn-rm
title: Executar Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Executar+Tarefa
version: 4
---

Este processo permite que um usuário do TOTVS Gestão Contábil execute Tarefas solicitadas por outros módulos que contabilizam.

Para que uma Tarefa possa ser executada é necessário que o usuário tenha recebido permissão.

Uma vez executada a Tarefa o seu status será atualizado e a contabilização será excluída conforme o Tipo da Tarefa.

Assim que a Tarefa for executada, um e-mail será enviado para o usuário solicitante da Tarefa.   
Caso haja uma falha no envio de e-mail, as tarefas serão **executadas normalmente** porém será adicionado no log do processo a informação de falha ao enviar e-mail.

**Observações**

Os usuários responsáveis por execução/cancelamento de Tarefas poderão receber notificações via e-mail quando alguma tarefa for solicitada e também quando houver execução ou cancelamento de tarefas solicitadas. Para isto o endereço de e-mail nos cadastros dos usuários deve estar preenchido e as informações para envio de e-mails dentro dos Parâmetros Globais devem estar cadastradas.

Este processo é multicoligada, ou seja, é possível executar várias tarefas de coligadas distintas.
