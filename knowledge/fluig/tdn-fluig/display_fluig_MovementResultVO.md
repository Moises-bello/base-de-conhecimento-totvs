---
content_hash: df64cca58ea9a7d0324451c0ef801a4f24b1d361b90108bd7f21b8103e625b60
fetched_at: '2026-06-28T21:35:29.963760+00:00'
page_id: '781872624'
product: fluig
source: tdn-fluig
title: MovementResultVO
type: documentation
url: https://tdn.totvs.com/display/fluig/MovementResultVO
version: 9
---

Este objeto é o retorno do método .

# Descrição

Este é um objeto de retorno do método de iniciar solicitação através do . Ele contém diversas informações sobre a solicitação iniciada como código da solicitação, do formulário, e, caso tenha gerado algum sub-processo, os códigos e ids de processos que foram gerados.

# Atributos da instância

**int requestId**

Retorna um valor numérico com o id da solicitação.

Caso a solicitação não tenha sido criada, retorna zero.

**int stateSequence**

Retorna um valor numérico com o código da atividade atual.

Caso a solicitação não tenha sido criada, retorna zero.

**String stateName**

Retorna uma string com o nome **não traduzido** da atividade atual da solicitação.

Caso a solicitação não tenha sido criada, retorna uma string vazia.

**int condition**

Retorna um valor numérico referente a qual condição do gateway foi atendida para definir o próxima atividade.

Caso a solicitação não tenha sido criada ou não tenha passado por um gateway, retorna zero.

**int movementSequence**

Retorna um valor numérico com o código do histórico de movimentação .

Caso a solicitação não tenha sido criada, retorna zero.

**int formId**

Retorna um valor numérico com o código do formulário associado à solicitação.

Caso a solicitação não tenha sido criada ou não possua um formulário, retorna zero.

**int formVersion**

Retorna um valor numérico com a versão do formulário associado à solicitação.

Caso a solicitação não tenha sido criada ou não possua um formulário, retorna zero.

**boolean joint**

Retorna um valor booleano *true* quando a solicitação está em uma situação de paralelismo, ou seja, passou por um gateway paralelo (fork) ou inclusivo, ou *false* quando não passou.

**String observation**

Retorna uma string com a observação criada na solicitação.

Caso a solicitação não tenha sido criada ou nenhum comentário seja informado, retorna uma string vazia.

**String[] currentAssignees**

Retorna uma  de strings com as matrículas dos usuários responsáveis pela atividade.

Caso a solicitação não tenha sido criada, retorna uma lista vazia.

**boolean multipleUsers**

Retorna um valor booleano *true* indicando há mais um usuário possível para a atividade e que deve ser indicado qual o usuário correto ou *false* quando não há necessidade de escolha.

No caso de uma atividade em consenso configurada para "Nunca selecionar colaboradores" ou atividades do tipo gateway esse retorno sempre será false.

**UserVO[] availableColleagues**

Retorna uma  de objetos do tipo  com os dados do usuários que podem ser selecionados para a atividade no caso de não ter criado uma solicitação pois a múltiplos usuários que podem ser responsáveis pela atividade (*multipleUsers*).

**boolean usingManagerUsers**

Retorna um valor booleano *true*quando, por não conseguir selecionar nenhum colaborador válido, atribuiu a atividade à um (ou mais) gestor do processo. Ou *false* quando não foi necessário ou possível utilizar o gestor.

**int[] subprocessRequestIds**

Retorna uma  de valores numéricos com os códigos das solicitações de subprocessos que foram criadas após a movimentação.

Caso nenhuma solicitação tenha sido criada por subprocessos, retorna uma lista vazia.

**String[] subprocessIds**

Retorna uma  de strings com os códigos dos processos que tiveram solicitações criadas como subprocessos após a movimentação.

Caso nenhuma solicitação tenha sido criada por subprocessos, retorna uma lista vazia.

# Exemplos de uso

## Imprimir os dados gerais da solicitação criada

jstrue

## Imprimir lista dos subprocessos criados

jstrue
