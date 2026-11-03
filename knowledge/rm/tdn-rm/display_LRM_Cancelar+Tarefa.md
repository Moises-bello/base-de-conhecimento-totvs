---
content_hash: 22babdad8ced9a5f418cf8be6789b846f6f140c66da76f4e13d0d8f8fa666d9c
fetched_at: '2026-06-29T00:09:28.013281+00:00'
page_id: '423938621'
product: rm
source: tdn-rm
title: Cancelar Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelar+Tarefa
version: 7
---

Este processo permite que um usuário do TOTVS Gestão Contábil cancele Tarefas solicitadas por outros aplicativos, desta forma a Tarefa não poderá mais ser executada.

Para que uma Tarefa possa ser cancelada é necessário que o usuário tenha recebido permissão.

Uma vez cancelada a Tarefa, a exclusão solicitada será cancelada.

Assim que a Tarefa for cancelada, um e-mail será enviado para o usuário solicitante da Tarefa.

**Observações**

Os usuários responsáveis por execução/cancelamento de Tarefas poderão receber notificações via e-mail quando alguma tarefa for solicitada e também quando houver execução ou cancelamento de tarefas solicitadas. Para isto o endereço de e-mail nos cadastros dos usuários deve estar preenchido e as informações para envio de e-mails dentro dos Parâmetros Globais devem estar cadastradas.

Este processo é **multicoligada**, ou seja, é possível cancelar várias tarefas de coligadas distintas.

A solicitação de cancelamento pode ter se originado em uma coligada diferente da coligada do contexto mas mesmo assim tais solicitações - caso o sistema esteja devidamente parametrizado e o usuário tenha as devidas permissões - serão apresentadas na visão do [Gerenciador de tarefas](https://tdn.totvs.com/display/LRM/Gerenciador+de+Tarefas) e poderão ser executadas nesta situação sendo que a execução sempre levará em consideração a coligada da tarefa ao invés da coligada do contexto que se está executando o processo.
