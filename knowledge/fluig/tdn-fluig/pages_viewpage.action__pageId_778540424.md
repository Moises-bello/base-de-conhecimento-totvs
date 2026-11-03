---
content_hash: bca5dae55ab15ec0702ea39ee54b957293f5cf286634ab5503779bf5cf5f33d9
fetched_at: '2026-06-28T21:35:29.945145+00:00'
page_id: '778540424'
product: fluig
source: tdn-fluig
title: hAPI.startProcess (nova)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=778540424
version: 4
---

# Índice

true.\*ndicenone

#f2f2f2#f2f2f2

O método **startProcess** da  inicia uma solicitação nova, podendo preencher dados e movimentar para a atividade seguinte selecionando quais os usuários irão receber a próxima atividade.

A solicitação **sempre** será iniciada pelo usuário atual, que está movimentando a solicitação.

# Sintaxe

---

js

# Parâmetros

---

**processId**

A string do id do processo da nova solicitação.

**chosenState**

Um número inteiro representando o sequencial da atividade para qual será encaminhado a solicitação após o início. Deve ser um sequencial de atividade existente no processo *processId* e que seja uma atividade que receba um fluxo da atividade inicial.

Caso seja enviado zero, será usado o sequencial da primeira atividade pós atividade inicial.

**colleagues**

```
(opcional)
```

Uma lista de strings com a(s) matrícula(s) dos usuários que irão receber a atividade.

Este campo é opcional quando *completeTask* é **false** ou quando o mecanismo de atribuição da atividade destino (*chosenState*) possui apenas uma opção de destino.

**comments**

```
(opcional)
```

Uma string com comentários que serão adicionando junto com a abertura da solicitação.

Caso não queira adicionar um comentário pode ser enviado **null** ou uma string vazia.

**completeTask**

Um booleano informando se a tarefa vai ser movimentada ou apenas salva.

Caso *true*, a solicitação será salva com os comentários e dados de formulário informados e movimentada para a próxima atividade.

Caso *false*, a solicitação será salva com os comentários e dados de formulário informados **mas** permanecerá na atividade inicial, sem movimentar.

**cardData**

```
(opcional)
```

Uma  com os dados do formulário, composta por chave do tipo String com o nome do campo de formulário e valores do tipo String com o valor respectivo de cada campo.

Caso não tenha formulário ou o formulário será preenchido posteriormente, pode ser enviado **null**.

**managerMode**

Um booleano informando se a tarefa vai ser movimentada como usuário gestor do processo.

Caso *true* a tarefa é movimentada como usuário gestor.

Caso *false* a tarefa é movimentada como usuário normal, responsável pela tarefa.

# Valor de retorno

---

Um objeto  com os dados da solicitação criada

# Exemplos de uso

---

**Inicialização simples mantendo a solicitação na atividade inicial:**

jstrue

**Inicialização simples movimentando a solicitação para a próxima atividade:**

jstrue

**Inicialização simples movimentando a solicitação para a próxima atividade, quando existe mais de uma opção:**

jstrue

**Movimentando uma tarefa que tem mecanismo de atribuição "para um Grupo":**

jstrue

**Movimentando uma tarefa que tem mecanismo de atribuição "para um Papel":**

jstrue

**Inicialização simples com dados de formulário:**

jstrue

**Inicialização simples com dados de formulário com registro pai x filho:**

jstrue

**Adicionando comentários na inicialização da solicitação:**

jstrue
