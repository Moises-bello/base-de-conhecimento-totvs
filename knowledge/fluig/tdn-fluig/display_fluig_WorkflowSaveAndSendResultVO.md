---
content_hash: c0bbf5ee255d69be76a3a3dcf6e7a63b82e8ba6f63b75884282c357dc1cea2e2
fetched_at: '2026-06-28T21:35:29.588672+00:00'
page_id: '754245151'
product: fluig
source: tdn-fluig
title: WorkflowSaveAndSendResultVO
type: documentation
url: https://tdn.totvs.com/display/fluig/WorkflowSaveAndSendResultVO
version: 7
---

# Índice

true.\*ndicenone

#f2f2f2#f2f2f2

Este objeto é o retorno do método .

# Descrição

---

Este é um objeto de retorno do método de iniciar solicitação. Foi introduzido no **fluig 1.8.1** e substitui o retorno anterior que era um  com chave do tipo string e valor do tipo Object.

Por questões de retrocompatibilidade, **este objeto também é um mapa**. Então, todos os códigos que funcionavam antes, continuam funcionando sem problemas.

# Atributos da instância

---

**int processInstanceId**

* Retorna um valor numérico com o id da solicitação.
* Caso a solicitação não tenha sido criada, retorna zero.

**int taskSequence**

* Retorna um valor numérico com o código da atividade atual.
* Caso a solicitação não tenha sido criada, retorna zero.

**int condition**

* Retorna um valor numérico referente a qual condição do gateway foi atendida para definir o próxima atividade.
* Caso a solicitação não tenha sido criada ou não tenha passado por um gateway, retorna zero.

**int movementSequence**

* Retorna um valor numérico com o código do histórico de movimentação .
* Caso a solicitação não tenha sido criada, retorna zero.

**int documentId**

* Retorna um valor numérico com o código do formulário associado à solicitação.
* Caso a solicitação não tenha sido criada ou não possua um formulário, retorna zero.

**int documentVersion**

* Retorna um valor numérico com a versão do formulário associado à solicitação.
* Caso a solicitação não tenha sido criada ou não possua um formulário, retorna zero.

**boolean joint**

* Retorna um valor booleano *true* quando a solicitação está em uma situação de paralelismo, ou seja, passou por um gateway paralelo (fork) ou inclusivo, ou *false* quando não passou.

**String stateName**

* Retorna uma string com o nome **não traduzido** da atividade atual da solicitação.
* Caso a solicitação não tenha sido criada, retorna uma string vazia.

**String observation**

* Retorna uma string com a observação criada na solicitação.
* Caso a solicitação não tenha sido criada ou nenhum comentário seja informado, retorna uma string vazia.

**ProcessLink processLink**

* Retorna um objeto ProcessLink indicando qual o fluxo foi utilizado para chegar na atividade atual da solicitação.
* Caso a solicitação não tenha sido criada, retorna **null**.

**List<String>currentAssignees**

* Retorna uma  de strings com as matrículas dos usuários responsáveis pela atividade.
* Caso a solicitação não tenha sido criada, retorna uma lista vazia.

**boolean multipleUsers**

* Retorna um valor booleano *true* indicando há mais um usuário possível para a atividade e que deve ser indicado qual o usuário correto ou *false* quando não há necessidade de escolha.
* No caso de uma atividade em consenso configurada para "Nunca selecionar colaboradores" ou atividades do tipo gateway esse retorno sempre será false.

**List<Colleague> availableColleagues**

* Retorna uma  de objetos do tipo Colleague com dados dos usuários que podem ser selecionados para a atividade no caso de não ter criado uma solicitação pois a múltiplos usuários que podem ser responsáveis pela atividade (*multipleUsers*).

**boolean usingManagerUsers**

* Retorna um valor booleano *true*quando, por não conseguir selecionar nenhum colaborador válido, atribuiu a atividade à um (ou mais) gestor do processo. Ou *false* quando não foi necessário ou possível utilizar o gestor.

**List<Integer> subProcessInstancesIds**

* Retorna uma  de valores numéricos com os códigos das solicitações de subprocessos que foram criadas após a movimentação.
* Caso nenhuma solicitação tenha sido criada por subprocessos, retorna uma lista vazia.
