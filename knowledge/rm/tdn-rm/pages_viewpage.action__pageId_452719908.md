---
content_hash: 10bbcc66d1d632dc81bffc46d3addf2b5f88bec5f75dc1da3ac577319b8aef19
fetched_at: '2026-06-29T00:10:10.688915+00:00'
page_id: '452719908'
product: rm
source: tdn-rm
title: Cancelar Requisição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719908
version: 2
---

**Cancelar Requisição**

Uma requisição só poderá ser cancelada quando estiver com status "Pendente", "Em Andamento", "Suspensa" ou "Aprovada".

Para o procedimento de cancelamento da requisição o usuário que estiver realizando este processo deverá, obrigatoriamente, informar uma justificativa para tal cancelamento e após a confirmação do cancelamento será criado um novo parecer para a requisição selecionada com as seguintes informações:

o nome do usuário logado, a justificativa fornecida e os dados completos da requisição. Além disso, será enviado e-mail para o requisitante, o Gestor do RH, o Gestor do Departamento. Pessoal e todos os participantes do fluxo que já tenham emitido pareceres sobre a requisição notificando o seu cancelamento.

**Requisições integradas ao RM Agilis:**

Poderá ter seu status alterado após ser cancelada utilizando o processo "Alterar Fluxo da Requisição", mas este processo dependerá de parametrizações realizadas previamente no mapeamento do fluxo de atendimento da requisição. 

**Requisições não integradas ao RM Agilis:**

O cancelamento é definitivo.

Para o cancelamento de requisições que possuam requisições filhas geradas serão realizados os seguintes processos:

- Se o status da requisição filha for "Pendente", "Em andamento" ou "Aprovada"

* Será criado um novo parecer para requisição filha registrando o nome do usuário logado, a justificativa fornecida e os dados completos da requisição.
* O status da requisição filha será alterado para cancelado e em seguida serão enviados e-mails para o requisitante, o Gestor do RH, o Gestor do Depto. Pessoal e todos os participantes do fluxo que já tenham emitido pareceres sobre a requisição notificando o seu cancelamento.
* Após o cancelamento da requisição filha, a requisição pai também será cancelada, um novo parecer será criado e os e-mails de notificação do cancelamento serão encaminhados.

- Se o status da requisição for "Reprovada", "Cancelada" ou "Concluída"

* Apenas a requisição pai sofrerá alterações, ou seja, ela será cancelada, um novo parecer será criado e os e-mails de notificação do cancelamento serão encaminhados.

**Observação**

O envio das mensagens de e-mail´s para os participantes do fluxo e a notificação ao gestor de RH e ao gestor do departamento pessoal ocorrerão se a parametrização tiver sido definida.

Para verificar acesse: Opções | Parâmetros | RM Vitae | Geral | Pasta "Requisições".  
   
**Atenção**

Se na requisição a ser cancelada existir progressões efetivadas, será exibida uma mensagem para que o usuário confirme o cancelamento da requisição. Caso não exista progressões efetivadas, esses alertas não são exibidos.
